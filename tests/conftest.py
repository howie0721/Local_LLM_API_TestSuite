import os
import pytest
import requests
import allure
import sys
from pathlib import Path

# helpers 匯入
HELPERS_PATH = Path(__file__).parent.parent / "helpers"
if str(HELPERS_PATH) not in sys.path:
    sys.path.insert(0, str(HELPERS_PATH))
import test_helper

# ========== API 配置常數 ==========
class APIConfig:
    """API 端點與 Headers 統一配置"""
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_GENERATE_URL = f"{OLLAMA_BASE_URL}/api/generate"
    OLLAMA_CHAT_URL = f"{OLLAMA_BASE_URL}/v1/chat/completions"
    OLLAMA_VERSION_URL = f"{OLLAMA_BASE_URL}/api/version"
    DEFAULT_HEADERS = {"Content-Type": "application/json"}
    # 允許以環境變數覆寫，CI 中可使用更輕量模型 (例如: llama3.2:1b 或 tinyllama)
    DEFAULT_MODEL = os.getenv("OLLAMA_MODEL", "llama3")
    # 單次請求超時 (秒)
    DEFAULT_TIMEOUT = int(os.getenv("OLLAMA_TIMEOUT", "120"))
    # 控制輸出長度：/v1/chat/completions 使用 max_tokens；/api/generate 使用 options.num_predict
    MAX_TOKENS = int(os.getenv("OLLAMA_MAX_TOKENS", "32"))
    NUM_PREDICT = int(os.getenv("OLLAMA_NUM_PREDICT", "32"))
    TEMPERATURE = float(os.getenv("OLLAMA_TEMPERATURE", "0.1"))
    # 請求重試
    RETRIES = int(os.getenv("OLLAMA_RETRIES", "1"))
    RETRY_BACKOFF_SEC = float(os.getenv("OLLAMA_RETRY_BACKOFF", "2.0"))

# ========== Pytest Fixtures ==========
@pytest.fixture
def api_config():
    """提供 API 配置"""
    return APIConfig()

class OllamaClient:
    """Ollama API 客戶端封裝，簡化測試程式碼"""
    def __init__(self, config: APIConfig):
        self.config = config
    def _post_with_retry(self, url: str, json: dict, headers: dict, timeout: int):
        last_exc = None
        for attempt in range(self.config.RETRIES + 1):
            try:
                return requests.post(url, json=json, headers=headers, timeout=timeout)
            except requests.exceptions.ReadTimeout as e:
                last_exc = e
                if attempt < self.config.RETRIES:
                    # 簡單退避重試
                    import time

                    time.sleep(self.config.RETRY_BACKOFF_SEC)
                    continue
                raise
    def generate(self, prompt: str = None, model: str = None, stream: bool = False, timeout: int = None, **kwargs):
        url = self.config.OLLAMA_GENERATE_URL
        headers = self.config.DEFAULT_HEADERS
        payload = {
            "model": model or self.config.DEFAULT_MODEL,
            "prompt": prompt,
            "stream": stream,
        }
        # 針對 /api/generate 加入 options，限制輸出長度與溫度，提升 CI 穩定度與速度
        options = kwargs.pop("options", {})
        options.setdefault("num_predict", self.config.NUM_PREDICT)
        options.setdefault("temperature", self.config.TEMPERATURE)
        if options:
            payload["options"] = options
        payload.update(kwargs)
        resp = self._post_with_retry(
            url,
            json=payload,
            headers=headers,
            timeout=timeout or self.config.DEFAULT_TIMEOUT,
        )
        return resp
    def chat(self, messages, model: str = None, stream: bool = False, timeout: int = None, **kwargs):
        url = self.config.OLLAMA_CHAT_URL
        headers = self.config.DEFAULT_HEADERS
        payload = {
            "model": model or self.config.DEFAULT_MODEL,
            "messages": messages,
            "stream": stream,
        }
        # 針對 OpenAI 相容端點加入 max_tokens/temperature，避免回應過長造成 CI 超時
        payload.setdefault("max_tokens", self.config.MAX_TOKENS)
        payload.setdefault("temperature", self.config.TEMPERATURE)
        payload.update(kwargs)
        resp = self._post_with_retry(
            url,
            json=payload,
            headers=headers,
            timeout=timeout or self.config.DEFAULT_TIMEOUT,
        )
        return resp
    def version(self, timeout: int = None):
        """呼叫 /api/version 端點，回傳 response"""
        url = self.config.OLLAMA_VERSION_URL
        headers = self.config.DEFAULT_HEADERS
        resp = requests.get(url, headers=headers, timeout=timeout or self.config.DEFAULT_TIMEOUT)
        return resp
    def get_version(self, timeout: int = None):
        """呼叫 /api/version 端點，回傳 response (別名)"""
        return self.version(timeout=timeout)

@pytest.fixture
def ollama_client(api_config):
    """提供封裝好的 Ollama API 客戶端"""
    return OllamaClient(api_config)

# ========== Pytest Fixture 提供驗證器 ==========
@pytest.fixture
def validator():
    """提供回應驗證器"""
    return test_helper.ResponseValidator()

# ========== Pytest Fixture 提供額外工具 ==========
@pytest.fixture
def test_helper_fixture():
    """提供測試輔助工具"""
    return test_helper.TestHelper()

@pytest.fixture
def schema_validator():
    """提供 Schema 驗證器"""
    return test_helper.SchemaValidator()

@pytest.fixture
def batch_helper():
    """提供批次測試輔助工具"""
    return test_helper.BatchTestHelper()

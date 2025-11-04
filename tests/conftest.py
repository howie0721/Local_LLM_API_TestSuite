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
    OLLAMA_BASE_URL = "http://localhost:11434"
    OLLAMA_GENERATE_URL = f"{OLLAMA_BASE_URL}/api/generate"
    OLLAMA_CHAT_URL = f"{OLLAMA_BASE_URL}/v1/chat/completions"
    OLLAMA_VERSION_URL = f"{OLLAMA_BASE_URL}/api/version"
    DEFAULT_HEADERS = {"Content-Type": "application/json"}
    DEFAULT_MODEL = "llama3"
    DEFAULT_TIMEOUT = 120

# ========== Pytest Fixtures ==========
@pytest.fixture
def api_config():
    """提供 API 配置"""
    return APIConfig()

class OllamaClient:
    """Ollama API 客戶端封裝，簡化測試程式碼"""
    def __init__(self, config: APIConfig):
        self.config = config
    def generate(self, prompt: str = None, model: str = None, stream: bool = False, timeout: int = None, **kwargs):
        url = self.config.OLLAMA_GENERATE_URL
        headers = self.config.DEFAULT_HEADERS
        payload = {
            "model": model or self.config.DEFAULT_MODEL,
            "prompt": prompt,
            "stream": stream,
        }
        payload.update(kwargs)
        resp = requests.post(url, json=payload, headers=headers, timeout=timeout or self.config.DEFAULT_TIMEOUT)
        return resp
    def chat(self, messages, model: str = None, stream: bool = False, timeout: int = None, **kwargs):
        url = self.config.OLLAMA_CHAT_URL
        headers = self.config.DEFAULT_HEADERS
        payload = {
            "model": model or self.config.DEFAULT_MODEL,
            "messages": messages,
            "stream": stream,
        }
        payload.update(kwargs)
        resp = requests.post(url, json=payload, headers=headers, timeout=timeout or self.config.DEFAULT_TIMEOUT)
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

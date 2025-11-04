# Test Framework Design

## 測試框架設計文件

本文件說明測試框架的設計決策、架構模式與最佳實踐。

---

## 設計原則

### 1. **可維護性 (Maintainability)**

**目標**: 降低測試維護成本，提高程式碼可讀性

**實踐**:
- ✅ 使用 Page Object Pattern 封裝 API 呼叫
- ✅ 共用 fixtures 減少重複程式碼
- ✅ 模組化測試結構（按類別分資料夾）
- ✅ 清晰的測試命名與 docstring

**範例**:
```python
# ❌ Bad: 直接呼叫 API
def test_chat():
    response = requests.post("http://localhost:11434/api/chat", json={...})
    # 重複程式碼，難以維護

# ✅ Good: 使用 Page Object
def test_chat(ollama_client):
    response = ollama_client.chat(messages=[...])
    # API 變更只需修改 ollama_client
```

---

### 2. **可擴展性 (Scalability)**

**目標**: 框架能隨著專案成長而擴展

**實踐**:
- ✅ 插件化架構（pytest plugins）
- ✅ 配置驅動（pytest.ini, conftest.py）
- ✅ 靈活的 marker 系統

**架構設計**:
```
tests/
├── conftest.py          # 核心 fixtures（可被所有測試使用）
├── unit/
│   └── conftest.py      # 單元測試專用 fixtures
├── integration/
│   └── conftest.py      # 整合測試專用 fixtures
└── e2e/
    └── conftest.py      # E2E 測試專用 fixtures
```

---

### 3. **可重用性 (Reusability)**

**目標**: 最大化測試元件的重用

**實踐**:
- ✅ Fixture 作用域管理（session, module, function）
- ✅ Helper 函式庫
- ✅ 測試資料共用（JSON fixtures）

**範例**:
```python
# conftest.py
@pytest.fixture(scope="session")
def ollama_client():
    """Session scope: 所有測試共用一個客戶端"""
    client = OllamaClient()
    yield client
    client.close()

@pytest.fixture
def sample_messages():
    """Function scope: 每個測試獨立的訊息副本"""
    return [{"role": "user", "content": "Hello"}]
```

---

### 4. **隔離性 (Isolation)**

**目標**: 測試之間互不影響

**實踐**:
- ✅ 每個測試獨立執行
- ✅ 使用 fixture teardown 清理資源
- ✅ 避免共用可變狀態

**範例**:
```python
@pytest.fixture
def temp_data():
    data = {"temp": []}
    yield data
    # Teardown: 清理資料
    data.clear()
```

---

### 5. **可讀性 (Readability)**

**目標**: 測試即文件，易於理解

**實踐**:
- ✅ AAA 模式（Arrange-Act-Assert）
- ✅ 清晰的測試命名
- ✅ 完整的 docstring
- ✅ Allure 裝飾器增強可讀性

**範例**:
```python
@pytest.mark.integration
@allure.feature("Multi-turn Conversation")
@allure.severity(allure.severity_level.CRITICAL)
def test_multi_turn_conversation_retains_context(ollama_client):
    """測試多輪對話保留上下文
    
    驗證點:
    1. LLM 能記住使用者名字
    2. 回應符合上下文
    """
    # Arrange: 準備對話訊息
    messages = []
    
    # Act: 第一輪對話
    messages.append({"role": "user", "content": "My name is Alice"})
    response1 = ollama_client.chat(messages=messages)
    messages.append({"role": "assistant", "content": response1.content})
    
    # Act: 第二輪對話
    messages.append({"role": "user", "content": "What's my name?"})
    response2 = ollama_client.chat(messages=messages)
    
    # Assert: 驗證記憶
    assert "Alice" in response2.content
```

---

## 架構模式

### Page Object Pattern

**目的**: 封裝 API 互動細節

**結構**:
```python
# Pages/ollama_client.py
class OllamaClient:
    def __init__(self, base_url="http://localhost:11434"):
        self.base_url = base_url
        self.session = requests.Session()
    
    def chat(self, model="llama3", messages=None, **kwargs):
        """發送聊天請求"""
        url = f"{self.base_url}/api/chat"
        payload = {
            "model": model,
            "messages": messages or [],
            **kwargs
        }
        response = self.session.post(url, json=payload)
        return response
    
    def list_models(self):
        """列出可用模型"""
        url = f"{self.base_url}/api/tags"
        response = self.session.get(url)
        return response.json()
```

**優點**:
- ✅ API 變更只需修改一處
- ✅ 測試程式碼更簡潔
- ✅ 易於 mock 與測試

---

### Fixture Factory Pattern

**目的**: 動態建立測試資料

**範例**:
```python
# conftest.py
@pytest.fixture
def message_factory():
    """訊息工廠 fixture"""
    def _create_message(role="user", content="Hello"):
        return {"role": role, "content": content}
    return _create_message

# 使用
def test_custom_message(message_factory):
    msg = message_factory(role="system", content="You are helpful")
    assert msg["role"] == "system"
```

---

### Data-Driven Testing

**目的**: 使用外部資料驅動測試

**結構**:
```
tests/fixtures/
├── prompts_basic.json           # 基本 prompts
├── prompts_multilingual.json    # 多語言 prompts
└── expected_responses.json      # 預期回應
```

**範例**:
```python
import json
from pathlib import Path

@pytest.fixture
def multilingual_prompts():
    path = Path(__file__).parent / "fixtures" / "prompts_multilingual.json"
    return json.load(path.open(encoding="utf-8"))

@pytest.mark.parametrize("language", ["en", "zh", "ja", "ko"])
def test_multilingual(ollama_client, multilingual_prompts, language):
    prompt = multilingual_prompts[language]
    response = ollama_client.chat(messages=[{"role": "user", "content": prompt}])
    assert response.status_code == 200
```

---

## 測試層級設計

### Layer 1: Unit Tests (單元測試)

**特徵**:
- 快速（< 1 秒/測試）
- 獨立（不依賴外部服務）
- 高覆蓋率

**適用場景**:
- Helper 函式測試
- 資料驗證邏輯
- API 客戶端單一方法測試

**範例**:
```python
@pytest.mark.unit
def test_validate_prompt_rejects_empty_string():
    """測試 prompt 驗證拒絕空字串"""
    validator = PromptValidator()
    with pytest.raises(ValueError, match="empty"):
        validator.validate("")
```

---

### Layer 2: Integration Tests (整合測試)

**特徵**:
- 中速（3-10 秒/測試）
- 依賴外部服務（Ollama API）
- 測試元件互動

**適用場景**:
- 多輪對話測試
- API 工作流程測試
- 上下文保留測試

**範例**:
```python
@pytest.mark.integration
def test_multi_turn_workflow(ollama_client):
    """測試多輪對話工作流程"""
    messages = []
    
    # 第一輪
    messages.append({"role": "user", "content": "Hi"})
    response1 = ollama_client.chat(messages=messages)
    messages.append({"role": "assistant", "content": response1.content})
    
    # 第二輪
    messages.append({"role": "user", "content": "Remember: my name is Alice"})
    response2 = ollama_client.chat(messages=messages)
    messages.append({"role": "assistant", "content": response2.content})
    
    # 第三輪：驗證記憶
    messages.append({"role": "user", "content": "What's my name?"})
    response3 = ollama_client.chat(messages=messages)
    assert "Alice" in response3.content
```

---

### Layer 3: E2E Tests (端到端測試)

**特徵**:
- 慢（10-30 秒/測試）
- 測試完整業務流程
- 最接近真實使用

**適用場景**:
- 使用者旅程測試
- 生產環境工作流程模擬
- 跨模組整合測試

**範例**:
```python
@pytest.mark.e2e
@allure.feature("User Journey")
def test_complete_research_workflow(ollama_client):
    """完整研究工作流程"""
    # 步驟 1: 查詢模型
    models = ollama_client.list_models()
    assert len(models) > 0
    
    # 步驟 2: 提交文章
    article = load_test_article()
    response = ollama_client.chat(messages=[
        {"role": "user", "content": f"請摘要：{article}"}
    ])
    
    # 步驟 3: 詢問細節
    # ...
```

---

## 測試資料管理

### 靜態測試資料

**位置**: `tests/fixtures/*.json`

**範例**:
```json
// prompts_basic.json
{
  "greeting": "Hello, how are you?",
  "question": "What is the capital of France?",
  "instruction": "請用繁體中文回答"
}
```

### 動態測試資料

**使用 Fixture Factory**:
```python
@pytest.fixture
def conversation_builder():
    """對話建構器"""
    class ConversationBuilder:
        def __init__(self):
            self.messages = []
        
        def add_user_message(self, content):
            self.messages.append({"role": "user", "content": content})
            return self
        
        def add_assistant_message(self, content):
            self.messages.append({"role": "assistant", "content": content})
            return self
        
        def build(self):
            return self.messages
    
    return ConversationBuilder()

# 使用
def test_with_builder(conversation_builder):
    messages = (conversation_builder
                .add_user_message("Hi")
                .add_assistant_message("Hello")
                .add_user_message("How are you?")
                .build())
    assert len(messages) == 3
```

---

## 錯誤處理設計

### 預期錯誤

**使用 `pytest.raises`**:
```python
@pytest.mark.error_handling
def test_invalid_model_raises_error(ollama_client):
    """測試無效模型拋出錯誤"""
    with pytest.raises(ValueError, match="model not found"):
        ollama_client.chat(model="invalid_model", messages=[...])
```

### 非預期錯誤

**使用 `pytest.fail`**:
```python
def test_api_response_format(ollama_client):
    """測試 API 回應格式"""
    try:
        response = ollama_client.chat(messages=[...])
        data = response.json()
        assert "choices" in data
    except Exception as e:
        pytest.fail(f"Unexpected error: {e}")
```

---

## 效能測試設計

### Benchmark Tests (使用 pytest-benchmark)

```python
@pytest.mark.performance
def test_api_response_time(ollama_client, benchmark):
    """測試 API 回應時間"""
    messages = [{"role": "user", "content": "Hello"}]
    result = benchmark(ollama_client.chat, messages=messages)
    assert result.status_code == 200
```

### Load Tests (使用 JMeter)

**設計原則**:
- 模擬真實使用場景
- 逐步增加負載
- 監控系統資源

**指標**:
- Throughput (請求數/秒)
- Response Time (P50, P95, P99)
- Error Rate

---

## CI/CD 整合設計

### 測試分層執行

**PR 階段** (快速回饋):
```yaml
# .github/workflows/pr-tests.yml
- name: Run Fast Tests
  run: pytest -m "unit or boundary or compatibility or error_handling"
  # 18 tests, ~5-10 minutes
```

**Nightly 階段** (完整驗證):
```yaml
# .github/workflows/nightly-tests.yml
- name: Run Full Tests
  run: |
    pytest -m e2e --alluredir=allure-results/e2e &
    pytest -m integration --alluredir=allure-results/integration &
    pytest -m security --alluredir=allure-results/security &
    wait
  # 20 tests, ~20-30 minutes
```

---

## 報告系統設計

### Allure Integration

**配置**:
```python
# conftest.py
import allure

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    allure.environment(
        python_version="3.11",
        pytest_version="7.4.3",
        ollama_version="0.1.14"
    )
```

**使用裝飾器**:
```python
@allure.feature("API Connection")
@allure.story("Basic Connection")
@allure.severity(allure.severity_level.BLOCKER)
def test_connection():
    with allure.step("步驟 1: 連接"):
        # ...
        allure.attach(data, "Request", allure.attachment_type.JSON)
```

---

## 最佳實踐

### 1. **測試獨立性**

```python
# ❌ Bad: 測試之間有依賴
test_order = []

def test_first():
    test_order.append("first")

def test_second():
    assert "first" in test_order  # 依賴 test_first

# ✅ Good: 測試獨立
def test_first():
    data = setup_data()
    assert data is not None

def test_second():
    data = setup_data()  # 獨立準備資料
    assert data is not None
```

---

### 2. **使用 Parametrize 減少重複**

```python
# ❌ Bad: 重複程式碼
def test_greeting_english():
    assert greet("en") == "Hello"

def test_greeting_chinese():
    assert greet("zh") == "你好"

# ✅ Good: 使用 parametrize
@pytest.mark.parametrize("lang,expected", [
    ("en", "Hello"),
    ("zh", "你好"),
    ("ja", "こんにちは"),
])
def test_greeting(lang, expected):
    assert greet(lang) == expected
```

---

### 3. **清晰的錯誤訊息**

```python
# ❌ Bad: 不清楚的錯誤
assert response.status_code == 200

# ✅ Good: 清晰的錯誤訊息
assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
```

---

## 未來擴展

### 計畫功能

1. **Contract Testing** (契約測試)
   - 使用 Pact 驗證 API 契約
   - 確保 API 版本相容性

2. **Mutation Testing** (變異測試)
   - 使用 mutmut 測試測試品質
   - 提高測試有效性

3. **Visual Testing** (視覺測試)
   - 若有 UI，使用 Playwright
   - 截圖比對

4. **Chaos Engineering** (混沌工程)
   - 模擬網路故障
   - 測試系統韌性

---

## 參考資源

- [Pytest Documentation](https://docs.pytest.org/)
- [Test Automation Patterns](https://testautomationpatterns.com/)
- [Google Testing Blog](https://testing.googleblog.com/)

---

**維護者**: @howie0721  
**最後更新**: 2025-11-04

# Coding Style Guide

## Python 編碼規範

本專案遵循 **PEP 8** 和 **Google Python Style Guide**，並使用工具自動化檢查。

---

## 核心原則

### 1. **可讀性優先**
> Code is read much more often than it is written. — Guido van Rossum

```python
# ❌ Bad
def f(x,y):return x*2+y*3

# ✅ Good
def calculate_weighted_sum(x, y):
    """計算加權總和: x*2 + y*3"""
    return x * 2 + y * 3
```

### 2. **明確優於隱晦（Explicit is better than implicit）**

```python
# ❌ Bad
def process(data):
    # data 是什麼？list? dict? str?
    pass

# ✅ Good
def process_user_data(user_dict: dict[str, Any]) -> list[str]:
    """處理使用者資料字典，回傳處理後的字串列表"""
    pass
```

### 3. **簡單優於複雜（Simple is better than complex）**

```python
# ❌ Bad
result = [x for x in list(map(lambda y: y * 2, filter(lambda z: z > 5, data)))]

# ✅ Good
filtered_data = [item for item in data if item > 5]
result = [item * 2 for item in filtered_data]
```

---

## 命名規範

### 變數與函式

```python
# 小寫加底線（snake_case）
user_name = "Alice"
max_retry_count = 3

def send_api_request():
    pass

def calculate_average_response_time():
    pass
```

### 類別

```python
# 大駝峰（PascalCase）
class OllamaClient:
    pass

class TestHelper:
    pass

class ResponseValidator:
    pass
```

### 常數

```python
# 全大寫加底線
API_TIMEOUT = 60
MAX_PROMPT_LENGTH = 10000
DEFAULT_MODEL = "llama3"
```

### 私有變數/函式

```python
class MyClass:
    def __init__(self):
        self._internal_state = 0  # 受保護（建議不從外部訪問）
        self.__private_data = {}   # 私有（名稱改寫）
    
    def public_method(self):
        pass
    
    def _internal_method(self):
        """內部使用，不建議外部呼叫"""
        pass
```

### 測試函式

```python
# test_ 開頭，描述測試目的
def test_connection_success():
    pass

def test_api_returns_valid_json_when_prompt_is_valid():
    pass

def test_error_handling_when_model_not_found():
    pass
```

---

## 格式化

### 行長度

```python
# 最大 88 字元（black 預設）
# ❌ Bad（超過 88 字元）
response = ollama_client.chat(model="llama3", messages=[{"role": "user", "content": "這是一個很長很長的 prompt，用來測試系統對於長輸入的處理能力"}])

# ✅ Good（使用換行）
response = ollama_client.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": "這是一個很長很長的 prompt，用來測試系統對於長輸入的處理能力"
        }
    ]
)
```

### 縮排

```python
# 使用 4 個空格（不使用 Tab）
def my_function():
    if condition:
        do_something()
        do_another_thing()
```

### 空行

```python
# 模組層級：兩個空行
import os
import sys


class MyClass:  # 類別定義前兩個空行
    pass


def my_function():  # 函式定義前兩個空行
    pass


# 類別內方法：一個空行
class MyClass:
    def method1(self):
        pass
    
    def method2(self):  # 方法間一個空行
        pass
```

### Import 順序

```python
# 1. 標準庫
import os
import sys
from typing import Any, Dict, List

# 2. 第三方庫
import pytest
import requests
import allure

# 3. 本地模組
from helpers.test_helper import TestHelper
from Pages.ollama_client import OllamaClient
```

---

## 型別提示（Type Hints）

### 函式簽名

```python
from typing import Any, Dict, List, Optional

def process_response(
    response: requests.Response,
    expected_status: int = 200
) -> Dict[str, Any]:
    """處理 API 回應
    
    Args:
        response: requests 回應物件
        expected_status: 預期的 HTTP 狀態碼
    
    Returns:
        解析後的 JSON 資料
    
    Raises:
        ValueError: 若狀態碼不符合預期
    """
    if response.status_code != expected_status:
        raise ValueError(f"意外的狀態碼: {response.status_code}")
    return response.json()
```

### 複雜型別

```python
from typing import Union, Tuple, Callable

# Union
def process_input(data: Union[str, int]) -> str:
    return str(data)

# Tuple
def get_coordinates() -> Tuple[float, float]:
    return (25.0, 121.5)

# Callable
def apply_function(func: Callable[[int], int], value: int) -> int:
    return func(value)

# Optional（等同於 Union[T, None]）
def find_user(user_id: int) -> Optional[Dict[str, Any]]:
    # 可能回傳 dict 或 None
    pass
```

---

## Docstring 規範

### Google Style

```python
def send_chat_request(
    model: str,
    messages: List[Dict[str, str]],
    temperature: float = 0.8,
    timeout: int = 60
) -> Dict[str, Any]:
    """發送聊天請求到 Ollama API
    
    Args:
        model: 使用的模型名稱（例如 "llama3"）
        messages: 對話訊息列表，每個訊息包含 role 和 content
        temperature: 生成溫度，範圍 0.0-1.0，預設 0.8
        timeout: 請求超時秒數，預設 60
    
    Returns:
        包含 API 回應的字典，包括：
        - choices: 生成的回應列表
        - usage: Token 使用資訊
        - model: 實際使用的模型名稱
    
    Raises:
        requests.exceptions.ConnectionError: 無法連接到 API
        requests.exceptions.Timeout: 請求超時
        ValueError: 參數驗證失敗
    
    Example:
        >>> client = OllamaClient()
        >>> messages = [{"role": "user", "content": "Hello"}]
        >>> response = send_chat_request("llama3", messages)
        >>> print(response["choices"][0]["message"]["content"])
    """
    # 實作...
```

### 類別 Docstring

```python
class ResponseValidator:
    """API 回應驗證器
    
    提供多種驗證方法來檢查 Ollama API 回應的格式與內容。
    
    Attributes:
        strict_mode: 是否啟用嚴格模式（預設 False）
        timeout: 驗證超時秒數（預設 10）
    
    Example:
        >>> validator = ResponseValidator(strict_mode=True)
        >>> validator.validate_response(response)
        >>> validator.assert_contains_keywords(response, ["hello", "world"])
    """
    
    def __init__(self, strict_mode: bool = False, timeout: int = 10):
        """初始化驗證器
        
        Args:
            strict_mode: 若為 True，驗證失敗時拋出異常而非回傳 False
            timeout: 驗證超時秒數
        """
        self.strict_mode = strict_mode
        self.timeout = timeout
```

---

## 測試命名與結構

### AAA 模式（Arrange-Act-Assert）

```python
import pytest

@pytest.mark.unit
def test_calculate_weighted_sum_with_positive_numbers():
    """測試加權總和計算（正數輸入）"""
    # Arrange（準備）
    x = 5
    y = 10
    expected_result = 5 * 2 + 10 * 3  # 40
    
    # Act（執行）
    result = calculate_weighted_sum(x, y)
    
    # Assert（驗證）
    assert result == expected_result
    assert isinstance(result, int)
```

### 測試函式命名

```python
# 格式: test_<被測試功能>_<測試場景>_<預期結果>

def test_connection_with_valid_url_returns_200():
    pass

def test_chat_with_empty_prompt_raises_value_error():
    pass

def test_multi_turn_conversation_with_context_retains_user_name():
    pass
```

---

## 程式碼品質工具

### Black（格式化）

```bash
# 安裝
pip install black

# 格式化單一檔案
black tests/unit/test_connection.py

# 格式化整個專案
black .

# 檢查但不修改
black --check .
```

**配置** (`pyproject.toml`):
```toml
[tool.black]
line-length = 88
target-version = ['py311']
include = '\.pyi?$'
```

---

### Flake8（Linting）

```bash
# 安裝
pip install flake8

# 檢查檔案
flake8 tests/unit/test_connection.py

# 檢查整個專案
flake8 .
```

**配置** (`.flake8`):
```ini
[flake8]
max-line-length = 88
extend-ignore = E203, W503
exclude = .git,__pycache__,venv
```

---

### MyPy（型別檢查）

```bash
# 安裝
pip install mypy

# 檢查檔案
mypy tests/unit/test_connection.py

# 檢查整個專案
mypy .
```

**配置** (`mypy.ini`):
```ini
[mypy]
python_version = 3.11
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
```

---

### isort（Import 排序）

```bash
# 安裝
pip install isort

# 排序 imports
isort tests/unit/test_connection.py

# 檢查但不修改
isort --check-only .
```

**配置** (`pyproject.toml`):
```toml
[tool.isort]
profile = "black"
line_length = 88
```

---

## Git Pre-commit Hook

自動在 commit 前執行檢查：

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.7.0
    hooks:
      - id: black
        language_version: python3.11

  - repo: https://github.com/PyCQA/flake8
    rev: 6.1.0
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.5.1
    hooks:
      - id: mypy

  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
```

**安裝**:
```bash
pip install pre-commit
pre-commit install
```

---

## 常見反模式

### 1. **Magic Numbers**

```python
# ❌ Bad
def wait_for_response():
    time.sleep(30)  # 30 是什麼意思？
    if retry_count > 5:  # 5 又是什麼意思？
        pass

# ✅ Good
DEFAULT_TIMEOUT = 30  # 秒
MAX_RETRY_COUNT = 5

def wait_for_response():
    time.sleep(DEFAULT_TIMEOUT)
    if retry_count > MAX_RETRY_COUNT:
        pass
```

---

### 2. **過長的函式**

```python
# ❌ Bad（100+ 行的函式）
def process_everything():
    # 連線
    # 驗證
    # 處理
    # 格式化
    # 儲存
    # 通知
    pass  # 太多責任！

# ✅ Good（拆分為小函式）
def process_everything():
    connection = establish_connection()
    validate_input(connection)
    data = process_data(connection)
    formatted = format_output(data)
    save_results(formatted)
    send_notification()
```

---

### 3. **過度巢狀**

```python
# ❌ Bad
def check_response(response):
    if response:
        if response.status_code == 200:
            if response.json():
                if "data" in response.json():
                    return response.json()["data"]
    return None

# ✅ Good（Early Return）
def check_response(response):
    if not response:
        return None
    if response.status_code != 200:
        return None
    data = response.json()
    if not data or "data" not in data:
        return None
    return data["data"]
```

---

### 4. **Bare Except**

```python
# ❌ Bad
try:
    do_something()
except:  # 捕捉所有異常，包括 KeyboardInterrupt
    pass

# ✅ Good
try:
    do_something()
except (ValueError, TypeError) as e:
    logger.error(f"處理失敗: {e}")
```

---

## 專案特定規範

### Fixture 命名

```python
# conftest.py
@pytest.fixture(scope="session")
def ollama_client():
    """提供 Ollama 客戶端（整個測試期間共用）"""
    return OllamaClient()

@pytest.fixture
def sample_messages():
    """提供範例對話訊息"""
    return [{"role": "user", "content": "Hello"}]
```

---

### Marker 使用

```python
# 檔案層級
pytestmark = pytest.mark.unit

# 函式層級
@pytest.mark.slow
@pytest.mark.integration
def test_slow_integration():
    pass
```

---

### 檔案命名

```
tests/
├── unit/
│   ├── test_connection.py        # 測試連線功能
│   └── test_model_info.py        # 測試模型資訊
├── integration/
│   └── test_api_workflow.py      # 測試 API 工作流程
└── fixtures/
    ├── prompts_basic.json        # 基本 prompt 資料
    └── expected_responses.json   # 預期回應資料
```

---

## 檢查清單

提交前確認：

- [ ] 執行 `black .` 格式化
- [ ] 執行 `flake8 .` 無錯誤
- [ ] 執行 `mypy .` 無型別錯誤
- [ ] 執行 `pytest` 所有測試通過
- [ ] 新增的函式有 docstring
- [ ] 複雜邏輯有註解說明
- [ ] 無 `print()` debug 語句（改用 `logger`）
- [ ] 無註解的程式碼（應刪除而非註解）

---

## 參考資源

- [PEP 8](https://peps.python.org/pep-0008/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Black Documentation](https://black.readthedocs.io/)
- [Flake8 Documentation](https://flake8.pycqa.org/)
- [MyPy Documentation](https://mypy.readthedocs.io/)

---

**維護者**: @howie0721  
**最後更新**: 2025-11-04

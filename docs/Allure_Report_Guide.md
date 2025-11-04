# Allure Report Guide

## 簡介

Allure Framework 是一個靈活、美觀的測試報告工具，支援多種語言與測試框架。本專案使用 **allure-pytest** 插件來生成互動式測試報告。

**主要功能**:
- 📊 美觀的測試結果視覺化
- 📈 歷史趨勢追蹤
- 🏷️ 測試分類與標籤
- 📎 附件支援（截圖、日誌、JSON）
- 🔗 與 CI/CD 整合
- 🌐 支援多語言

---

## 快速開始

### 安裝

```bash
# 安裝 Python 套件
pip install allure-pytest

# 安裝 Allure Commandline
# Windows (Chocolatey)
choco install allure

# Mac
brew install allure

# Linux
apt-add-repository ppa:qameta/allure
apt-get update
apt-get install allure

# 確認安裝
allure --version  # 應顯示 2.20.0 或更高
```

### 生成報告

```bash
# 1. 執行測試並生成原始數據
pytest --alluredir=allure-results

# 2. 生成並開啟 HTML 報告
allure serve allure-results

# 或分兩步：
# 2a. 生成 HTML 報告
allure generate allure-results -o allure-report --clean

# 2b. 開啟報告
allure open allure-report
```

---

## 報告結構

### Overview (概覽)

![Allure Overview](https://via.placeholder.com/800x400?text=Allure+Overview)

**顯示內容**:
- **Total Tests**: 總測試數
- **Passed**: 通過數
- **Failed**: 失敗數
- **Broken**: 中斷數
- **Skipped**: 跳過數
- **Success Rate**: 成功率

**測試狀態說明**:
- ✅ **Passed**: 測試通過
- ❌ **Failed**: 斷言失敗
- 💥 **Broken**: 測試執行中拋出異常
- ⏭️ **Skipped**: 測試被跳過（`@pytest.mark.skip`）
- ⏸️ **Unknown**: 狀態未知

---

### Suites (測試套件)

按測試檔案分組顯示：

```
tests/
├── unit/
│   ├── test_connection.py ✅ (5/5)
│   └── test_model_info.py ✅ (4/4)
├── integration/
│   ├── test_api_workflow.py ✅ (3/3)
│   └── test_multi_turn.py ❌ (2/3)
└── e2e/
    └── test_user_scenarios.py ✅ (5/5)
```

---

### Graphs (圖表)

#### 1. **Status Chart** (狀態圖)
```
Passed:  85% ████████████████░░░░
Failed:  10% ██░░░░░░░░░░░░░░░░░░
Broken:   3% █░░░░░░░░░░░░░░░░░░░
Skipped:  2% ░░░░░░░░░░░░░░░░░░░░
```

#### 2. **Severity Chart** (嚴重性圖)
```
Blocker:  5% ████░░░░░░░░░░░░░░░░
Critical: 15% ███████░░░░░░░░░░░░░
Normal:   60% ████████████████████
Minor:    15% ███████░░░░░░░░░░░░░
Trivial:   5% ████░░░░░░░░░░░░░░░░
```

#### 3. **Duration Chart** (執行時間圖)
```
< 1s:   20 tests █████████░░░░░░░░░░
1-3s:   10 tests ████░░░░░░░░░░░░░░░
3-5s:    5 tests ██░░░░░░░░░░░░░░░░░
> 5s:    3 tests █░░░░░░░░░░░░░░░░░░
```

---

### Behaviors (行為分類)

按功能特性分類：

```
Feature: API Connection
  ├── Story: Basic Connection
  │   ├── ✅ test_connection_success
  │   └── ✅ test_connection_timeout
  └── Story: Authentication
      ├── ✅ test_auth_with_token
      └── ❌ test_auth_without_token

Feature: Chat Functionality
  ├── Story: Single Turn
  │   └── ✅ test_single_turn_chat
  └── Story: Multi Turn
      ├── ✅ test_multi_turn_conversation
      └── ✅ test_context_retention
```

---

### Timeline (時間軸)

視覺化測試執行順序與並行情況：

```
Thread 1: |███ test_1 ███|     |██ test_4 ██|
Thread 2: |████ test_2 ████|   |███ test_5 ███|
Thread 3:     |█████ test_3 █████|
          ────────────────────────────────────▶ Time
          0s    2s    4s    6s    8s    10s
```

---

## Allure 裝飾器

### @allure.feature

定義功能特性：

```python
import allure

@allure.feature("API Connection")
class TestConnection:
    
    @allure.story("Basic Connection")
    def test_connection_success(self):
        pass
    
    @allure.story("Error Handling")
    def test_connection_timeout(self):
        pass
```

---

### @allure.severity

定義測試嚴重性：

```python
import allure

@allure.severity(allure.severity_level.BLOCKER)
def test_critical_api_failure():
    """若此測試失敗，系統無法運作"""
    pass

@allure.severity(allure.severity_level.CRITICAL)
def test_major_feature_broken():
    """若此測試失敗，主要功能無法使用"""
    pass

@allure.severity(allure.severity_level.NORMAL)
def test_standard_functionality():
    """標準功能測試"""
    pass

@allure.severity(allure.severity_level.MINOR)
def test_minor_ui_issue():
    """次要問題"""
    pass

@allure.severity(allure.severity_level.TRIVIAL)
def test_typo_in_message():
    """微小問題"""
    pass
```

**嚴重性等級**:
- **BLOCKER**: 阻斷性，系統無法運作
- **CRITICAL**: 關鍵性，主要功能損壞
- **NORMAL**: 一般（預設）
- **MINOR**: 次要
- **TRIVIAL**: 微小

---

### @allure.step

定義測試步驟：

```python
import allure

@allure.step("步驟 1: 連接到 API")
def connect_to_api():
    # ...
    pass

@allure.step("步驟 2: 發送訊息 '{message}'")
def send_message(message):
    # ...
    pass

@allure.step("步驟 3: 驗證回應")
def verify_response(response):
    # ...
    pass

def test_chat_workflow():
    connect_to_api()
    send_message("Hello")
    response = get_response()
    verify_response(response)
```

**報告中顯示**:
```
✅ test_chat_workflow (3.2s)
  ├── ✅ 步驟 1: 連接到 API (0.5s)
  ├── ✅ 步驟 2: 發送訊息 'Hello' (1.2s)
  └── ✅ 步驟 3: 驗證回應 (1.5s)
```

---

### allure.attach

附加檔案到報告：

```python
import allure
import json

def test_api_request():
    request_data = {"prompt": "Hello"}
    
    # 附加請求資料
    allure.attach(
        json.dumps(request_data, indent=2),
        name="Request",
        attachment_type=allure.attachment_type.JSON
    )
    
    response = call_api(request_data)
    
    # 附加回應資料
    allure.attach(
        response.text,
        name="Response",
        attachment_type=allure.attachment_type.TEXT
    )
    
    # 附加截圖（若有 UI）
    # screenshot = driver.get_screenshot_as_png()
    # allure.attach(
    #     screenshot,
    #     name="Screenshot",
    #     attachment_type=allure.attachment_type.PNG
    # )
```

**支援的附件類型**:
- `TEXT`: 純文字
- `JSON`: JSON 格式
- `HTML`: HTML 頁面
- `XML`: XML 文件
- `PNG`, `JPG`: 圖片
- `CSV`: CSV 檔案
- `PDF`: PDF 文件

---

### @allure.link / @allure.issue / @allure.testcase

連結到外部資源：

```python
import allure

@allure.link("https://github.com/howie0721/Local_LLM_API_TestSuite")
@allure.issue("ISSUE-123", "https://jira.example.com/ISSUE-123")
@allure.testcase("TC-456", "https://testrail.example.com/TC-456")
def test_with_links():
    pass
```

**報告中顯示**:
```
🔗 Links:
  - 🌐 Link
  - 🐛 ISSUE-123
  - 📋 TC-456
```

---

## 進階配置

### pytest.ini

```ini
[pytest]
# Allure 預設輸出目錄
allure_results_dir = allure-results

# 自動清理舊報告
addopts = --alluredir=allure-results --clean-alluredir
```

---

### 環境資訊

顯示測試環境資訊：

```python
# conftest.py
import pytest
import allure

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # 設定環境資訊
    allure.environment(
        python_version="3.11.5",
        pytest_version="7.4.3",
        os="Windows 11",
        ollama_version="0.1.14",
        test_environment="Local"
    )
```

**報告中顯示**:
```
Environment:
  Python Version: 3.11.5
  Pytest Version: 7.4.3
  OS: Windows 11
  Ollama Version: 0.1.14
  Test Environment: Local
```

---

### 測試分類（Categories）

自訂測試失敗分類：

```json
// allure-results/categories.json
[
  {
    "name": "API Connection Failures",
    "matchedStatuses": ["failed", "broken"],
    "messageRegex": ".*ConnectionError.*"
  },
  {
    "name": "Timeout Errors",
    "matchedStatuses": ["failed"],
    "messageRegex": ".*timeout.*"
  },
  {
    "name": "Assertion Failures",
    "matchedStatuses": ["failed"],
    "messageRegex": ".*AssertionError.*"
  }
]
```

---

## 歷史趨勢

### 啟用歷史追蹤

```bash
# 第一次執行
pytest --alluredir=allure-results
allure generate allure-results -o allure-report

# 第二次執行（保留歷史）
pytest --alluredir=allure-results
allure generate allure-results -o allure-report --clean
cp -r allure-report/history allure-results/history

# 第三次執行
pytest --alluredir=allure-results
allure generate allure-results -o allure-report --clean
```

### 視覺化趨勢

![Allure Trend](https://via.placeholder.com/800x300?text=Allure+Trend+Chart)

```
Pass Rate:
100% |██████████████████████▓▓▓▓▓░░░ (85%)
 75% |────────────────────────────────
 50% |────────────────────────────────
  0% |────────────────────────────────
      v1   v2   v3   v4   v5   v6   v7
```

---

## CI/CD 整合

### GitHub Actions

```yaml
# .github/workflows/pr-tests.yml
name: PR Tests with Allure

on: [pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      
      - name: Run tests with Allure
        run: |
          pytest --alluredir=allure-results
      
      - name: Generate Allure Report
        if: always()
        run: |
          allure generate allure-results -o allure-report --clean
      
      - name: Deploy to GitHub Pages
        if: always()
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./allure-report
          destination_dir: allure-report
```

**訪問報告**:
```
https://<username>.github.io/<repo>/allure-report/
```

---

### 保留多次執行記錄

```yaml
- name: Copy Allure History
  if: always()
  run: |
    if [ -d "gh-pages/allure-report/history" ]; then
      cp -r gh-pages/allure-report/history allure-results/
    fi

- name: Generate Allure Report
  if: always()
  run: |
    allure generate allure-results -o allure-report --clean
```

---

## 本專案範例

### 測試檔案示範

```python
# tests/integration/test_api_workflow.py
import pytest
import allure

@allure.feature("API Workflow")
@allure.severity(allure.severity_level.CRITICAL)
class TestAPIWorkflow:
    
    @allure.story("Multi-turn Conversation")
    @allure.title("測試多輪對話流程")
    @allure.description("驗證系統能否正確處理多輪對話並保留上下文")
    @pytest.mark.integration
    def test_multi_turn_conversation(self, ollama_client):
        messages = []
        
        with allure.step("第一輪對話：打招呼"):
            messages.append({"role": "user", "content": "你好"})
            response1 = ollama_client.chat(messages=messages)
            allure.attach(response1.text, "回應 1", allure.attachment_type.TEXT)
            messages.append({"role": "assistant", "content": response1.content})
        
        with allure.step("第二輪對話：告知名字"):
            messages.append({"role": "user", "content": "我叫 Alice"})
            response2 = ollama_client.chat(messages=messages)
            allure.attach(response2.text, "回應 2", allure.attachment_type.TEXT)
            messages.append({"role": "assistant", "content": response2.content})
        
        with allure.step("第三輪對話：驗證記憶"):
            messages.append({"role": "user", "content": "我叫什麼名字？"})
            response3 = ollama_client.chat(messages=messages)
            allure.attach(response3.text, "回應 3", allure.attachment_type.TEXT)
            
            assert "Alice" in response3.content, "LLM 未記住使用者名字"
```

### 執行與查看

```bash
# 執行整合測試並生成 Allure 報告
pytest tests/integration/ --alluredir=allure-results

# 開啟報告
allure serve allure-results
```

**報告顯示**:
```
✅ TestAPIWorkflow::test_multi_turn_conversation (12.3s)
  Feature: API Workflow
  Story: Multi-turn Conversation
  Severity: Critical
  
  Steps:
  ├── ✅ 第一輪對話：打招呼 (3.2s)
  │   └── 📎 回應 1 (text/plain)
  ├── ✅ 第二輪對話：告知名字 (4.5s)
  │   └── 📎 回應 2 (text/plain)
  └── ✅ 第三輪對話：驗證記憶 (4.6s)
      └── 📎 回應 3 (text/plain)
```

---

## 常見問題

### Q1: 報告不顯示中文

**解決方案**:

```python
# conftest.py
import pytest

def pytest_collection_modifyitems(items):
    for item in items:
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
```

---

### Q2: 報告檔案過大

**原因**: 附加了過多或過大的附件

**解決方案**:

```python
# 限制附件大小
def attach_if_small(data, name, attachment_type):
    if len(data) < 1024 * 100:  # 100 KB
        allure.attach(data, name, attachment_type)
```

---

### Q3: 歷史趨勢不顯示

**解決方案**:

```bash
# 確保每次生成報告前複製歷史
cp -r allure-report/history allure-results/history
allure generate allure-results -o allure-report --clean
```

---

## 進階功能

### 1. **參數化測試顯示**

```python
@pytest.mark.parametrize("language,expected", [
    ("en", "Hello"),
    ("zh", "你好"),
    ("ja", "こんにちは"),
])
def test_greeting(language, expected):
    result = get_greeting(language)
    assert result == expected
```

**報告顯示**:
```
✅ test_greeting[en-Hello]
✅ test_greeting[zh-你好]
✅ test_greeting[ja-こんにちは]
```

---

### 2. **動態標題與描述**

```python
import allure

@allure.title("測試 {model} 模型的回應")
@pytest.mark.parametrize("model", ["llama3", "mistral", "gemma"])
def test_model_response(model):
    pass
```

**報告顯示**:
```
✅ 測試 llama3 模型的回應
✅ 測試 mistral 模型的回應
✅ 測試 gemma 模型的回應
```

---

### 3. **子步驟（Nested Steps）**

```python
@allure.step("主步驟：完整測試流程")
def main_workflow():
    sub_step_1()
    sub_step_2()

@allure.step("子步驟 1：初始化")
def sub_step_1():
    pass

@allure.step("子步驟 2：執行")
def sub_step_2():
    pass
```

**報告顯示**:
```
✅ 主步驟：完整測試流程
  ├── ✅ 子步驟 1：初始化
  └── ✅ 子步驟 2：執行
```

---

## 參考資源

- [Allure 官方文件](https://docs.qameta.io/allure/)
- [allure-pytest GitHub](https://github.com/allure-framework/allure-python)
- [Allure Docker Service](https://github.com/fescobar/allure-docker-service)

---

**維護者**: @howie0721  
**最後更新**: 2025-11-04

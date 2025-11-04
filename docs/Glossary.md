# Glossary (術語表)

## A

### API (Application Programming Interface)
應用程式介面，允許不同軟體之間互相溝通的介面規範。

### AAA Pattern (Arrange-Act-Assert)
測試設計模式，將測試分為三個階段：準備（Arrange）、執行（Act）、驗證（Assert）。

### Allure
開源測試報告框架，提供美觀且互動式的測試結果視覺化。

### Assertion
斷言，用於驗證測試結果是否符合預期的語句（如 `assert result == expected`）。

---

## B

### Boundary Testing
邊界測試，測試輸入值的邊界條件（最小值、最大值、空值、特殊字元等）。

### Bug
程式錯誤或缺陷，導致系統行為不符合預期。

### Black
Python 程式碼自動格式化工具，強制執行一致的程式碼風格。

---

## C

### CI/CD (Continuous Integration/Continuous Deployment)
持續整合/持續部署，自動化構建、測試、部署流程。

### Chat Completion
聊天補全，LLM 根據輸入的對話歷史生成回應的功能。

### Containerization
容器化，使用 Docker 等技術將應用程式及其依賴打包成獨立可執行的容器。

### Coverage (測試覆蓋率)
衡量測試執行時覆蓋了多少程式碼的指標，包括行覆蓋、分支覆蓋等。

### Conftest.py
Pytest 的特殊檔案，用於定義共用的 fixtures 和設定。

---

## D

### Docker
容器化平台，用於打包和執行應用程式及其依賴環境。

### Docstring
Python 函式、類別、模組的文件字串，用於說明用途、參數、回傳值等。

---

## E

### E2E Testing (End-to-End Testing)
端到端測試，從使用者角度測試完整的業務流程。

### Environment Variable
環境變數，用於配置應用程式行為的外部變數（如 `API_URL`, `TIMEOUT`）。

---

## F

### Fixture
Pytest 的測試前置作業機制，用於準備測試所需的資源（如資料庫連線、測試資料）。

### Flake8
Python 程式碼檢查工具，檢測語法錯誤、風格問題、複雜度等。

### Flaky Test
不穩定測試，有時通過有時失敗的測試，通常由於隨機性或外部依賴不穩定。

---

## G

### GitHub Actions
GitHub 提供的 CI/CD 平台，透過 YAML 定義自動化工作流程。

### GitHub Pages
GitHub 提供的靜態網站託管服務，常用於部署文件或測試報告。

---

## H

### HTTP Status Code
HTTP 狀態碼，表示 HTTP 請求的結果（如 200 成功、404 未找到、500 伺服器錯誤）。

---

## I

### Integration Testing
整合測試，測試多個模組或元件之間的互動。

### ISO 8601
國際標準日期時間格式（如 `2025-11-04T14:30:00Z`）。

---

## J

### JMeter
Apache JMeter，開源效能測試工具，用於模擬大量使用者請求。

### JSON (JavaScript Object Notation)
輕量級資料交換格式，易於人類閱讀和機器解析。

---

## L

### LLM (Large Language Model)
大型語言模型，如 LLaMA、GPT、Gemini 等，能夠理解和生成人類語言。

### Llama
Meta 開發的開源 LLM 系列（如 Llama 2、Llama 3）。

### Localhost
本地主機，指向當前電腦的網路位址（通常為 `127.0.0.1` 或 `localhost`）。

---

## M

### Marker
Pytest 標記，用於分類測試（如 `@pytest.mark.unit`, `@pytest.mark.slow`）。

### Mock
模擬物件，用於在測試中替代真實的外部依賴（如資料庫、API）。

### MyPy
Python 靜態型別檢查工具，檢查型別提示的正確性。

---

## N

### Nightly Build
每日構建，通常在夜間執行完整的測試套件。

---

## O

### Ollama
開源工具，用於在本地執行 LLM（如 Llama、Mistral、Gemini）。

---

## P

### Parametrize
Pytest 參數化，使用 `@pytest.mark.parametrize` 以不同參數執行同一測試。

### PEP 8
Python Enhancement Proposal 8，Python 官方程式碼風格指南。

### Prompt
提示詞，輸入給 LLM 的文字，用於引導 LLM 生成回應。

### Pull Request (PR)
拉取請求，在 Git 工作流程中，將變更合併到主分支前的審查流程。

### Pytest
Python 測試框架，提供簡潔的測試撰寫與執行方式。

---

## R

### Regression Testing
回歸測試，確保新變更不會破壞現有功能。

### Retry
重試機制，測試失敗時自動重新執行（如 `@pytest.mark.flaky(reruns=3)`）。

---

## S

### Scope (Fixture Scope)
Fixture 的作用範圍：
- `function`: 每個測試函式執行一次
- `class`: 每個測試類別執行一次
- `module`: 每個測試模組執行一次
- `session`: 整個測試期間執行一次

### Security Testing
安全性測試，測試系統的安全性（如防注入攻擊、資料洩漏）。

### Skip
跳過測試，使用 `@pytest.mark.skip` 或 `pytest.skip()` 暫時不執行某些測試。

### Snapshot Testing
快照測試，將測試結果與預先儲存的「快照」比對。

### Streaming
串流，LLM 逐步生成回應而非一次性回傳完整結果。

---

## T

### Temperature
LLM 生成參數，控制回應的隨機性（0.0 = 確定性，1.0 = 高隨機性）。

### Test Fixture
見 **Fixture**。

### Test Pyramid
測試金字塔，測試策略模型，強調大量單元測試、適量整合測試、少量端到端測試。

### Timeout
超時，請求或操作超過指定時間未完成時的處理機制。

### Token
LLM 處理的最小文字單位（約為一個字或 4 個字元）。

### Type Hints
型別提示，Python 3.5+ 引入的語法，用於標註變數與函式的型別。

---

## U

### Unit Testing
單元測試，測試最小可測試單元（如函式、類別）。

### Usability Testing
易用性測試，評估系統的使用者體驗與易用性。

---

## V

### Validator
驗證器，用於檢查資料或回應是否符合預期格式的工具或函式。

### Virtual Environment
虛擬環境，隔離 Python 專案依賴的機制（如 `venv`, `virtualenv`）。

---

## W

### Workflow
工作流程，GitHub Actions 中定義的自動化流程（如 PR 測試、每日構建）。

---

## X

### Xdist
`pytest-xdist` 插件，用於並行執行 Pytest 測試。

---

## Y

### YAML (YAML Ain't Markup Language)
人類友好的資料序列化格式，常用於配置檔案（如 GitHub Actions workflows）。

---

## 常見縮寫

| 縮寫 | 全名 | 中文 |
|------|------|------|
| API | Application Programming Interface | 應用程式介面 |
| CI/CD | Continuous Integration/Continuous Deployment | 持續整合/持續部署 |
| E2E | End-to-End | 端到端 |
| HTTP | Hypertext Transfer Protocol | 超文本傳輸協定 |
| JSON | JavaScript Object Notation | JavaScript 物件表示法 |
| LLM | Large Language Model | 大型語言模型 |
| PR | Pull Request | 拉取請求 |
| TDD | Test-Driven Development | 測試驅動開發 |
| URL | Uniform Resource Locator | 統一資源定位符 |
| UUID | Universally Unique Identifier | 通用唯一識別碼 |

---

## 測試相關術語對照

| 英文 | 中文 | 說明 |
|------|------|------|
| Arrange | 準備 | AAA 模式第一階段 |
| Act | 執行 | AAA 模式第二階段 |
| Assert | 驗證 | AAA 模式第三階段 |
| Blocker | 阻斷性 | 最高嚴重性等級 |
| Critical | 關鍵性 | 高嚴重性等級 |
| Flaky | 不穩定 | 測試結果不一致 |
| Mock | 模擬 | 替代真實依賴 |
| Stub | 存根 | 預定義回應的模擬物件 |
| Spy | 監視 | 記錄呼叫的模擬物件 |

---

## Pytest Marker 對照

| Marker | 用途 |
|--------|------|
| `@pytest.mark.unit` | 單元測試 |
| `@pytest.mark.integration` | 整合測試 |
| `@pytest.mark.e2e` | 端到端測試 |
| `@pytest.mark.boundary` | 邊界測試 |
| `@pytest.mark.security` | 安全性測試 |
| `@pytest.mark.regression` | 回歸測試 |
| `@pytest.mark.compatibility` | 相容性測試 |
| `@pytest.mark.error_handling` | 錯誤處理測試 |
| `@pytest.mark.usability` | 易用性測試 |
| `@pytest.mark.slow` | 慢速測試 |
| `@pytest.mark.skip` | 跳過測試 |
| `@pytest.mark.xfail` | 預期失敗 |
| `@pytest.mark.parametrize` | 參數化測試 |

---

**維護者**: @howie0721  
**最後更新**: 2025-11-04

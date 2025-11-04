# Test Framework Architecture

## 系統架構概覽

本測試框架採用分層架構設計，遵循 SOLID 原則與測試金字塔最佳實踐。

### 整體架構圖

```
┌─────────────────────────────────────────────────────────┐
│                    CI/CD Pipeline                        │
│  (GitHub Actions: PR Tests + Nightly Tests)             │
└──────────────────┬──────────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────────┐
│              Test Execution Layer                        │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │  Pytest  │  │ Allure   │  │ JMeter   │              │
│  │  Runner  │  │ Reporter │  │ Runner   │              │
│  └──────────┘  └──────────┘  └──────────┘              │
└──────────────────┬──────────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────────┐
│              Test Organization Layer                     │
│  ┌───────────────────────────────────────────────┐      │
│  │  Test Suites (Marker-based)                   │      │
│  │  • unit  • boundary  • compatibility          │      │
│  │  • error_handling  • integration  • e2e       │      │
│  │  • regression  • security  • usability        │      │
│  └───────────────────────────────────────────────┘      │
└──────────────────┬──────────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────────┐
│              Test Implementation Layer                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  Test Cases  │  │   Fixtures   │  │   Helpers    │  │
│  │  (tests/*/)  │  │ (conftest.py)│  │ (helpers/)   │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└──────────────────┬──────────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────────┐
│              Service Abstraction Layer                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ OllamaClient │  │  Validator   │  │SchemaValidator│ │
│  │   (API封裝)   │  │  (斷言工具)  │  │  (JSON驗證)  │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└──────────────────┬──────────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────────┐
│              Target System Under Test                    │
│                   Ollama LLM API                         │
│              (http://localhost:11434)                    │
└─────────────────────────────────────────────────────────┘
```

## 核心設計原則

### 1. 關注點分離 (Separation of Concerns)

- **測試邏輯層**：純粹的業務斷言與驗證
- **服務抽象層**：API 呼叫封裝，隔離變更
- **資料管理層**：Fixtures 與測試資料集中管理

### 2. 可維護性 (Maintainability)

- **DRY 原則**：共用邏輯抽取至 `helpers/` 與 `conftest.py`
- **模組化設計**：每個測試檔案職責單一、功能明確
- **標記系統**：透過 pytest markers 靈活組合測試集

### 3. 可擴展性 (Extensibility)

- **插件化**：支援新增自訂 fixtures、validators
- **多環境支援**：透過 `.env` 切換不同測試環境
- **多模型支援**：OllamaClient 可擴展支援其他 LLM

### 4. 可靠性 (Reliability)

- **並行執行**：pytest-xdist 提升測試速度
- **失敗隔離**：測試間相互獨立，無順序依賴
- **重試機制**：針對不穩定測試可加 `@pytest.mark.flaky`

## 目錄結構說明

```
Local_LLM_test/
├── .github/workflows/       # CI/CD 配置
│   ├── pr-tests.yml         # PR 快速測試
│   ├── nightly-tests.yml    # 定時完整測試
│   └── manual-tests.yml     # 手動觸發測試
│
├── docs/                    # 文件目錄
│   ├── Architecture.md      # 本文件
│   ├── Test_Strategy.md     # 測試策略
│   └── ...
│
├── helpers/                 # 測試輔助工具
│   ├── __init__.py
│   └── test_helper.py       # 通用 helper 函數
│
├── tests/                   # 測試套件根目錄
│   ├── conftest.py          # 全域 fixtures
│   ├── fixtures/            # 測試資料
│   │   ├── prompts_multilingual.json
│   │   └── prompts_specialchar.json
│   │
│   ├── unit/                # 單元測試
│   ├── boundary/            # 邊界值測試
│   ├── compatibility/       # 相容性測試
│   ├── error_handling/      # 錯誤處理測試
│   ├── integration/         # 整合測試
│   ├── e2e/                 # 端對端測試
│   ├── regression/          # 回歸測試
│   ├── security/            # 安全性測試
│   ├── usability/           # 易用性測試
│   ├── performance/         # 效能測試 (JMeter)
│   └── stability/           # 穩定性測試 (JMeter)
│
├── pytest.ini               # Pytest 配置
├── requirements.txt         # Python 依賴
├── .env.example             # 環境變數範本
└── Readme.md                # 專案首頁

```

## 關鍵元件說明

### conftest.py

提供全域 fixtures，包括：

- **ollama_client**: OllamaClient 實例，封裝 API 呼叫
- **validator**: 通用驗證器，提供斷言方法
- **schema_validator**: JSON schema 驗證器
- **batch_helper**: 批次執行工具
- **test_helper**: 測試輔助函數

### OllamaClient

```python
class OllamaClient:
    def chat(messages, model="llama3", timeout=60)
    def generate(prompt, model="llama3", timeout=60)
    def version()
    def get_version()
```

### Validator

```python
class Validator:
    def assert_status_code(response, expected_code)
    def assert_json_field(data, field_name)
    def assert_contains_keywords(text, keywords)
    def assert_non_empty_string(text, field_name)
    def get_chat_reply(response)
    def get_generate_reply(response)
```

## 資料流動

```
1. Pytest 收集測試 (根據 markers)
       ↓
2. 執行 conftest.py 建立 fixtures
       ↓
3. 注入 fixtures 到測試函數
       ↓
4. 測試呼叫 OllamaClient → Ollama API
       ↓
5. Validator 驗證回應
       ↓
6. Allure 收集結果與附件
       ↓
7. CI/CD 發布報告到 GitHub Pages
```

## 擴展指南

### 新增測試分類

1. 在 `tests/` 下建立新資料夾（如 `tests/accessibility/`）
2. 在 `pytest.ini` 註冊新 marker
3. 在 CI workflow 中加入新的測試組合

### 新增測試資料

1. 在 `tests/fixtures/` 加入 JSON 檔案
2. 使用 `@pytest.mark.parametrize` 讀取
3. 範例參考 `test_multilingual_input_schema.py`

### 新增自訂 Validator

```python
# 在 conftest.py 或 helpers/ 中
class CustomValidator:
    def assert_custom_rule(self, data):
        # 自訂驗證邏輯
        pass

@pytest.fixture
def custom_validator():
    return CustomValidator()
```

## 效能最佳化

- **並行執行**: `pytest -n auto`（利用多核心）
- **失敗快速停止**: `pytest --maxfail=5`（發現 5 個失敗即停止）
- **快取機制**: pytest 自動快取失敗測試，下次先執行
- **分組策略**: PR 測試跑快速測試，nightly 跑完整測試

## 安全性考量

- **敏感資訊**: 使用 `.env` 管理，不提交到 git
- **API Key**: 透過 GitHub Secrets 注入 CI
- **測試隔離**: 每個測試獨立，避免資料洩漏
- **權限控管**: GitHub Actions 使用最小權限原則

## 監控與告警

- **Allure 報告**: 視覺化測試結果與趨勢
- **GitHub Actions**: 失敗時自動通知（可整合 Slack/Teams）
- **Coverage 報告**: 追蹤測試覆蓋率變化
- **Performance 基線**: JMeter 報告追蹤效能退化

## 技術棧

| 層級 | 技術 | 版本 |
|------|------|------|
| 測試框架 | Pytest | 7.4+ |
| 並行執行 | pytest-xdist | 3.3+ |
| 報告工具 | Allure | 2.13+ |
| 效能測試 | JMeter | 5.x |
| CI/CD | GitHub Actions | - |
| 受測系統 | Ollama | latest |
| 語言 | Python | 3.10+ |

---

**維護者**: @howie0721  
**最後更新**: 2025-11-04

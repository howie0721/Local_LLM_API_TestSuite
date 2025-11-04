# Local LLM API Test Suite

[![PR Tests](https://github.com/<your-org>/<repo>/actions/workflows/pr-tests.yml/badge.svg)](https://github.com/<your-org>/<repo>/actions/workflows/pr-tests.yml)
[![Nightly Tests](https://github.com/<your-org>/<repo>/actions/workflows/nightly-tests.yml/badge.svg)](https://github.com/<your-org>/<repo>/actions/workflows/nightly-tests.yml)

> 專業級 Local LLM（Ollama）API 自動化測試框架，涵蓋單元、整合、E2E、回歸、安全性等多層次測試。

## 📋 目錄

- [專案簡介](#專案簡介)
- [測試架構](#測試架構)
- [快速開始](#快速開始)
- [測試分類](#測試分類)
- [CI/CD](#cicd)
- [報告查看](#報告查看)
- [進階使用](#進階使用)

---

## 🎯 專案簡介

本專案針對 Local LLM API（以 Ollama 為主）建立完整的自動化測試體系，遵循測試金字塔原則，確保：

- ✅ API 功能正確性
- ✅ 多語言與特殊字元相容性
- ✅ 邊界值與錯誤處理穩健性
- ✅ 回歸測試防止功能退化
- ✅ 安全性與隱私保護
- ✅ 性能與穩定性指標

---

## 🏗️ 測試架構

```
測試金字塔
    🔺
   /E2E\          端對端測試（情境完整性）
  /-----\
 /整合測試\        多模組協作驗證
/----------\
|  單元測試  |      基礎功能驗證
|__________|

橫切關注點：
├─ 安全性測試（Security）
├─ 效能測試（Performance）
├─ 穩定性測試（Stability）
└─ 易用性測試（Usability）
```

詳細架構請參考：[tests/README.md](tests/README.md)

---

## 🚀 快速開始

### 前置需求

- Python 3.10+
- Ollama（本地執行）或 Docker
- Git

### 安裝

```bash
# 克隆專案
git clone <repo-url>
cd Local_LLM_test

# 安裝依賴
pip install -r requirements.txt

# 啟動 Ollama（本地）
ollama serve
ollama pull llama3

# 或使用 Docker
docker run -d -p 11434:11434 --name ollama ollama/ollama:latest
docker exec ollama ollama pull llama3
```

### 執行測試

```bash
# 快速測試（單元 + 邊界 + 相容性 + 錯誤處理）
pytest -m "unit or boundary or compatibility or error_handling" -v

# 完整測試
pytest -v

# 特定標記
pytest -m security -v
pytest -m e2e -v

# 並行執行（加速）
pytest -n auto -v

# 生成 Allure 報告
pytest --alluredir=allure-results
allure serve allure-results
```

---

## 📦 測試分類

| 分類 | 標記 | 檔案數 | 說明 |
|------|------|:------:|------|
| 🧪 單元測試 | `unit` | 6 | API 基礎功能驗證 |
| 📏 邊界值測試 | `boundary` | 4 | 輸入極限與邊界條件 |
| 🔄 相容性測試 | `compatibility` | 4 | 多語言、特殊字元、Schema |
| ⚠️ 錯誤處理測試 | `error_handling` | 4 | 異常情境與錯誤回應 |
| 🔗 整合測試 | `integration` | 4 | 多階段流程串接 |
| 🎭 端對端測試 | `e2e` | 4 | 完整業務情境模擬 |
| 🔄 回歸測試 | `regression` | 4 | 防止功能退化 |
| 🔒 安全性測試 | `security` | 4 | Prompt Injection、敏感資訊 |
| 👥 易用性測試 | `usability` | 4 | 回應格式可讀性 |
| ⚡ 效能測試 | `perf` | 4 | JMeter 負載測試 |
| 🛡️ 穩定性測試 | `stability` | 4 | 長時運行與記憶體監控 |

**總計：42 個測試檔案**

詳細測試清單：[tests/README.md](tests/README.md)

---

## 🔄 CI/CD

### 自動化測試流程

本專案使用 GitHub Actions 實現三階段測試策略：

#### 1️⃣ PR 快速測試（5-10 分鐘）

- **觸發時機：** 每次 Pull Request
- **執行範圍：** `unit` + `boundary` + `compatibility` + `error_handling`
- **目的：** 快速回饋，確保基礎功能無誤

#### 2️⃣ Nightly 完整測試（每日 00:00 UTC）

- **觸發時機：** 定時排程 + 手動觸發
- **執行範圍：** `e2e` + `regression` + `security` + `integration` + `usability`
- **目的：** 深度驗證，防止功能退化與安全漏洞

#### 3️⃣ 手動測試（按需執行）

- **觸發時機：** GitHub Actions UI
- **執行範圍：** 自訂 markers、Python 版本、並行設定
- **目的：** 靈活測試特定功能或環境

詳細 CI/CD 設定：[docs/CI_CD_Setup_Guide.md](docs/CI_CD_Setup_Guide.md)

---

## 📊 報告查看

### Allure 報告（推薦）

```bash
# 本地生成並開啟
pytest --alluredir=allure-results
allure serve allure-results
```

### GitHub Pages（CI 自動發布）

- **PR 測試報告：** `https://<your-org>.github.io/<repo>/pr-tests/`
- **Nightly 測試報告：** `https://<your-org>.github.io/<repo>/nightly-tests/`
- **手動測試報告：** `https://<your-org>.github.io/<repo>/manual-tests/`

### JMeter Dashboard（效能測試）

```bash
# 執行效能測試
python run_jmeter_dashboard.py

# 查看報告
# 瀏覽器開啟 jmeter-dashboard-report/performance/index.html
```

---

## 🔧 進階使用

### 自訂測試組合

```bash
# 只跑安全性與回歸
pytest -m "security or regression" -v

# 排除慢測試
pytest -m "not slow" -v

# 指定檔案
pytest tests/unit/test_connection.py -v
```

### 環境變數設定

```bash
# 複製範本
cp .env.example .env

# 編輯設定
# OLLAMA_BASE_URL=http://localhost:11434
# OLLAMA_MODEL=llama3
# OLLAMA_TIMEOUT=120
```

### 並行執行優化

```bash
# 自動偵測 CPU 核心數
pytest -n auto

# 指定並行數
pytest -n 4

# 關閉並行（偵錯用）
pytest
```

### 測試覆蓋率

```bash
# 安裝 coverage
pip install pytest-cov

# 生成覆蓋率報告
pytest --cov=. --cov-report=html
# 查看 htmlcov/index.html
```

---

## 📚 文件索引

- [測試架構與金字塔](tests/README.md)
- [CI/CD 設定指南](docs/CI_CD_Setup_Guide.md)
- [測試策略](docs/Test_Strategy.md)
- [如何執行測試](docs/How_To_Run.md)
- [貢獻指南](docs/Contributing.md)
- [故障排除](docs/Troubleshooting.md)

---

## 🤝 貢獻

歡迎提交 Issue 或 Pull Request！請參考 [Contributing.md](docs/Contributing.md) 了解貢獻流程。

---

## 📝 License

MIT License

---

## 🔗 相關連結

- [Ollama 官方文件](https://ollama.ai/docs)
- [Pytest 官方文件](https://docs.pytest.org/)
- [Allure 報告文件](https://docs.qameta.io/allure/)
- [GitHub Actions 文件](https://docs.github.com/en/actions)

---

**維護者：** @howie  
**最後更新：** 2025-11-04

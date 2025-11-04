# How To Run Tests

## 快速開始

### 前置需求

```bash
# 檢查 Python 版本
python --version  # 需要 3.10+

# 檢查 Ollama 是否運行
curl http://localhost:11434/api/version
```

### 安裝依賴

```bash
# 安裝測試依賴
pip install -r requirements.txt

# 或使用 虛擬環境（推薦）
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

### 啟動 Ollama

```bash
# 方法 1: 本地安裝
ollama serve
ollama pull llama3

# 方法 2: Docker（推薦）
docker run -d --name ollama -p 11434:11434 ollama/ollama:latest
docker exec ollama ollama pull llama3
```

---

## 執行測試

### 基礎用法

```bash
# 執行所有測試
pytest

# 詳細輸出
pytest -v

# 顯示 print 輸出
pytest -s

# 只顯示失敗測試
pytest -v --tb=short
```

### 按標記執行

```bash
# PR 快速測試（單元+邊界+相容性+錯誤處理）
pytest -m "unit or boundary or compatibility or error_handling" -v

# Nightly 完整測試
pytest -m "e2e or regression or security or integration or usability" -v

# 單一標記
pytest -m unit -v
pytest -m security -v
pytest -m e2e -v

# 排除特定標記
pytest -m "not slow" -v
```

### 按目錄執行

```bash
# 執行特定目錄
pytest tests/unit/ -v
pytest tests/security/ -v

# 執行特定檔案
pytest tests/unit/test_connection.py -v

# 執行特定測試函數
pytest tests/unit/test_connection.py::test_TC_UNIT_0001_connection -v
```

### 並行執行

```bash
# 自動偵測 CPU 核心數
pytest -n auto

# 指定並行數量
pytest -n 4

# 並行 + 標記組合
pytest -m "unit or boundary" -n auto -v
```

### 失敗處理

```bash
# 首次失敗即停止
pytest -x

# 最多允許 5 個失敗
pytest --maxfail=5

# 只重跑上次失敗的測試
pytest --lf

# 先跑上次失敗，再跑其他
pytest --ff
```

---

## Allure 報告

### 生成報告

```bash
# 執行測試並生成 Allure 資料
pytest --alluredir=allure-results

# 啟動 Allure server 查看報告（互動式）
allure serve allure-results

# 生成靜態 HTML 報告
allure generate allure-results -o allure-report --clean

# 開啟靜態報告
# Windows
start allure-report/index.html
# Mac
open allure-report/index.html
# Linux
xdg-open allure-report/index.html
```

### Allure 進階選項

```bash
# 清除舊報告
pytest --alluredir=allure-results --clean-alluredir

# 加入環境資訊
pytest --alluredir=allure-results --allure-env TEST_ENV=local

# 附加截圖/日誌
# （測試中使用 allure.attach）
```

---

## JMeter 效能測試

### 安裝 JMeter

```bash
# Windows: 下載並解壓 https://jmeter.apache.org/download_jmeter.cgi
# Mac: brew install jmeter
# Linux: apt-get install jmeter
```

### 執行效能測試

```bash
# GUI 模式（調試用）
jmeter -t tests/performance/ollama_llama3_single_request.jmx

# CLI 模式（正式測試）
jmeter -n -t tests/performance/ollama_llama3_concurrent_requests.jmx \
       -l results.jtl \
       -e -o jmeter-report

# 使用腳本自動生成報告
python run_jmeter_dashboard.py
```

### 查看 JMeter 報告

```bash
# 開啟 Dashboard
# Windows
start jmeter-dashboard-report/performance/index.html
# Mac/Linux
open jmeter-dashboard-report/performance/index.html
```

---

## 測試覆蓋率

### 安裝 Coverage 工具

```bash
pip install pytest-cov
```

### 生成覆蓋率報告

```bash
# 終端顯示覆蓋率
pytest --cov=. --cov-report=term

# 生成 HTML 報告
pytest --cov=. --cov-report=html

# 查看報告
start htmlcov/index.html  # Windows
open htmlcov/index.html   # Mac

# 生成 XML（for CI/CD）
pytest --cov=. --cov-report=xml
```

---

## 環境變數設定

### 複製範本

```bash
cp .env.example .env
```

### 編輯 .env

```ini
# Ollama API 設定
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3
OLLAMA_TIMEOUT=120

# 測試設定
TEST_ENV=local
TEST_PARALLEL=auto
TEST_MAX_WORKERS=4
```

### 使用環境變數

```bash
# Linux/Mac
export OLLAMA_BASE_URL=http://localhost:11434
pytest -v

# Windows PowerShell
$env:OLLAMA_BASE_URL="http://localhost:11434"
pytest -v

# 或直接在命令中指定
OLLAMA_BASE_URL=http://localhost:11434 pytest -v
```

---

## 偵錯技巧

### 1. 使用 pdb 偵錯器

```bash
# 進入失敗測試的偵錯模式
pytest --pdb

# 進入所有測試的偵錯模式
pytest --trace
```

### 2. 顯示詳細輸出

```bash
# 顯示 print 與 logging
pytest -s -v

# 顯示完整錯誤堆疊
pytest --tb=long

# 顯示本地變數
pytest -l
```

### 3. 只執行特定測試

```bash
# 使用關鍵字過濾
pytest -k "connection" -v
pytest -k "security and not slow" -v

# 使用節點 ID
pytest tests/unit/test_connection.py::test_TC_UNIT_0001_connection -v
```

### 4. 查看測試收集資訊

```bash
# 查看會執行哪些測試（不執行）
pytest --collect-only

# 查看特定標記的測試
pytest -m unit --collect-only
```

---

## 常見問題排解

### 1. Ollama 連線失敗

```bash
# 檢查 Ollama 是否運行
curl http://localhost:11434/api/version

# 檢查防火牆
netstat -an | findstr 11434  # Windows
netstat -an | grep 11434     # Linux/Mac

# 重啟 Ollama
ollama serve  # 或重啟 Docker 容器
```

### 2. 測試超時

```bash
# 增加超時時間
pytest --timeout=300

# 或在測試中設定
@pytest.mark.timeout(300)
def test_long_running():
    pass
```

### 3. Import 錯誤

```bash
# 確認在專案根目錄
cd Local_LLM_test

# 確認 Python 路徑
python -c "import sys; print('\n'.join(sys.path))"

# 重新安裝依賴
pip install -r requirements.txt --force-reinstall
```

### 4. Allure 報告無法開啟

```bash
# 確認 Allure 已安裝
allure --version

# Windows: 下載並加入 PATH
# https://github.com/allure-framework/allure2/releases

# Mac
brew install allure

# Linux
apt-add-repository ppa:qameta/allure
apt-get update
apt-get install allure
```

---

## CI/CD 本地模擬

### 模擬 PR Tests

```bash
# 使用 Docker Ollama
docker run -d --name ollama -p 11434:11434 ollama/ollama:latest
docker exec ollama ollama pull llama3

# 執行 PR 測試
pytest -m "unit or boundary or compatibility or error_handling" \
       -v \
       --tb=short \
       --alluredir=allure-results \
       --maxfail=5 \
       -n auto

# 查看報告
allure serve allure-results
```

### 模擬 Nightly Tests

```bash
# 執行完整測試套件
pytest -m "e2e or regression or security or integration or usability" \
       -v \
       --tb=short \
       --alluredir=allure-results \
       -n auto

# 生成報告
allure serve allure-results
```

---

## 效能優化建議

### 1. 並行執行

```bash
# 使用所有 CPU 核心
pytest -n auto

# 保留一個核心給系統
pytest -n logical-1
```

### 2. 快取失敗測試

```bash
# Pytest 自動快取，優先執行上次失敗的測試
pytest --ff
```

### 3. 跳過慢測試

```bash
# 開發時跳過慢測試
pytest -m "not slow"

# 或在測試中標記
@pytest.mark.slow
def test_long_running():
    pass
```

### 4. 使用 pytest-xdist 進階選項

```bash
# 按檔案分組
pytest -n auto --dist loadfile

# 按類別分組
pytest -n auto --dist loadscope

# 按測試函數分組（預設）
pytest -n auto --dist load
```

---

## 進階用法

### 自訂 Pytest 參數

```ini
# pytest.ini
[pytest]
addopts = -ra -q --strict-markers
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
```

### 使用 Fixtures

```python
# conftest.py
@pytest.fixture(scope="session")
def ollama_client():
    # Session 級別，整個測試過程只建立一次
    return OllamaClient()

@pytest.fixture(scope="function")
def clean_data():
    # Function 級別，每個測試執行前都會執行
    yield
    # 清理邏輯
```

### 參數化測試

```python
@pytest.mark.parametrize("input,expected", [
    ("hello", "HELLO"),
    ("world", "WORLD"),
])
def test_upper(input, expected):
    assert input.upper() == expected
```

---

## 團隊協作建議

### 1. 本地開發

```bash
# 開發前先跑單元測試
pytest -m unit -v

# 提交前跑 PR 測試
pytest -m "unit or boundary or compatibility or error_handling" -v
```

### 2. 提交 PR

```bash
# 確保測試通過
pytest -m "unit or boundary or compatibility or error_handling" -v

# 生成報告（可選）
pytest --alluredir=allure-results
allure serve allure-results
```

### 3. Code Review

- ✅ 檢查測試覆蓋率是否符合標準
- ✅ 檢查是否有 Flaky tests
- ✅ 檢查測試執行時間是否合理

---

## 參考資源

- [Pytest 官方文件](https://docs.pytest.org/)
- [Allure 報告文件](https://docs.qameta.io/allure/)
- [JMeter 使用指南](https://jmeter.apache.org/usermanual/)
- [pytest-xdist 文件](https://pytest-xdist.readthedocs.io/)

---

**維護者**: @howie0721  
**最後更新**: 2025-11-04

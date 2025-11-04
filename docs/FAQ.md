# Frequently Asked Questions (FAQ)

## 安裝與設定

### Q1: 安裝依賴時出現錯誤怎麼辦？

**A:** 常見解決方案：

```bash
# 1. 升級 pip
python -m pip install --upgrade pip

# 2. 清除快取重新安裝
pip cache purge
pip install -r requirements.txt --no-cache-dir

# 3. 使用虛擬環境（推薦）
python -m venv venv
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### Q2: 如何切換不同的 Python 版本？

**A:** 使用 pyenv (推薦) 或 Anaconda：

```bash
# pyenv
pyenv install 3.11.0
pyenv local 3.11.0

# Anaconda
conda create -n llm_test python=3.11
conda activate llm_test
```

### Q3: Ollama 安裝在哪裡？

**A:** 
- **本地安裝**: https://ollama.ai/download
- **Docker**: `docker pull ollama/ollama:latest`
- **驗證**: `curl http://localhost:11434/api/version`

---

## 測試執行

### Q4: 為什麼測試執行很慢？

**A:** 優化方案：

```bash
# 1. 使用並行執行
pytest -n auto

# 2. 只跑快速測試
pytest -m "unit or boundary"

# 3. 跳過慢測試
pytest -m "not slow"

# 4. 使用快取（重跑失敗測試）
pytest --lf
```

### Q5: 測試一直超時怎麼辦？

**A:** 

```bash
# 1. 增加全域超時
pytest --timeout=300

# 2. 檢查 Ollama 是否正常運行
curl http://localhost:11434/api/version

# 3. 檢查系統資源（CPU、記憶體）
# 4. 針對特定測試增加超時

@pytest.mark.timeout(120)
def test_long_running():
    pass
```

### Q6: 如何只執行失敗的測試？

**A:**

```bash
# 只重跑上次失敗的測試
pytest --lf

# 先跑上次失敗的，再跑其他
pytest --ff

# 記錄失敗測試
pytest --lf -v
```

---

## Ollama 相關

### Q7: Ollama 連線失敗 (Connection Refused)

**A:** 檢查清單：

```bash
# 1. 確認 Ollama 正在運行
# Windows/Mac: 檢查系統托盤
# Linux: systemctl status ollama

# 2. 確認埠號正確
netstat -an | findstr 11434  # Windows
netstat -an | grep 11434     # Linux/Mac

# 3. 檢查防火牆設定

# 4. 重啟 Ollama
# 本地: ollama serve
# Docker: docker restart ollama
```

### Q8: 模型拉取失敗或很慢

**A:**

```bash
# 1. 檢查網路連線
curl https://ollama.ai

# 2. 使用代理（如需要）
export HTTP_PROXY=http://proxy.example.com:8080
export HTTPS_PROXY=http://proxy.example.com:8080

# 3. 手動拉取模型
ollama pull llama3

# 4. 使用較小的模型測試
ollama pull llama3:8b
```

### Q9: LLM 回應不穩定或錯誤

**A:**

```python
# 1. 使用關鍵字驗證取代精確比對
validator.assert_contains_keywords(reply, ["LLaMA", "AI"])

# 2. 標記為 flaky test
@pytest.mark.flaky(reruns=3)
def test_unstable_llm():
    pass

# 3. 增加溫度參數（讓回應更穩定）
response = ollama_client.chat(
    messages=messages,
    temperature=0.1  # 降低隨機性
)
```

---

## CI/CD

### Q10: GitHub Actions 失敗但本地測試通過

**A:** 常見原因：

1. **環境差異**
   ```yaml
   # 在 CI 中使用固定 Python 版本
   - uses: actions/setup-python@v5
     with:
       python-version: '3.11'
   ```

2. **依賴版本不同**
   ```bash
   # 固定版本號
   pytest==7.4.3  # 而非 pytest>=7.4.0
   ```

3. **Ollama 未就緒**
   ```yaml
   # 增加等待時間
   - name: Wait for Ollama
     run: |
       timeout 120 bash -c 'until curl -s http://localhost:11434/api/version; do sleep 2; done'
   ```

### Q11: Allure 報告無法發布到 GitHub Pages

**A:**

1. **檢查權限**
   - Settings → Actions → General
   - Workflow permissions: "Read and write permissions"

2. **確認分支存在**
   ```bash
   git branch -r | grep gh-pages
   ```

3. **手動建立 gh-pages 分支**
   ```bash
   git checkout --orphan gh-pages
   git rm -rf .
   git commit --allow-empty -m "Initial gh-pages"
   git push origin gh-pages
   ```

### Q12: CI 執行時間過長

**A:**

```yaml
# 1. 使用並行執行
- name: Run tests
  run: pytest -n auto

# 2. 分組執行
strategy:
  matrix:
    test-group: [unit, integration, e2e]
    
# 3. 使用快取
- uses: actions/cache@v3
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
```

---

## Allure 報告

### Q13: Allure 報告顯示亂碼

**A:**

```bash
# 1. 確認環境變數編碼
export LANG=zh_TW.UTF-8

# 2. 在測試中指定編碼
with open("file.txt", encoding="utf-8") as f:
    pass

# 3. Allure 配置
allure.environment(charset="UTF-8")
```

### Q14: Allure 報告中看不到測試歷史

**A:**

```bash
# 生成報告時保留歷史
allure generate allure-results -o allure-report --clean

# 不要使用 --clean，改用
allure generate allure-results -o allure-report
```

### Q15: 如何在 Allure 中加入自訂資訊？

**A:**

```python
import allure

@allure.title("自訂測試標題")
@allure.description("詳細說明")
@allure.severity(allure.severity_level.CRITICAL)
def test_example():
    allure.attach("額外資訊", name="備註", attachment_type=allure.attachment_type.TEXT)
    allure.step("步驟 1: 準備資料")
    allure.step("步驟 2: 執行測試")
```

---

## JMeter 效能測試

### Q16: JMeter 測試失敗怎麼辦？

**A:**

```bash
# 1. 檢查 Java 版本
java -version  # 需要 Java 8+

# 2. 增加 JMeter heap size
export JVM_ARGS="-Xms1024m -Xmx4096m"

# 3. 檢查 JMX 檔案路徑
ls -la tests/performance/*.jmx

# 4. 使用 GUI 模式偵錯
jmeter -t tests/performance/ollama_llama3_single_request.jmx
```

### Q17: JMeter 報告顯示錯誤率很高

**A:**

1. **降低併發數**
   - 調整 Thread Group 的 Number of Threads

2. **增加 Ramp-up 時間**
   - 讓請求逐步增加，避免瞬間壓力

3. **檢查系統資源**
   ```bash
   # CPU 使用率
   top
   
   # 記憶體使用
   free -m
   
   # 網路連線
   netstat -an | grep 11434
   ```

---

## 資料與 Fixtures

### Q18: 如何新增測試資料？

**A:**

```bash
# 1. 在 tests/fixtures/ 建立 JSON
cat > tests/fixtures/my_data.json << EOF
[
  {"prompt": "test1", "expected": "result1"},
  {"prompt": "test2", "expected": "result2"}
]
EOF

# 2. 在測試中使用
@pytest.mark.parametrize("item", json.load(open("fixtures/my_data.json")))
def test_with_data(item):
    assert item["expected"] in response
```

### Q19: Fixtures 如何共用？

**A:**

```python
# 在 conftest.py 定義（自動載入所有測試）
@pytest.fixture
def shared_data():
    return {"key": "value"}

# 在測試中使用
def test_example(shared_data):
    assert shared_data["key"] == "value"
```

---

## 程式碼品質

### Q20: 如何確保程式碼品質？

**A:**

```bash
# 1. 格式化
black .

# 2. Linting
flake8 tests/ helpers/

# 3. 型別檢查
mypy tests/

# 4. 測試覆蓋率
pytest --cov=. --cov-report=html

# 5. 安全性掃描
bandit -r tests/ helpers/
```

### Q21: Pre-commit Hook 設定

**A:**

```bash
# 1. 安裝 pre-commit
pip install pre-commit

# 2. 建立 .pre-commit-config.yaml
cat > .pre-commit-config.yaml << EOF
repos:
  - repo: https://github.com/psf/black
    rev: 23.0.0
    hooks:
      - id: black
  - repo: https://github.com/PyCQA/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
EOF

# 3. 安裝 hooks
pre-commit install

# 4. 手動執行
pre-commit run --all-files
```

---

## 效能優化

### Q22: 如何加快測試執行速度？

**A:**

```bash
# 1. 並行執行
pytest -n auto

# 2. 使用快取
pytest --cache-show
pytest --lf  # 只跑失敗的

# 3. 分層測試
# PR: 只跑 unit + boundary
# Nightly: 跑完整測試

# 4. 使用 Session 級別 fixtures
@pytest.fixture(scope="session")
def expensive_fixture():
    # 只建立一次
    return heavy_object()
```

### Q23: 記憶體使用過高怎麼辦？

**A:**

```python
# 1. 使用 Generator 取代 List
@pytest.mark.parametrize("item", 
    (item for item in get_large_dataset())  # Generator
)

# 2. 清理 Fixtures
@pytest.fixture
def data():
    obj = create_large_object()
    yield obj
    del obj  # 明確釋放

# 3. 使用 Function scope
@pytest.fixture(scope="function")  # 每個測試後清理
def fresh_data():
    return Data()
```

---

## 其他

### Q24: 如何貢獻程式碼？

**A:** 請參考 [Contributing Guide](Contributing.md)

### Q25: 在哪裡回報 Bug？

**A:** 請到 [GitHub Issues](https://github.com/howie0721/Local_LLM_API_TestSuite/issues) 建立 Issue，並提供：
- 錯誤訊息
- 重現步驟
- 環境資訊（Python 版本、OS、Ollama 版本）

### Q26: 支援哪些 LLM 模型？

**A:** 目前主要測試 `llama3`，但架構上支援所有 Ollama 模型：

```python
# 在測試中指定模型
response = ollama_client.chat(
    messages=messages,
    model="llama2"  # 或其他模型
)
```

### Q27: 可以用於其他 LLM API 嗎？

**A:** 可以！只需修改 `OllamaClient` 類別：

```python
class OpenAIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        
    def chat(self, messages, model="gpt-4"):
        # 呼叫 OpenAI API
        pass
```

---

## 聯絡方式

- **GitHub Issues**: https://github.com/howie0721/Local_LLM_API_TestSuite/issues
- **Discussions**: https://github.com/howie0721/Local_LLM_API_TestSuite/discussions
- **Email**: howie@example.com

---

**維護者**: @howie0721  
**最後更新**: 2025-11-04

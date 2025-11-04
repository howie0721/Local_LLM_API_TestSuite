# Troubleshooting Guide

## 常見錯誤與解決方案

### 連線相關

#### 錯誤: `Connection refused` 或 `Connection timeout`

**症狀**:
```
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): 
Max retries exceeded with url: /api/version
```

**可能原因**:
1. Ollama 服務未啟動
2. 埠號被佔用
3. 防火牆阻擋

**解決方案**:

```bash
# 1. 檢查 Ollama 是否運行
curl http://localhost:11434/api/version

# 2. 啟動 Ollama
ollama serve  # 本地
# 或
docker start ollama  # Docker

# 3. 檢查埠號佔用
netstat -ano | findstr 11434  # Windows
lsof -i :11434  # Mac/Linux

# 4. 檢查防火牆
# Windows: 控制台 → Windows Defender 防火牆
# Linux: sudo ufw status
```

---

#### 錯誤: `requests.exceptions.ReadTimeout`

**症狀**:
```
requests.exceptions.ReadTimeout: HTTPConnectionPool(host='localhost', port=11434): 
Read timed out. (read timeout=60)
```

**可能原因**:
1. Prompt 過長，LLM 處理時間超過 timeout
2. 系統資源不足（CPU/記憶體）
3. 模型未完全載入

**解決方案**:

```python
# 1. 增加 timeout
response = ollama_client.chat(
    messages=messages,
    timeout=180  # 從 60 增加到 180 秒
)

# 2. 檢查系統資源
# Windows: 工作管理員
# Linux: top, htop

# 3. 使用較小的模型
ollama pull llama3:8b  # 而非 llama3:70b
```

---

### 測試執行相關

#### 錯誤: `ModuleNotFoundError: No module named 'pytest'`

**症狀**:
```
ModuleNotFoundError: No module named 'pytest'
```

**解決方案**:

```bash
# 1. 確認在正確的虛擬環境
which python  # Linux/Mac
where python  # Windows

# 2. 安裝依賴
pip install -r requirements.txt

# 3. 確認安裝成功
pip list | grep pytest
```

---

#### 錯誤: `fixture 'ollama_client' not found`

**症狀**:
```
E       fixture 'ollama_client' not found
```

**可能原因**:
1. `conftest.py` 不在正確位置
2. Fixture 定義錯誤
3. Import 錯誤

**解決方案**:

```bash
# 1. 確認 conftest.py 存在
ls tests/conftest.py

# 2. 確認 fixture 定義
grep "def ollama_client" tests/conftest.py

# 3. 執行測試時在專案根目錄
cd Local_LLM_test
pytest tests/unit/test_connection.py
```

---

#### 錯誤: `INTERNALERROR> AttributeError: 'NoneType' object has no attribute 'get'`

**症狀**:
```
INTERNALERROR> AttributeError: 'NoneType' object has no attribute 'get'
```

**可能原因**:
1. API 回應為 None
2. JSON 解析失敗
3. Ollama 回應異常

**解決方案**:

```python
# 1. 加入防禦性檢查
response = ollama_client.chat(messages=messages)
if response is None:
    pytest.skip("API 回應為 None，跳過測試")

data = response.json()
if not data:
    pytest.skip("JSON 解析失敗，跳過測試")

# 2. 使用 try-except
try:
    reply = data["choices"][0]["message"]["content"]
except (KeyError, IndexError, TypeError) as e:
    pytest.fail(f"回應格式異常: {e}")
```

---

### Ollama 相關

#### 錯誤: `model 'llama3' not found`

**症狀**:
```
Error: model 'llama3' not found
```

**解決方案**:

```bash
# 1. 列出已安裝模型
ollama list

# 2. 拉取模型
ollama pull llama3

# 3. 確認模型可用
ollama run llama3 "Hello"

# 4. Docker 環境
docker exec ollama ollama pull llama3
```

---

#### 錯誤: LLM 回應不穩定或錯誤

**症狀**:
- 同樣的 prompt，回應內容每次不同
- 測試時通過，時而失敗（Flaky）

**解決方案**:

```python
# 1. 降低 temperature（增加穩定性）
response = ollama_client.chat(
    messages=messages,
    temperature=0.1  # 預設 0.8
)

# 2. 使用關鍵字驗證取代精確比對
# ❌ Bad
assert reply == "我是 LLaMA，一個 AI 助手。"

# ✅ Good
validator.assert_contains_keywords(reply, ["LLaMA", "AI", "助手"])

# 3. 標記為 flaky test
@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_unstable_llm():
    pass
```

---

### CI/CD 相關

#### 錯誤: GitHub Actions 權限不足

**症狀**:
```
remote: Permission to howie0721/Local_LLM_API_TestSuite.git denied to github-actions[bot].
```

**解決方案**:

1. **修改 Workflow 權限**
   - Settings → Actions → General
   - Workflow permissions: "Read and write permissions"
   - ✅ Allow GitHub Actions to create and approve pull requests

2. **確認 token 使用**
   ```yaml
   - uses: peaceiris/actions-gh-pages@v3
     with:
       github_token: ${{ secrets.GITHUB_TOKEN }}  # 確認此行存在
   ```

---

#### 錯誤: Docker Ollama 啟動失敗

**症狀**:
```
Error response from daemon: driver failed programming external connectivity
```

**解決方案**:

```bash
# 1. 停止現有容器
docker stop ollama
docker rm ollama

# 2. 確認埠號未被佔用
netstat -ano | findstr 11434

# 3. 重新啟動
docker run -d --name ollama -p 11434:11434 ollama/ollama:latest

# 4. 確認啟動成功
docker ps | grep ollama
docker logs ollama
```

---

#### 錯誤: Allure 報告生成失敗

**症狀**:
```
Error: Allure commandline not found
```

**解決方案**:

```bash
# 1. 安裝 Allure commandline
# Windows
# 下載並解壓到 C:\allure
# 加入 PATH

# Mac
brew install allure

# Linux
apt-add-repository ppa:qameta/allure
apt-get update
apt-get install allure

# 2. 確認安裝
allure --version

# 3. 生成報告
allure serve allure-results
```

---

### 效能相關

#### 問題: 測試執行速度過慢

**症狀**:
- 完整測試套件執行超過 30 分鐘
- 單一測試執行超過 10 秒

**解決方案**:

```bash
# 1. 使用並行執行
pytest -n auto  # 使用所有 CPU 核心

# 2. 只跑快速測試
pytest -m "unit or boundary"  # 跳過 E2E

# 3. 優化 fixtures scope
# conftest.py
@pytest.fixture(scope="session")  # 整個測試過程只建立一次
def ollama_client():
    return OllamaClient()

# 4. 使用快取
pytest --lf  # 只重跑失敗的測試
```

---

#### 問題: 記憶體使用過高

**症狀**:
```
MemoryError: Unable to allocate array
```

**解決方案**:

```python
# 1. 使用 Generator 取代 List
@pytest.mark.parametrize("item", 
    (item for item in large_dataset())  # Generator
)

# 2. 明確釋放資源
@pytest.fixture
def large_data():
    data = create_large_object()
    yield data
    del data  # 釋放記憶體

# 3. 使用 function scope
@pytest.fixture(scope="function")  # 每個測試後清理
def data():
    return Data()

# 4. 限制並行數
pytest -n 4  # 而非 -n auto
```

---

### JMeter 相關

#### 錯誤: `java.lang.OutOfMemoryError: Java heap space`

**症狀**:
```
java.lang.OutOfMemoryError: Java heap space
```

**解決方案**:

```bash
# 1. 增加 JVM heap size
export JVM_ARGS="-Xms1024m -Xmx4096m"

# 2. 或修改 jmeter.bat / jmeter.sh
set HEAP=-Xms1g -Xmx4g

# 3. 減少併發數
# 在 JMX 中調整 Thread Group → Number of Threads
```

---

#### 錯誤: JMeter 報告顯示 100% 錯誤率

**症狀**:
- Dashboard 顯示 Error %: 100%
- Throughput: 0/sec

**解決方案**:

```bash
# 1. 檢查 Ollama 是否運行
curl http://localhost:11434/api/version

# 2. 降低併發數
# Thread Group:
#   - Number of Threads: 10 → 5
#   - Ramp-Up Period: 1 → 10

# 3. 增加超時時間
# HTTP Request → Advanced:
#   - Connect Timeout: 5000 → 30000
#   - Response Timeout: 60000 → 180000

# 4. 檢查系統資源
top  # Linux/Mac
# Windows: 工作管理員
```

---

### 資料與 Fixtures 相關

#### 錯誤: `FileNotFoundError: [Errno 2] No such file or directory: 'fixtures/...'`

**症狀**:
```
FileNotFoundError: [Errno 2] No such file or directory: 'fixtures/prompts_multilingual.json'
```

**解決方案**:

```python
# 1. 使用絕對路徑
import os
fixture_path = os.path.join(
    os.path.dirname(__file__), 
    "..", 
    "fixtures", 
    "prompts_multilingual.json"
)
data = json.load(open(fixture_path, encoding="utf-8"))

# 2. 或使用 pathlib
from pathlib import Path
fixture_path = Path(__file__).parent.parent / "fixtures" / "prompts_multilingual.json"
data = json.load(fixture_path.open(encoding="utf-8"))

# 3. 確認檔案存在
assert fixture_path.exists(), f"Fixture 檔案不存在: {fixture_path}"
```

---

### 編碼相關

#### 錯誤: `UnicodeDecodeError: 'charmap' codec can't decode byte`

**症狀**:
```
UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 123
```

**解決方案**:

```python
# 1. 明確指定編碼
with open("file.txt", encoding="utf-8") as f:
    content = f.read()

# 2. JSON 檔案
data = json.load(open("data.json", encoding="utf-8"))

# 3. 設定環境變數
# Linux/Mac
export LANG=zh_TW.UTF-8
export LC_ALL=zh_TW.UTF-8

# Windows PowerShell
$env:PYTHONIOENCODING="utf-8"
```

---

## 偵錯技巧

### 使用 pytest 偵錯模式

```bash
# 1. 進入失敗測試的 pdb
pytest --pdb

# 2. 進入所有測試的 pdb
pytest --trace

# 3. 顯示完整錯誤堆疊
pytest --tb=long

# 4. 顯示本地變數
pytest -l

# 5. 顯示 print 輸出
pytest -s
```

### 使用 logging

```python
import logging

# 設定 logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def test_example():
    logger.debug("開始測試")
    response = ollama_client.chat(messages=messages)
    logger.debug(f"回應: {response.text}")
```

### 使用 Allure 附件

```python
import allure

def test_example():
    response = ollama_client.chat(messages=messages)
    
    # 附加請求資訊
    allure.attach(
        str(messages),
        name="Request",
        attachment_type=allure.attachment_type.JSON
    )
    
    # 附加回應資訊
    allure.attach(
        response.text,
        name="Response",
        attachment_type=allure.attachment_type.TEXT
    )
```

---

## 尋求協助

如果上述方案無法解決問題，請：

1. **建立 Issue**: https://github.com/howie0721/Local_LLM_API_TestSuite/issues
2. **提供以下資訊**:
   - 錯誤訊息（完整堆疊）
   - 重現步驟
   - 環境資訊：
     ```bash
     python --version
     pip list
     ollama --version
     # 或
     docker --version
     ```
   - 測試程式碼片段

3. **參考資源**:
   - [FAQ](FAQ.md)
   - [How To Run](How_To_Run.md)
   - [GitHub Discussions](https://github.com/howie0721/Local_LLM_API_TestSuite/discussions)

---

**維護者**: @howie0721  
**最後更新**: 2025-11-04

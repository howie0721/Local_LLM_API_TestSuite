# Contributing Guide

感謝您對本專案的興趣！我們歡迎各種形式的貢獻，包括但不限於：

- 🐛 回報 Bug
- ✨ 提出新功能
- 📝 改進文件
- 🧪 新增測試案例
- 🔧 優化程式碼

## 快速開始

### 1. Fork 專案

點擊 GitHub 頁面右上角的 `Fork` 按鈕，建立自己的副本。

### 2. Clone 到本地

```bash
git clone https://github.com/YOUR_USERNAME/Local_LLM_API_TestSuite.git
cd Local_LLM_API_TestSuite
```

### 3. 建立開發環境

```bash
# 建立虛擬環境
python -m venv venv

# 啟動虛擬環境
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# 安裝依賴
pip install -r requirements.txt

# 安裝開發依賴
pip install black flake8 pytest-cov
```

### 4. 建立功能分支

```bash
git checkout -b feature/your-feature-name
```

---

## 開發流程

### 1. 編寫程式碼

遵循專案的 [Coding Style Guide](Coding_Style_Guide.md)：

```python
# ✅ Good
def test_TC_UNIT_0001_connection(ollama_client, validator):
    """
    TC-UNIT-0001: 測試本地 Ollama API 是否可連線
    """
    response = ollama_client.version()
    validator.assert_status_code(response, 200)

# ❌ Bad
def test_connection():  # 缺少 TC 編號與說明
    r = get("http://localhost:11434/api/version")
    assert r.status_code == 200
```

### 2. 新增測試

每個新功能都應包含對應的測試：

```python
import pytest

pytestmark = pytest.mark.unit  # 加上測試標記

def test_new_feature(ollama_client, validator):
    """
    TC-UNIT-XXXX: 測試新功能
    """
    # Arrange
    messages = [{"role": "user", "content": "test"}]
    
    # Act
    response = ollama_client.chat(messages=messages)
    
    # Assert
    validator.assert_status_code(response, 200)
```

### 3. 執行測試

```bash
# 執行所有測試
pytest -v

# 執行特定標記
pytest -m unit -v

# 檢查覆蓋率
pytest --cov=. --cov-report=html
```

### 4. 程式碼檢查

```bash
# 格式化程式碼
black .

# Linting 檢查
flake8 tests/ helpers/

# 型別檢查（可選）
mypy tests/
```

### 5. 提交變更

遵循 [Commit Message 規範](#commit-message-規範)：

```bash
git add .
git commit -m "feat: 新增 boundary test for max token length"
```

### 6. Push 到 Fork

```bash
git push origin feature/your-feature-name
```

### 7. 建立 Pull Request

1. 到 GitHub 上的 Fork 頁面
2. 點擊 `New Pull Request`
3. 填寫 PR 模板（見下方）
4. 等待 CI 測試通過
5. 等待 Code Review

---

## Commit Message 規範

遵循 [Conventional Commits](https://www.conventionalcommits.org/) 規範：

### 格式

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type 類型

| Type | 說明 | 範例 |
|------|------|------|
| `feat` | 新功能 | `feat: 新增 security 測試` |
| `fix` | Bug 修復 | `fix: 修正 timeout 問題` |
| `test` | 測試相關 | `test: 加入 boundary 測試` |
| `docs` | 文件更新 | `docs: 更新 README` |
| `style` | 程式碼格式 | `style: 套用 black 格式化` |
| `refactor` | 重構 | `refactor: 抽取 validator 邏輯` |
| `perf` | 效能優化 | `perf: 優化並行執行邏輯` |
| `chore` | 雜項 | `chore: 更新依賴版本` |
| `ci` | CI/CD 相關 | `ci: 加入 nightly test workflow` |

### 範例

```bash
# 簡單 commit
git commit -m "feat: 新增 multilingual support"

# 詳細 commit
git commit -m "fix: 修正 connection timeout 問題

在高負載情況下，connection 會超時。
將 timeout 從 30s 增加到 60s，並加入重試機制。

Fixes #123"
```

---

## Pull Request 模板

```markdown
## 變更摘要
<!-- 簡述此 PR 的目的 -->

## 變更類型
- [ ] 🐛 Bug fix
- [ ] ✨ New feature
- [ ] 📝 Documentation
- [ ] 🧪 Test
- [ ] 🔧 Refactor
- [ ] ⚡ Performance
- [ ] 🎨 Style

## 變更內容
<!-- 詳細說明變更內容 -->

- 新增 XXX 測試
- 修正 YYY 問題
- 優化 ZZZ 邏輯

## 測試
<!-- 說明如何測試此變更 -->

```bash
pytest -m security -v
```

## 檢查清單
- [ ] 通過所有測試 (`pytest -v`)
- [ ] 覆蓋率 > 80% (`pytest --cov`)
- [ ] 通過 Linting (`flake8`)
- [ ] 格式化程式碼 (`black`)
- [ ] 更新文件（如需要）
- [ ] 新增測試案例

## 相關 Issue
Fixes #123
Related to #456

## 截圖（如適用）
<!-- 貼上 Allure 報告或測試結果截圖 -->
```

---

## Code Review 流程

### Reviewer 檢查事項

#### 程式碼品質
- [ ] 符合 [Coding Style Guide](Coding_Style_Guide.md)
- [ ] 無明顯的程式碼異味（Code Smell）
- [ ] 命名清晰易懂
- [ ] 註解適當（複雜邏輯需要註解）

#### 測試品質
- [ ] 測試案例完整
- [ ] 測試獨立且可重複執行
- [ ] 斷言清晰明確
- [ ] 加上適當的 pytest marker

#### 文件
- [ ] Docstring 完整
- [ ] README 更新（如需要）
- [ ] CHANGELOG 更新（如需要）

#### 安全性
- [ ] 無硬編碼敏感資訊
- [ ] 無潛在安全漏洞
- [ ] 輸入驗證正確

### Review Comments 範例

```markdown
# ✅ Good
建議將 timeout 抽取為常數，方便日後調整：
```python
DEFAULT_TIMEOUT = 60
response = ollama_client.chat(messages=messages, timeout=DEFAULT_TIMEOUT)
```

# ❌ Bad
這裡寫得不好。
```

---

## 測試指南

### 測試命名規範

```python
# 格式: test_TC_<類別>_<編號>_<描述>
def test_TC_UNIT_0001_connection(ollama_client):
    """
    TC-UNIT-0001: 測試 Ollama API 連線
    """
    pass
```

### 測試結構（AAA Pattern）

```python
def test_example(ollama_client, validator):
    # Arrange - 準備資料
    messages = [{"role": "user", "content": "test"}]
    
    # Act - 執行動作
    response = ollama_client.chat(messages=messages)
    
    # Assert - 驗證結果
    validator.assert_status_code(response, 200)
```

### 使用 Fixtures

```python
# conftest.py
@pytest.fixture
def sample_data():
    return {"key": "value"}

# test file
def test_with_fixture(sample_data):
    assert sample_data["key"] == "value"
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

## 文件撰寫指南

### Markdown 規範

```markdown
# 一級標題（每個檔案只有一個）

## 二級標題

### 三級標題

- 列表項目
  - 子項目

1. 數字列表
2. 項目二

**粗體** 和 *斜體*

`行內程式碼`

\```python
# 程式碼區塊
def example():
    pass
\```

[連結文字](https://example.com)

| 表頭1 | 表頭2 |
|------|------|
| 內容1 | 內容2 |
```

### Docstring 規範

```python
def function_name(param1: str, param2: int) -> bool:
    """
    簡短描述（一行）
    
    詳細說明（多行，可選）
    
    Args:
        param1: 參數1 說明
        param2: 參數2 說明
    
    Returns:
        回傳值說明
    
    Raises:
        ValueError: 何時拋出異常
    
    Example:
        >>> function_name("test", 123)
        True
    """
    pass
```

---

## 常見問題

### Q: 如何新增一個測試分類？

A: 
1. 在 `tests/` 下建立新目錄
2. 在 `pytest.ini` 註冊新 marker
3. 在 CI workflow 中加入對應測試組合
4. 更新 `tests/README.md`

### Q: 測試失敗怎麼辦？

A: 
1. 本地重現問題：`pytest tests/path/to/test.py -v`
2. 使用偵錯模式：`pytest --pdb`
3. 檢查 Allure 報告
4. 尋求幫助（建立 Issue）

### Q: 如何更新依賴版本？

A: 
1. 更新 `requirements.txt`
2. 執行完整測試確保相容性
3. 更新 `CHANGELOG.md`
4. 提交 PR 並註明測試結果

### Q: 如何報告安全性漏洞？

A: 
請不要公開報告！發送郵件至：security@example.com

---

## 社群守則

### 行為準則

- ✅ 尊重所有貢獻者
- ✅ 建設性的回饋
- ✅ 專注於技術討論
- ❌ 禁止人身攻擊
- ❌ 禁止歧視言論
- ❌ 禁止垃圾資訊

### 溝通管道

- **GitHub Issues**: Bug 回報、功能建議
- **Pull Requests**: 程式碼貢獻
- **Discussions**: 技術討論、問題求助

---

## 貢獻者名單

感謝所有貢獻者！🎉

<!-- 自動更新
[![Contributors](https://contrib.rocks/image?repo=howie0721/Local_LLM_API_TestSuite)](https://github.com/howie0721/Local_LLM_API_TestSuite/graphs/contributors)
-->

---

## 授權

本專案採用 MIT License。貢獻程式碼即表示您同意將您的貢獻以相同授權釋出。

---

## 參考資源

- [Pytest 最佳實踐](https://docs.pytest.org/en/stable/goodpractices.html)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

---

**維護者**: @howie0721  
**最後更新**: 2025-11-04

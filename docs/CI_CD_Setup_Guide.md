# CI/CD 設定指南

## GitHub Actions Workflows

本專案包含三個 CI/CD workflow，依據測試範圍與執行時機分流：

### 1. PR Tests (Fast) - `pr-tests.yml`

**觸發時機：**
- Pull Request 到 `main` 或 `develop` 分支
- Push 到 `main` 或 `develop` 分支

**執行範圍：**
- ✅ Unit Tests (`unit`)
- ✅ Boundary Tests (`boundary`)
- ✅ Compatibility Tests (`compatibility`)
- ✅ Error Handling Tests (`error_handling`)

**特色：**
- 多 Python 版本矩陣測試（3.10, 3.11）
- 並行執行（`-n auto`）
- 快速回饋（預計 5-10 分鐘）
- 失敗時最多顯示 5 個錯誤

**Allure 報告：** `https://<your-org>.github.io/<repo>/pr-tests/`

---

### 2. Nightly Tests (Full Suite) - `nightly-tests.yml`

**觸發時機：**
- 每天 UTC 00:00（台灣時間早上 8:00）
- 手動觸發（workflow_dispatch）

**執行範圍：**
- 🔄 End-to-End Tests (`e2e`)
- 🔄 Regression Tests (`regression`)
- 🔒 Security Tests (`security`)
- 🔗 Integration Tests (`integration`)
- 👥 Usability Tests (`usability`)

**特色：**
- 多 Python 版本矩陣測試（3.10, 3.11）
- 按測試類型分組並行執行
- `fail-fast: false`（一組失敗不影響其他組）
- 測試失敗時繼續執行（`continue-on-error: true`）
- 報告保留 30 天

**Allure 報告：** `https://<your-org>.github.io/<repo>/nightly-tests/`

---

### 3. Manual Test Run - `manual-tests.yml`

**觸發時機：**
- 手動觸發（GitHub Actions UI）

**執行範圍：**
- 🎯 自訂 pytest markers（輸入參數）
- 🐍 自訂 Python 版本（3.10, 3.11, 3.12）
- ⚡ 可選並行或序列執行

**Allure 報告：** `https://<your-org>.github.io/<repo>/manual-tests/`

---

## 設定步驟

### 1. 啟用 GitHub Pages

1. 進入 Repository → Settings → Pages
2. Source 選擇 `gh-pages` 分支
3. 目錄選擇 `/ (root)`
4. 儲存後等待部署完成

### 2. 本地測試

```powershell
# 安裝依賴
pip install -r requirements.txt

# 執行 PR 快速測試（本地模擬）
pytest -m "unit or boundary or compatibility or error_handling" -v -n auto

# 執行 nightly 完整測試（本地模擬）
pytest -m "e2e or regression or security or integration or usability" -v

# 執行特定標記
pytest -m unit -v
pytest -m security -v
```

### 3. Allure 報告（本地）

```powershell
# 生成報告
pytest --alluredir=allure-results
allure serve allure-results

# 或生成靜態報告
allure generate allure-results -o allure-report --clean
```

---

## 測試標記對照表

| 標記 | 說明 | PR 快速測試 | Nightly 完整測試 |
|------|------|:----------:|:--------------:|
| `unit` | 單元測試 | ✅ | ❌ |
| `boundary` | 邊界值測試 | ✅ | ❌ |
| `compatibility` | 相容性測試 | ✅ | ❌ |
| `error_handling` | 錯誤處理測試 | ✅ | ❌ |
| `e2e` | 端對端測試 | ❌ | ✅ |
| `regression` | 回歸測試 | ❌ | ✅ |
| `security` | 安全性測試 | ❌ | ✅ |
| `integration` | 整合測試 | ❌ | ✅ |
| `usability` | 易用性測試 | ❌ | ✅ |

---

## 環境變數設定

CI/CD 使用 Docker Ollama，無需額外設定。本地開發可複製 `.env.example` 為 `.env`：

```bash
cp .env.example .env
```

---

## Troubleshooting

### Ollama 連線逾時

如果 CI 中 Ollama 啟動失敗，可調整等待時間：

```yaml
- name: Wait for Ollama to be ready
  run: |
    timeout 120 bash -c 'until curl -s http://localhost:11434/api/version; do sleep 2; done'
```

### GitHub Pages 404

確認：
1. `gh-pages` 分支已建立
2. Settings → Pages 已啟用
3. Actions 有 `GITHUB_TOKEN` 權限（預設已有）

### 測試失敗但 CI 顯示成功

檢查 `continue-on-error` 設定，nightly 預設允許失敗但會上傳報告。若需嚴格失敗，移除此設定。

---

## 進階設定

### 加入 Slack/Teams 通知

在 `nightly-tests.yml` 最後加入：

```yaml
- name: Send Slack notification
  if: failure()
  uses: slackapi/slack-github-action@v1
  with:
    webhook-url: ${{ secrets.SLACK_WEBHOOK_URL }}
    payload: |
      {
        "text": "❌ Nightly tests failed! Check report: https://<your-org>.github.io/<repo>/nightly-tests/"
      }
```

### 自訂測試分組

修改 `pr-tests.yml` 中的 marker 組合：

```yaml
pytest -m "unit or boundary or compatibility or error_handling or integration"
```

### 加入 Code Coverage

```yaml
- name: Run tests with coverage
  run: |
    pytest -m "unit or boundary" --cov=. --cov-report=xml

- name: Upload coverage to Codecov
  uses: codecov/codecov-action@v3
  with:
    files: ./coverage.xml
```

---

## 維護建議

- ✅ 每週檢視 nightly 報告，確保回歸測試通過
- ✅ PR 測試失敗時立即修復，避免積累技術債
- ✅ 定期更新依賴與 Ollama 版本
- ✅ 監控 GitHub Actions 用量（免費帳號每月 2000 分鐘）

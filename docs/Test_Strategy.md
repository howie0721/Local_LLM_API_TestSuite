# Test Strategy

## 目標與範圍

### 測試目標

1. **功能正確性**: 確保 LLM API 功能符合預期行為
2. **穩定性**: 驗證系統在各種條件下的穩健性
3. **效能**: 評估回應時間、吞吐量與資源消耗
4. **安全性**: 防止 Prompt Injection、資訊洩漏等風險
5. **可用性**: 確保回應格式易於解析與應用
6. **回歸防護**: 及早發現功能退化或破壞性變更

### 測試範圍

#### 包含 (In Scope)

- ✅ Ollama API 端點 (`/api/chat`, `/api/generate`, `/api/version`)
- ✅ 單輪與多輪對話情境
- ✅ 多語言支援 (中文、英文、日文等)
- ✅ 特殊字元與邊界值處理
- ✅ 錯誤處理與異常情境
- ✅ 效能與穩定性指標
- ✅ 安全性漏洞掃描

#### 不包含 (Out of Scope)

- ❌ Ollama 內部實作細節
- ❌ 模型訓練與微調流程
- ❌ 前端 UI/UX 測試（如有 web 界面）
- ❌ 資料庫層測試（Ollama 無外部 DB）
- ❌ 網路層深度測試（TCP/IP、DNS）

---

## 測試金字塔策略

```
        ▲
       /E2E\        10% - 情境完整性驗證
      /------\
     /整合測試 \     20% - 多模組協作
    /----------\
   /  單元測試   \   70% - 基礎功能快速驗證
  /--------------\
 
橫切關注點（貫穿各層）：
├─ 安全性 (Security)
├─ 效能 (Performance)
├─ 穩定性 (Stability)
└─ 易用性 (Usability)
```

### 各層級策略

#### 1. 單元測試 (Unit Tests) - 70%

**策略**: 快速、獨立、大量

- **執行頻率**: 每次 commit
- **執行時間**: < 5 分鐘
- **隔離性**: 每個測試獨立，無順序依賴
- **覆蓋率**: 核心 API 功能 100%

**範例**:
- API 連線測試
- 回應格式驗證
- 基本錯誤處理

#### 2. 整合測試 (Integration Tests) - 20%

**策略**: 驗證模組間協作

- **執行頻率**: 每日 nightly
- **執行時間**: 10-15 分鐘
- **情境**: 多階段流程串接（生成→翻譯→摘要）

**範例**:
- 多模型一致性測試
- 多語言切換測試
- 後處理流程測試

#### 3. 端對端測試 (E2E Tests) - 10%

**策略**: 完整業務情境模擬

- **執行頻率**: 每日 nightly + release 前
- **執行時間**: 15-20 分鐘
- **情境**: 真實用戶使用流程

**範例**:
- 多輪對話情境
- FAQ 知識查詢
- 程式碼生成與解釋

---

## 測試類型與優先級

| 測試類型 | 優先級 | 執行頻率 | Marker | 典型執行時間 |
|---------|--------|---------|--------|-------------|
| 單元測試 | P0 | 每次 PR | `unit` | 2-3 min |
| 邊界值測試 | P0 | 每次 PR | `boundary` | 3-5 min |
| 相容性測試 | P0 | 每次 PR | `compatibility` | 3-5 min |
| 錯誤處理測試 | P0 | 每次 PR | `error_handling` | 2-3 min |
| 整合測試 | P1 | Nightly | `integration` | 5-8 min |
| 回歸測試 | P1 | Nightly | `regression` | 5-8 min |
| 端對端測試 | P1 | Nightly | `e2e` | 8-12 min |
| 安全性測試 | P1 | Nightly | `security` | 5-8 min |
| 易用性測試 | P2 | Nightly | `usability` | 5-8 min |
| 效能測試 | P2 | Weekly | `perf` | 15-30 min |
| 穩定性測試 | P2 | Weekly | `stability` | 30-60 min |

---

## 測試環境策略

### 環境分層

```
┌─────────────────┐
│  Production     │ ❌ 不執行自動化測試
└─────────────────┘
┌─────────────────┐
│  Staging        │ ✅ 執行完整測試套件（含效能）
└─────────────────┘
┌─────────────────┐
│  CI/CD (Docker) │ ✅ 執行 PR + Nightly 測試
└─────────────────┘
┌─────────────────┐
│  Local Dev      │ ✅ 開發時快速測試
└─────────────────┘
```

### 環境配置

- **Local Dev**: `OLLAMA_BASE_URL=http://localhost:11434`
- **CI/CD**: Docker Ollama + 自動拉取 llama3 模型
- **Staging**: 獨立 Ollama 伺服器 + 固定模型版本
- **Production**: 僅監控，不執行測試

---

## 資料驅動測試策略

### Fixtures 管理

```
tests/fixtures/
├── prompts_multilingual.json   # 多語言測試資料
├── prompts_specialchar.json    # 特殊字元測試資料
├── baseline_responses.json     # 回歸測試基線
└── security_payloads.json      # 安全性測試 payload
```

### 參數化測試

使用 `@pytest.mark.parametrize` 實現資料驅動：

```python
@pytest.mark.parametrize("prompt,lang", [
    (item["prompt"], item["lang"]) 
    for item in json.load(open("fixtures/prompts_multilingual.json"))
])
def test_multilingual(ollama_client, prompt, lang):
    # 測試邏輯
```

---

## 失敗處理策略

### 1. 快速失敗 (Fail Fast)

```bash
# PR 測試：發現 5 個失敗即停止
pytest -m "unit or boundary" --maxfail=5
```

### 2. 失敗重試 (Flaky Test Handling)

```python
@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_unstable_feature():
    # 不穩定測試可重試 3 次
```

### 3. 繼續執行 (Continue on Error)

```yaml
# Nightly 測試：允許失敗但收集所有結果
continue-on-error: true
```

---

## 效能測試策略

### JMeter 測試場景

1. **單請求基線** (`ollama_llama3_single_request.jmx`)
   - 1 user, 10 iterations
   - 建立效能基線

2. **併發壓測** (`ollama_llama3_concurrent_requests.jmx`)
   - 10/50/100 concurrent users
   - 評估吞吐量與回應時間

3. **長時穩定性** (`ollama_llama3_long_duration_stress.jmx`)
   - 持續 30 分鐘
   - 監控記憶體洩漏與效能退化

4. **長文本處理** (`ollama_llama3_long_prompt.jmx`)
   - 極限 token 數測試
   - 驗證系統穩健性

### 效能指標 (SLA)

| 指標 | 目標 | 警告閾值 | 失敗閾值 |
|------|------|---------|---------|
| 平均回應時間 | < 2s | 3s | 5s |
| P95 回應時間 | < 5s | 8s | 10s |
| 吞吐量 (TPS) | > 10 | 8 | 5 |
| 錯誤率 | < 1% | 3% | 5% |
| CPU 使用率 | < 70% | 85% | 95% |
| 記憶體使用 | < 4GB | 6GB | 8GB |

---

## 安全性測試策略

### 測試場景

1. **Prompt Injection**
   - 嘗試洩漏系統 prompt
   - 繞過內容過濾
   - 指令注入攻擊

2. **敏感資訊洩漏**
   - 要求生成密碼/金鑰
   - 嘗試提取訓練資料
   - 個資洩漏風險

3. **內容過濾**
   - 色情、暴力、仇恨言論
   - 驗證模型拒答機制

4. **DoS 防護**
   - 超長 prompt 攻擊
   - 高頻請求壓測

### 安全性基線

```python
# 所有安全性測試必須通過以下驗證：
1. 回應中不包含敏感關鍵字
2. 模型正確拒絕不當請求
3. 錯誤訊息不洩漏系統資訊
4. 無 SQL Injection 風險（如適用）
```

---

## 回歸測試策略

### 基線管理

```
tests/fixtures/baseline_responses.json
{
  "test_case_id": "TC-REG-0001",
  "prompt": "請用一句話介紹你自己",
  "expected_keywords": ["LLaMA", "AI", "助手"],
  "version": "llama3-8b",
  "timestamp": "2025-11-04"
}
```

### 回歸觸發條件

- ✅ 模型版本更新
- ✅ API 端點變更
- ✅ 重大功能發布
- ✅ 安全性修補後

### 回歸範圍

- **完整回歸**: 所有測試（Release 前）
- **增量回歸**: 受影響模組（日常開發）
- **煙霧測試**: 關鍵路徑（Hotfix 後）

---

## CI/CD 整合策略

### 三階段測試流水線

```
┌──────────────┐
│   PR Tests   │ ← 開發者提交 PR
│  5-10 min    │   unit + boundary + compatibility + error_handling
└──────┬───────┘
       │ ✅ Pass
┌──────▼───────┐
│ Merge to main│
└──────┬───────┘
       │
┌──────▼───────┐
│Nightly Tests │ ← 每天 00:00 UTC
│  20-30 min   │   e2e + regression + security + integration + usability
└──────┬───────┘
       │ ✅ Pass
┌──────▼───────┐
│Weekly Perf   │ ← 每週日
│  30-60 min   │   performance + stability (JMeter)
└──────────────┘
```

### 閘門策略 (Quality Gates)

| 階段 | 必過條件 | 阻斷 Merge |
|------|---------|-----------|
| PR Tests | 100% 通過 | ✅ 是 |
| Nightly Tests | > 95% 通過 | ❌ 否（告警） |
| Weekly Perf | 無效能退化 > 20% | ❌ 否（告警） |

---

## 報告與度量

### Allure 報告內容

- ✅ 測試通過率趨勢
- ✅ 失敗測試明細與截圖
- ✅ 執行時間分佈
- ✅ Flaky test 統計
- ✅ 標記分類統計

### 關鍵指標 (KPI)

1. **測試覆蓋率**: > 80%
2. **通過率**: > 95%
3. **平均執行時間**: < 10 分鐘 (PR)
4. **Flaky test 比例**: < 5%
5. **Bug 逃逸率**: < 2%

---

## 風險與緩解

| 風險 | 影響 | 機率 | 緩解措施 |
|------|------|------|---------|
| LLM 回應不穩定 | 高 | 中 | 使用關鍵字驗證取代精確比對 |
| 測試環境不一致 | 中 | 中 | Docker 固定版本 |
| 測試執行時間過長 | 中 | 低 | 並行執行 + 分層測試 |
| Flaky tests 過多 | 高 | 中 | 標記 flaky + 自動重試 |
| 安全性測試誤判 | 低 | 低 | 人工審查 + baseline |

---

## 持續改進

### 每週 Review

- ✅ 檢視 Allure 報告
- ✅ 分析 flaky tests
- ✅ 更新 baseline 資料
- ✅ 調整效能閾值

### 每月 Review

- ✅ 測試覆蓋率分析
- ✅ 測試執行時間優化
- ✅ 新增測試場景
- ✅ 移除過時測試

### 季度 Review

- ✅ 測試策略調整
- ✅ 工具鏈升級
- ✅ 團隊培訓
- ✅ 最佳實踐分享

---

**維護者**: @howie0721  
**最後更新**: 2025-11-04

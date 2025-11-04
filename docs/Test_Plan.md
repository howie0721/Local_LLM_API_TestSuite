# Test Plan

## Local LLM API 測試計畫

**專案名稱**: Local LLM API Test Suite  
**版本**: 1.0.0  
**建立日期**: 2025-11-04  
**作者**: @howie0721  
**狀態**: Active

---

## 1. 簡介

### 1.1 目的

本測試計畫旨在確保 Local LLM (Ollama) API 的功能正確性、穩定性、安全性與效能符合預期標準。

### 1.2 範圍

#### 涵蓋範圍
- ✅ API 連線功能
- ✅ 單輪與多輪對話
- ✅ 模型資訊查詢
- ✅ Prompt 驗證與處理
- ✅ 錯誤處理機制
- ✅ 多語言支援
- ✅ 安全性驗證
- ✅ 相容性測試
- ✅ 回歸測試

#### 不涵蓋範圍
- ❌ Ollama 內部實作測試
- ❌ LLM 模型訓練品質
- ❌ 硬體效能測試（GPU/CPU）
- ❌ Ollama UI 測試（僅測試 API）

### 1.3 目標受眾

- 測試工程師
- 開發工程師
- 專案經理
- QA Lead

---

## 2. 測試策略

### 2.1 測試金字塔

```
        /\
       /  \      E2E (5 tests, 13%)
      /____\     
     /      \    Integration (5 tests, 13%)
    /________\   
   /          \  Unit + Boundary (12 tests, 31%)
  /__________  \
```

**原則**:
- 大量快速的單元測試作為基礎
- 適量的整合測試驗證元件互動
- 少量的端到端測試涵蓋關鍵路徑

### 2.2 測試類型

| 類型 | 數量 | 執行時間 | 觸發時機 |
|------|------|----------|---------|
| Unit | 6 | 30s | PR + Nightly |
| Boundary | 6 | 45s | PR + Nightly |
| Compatibility | 4 | 3m | PR + Nightly |
| Error Handling | 2 | 15s | PR + Nightly |
| Integration | 5 | 8m | Nightly |
| E2E | 5 | 15m | Nightly |
| Regression | 5 | 5m | Nightly |
| Security | 5 | 4m | Nightly |

### 2.3 測試環境

| 環境 | 用途 | Ollama 版本 | Python 版本 |
|------|------|------------|------------|
| Local | 開發測試 | 0.1.14+ | 3.10+ |
| CI (GitHub Actions) | 自動化測試 | Docker latest | 3.10, 3.11 |
| Staging | 預生產驗證 | 0.1.14+ | 3.11 |

---

## 3. 測試範圍

### 3.1 功能需求測試

#### REQ-001: API 基礎連線

| Test ID | 測試項目 | 優先級 | 狀態 |
|---------|---------|--------|------|
| TC-UNIT-001 | 連線成功測試 | P0 | ✅ Pass |
| TC-UNIT-002 | 取得版本資訊 | P1 | ✅ Pass |
| TC-ERROR-001 | 連線失敗處理 | P1 | ✅ Pass |
| TC-UNIT-006 | 連線超時處理 | P1 | ✅ Pass |

#### REQ-002: 模型資訊查詢

| Test ID | 測試項目 | 優先級 | 狀態 |
|---------|---------|--------|------|
| TC-UNIT-003 | 列出所有模型 | P0 | ✅ Pass |
| TC-UNIT-004 | 查詢特定模型 | P1 | ✅ Pass |
| TC-ERROR-002 | 無效模型錯誤 | P1 | ✅ Pass |
| TC-COMPAT-002 | 多模型支援 | P2 | ✅ Pass |

#### REQ-003: 單輪對話

| Test ID | 測試項目 | 優先級 | 狀態 |
|---------|---------|--------|------|
| TC-INT-001 | 基本對話請求 | P0 | ✅ Pass |
| TC-UNIT-005 | 回應格式驗證 | P1 | ✅ Pass |
| TC-INT-002 | 自訂參數支援 | P2 | ✅ Pass |
| TC-PERF-001 | 回應時間 < 10s | P1 | ⚠️ Pending |

#### REQ-004: 多輪對話

| Test ID | 測試項目 | 優先級 | 狀態 |
|---------|---------|--------|------|
| TC-INT-003 | 上下文保留 | P0 | ✅ Pass |
| TC-INT-004 | 支援 10+ 輪對話 | P1 | ✅ Pass |
| TC-BOUND-005 | 上下文長度限制 | P1 | ✅ Pass |
| TC-INT-005 | 對話重置 | P2 | ✅ Pass |

### 3.2 非功能需求測試

#### 安全性測試

| Test ID | 測試項目 | 優先級 | 狀態 |
|---------|---------|--------|------|
| TC-SEC-001 | SQL 注入防護 | P0 | ✅ Pass |
| TC-SEC-002 | Prompt 注入防護 | P0 | ✅ Pass |
| TC-SEC-003 | 敏感資料保護 | P1 | ✅ Pass |

#### 效能測試

| Test ID | 測試項目 | 目標 | 狀態 |
|---------|---------|------|------|
| TC-PERF-001 | 回應時間 | < 10s | ⚠️ Pending |
| TC-PERF-002 | 成功率 | > 99% | ⚠️ Pending |
| TC-PERF-003 | 吞吐量 | > 5 req/s | ⚠️ Pending |

#### 相容性測試

| Test ID | 測試項目 | 優先級 | 狀態 |
|---------|---------|--------|------|
| TC-COMPAT-001 | 多語言支援 | P1 | ✅ Pass |
| TC-COMPAT-003 | Python 3.10+ | P1 | ✅ Pass |
| TC-COMPAT-004 | Windows/Linux/macOS | P1 | ✅ Pass |

---

## 4. 測試排程

### 4.1 PR 測試（Pull Request）

**觸發條件**: 建立或更新 Pull Request  
**執行時間**: 5-10 分鐘  
**測試範圍**: 快速測試（Unit + Boundary + Compatibility + Error Handling）

```yaml
# .github/workflows/pr-tests.yml
on: [pull_request]
jobs:
  fast-tests:
    strategy:
      matrix:
        python-version: [3.10, 3.11]
    steps:
      - run: pytest -m "unit or boundary or compatibility or error_handling" -n auto
```

**通過標準**: 所有測試必須通過（18/18）

---

### 4.2 Nightly 測試（每日全量測試）

**觸發條件**: 每日 00:00 UTC  
**執行時間**: 20-30 分鐘  
**測試範圍**: 完整測試套件

```yaml
# .github/workflows/nightly-tests.yml
on:
  schedule:
    - cron: '0 0 * * *'
jobs:
  full-tests:
    steps:
      - run: pytest --alluredir=allure-results
```

**通過標準**: 
- 測試通過率 > 95% (36/38+)
- 無 P0/P1 測試失敗

---

### 4.3 Release 測試（發布前測試）

**觸發條件**: 建立 Release Tag  
**執行時間**: 45-60 分鐘  
**測試範圍**: 完整測試 + 額外驗證

**額外驗證**:
1. 完整回歸測試
2. 效能基準測試（JMeter）
3. 安全性掃描
4. 多環境驗證

**通過標準**: 
- 100% 測試通過
- 程式碼覆蓋率 > 80%
- 無 Critical/Blocker 缺陷

---

## 5. 測試資源

### 5.1 人力資源

| 角色 | 姓名 | 責任 |
|------|------|------|
| Test Lead | @howie0721 | 測試策略、計畫、協調 |
| Test Engineer 1 | TBD | 功能測試、自動化 |
| Test Engineer 2 | TBD | 效能測試、安全測試 |
| DevOps | TBD | CI/CD 維護 |

### 5.2 軟體工具

| 工具 | 版本 | 用途 |
|------|------|------|
| Pytest | 7.4+ | 測試框架 |
| Allure | 2.20+ | 測試報告 |
| JMeter | 5.6+ | 效能測試 |
| Docker | 24.0+ | 環境隔離 |
| GitHub Actions | - | CI/CD |

### 5.3 硬體需求

| 環境 | 配置 |
|------|------|
| 開發機 | CPU: 4+ cores, RAM: 16GB+, GPU: Optional |
| CI Runner | GitHub-hosted (ubuntu-latest) |
| Ollama Container | 2 cores, 4GB RAM minimum |

---

## 6. 風險管理

### 6.1 高風險項目

| 風險 | 影響 | 機率 | 緩解措施 |
|------|------|------|---------|
| Ollama API 變更 | High | Medium | 監控 API 版本，建立契約測試 |
| LLM 回應不穩定 | Medium | High | 降低 temperature，使用關鍵字驗證 |
| CI 資源不足 | Medium | Low | 使用測試分層，優化執行時間 |

### 6.2 中風險項目

| 風險 | 影響 | 機率 | 緩解措施 |
|------|------|------|---------|
| 測試資料過時 | Medium | Medium | 定期更新測試資料 |
| 測試執行時間過長 | Low | High | 並行執行，優化慢測試 |

---

## 7. 測試交付物

### 7.1 測試案例文件

- ✅ 38 個自動化測試腳本
- ✅ Test Case Template
- ✅ Mapping Requirement to Test

### 7.2 測試報告

- ✅ Allure 測試報告（自動生成）
- ✅ Test Coverage Report
- ✅ JMeter 效能報告

### 7.3 測試文件

- ✅ Test Plan（本文件）
- ✅ Test Strategy
- ✅ Test Framework Design
- ✅ How To Run
- ✅ Troubleshooting Guide

---

## 8. 測試通過/失敗標準

### 8.1 通過標準

**PR 階段**:
- ✅ 所有快速測試通過（18/18）
- ✅ 無新增 Linting 錯誤
- ✅ 程式碼格式符合規範（Black）

**Nightly 階段**:
- ✅ 測試通過率 > 95%
- ✅ 無 P0 (Blocker) 失敗
- ✅ 程式碼覆蓋率 > 78%

**Release 階段**:
- ✅ 100% 測試通過
- ✅ 程式碼覆蓋率 > 80%
- ✅ 需求覆蓋率 > 90%
- ✅ 無 Critical/Blocker 缺陷

### 8.2 失敗標準

**立即停止測試**:
- ❌ Ollama 服務無法啟動
- ❌ 超過 50% 測試失敗
- ❌ 發現 Security 缺陷

**需要修復後重測**:
- ❌ 任何 P0 (Blocker) 測試失敗
- ❌ P1 (Critical) 測試失敗 > 3 個

---

## 9. 測試指標

### 9.1 關鍵指標（KPI）

| 指標 | 目標 | 當前 | 狀態 |
|------|------|------|------|
| 測試通過率 | > 95% | 97% (37/38) | ✅ |
| 程式碼覆蓋率 | > 80% | 78% | ⚠️ |
| 需求覆蓋率 | > 90% | 83% (29/35) | ⚠️ |
| Flaky Test 比例 | < 5% | 5.3% (2/38) | ⚠️ |
| 測試執行時間 (PR) | < 10m | ~7m | ✅ |
| 測試執行時間 (Nightly) | < 30m | ~25m | ✅ |

### 9.2 品質指標

| 指標 | 目標 | 當前 | 狀態 |
|------|------|------|------|
| Docstring 覆蓋率 | 100% | 100% | ✅ |
| Type Hints 使用率 | > 80% | 85% | ✅ |
| 平均測試長度 | < 30 行 | 25 行 | ✅ |
| 重複程式碼 | < 10% | ~8% | ✅ |

---

## 10. 測試結束標準

### 10.1 功能測試結束標準

- ✅ 所有 P0 和 P1 測試案例已執行
- ✅ 測試通過率 > 95%
- ✅ 所有 Blocker 和 Critical 缺陷已修復
- ✅ 回歸測試通過

### 10.2 非功能測試結束標準

- ✅ 效能測試完成並符合 SLA
- ✅ 安全性測試無 High/Critical 漏洞
- ✅ 相容性測試涵蓋所有目標平台

### 10.3 發布結束標準

- ✅ 所有測試交付物完成
- ✅ 測試報告經 Test Lead 審核通過
- ✅ 利害關係人 Sign-off

---

## 11. 附錄

### 11.1 測試環境 URL

- **GitHub Repository**: https://github.com/howie0721/Local_LLM_API_TestSuite
- **Allure Report**: https://howie0721.github.io/Local_LLM_API_TestSuite/allure-report/
- **CI/CD Workflows**: https://github.com/howie0721/Local_LLM_API_TestSuite/actions

### 11.2 相關文件

- [Test Strategy](Test_Strategy.md)
- [Test Framework Design](Test_Framework_Design.md)
- [How To Run](How_To_Run.md)
- [Architecture](Architecture.md)
- [FAQ](FAQ.md)

### 11.3 聯絡資訊

| 角色 | 聯絡方式 |
|------|---------|
| Test Lead | @howie0721 |
| GitHub Issues | https://github.com/howie0721/Local_LLM_API_TestSuite/issues |

---

## 12. 變更歷史

| 版本 | 日期 | 變更內容 | 作者 |
|------|------|---------|------|
| 1.0.0 | 2025-11-04 | 初版發布 | @howie0721 |

---

## 13. 審核與批准

| 角色 | 姓名 | 簽名 | 日期 |
|------|------|------|------|
| Test Lead | @howie0721 | ✅ | 2025-11-04 |
| Project Manager | TBD | - | - |
| Stakeholder | TBD | - | - |

---

**維護者**: @howie0721  
**最後更新**: 2025-11-04  
**下次審查**: 2025-12-04

# 🤖 Local LLM API 測試計畫書

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/pytest-Latest-green.svg)](https://pytest.org/)
[![Allure](https://img.shields.io/badge/Allure-Report-orange.svg)](https://allurereport.org/)
[![GitHub Actions](https://img.shields.io/badge/CI-GitHub_Actions-blue.svg)](https://github.com/features/actions)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **企業級 Ollama LLM API 自動化測試框架** - 涵蓋功能、效能、安全性、穩定性的全方位測試解決方案

---

## 📋 目錄

- [1. 專案背景與目的](#1-專案背景與目的)
  - [1.1 專案簡介與商業目標](#11-專案簡介與商業目標)
  - [1.2 測試的角色與價值定位](#12-測試的角色與價值定位)
  - [1.3 涉及系統與模組概覽](#13-涉及系統與模組概覽)
- [2. 測試範疇與目標](#2-測試範疇與目標)
  - [2.1 測試涵蓋範圍（功能、非功能）](#21-測試涵蓋範圍功能非功能)
  - [2.2 不在測試範圍的項目](#22-不在測試範圍的項目)
  - [2.3 測試目標與成功定義](#23-測試目標與成功定義)
- [3. 測試策略與方法](#3-測試策略與方法)
  - [3.1 測試類型（單元、整合、系統、驗收）](#31-測試類型單元整合系統驗收)
  - [3.2 測試方法（黑箱、白箱、灰箱）](#32-測試方法黑箱白箱灰箱)
  - [3.3 自動化與手動測試策略](#33-自動化與手動測試策略)
  - [3.4 測試優先順序與風險導向策略](#34-測試優先順序與風險導向策略)
- [4. 測試環境與工具](#4-測試環境與工具)
  - [4.1 測試環境架構與配置](#41-測試環境架構與配置)
  - [4.2 測試工具清單與版本](#42-測試工具清單與版本)
  - [4.3 自動化測試架構設計](#43-自動化測試架構設計)
  - [4.4 CI/CD 整合與部署流程](#44-cicd-整合與部署流程)
  - [4.5 測試儀表板與可視化設計](#45-測試儀表板與可視化設計)
- [5. 測試項目與案例設計原則](#5-測試項目與案例設計原則)
  - [5.1 測試案例設計方法與分類](#51-測試案例設計方法與分類)
  - [5.2 資料驅動與模組化策略](#52-資料驅動與模組化策略)
  - [5.3 覆蓋率矩陣與測試深度](#53-覆蓋率矩陣與測試深度)
  - [5.4 測試流程圖與責任分工](#54-測試流程圖與責任分工)
- [6. 測試排程與里程碑](#6-測試排程與里程碑)
  - [6.1 測試活動時間表](#61-測試活動時間表)
  - [6.2 測試階段與交付節點](#62-測試階段與交付節點)
  - [6.3 測試進度追蹤方式](#63-測試進度追蹤方式)
- [7. 測試資源與角色分工](#7-測試資源與角色分工)
  - [7.1 測試團隊成員與職責](#71-測試團隊成員與職責)
  - [7.2 跨部門協作與溝通窗口](#72-跨部門協作與溝通窗口)
  - [7.3 測試資源需求與工具授權](#73-測試資源需求與工具授權)
- [8. 風險評估與應變計畫](#8-風險評估與應變計畫)
  - [8.1 測試風險清單](#81-測試風險清單)
  - [8.2 風險影響分析](#82-風險影響分析)
  - [8.3 應變策略與備援方案](#83-應變策略與備援方案)
- [9. 測試進度追蹤與品質指標](#9-測試進度追蹤與品質指標)
  - [9.1 測試通過率與缺陷密度](#91-測試通過率與缺陷密度)
  - [9.2 測試覆蓋率與穩定性指標](#92-測試覆蓋率與穩定性指標)
  - [9.3 測試報告頻率與儀表板設計](#93-測試報告頻率與儀表板設計)
- [10. 缺陷管理流程](#10-缺陷管理流程)
  - [10.1 缺陷提報與分類原則](#101-缺陷提報與分類原則)
  - [10.2 缺陷處理流程與狀態追蹤](#102-缺陷處理流程與狀態追蹤)
  - [10.3 缺陷驗證與關閉準則](#103-缺陷驗證與關閉準則)
- [11. 測試報告與交付物](#11-測試報告與交付物)
  - [11.1 測試報告格式與內容](#111-測試報告格式與內容)
  - [11.2 測試成果交付物清單](#112-測試成果交付物清單)
  - [11.3 報告審核與簽核流程](#113-報告審核與簽核流程)
- [12. 測試結束準則與驗收標準](#12-測試結束準則與驗收標準)
  - [12.1 測試完成條件](#121-測試完成條件)
  - [12.2 驗收標準與品質門檻](#122-驗收標準與品質門檻)
  - [12.3 測試結束審查流程](#123-測試結束審查流程)
- [13. 附錄與參考資料](#13-附錄與參考資料)
  - [13.1 測試案例樣本](#131-測試案例樣本)
  - [13.2 測試環境設定細節](#132-測試環境設定細節)
  - [13.3 工具安裝與使用說明](#133-工具安裝與使用說明)
  - [13.4 參考文件與連結](#134-參考文件與連結)

---

## 1. 專案背景與目的

### 1.1 專案簡介與商業目標

本專案旨在建立一套**企業級 Ollama Local LLM API 自動化測試框架**，確保本地大型語言模型服務在生產環境中的穩定性、效能與安全性。

#### 商業價值
- **降低風險**：透過全方位測試覆蓋，在上線前發現潛在問題
- **提升品質**：確保 API 回應準確性、穩定性符合業務需求
- **加速交付**：自動化測試縮短回歸測試時間 80%
- **增強信心**：完整的測試報告為產品發布提供數據支撐

#### 專案目標
1. **功能正確性**：驗證 `/api/chat` 和 `/api/generate` 兩大核心 API 的功能完整性
2. **非功能需求**：確保效能、安全性、穩定性達到生產標準
3. **多語言支援**：驗證 10 種語言（中文、英文、日文、韓文、法文、德文、西班牙文、俄文、阿拉伯文、印地文）的處理能力
4. **異常處理**：確保系統在邊界條件、錯誤場景下的健壯性

---

### 1.2 測試的角色與價值定位

#### 在 SDLC 中的角色
```
需求分析 → 設計 → 開發 → [測試] → 部署 → 維運
                        ↑
                  品質守門員角色
```

#### 價值定位

| 階段 | 測試活動 | 產出價值 |
|------|---------|---------|
| **需求階段** | 測試計畫書撰寫 | 明確測試範疇與驗收標準 |
| **開發階段** | 單元測試與整合測試 | 即時發現開發問題，降低修復成本 |
| **發布前** | 完整回歸測試與效能測試 | 確保發布品質，降低生產風險 |
| **上線後** | Nightly 穩定性測試 | 監控系統健康度，預警潛在問題 |

#### 測試投資報酬率（ROI）
- **缺陷修復成本降低**：開發階段發現缺陷的修復成本僅為生產環境的 1/10
- **時間成本節省**：自動化測試執行時間從 4 小時縮短至 30 分鐘
- **信心指數提升**：測試覆蓋率達 85%，發布信心度提升 95%

---

### 1.3 涉及系統與模組概覽

#### 系統架構

```
┌─────────────────────────────────────────────────────┐
│                    測試框架層                         │
│  pytest + Allure + GitHub Actions + JMeter          │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│                   Ollama API 層                      │
│  /api/chat  |  /api/generate  |  /api/tags          │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│                  Ollama 引擎層                       │
│  tinyllama (CI)  |  llama3 (Local)                  │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│                   Docker 容器層                      │
│  ollama/ollama:latest                               │
└─────────────────────────────────────────────────────┘
```

#### 核心模組

1. **測試框架核心** (`tests/`)
   - 11 個測試分類（unit, boundary, compatibility, e2e, integration, regression, security, stability, performance, usability, error_handling）
   - 37 個測試檔案，56 個測試案例

2. **共用元件** (`helpers/`, `tests/conftest.py`)
   - `ResponseValidator`：API 回應驗證器
   - `SchemaValidator`：JSON Schema 驗證器
   - `TestHelper`：測試輔助工具（JSON 解析、Markdown 驗證）
   - `BatchTestHelper`：批次測試執行器

3. **測試資料** (`fixtures/`)
   - 多語言測試資料（10 種語言）
   - 特殊字元測試資料（Emoji、符號、控制字元、混合字元）

4. **CI/CD 整合** (`.github/workflows/`)
   - PR 快速測試（5-10 分鐘）
   - Nightly 完整測試（20-30 分鐘）
   - Manual 彈性測試
   - JMeter 效能測試（每週執行）

5. **測試報告** (`allure-report/`, `jmeter-dashboard-report/`)
   - Allure 測試報告（GitHub Pages 自動發布）
   - JMeter Dashboard 報告（效能與穩定性）

---

## 2. 測試範疇與目標

### 2.1 測試涵蓋範圍（功能、非功能）

#### 功能測試範疇

| 測試類別 | 涵蓋範圍 | 測試重點 |
|---------|---------|---------|
| **Unit Testing** | 單一 API endpoint 基本功能 | 參數驗證、回應格式、錯誤處理 |
| **Boundary Testing** | 邊界值與極端輸入 | Token 限制、空值、超長輸入 |
| **Compatibility Testing** | 多語言與特殊字元 | 10 種語言、Emoji、符號、控制字元 |
| **Integration Testing** | API 間互動與流程 | Chat + Generate 組合、上下文保留 |
| **E2E Testing** | 端到端業務場景 | 完整對話流程、多輪互動 |
| **Regression Testing** | 版本變更影響 | 核心功能穩定性、向下相容性 |
| **Error Handling** | 異常情境處理 | 無效模型、錯誤參數、網路異常 |
| **Usability Testing** | 使用者體驗 | API 易用性、錯誤訊息清晰度 |

#### 非功能測試範疇

| 測試類別 | 測試指標 | 成功標準 |
|---------|---------|---------|
| **Performance Testing** | 回應時間、吞吐量 | P95 < 5s，QPS > 10 |
| **Stability Testing** | 長時間運行穩定性 | 1000 次請求成功率 > 99% |
| **Security Testing** | Injection 攻擊、敏感資訊 | 無 SQL/Prompt Injection 風險 |
| **Concurrency Testing** | 並行請求處理能力 | 10 並行無錯誤 |

---

### 2.2 不在測試範圍的項目

為確保測試專注於核心價值，以下項目**不在本測試計畫範圍內**：

#### 排除項目

| 排除項目 | 原因 |
|---------|------|
| **Ollama 引擎內部邏輯** | 屬於第三方套件測試責任 |
| **模型訓練與調校** | 非 API 測試範疇 |
| **硬體效能調校** | 屬於基礎設施層級 |
| **UI/前端測試** | 本專案為 API 測試 |
| **模型回應內容準確性** | 語意正確性非 API 測試目標 |
| **Docker 容器安全性掃描** | 屬於 DevOps 安全流程 |

#### 邊界說明
- **測試焦點**：API 行為、介面契約、非功能需求
- **不測試**：模型演算法、向量計算、硬體效能

---

### 2.3 測試目標與成功定義

#### 量化目標

| 指標類別 | 目標值 | 測量方式 |
|---------|-------|---------|
| **測試覆蓋率** | ≥ 85% | Allure 報告 + pytest-cov |
| **PR 測試通過率** | ≥ 98% | GitHub Actions 統計 |
| **Nightly 測試通過率** | ≥ 96% | GitHub Actions 統計 |
| **P0 測試通過率** | 100% | 關鍵路徑測試零失敗 |
| **缺陷逃逸率** | < 2% | 生產環境缺陷 / 測試期發現缺陷 |
| **自動化率** | ≥ 90% | 自動化測試案例 / 總測試案例 |

#### 質化目標

1. **可維護性**
   - 測試程式碼符合 PEP 8 規範
   - 共用元件重用率 > 80%
   - 測試案例命名清晰，可讀性高

2. **可擴展性**
   - 新增 API endpoint 測試時間 < 2 小時
   - 支援插件式新增測試類型

3. **可靠性**
   - 測試結果一致性 > 99%（減少 flaky tests）
   - CI/CD pipeline 穩定性 > 95%

#### 成功定義（Release Criteria）

專案達到以下條件視為測試成功，可進行發布：

✅ **必要條件（Must Have）**
- [ ] 所有 P0 測試 100% 通過
- [ ] PR 測試通過率 ≥ 98%
- [ ] 無 Critical 或 High 等級未修復缺陷
- [ ] 測試覆蓋率 ≥ 85%

✅ **期望條件（Should Have）**
- [ ] Nightly 測試通過率 ≥ 96%
- [ ] 效能測試指標達標（P95 < 5s）
- [ ] 安全測試無高風險項目

✅ **加分條件（Nice to Have）**
- [ ] 測試報告完整且可視化清晰
- [ ] 測試文件更新完整
- [ ] 新增測試案例涵蓋 edge cases

---

## 3. 測試策略與方法

### 3.1 測試類型（單元、整合、系統、驗收）

本專案採用**測試金字塔**策略，確保測試效率與覆蓋率平衡。

#### 測試金字塔分布

```
           ╱╲
          ╱E2E╲          10% - 端到端測試
         ╱──────╲        
        ╱ Integ. ╲       20% - 整合測試
       ╱──────────╲      
      ╱ Component  ╲     30% - 元件測試（Boundary + Compatibility）
     ╱──────────────╲    
    ╱      Unit      ╲   40% - 單元測試
   ╱──────────────────╲  
```

#### 測試類型詳細說明

| 測試類型 | 佔比 | 執行頻率 | 執行時間 | 測試重點 |
|---------|-----|---------|---------|---------|
| **單元測試** | 40% | 每次 PR | < 2 分鐘 | 單一 API 基本功能、參數驗證 |
| **元件測試** | 30% | 每次 PR | < 3 分鐘 | 邊界值、多語言、特殊字元 |
| **整合測試** | 20% | Nightly | < 5 分鐘 | API 間互動、流程驗證 |
| **端到端測試** | 10% | Nightly | < 5 分鐘 | 完整業務場景、多輪對話 |

#### 橫切面測試（Cross-Cutting）

除了金字塔結構，以下測試貫穿各層級：

- **安全性測試**：Injection 攻擊、參數污染（每次 Nightly 執行）
- **效能測試**：回應時間、吞吐量（每週 JMeter 執行）
- **穩定性測試**：長時間運行、重複請求（每週 JMeter 執行）
- **可用性測試**：錯誤訊息、API 易用性（每次 Nightly 執行）

---

### 3.2 測試方法（黑箱、白箱、灰箱）

#### 測試方法應用矩陣

| 測試類別 | 測試方法 | 原因 | 範例 |
|---------|---------|------|------|
| **Unit Testing** | 黑箱 + 灰箱 | 驗證 API 契約，必要時檢查日誌 | 驗證 `/api/chat` 回應格式 |
| **Boundary Testing** | 黑箱 | 專注於輸入輸出邊界 | Token 上限 32 的邊界測試 |
| **Integration Testing** | 灰箱 | 需理解 API 互動流程 | Chat + Generate 組合呼叫 |
| **Security Testing** | 黑箱 | 模擬攻擊者視角 | SQL Injection 測試 |
| **Performance Testing** | 灰箱 | 需監控系統資源使用 | 回應時間與 CPU 使用率 |

#### 方法論詳細說明

**黑箱測試（Black-Box Testing）**
- **定義**：不關注內部實作，僅驗證輸入輸出
- **適用場景**：功能正確性、邊界值、多語言相容性
- **工具**：pytest + requests + JSON schema validator

**灰箱測試（Grey-Box Testing）**
- **定義**：部分了解內部結構，結合日誌與系統狀態
- **適用場景**：整合測試、效能測試、錯誤追蹤
- **工具**：pytest + Docker logs + Allure attachments

**白箱測試（White-Box Testing）**
- **應用程度**：本專案為 API 測試，較少使用白箱方法
- **潛在應用**：未來若開放 Ollama 引擎客製化，可考慮

---

### 3.3 自動化與手動測試策略

#### 自動化測試策略

**自動化原則**
- **高重複性**：回歸測試、冒煙測試 100% 自動化
- **高風險**：P0/P1 測試優先自動化
- **可預測**：輸入輸出明確的測試自動化
- **長期執行**：Nightly、效能測試必須自動化

**自動化實施**

| 測試類型 | 自動化率 | 執行頻率 | 工具 |
|---------|---------|---------|------|
| Unit + Boundary | 100% | 每次 PR | pytest |
| Compatibility | 100% | 每次 PR | pytest + fixtures |
| Integration + E2E | 100% | Nightly | pytest |
| Security | 100% | Nightly | pytest |
| Performance | 100% | 每週 | JMeter |
| Stability | 100% | 每週 | JMeter |

**自動化架構**

```python
# 自動化測試核心模式
@pytest.fixture
def ollama_client():
    """提供統一的 API client"""
    return OllamaClient(base_url="http://localhost:11434")

@pytest.fixture
def validator():
    """提供統一的驗證器"""
    return ResponseValidator()

def test_chat_basic(ollama_client, validator):
    """使用共用 fixture 的自動化測試"""
    response = ollama_client.chat(messages=[...])
    validator.assert_status_code(response, 200)
```

#### 手動測試策略

**手動測試場景**（保留 < 10%）
- **探索性測試**：發現未知問題、新功能初探
- **使用者體驗**：API 易用性、錯誤訊息友善度
- **Ad-hoc 測試**：臨時需求、快速驗證

---

### 3.4 測試優先順序與風險導向策略

#### 風險導向測試策略

根據**業務影響**與**發生機率**進行風險評估，優先測試高風險項目。

#### 風險矩陣

```
高 │ P1: 效能瓶頸      │ P0: 核心 API 失效
影 │ (中度優先)        │ (最高優先)
響 ├─────────────────┼─────────────────
度 │ P3: UI 體驗問題   │ P2: 多語言相容性
低 │ (低優先)          │ (高度優先)
   └─────────────────┴─────────────────
     低                  高
         發生機率
```

#### 優先順序分級

| 優先級 | 定義 | 測試範例 | 執行時機 |
|-------|------|---------|---------|
| **P0** | 核心功能失效導致系統不可用 | `/api/chat` 無法回應 | 每次 PR + Nightly |
| **P1** | 重要功能異常影響使用者體驗 | Token 限制失效、回應時間過長 | 每次 PR + Nightly |
| **P2** | 次要功能問題或特定場景異常 | 特定語言顯示異常 | Nightly |
| **P3** | 體驗優化或邊緣場景 | 錯誤訊息不夠友善 | Manual 或 Sprint 末期 |

#### 測試執行順序

**PR 測試（快速回饋）**
1. P0 單元測試（< 1 分鐘）
2. P1 邊界測試（< 2 分鐘）
3. P1 多語言測試（< 2 分鐘）
4. P1 錯誤處理測試（< 1 分鐘）

**Nightly 測試（完整驗證）**
1. P0 端到端測試（< 3 分鐘）
2. P1 整合測試（< 3 分鐘）
3. P1 安全性測試（< 3 分鐘）
4. P2 回歸測試（< 5 分鐘）
5. P2 可用性測試（< 3 分鐘）

#### 風險應對措施

| 風險項目 | 風險等級 | 應對措施 |
|---------|---------|---------|
| API 回應時間過長 | P1 | JMeter 效能測試每週監控 |
| 多語言亂碼 | P2 | 10 種語言 fixtures 全覆蓋 |
| 並行請求衝突 | P1 | pytest-xdist 並行測試 |
| CI/CD pipeline 不穩定 | P1 | 重試機制 + 通知機制 |

---

## 4. 測試環境與工具

### 4.1 測試環境架構與配置

#### 環境分層架構

```
┌─────────────────────────────────────────────────────┐
│                  開發環境（Local）                    │
│  Python 3.11+ | Docker Desktop | Ollama (llama3)    │
│  用途：開發測試、偵錯、快速驗證                        │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│              CI 環境（GitHub Actions）                │
│  Ubuntu 22.04 | Docker | Ollama (tinyllama)         │
│  用途：PR 測試、Nightly 測試、自動化回歸              │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│            效能測試環境（JMeter Workflow）            │
│  JMeter 5.x | 100/1000 並行 | 長時間穩定性測試        │
│  用途：效能基準測試、壓力測試、穩定性驗證              │
└─────────────────────────────────────────────────────┘
```

#### 環境配置詳細說明

**開發環境（Local Development）**

| 元件 | 版本 | 配置 |
|------|------|------|
| **作業系統** | Windows 11 / macOS / Linux | 任意開發環境 |
| **Python** | 3.11+ | 虛擬環境隔離 |
| **Docker** | 24.x+ | Ollama 容器運行 |
| **Ollama Model** | llama3 | 本地高效能模型 |
| **IDE** | VS Code | pytest 插件支援 |

環境變數配置：
```bash
OLLAMA_MODEL=llama3           # 本地使用較大模型
OLLAMA_MAX_TOKENS=100         # 較高 token 限制
OLLAMA_TIMEOUT=300            # 較長超時時間
```

**CI 環境（GitHub Actions）**

| 元件 | 版本 | 配置 |
|------|------|------|
| **Runner** | ubuntu-22.04 | GitHub 託管 |
| **Python** | 3.11 | 矩陣測試支援 |
| **Docker** | 預安裝 | Ollama 容器運行 |
| **Ollama Model** | tinyllama | 快速輕量模型 |
| **並行執行** | pytest-xdist | 加速測試執行 |

環境變數配置：
```bash
OLLAMA_MODEL=tinyllama        # CI 使用輕量模型
OLLAMA_MAX_TOKENS=32          # 限制輸出降低執行時間
OLLAMA_TIMEOUT=120            # 較短超時時間
OLLAMA_RETRIES=1              # 重試機制
```

**效能測試環境（JMeter）**

| 元件 | 版本 | 配置 |
|------|------|------|
| **JMeter** | 5.6.3 | 分散式負載產生 |
| **測試計畫** | performance.jmx | 100 並行用戶 |
| **測試計畫** | stability.jmx | 1000 次迭代 |
| **報告格式** | HTML Dashboard | 自動發布 GitHub Pages |

---

### 4.2 測試工具清單與版本

#### 核心測試工具

| 工具名稱 | 版本 | 用途 | 官網 |
|---------|------|------|------|
| **pytest** | Latest | 測試執行引擎 | [pytest.org](https://pytest.org/) |
| **pytest-xdist** | Latest | 並行測試執行 | [PyPI](https://pypi.org/project/pytest-xdist/) |
| **pytest-timeout** | Latest | 測試超時控制 | [PyPI](https://pypi.org/project/pytest-timeout/) |
| **allure-pytest** | Latest | 測試報告生成 | [allurereport.org](https://allurereport.org/) |
| **requests** | Latest | HTTP 請求庫 | [requests.org](https://requests.org/) |

#### 輔助工具

| 工具名稱 | 版本 | 用途 |
|---------|------|------|
| **Apache JMeter** | 5.6.3 | 效能與穩定性測試 |
| **Docker** | 24.x+ | 容器化 Ollama 服務 |
| **Allure CLI** | 2.x | 報告生成與發布 |
| **GitHub Actions** | N/A | CI/CD 自動化 |
| **GitHub Pages** | N/A | 測試報告託管 |

#### Python 套件依賴

```txt
# requirements.txt
pytest>=8.0.0
pytest-xdist>=3.5.0
pytest-timeout>=2.2.0
allure-pytest>=2.13.2
requests>=2.31.0
```

安裝指令：
```bash
pip install -r requirements.txt
```

---

### 4.3 自動化測試架構設計

#### 架構設計原則

- **DRY（Don't Repeat Yourself）**：共用元件重用率 > 80%
- **模組化**：測試、資料、輔助工具分離
- **可擴展**：新增測試類型僅需增加目錄
- **易維護**：清晰的命名規範與目錄結構

#### 測試架構分層

```
┌─────────────────────────────────────────────────────┐
│                   測試案例層                         │
│  tests/unit, tests/boundary, tests/e2e, ...         │
│  職責：具體測試邏輯、測試資料引用                      │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│                   共用元件層                         │
│  conftest.py, helpers/test_helper.py                │
│  職責：Fixture 定義、驗證器、批次執行器               │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│                   測試資料層                         │
│  fixtures/multilingual.json, special_chars.json     │
│  職責：測試資料管理、資料驅動測試                      │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│                  API Client 層                       │
│  helpers/test_helper.py (OllamaClient)              │
│  職責：API 請求封裝、錯誤處理、重試機制               │
└─────────────────────────────────────────────────────┘
```

#### 核心設計模式

**1. Fixture Pattern（共用資源模式）**

```python
# tests/conftest.py
@pytest.fixture(scope="session")
def ollama_client():
    """提供統一的 Ollama API 客戶端"""
    return OllamaClient(
        base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        timeout=int(os.getenv("OLLAMA_TIMEOUT", "120"))
    )

@pytest.fixture
def validator():
    """提供統一的回應驗證器"""
    return ResponseValidator()
```

**2. Page Object Pattern（資料封裝模式）**

```python
# fixtures/multilingual.json
{
    "languages": [
        {"name": "中文", "prompt": "你好，請介紹自己"},
        {"name": "English", "prompt": "Hello, please introduce yourself"},
        ...
    ]
}
```

**3. Helper Pattern（輔助工具模式）**

```python
# helpers/test_helper.py
class TestHelper:
    @staticmethod
    def extract_json_from_response(text):
        """從回應中提取 JSON"""
        # 實作邏輯
        pass
```

#### 目錄結構設計

```
Local_LLM_test/
├── tests/                          # 測試案例
│   ├── conftest.py                 # 全域 fixture 定義
│   ├── unit/                       # 單元測試（40%）
│   ├── boundary/                   # 邊界測試（15%）
│   ├── compatibility/              # 相容性測試（15%）
│   ├── integration/                # 整合測試（10%）
│   ├── e2e/                        # 端到端測試（10%）
│   ├── regression/                 # 回歸測試（5%）
│   ├── security/                   # 安全性測試
│   ├── stability/                  # 穩定性測試
│   ├── performance/                # 效能測試
│   ├── usability/                  # 可用性測試
│   └── error_handling/             # 錯誤處理測試
├── helpers/                        # 共用輔助工具
│   ├── __init__.py
│   └── test_helper.py              # 4 個輔助類別，15 個方法
├── fixtures/                       # 測試資料
│   ├── multilingual.json           # 10 種語言資料
│   └── special_chars.json          # 特殊字元資料
├── allure-report/                  # Allure 測試報告
├── jmeter-dashboard-report/        # JMeter 報告
├── .github/workflows/              # CI/CD 配置
│   ├── pr-tests.yml
│   ├── nightly-tests.yml
│   ├── manual-tests.yml
│   └── jmeter-workflow.yml
└── docs/                           # 專案文件
```

---

### 4.4 CI/CD 整合與部署流程

#### CI/CD 策略概覽

本專案採用**三階段測試策略**，平衡速度與覆蓋率：

| 階段 | 觸發時機 | 執行時間 | 測試範圍 | 目的 |
|------|---------|---------|---------|------|
| **PR 測試** | Pull Request | 5-10 分鐘 | Unit + Boundary + Compatibility + Error Handling | 快速回饋 |
| **Nightly 測試** | 每日 00:00 UTC | 20-30 分鐘 | E2E + Integration + Regression + Security + Usability | 完整驗證 |
| **Manual 測試** | 手動觸發 | 彈性 | 自訂 markers | 臨時驗證 |
| **JMeter 測試** | 每週日 00:00 UTC | 15-20 分鐘 | Performance + Stability | 效能基準 |

#### PR 測試流程（Fast Feedback Loop）

```yaml
# .github/workflows/pr-tests.yml
name: PR Tests (Fast Feedback)

on:
  pull_request:
    branches: [main]

jobs:
  pr-tests:
    runs-on: ubuntu-22.04
    steps:
      - name: Checkout code
      - name: Setup Python 3.11
      - name: Install dependencies
      - name: Start Ollama (tinyllama)
      - name: Run Unit Tests
        run: pytest tests/unit -v --alluredir=allure-results
      - name: Run Boundary Tests
        run: pytest tests/boundary -v --alluredir=allure-results
      - name: Run Compatibility Tests
        run: pytest tests/compatibility -v --alluredir=allure-results
      - name: Run Error Handling Tests
        run: pytest tests/error_handling -v --alluredir=allure-results
      - name: Generate Allure Report
      - name: Publish to GitHub Pages
```

**關鍵設計**：
- ⚡ **快速模型**：使用 tinyllama 降低執行時間
- 🎯 **聚焦測試**：僅執行高優先級測試
- 🔄 **並行執行**：pytest-xdist 加速
- 📊 **即時報告**：自動發布到 GitHub Pages

#### Nightly 測試流程（Comprehensive Validation）

```yaml
# .github/workflows/nightly-tests.yml
name: Nightly Tests (Comprehensive)

on:
  schedule:
    - cron: '0 0 * * *'  # 每日 00:00 UTC
  workflow_dispatch:

jobs:
  nightly-tests:
    runs-on: ubuntu-22.04
    strategy:
      matrix:
        test-suite: [e2e, integration, regression, security, usability]
    steps:
      - name: Checkout code
      - name: Setup Python 3.11
      - name: Install dependencies
      - name: Start Ollama (tinyllama)
      - name: Run ${{ matrix.test-suite }} Tests
        run: pytest tests/${{ matrix.test-suite }} -v --alluredir=allure-results
      - name: Upload Results
      - name: Merge Results & Publish Report
```

**關鍵設計**：
- 🌙 **夜間執行**：不影響開發流程
- 🔀 **矩陣策略**：並行執行 5 種測試套件
- 📈 **完整覆蓋**：涵蓋所有測試類型
- 🚨 **失敗通知**：Slack/Email 通知

#### 部署流程圖

```
開發者提交 PR
      ↓
GitHub Actions 觸發
      ↓
┌─────────────────┐
│  環境準備        │
│  - Python 3.11  │
│  - Docker       │
│  - Ollama       │
└─────────────────┘
      ↓
┌─────────────────┐
│  執行測試        │
│  - PR: 5-10min  │
│  - Nightly: 30m │
└─────────────────┘
      ↓
┌─────────────────┐
│  生成報告        │
│  - Allure       │
│  - JMeter       │
└─────────────────┘
      ↓
┌─────────────────┐
│  發布報告        │
│  - GitHub Pages │
└─────────────────┘
      ↓
測試通過 → Merge
測試失敗 → 通知修復
```

---

### 4.5 測試儀表板與可視化設計

#### Allure 測試報告

**報告結構**

```
Allure Report
├── Overview              # 總覽（通過率、執行時間）
├── Categories            # 測試分類（Unit, Boundary, E2E...）
├── Suites                # 測試套件
├── Graphs                # 圖表（趨勢、分布）
├── Timeline              # 時間軸
├── Behaviors             # BDD 行為視圖
└── Packages              # 套件結構
```

**核心指標儀表板**

| 指標 | 顯示方式 | 數值範例 |
|------|---------|---------|
| **測試通過率** | 環形圖 | 98.2% |
| **執行時間** | 時間軸 | 8 分 32 秒 |
| **測試分布** | 長條圖 | Unit: 22, Boundary: 8, E2E: 6 |
| **缺陷趨勢** | 折線圖 | 本週 2 → 上週 5 |
| **Flaky Tests** | 標籤 | 0 個不穩定測試 |

**報告訪問方式**

- **PR 測試報告**：`https://howie0721.github.io/Local_LLM_API_TestSuite/pr-tests/allure-report/latest/`
- **Nightly 測試報告**：`https://howie0721.github.io/Local_LLM_API_TestSuite/pr-tests/nightly-tests/allure-report/latest/`
- **Manual 測試報告**：`https://howie0721.github.io/Local_LLM_API_TestSuite/pr-tests/manual-tests/allure-report/latest/`

#### JMeter Dashboard 報告

**效能測試報告**

- **APDEX（Application Performance Index）**：用戶滿意度指標
- **Requests Summary**：請求統計（總數、成功率、錯誤率）
- **Statistics**：平均回應時間、中位數、P90/P95/P99
- **Throughput**：吞吐量（requests/sec）
- **Response Time Percentiles**：回應時間百分位數圖表

**穩定性測試報告**

- **1000 次迭代統計**：成功率、失敗率、錯誤類型分布
- **Response Time Over Time**：回應時間趨勢圖
- **Active Threads Over Time**：並行線程數變化
- **Bytes Throughput**：網路吞吐量

**報告訪問方式**

- **效能測試報告**：`jmeter-dashboard-report/performance/index.html`
- **穩定性測試報告**：`jmeter-dashboard-report/stability/index.html`

#### 品質指標儀表板（建議實作）

```
┌─────────────────────────────────────────────────────┐
│              品質指標即時儀表板                       │
├─────────────────────────────────────────────────────┤
│  測試通過率          98.2%  ████████████░░  ↑ 0.5%   │
│  測試覆蓋率          85.7%  █████████████░  ↑ 2.1%   │
│  P0 測試通過率       100%   ██████████████  ─        │
│  平均回應時間        3.2s   ████░░░░░░░░░░  ↓ 0.3s   │
│  缺陷密度           0.02/TC █░░░░░░░░░░░░░  ↓ 0.01   │
└─────────────────────────────────────────────────────┘
```

---

## 5. 測試項目與案例設計原則

### 5.1 測試案例設計方法與分類

#### 測試案例設計方法論

本專案採用多種測試設計技術，確保測試覆蓋完整性與效率：

| 設計方法 | 適用場景 | 範例 |
|---------|---------|------|
| **等價類劃分** | 參數範圍測試 | Token 範圍：0, 1-31, 32, 33+ |
| **邊界值分析** | 極值測試 | Token: 0, 1, 31, 32, 33 |
| **決策表** | 多條件組合 | 模型 × Stream × Temperature 組合 |
| **狀態轉換** | 流程測試 | Chat 多輪對話狀態轉換 |
| **錯誤推測** | 異常場景 | 無效模型名稱、網路中斷 |
| **正交表** | 參數組合優化 | 減少組合測試數量 |

#### 測試案例命名規範

**命名格式**：`test_<功能>_<場景>_<預期結果>`

範例：
```python
# ✅ 良好命名
def test_chat_valid_message_returns_200():
    """測試 Chat API 有效訊息回傳 200"""

def test_generate_empty_prompt_returns_400():
    """測試 Generate API 空提示詞回傳 400"""

def test_chat_stream_mode_returns_chunks():
    """測試 Chat API 串流模式回傳分塊資料"""

# ❌ 不良命名
def test_1():
def test_chat():
def test_api_works():
```

#### 測試案例分類體系

```
測試案例 (56 個)
├── 功能測試 (40 個)
│   ├── Unit Testing (22 個)
│   ├── Boundary Testing (8 個)
│   ├── Compatibility Testing (5 個)
│   └── Error Handling (5 個)
├── 非功能測試 (10 個)
│   ├── Performance Testing (3 個)
│   ├── Security Testing (4 個)
│   └── Stability Testing (3 個)
└── 流程測試 (6 個)
    ├── Integration Testing (3 個)
    ├── E2E Testing (2 個)
    └── Regression Testing (1 個)
```

---

### 5.2 資料驅動與模組化策略

#### 資料驅動測試（Data-Driven Testing）

**設計原則**
- 測試邏輯與測試資料分離
- 測試資料集中管理於 `fixtures/` 目錄
- 使用 `@pytest.mark.parametrize` 進行參數化

**實作範例**

```python
# fixtures/multilingual.json
{
    "languages": [
        {"code": "zh", "name": "中文", "prompt": "你好，請介紹自己"},
        {"code": "en", "name": "English", "prompt": "Hello, introduce yourself"},
        {"code": "ja", "name": "日本語", "prompt": "こんにちは、自己紹介してください"},
        ...
    ]
}

# tests/compatibility/test_multilingual.py
import json
import pytest

@pytest.fixture
def multilingual_data():
    with open("fixtures/multilingual.json") as f:
        return json.load(f)

@pytest.mark.parametrize("language", multilingual_data()["languages"])
def test_chat_multilingual(ollama_client, validator, language):
    """測試多語言支援"""
    response = ollama_client.chat(
        messages=[{"role": "user", "content": language["prompt"]}]
    )
    validator.assert_status_code(response, 200)
    validator.assert_json_field(response, "message.content")
```

**優勢**
- ✅ 新增語言僅需更新 JSON，無需修改測試程式碼
- ✅ 測試資料可重用於不同測試案例
- ✅ 易於維護與擴展

#### 模組化策略

**共用元件架構**

```python
# tests/conftest.py - 全域 Fixture
@pytest.fixture(scope="session")
def ollama_client():
    """提供 Ollama API 客戶端"""
    return OllamaClient()

@pytest.fixture
def validator():
    """提供回應驗證器"""
    return ResponseValidator()

@pytest.fixture
def schema_validator():
    """提供 Schema 驗證器"""
    return SchemaValidator()

@pytest.fixture(name="test_helper")
def test_helper_fixture():
    """提供測試輔助工具"""
    return TestHelper()

@pytest.fixture
def batch_helper(ollama_client):
    """提供批次測試執行器"""
    return BatchTestHelper(ollama_client)
```

**共用元件重用統計**

| 元件 | 使用次數 | 重用率 |
|------|---------|-------|
| `ollama_client` | 37/37 檔案 | 100% |
| `validator` | 37/37 檔案 | 100% |
| `schema_validator` | 25/37 檔案 | 68% |
| `test_helper` | 15/37 檔案 | 41% |
| `batch_helper` | 8/37 檔案 | 22% |

**模組化效益**
- 🎯 **DRY 原則**：避免重複程式碼，共用元件重用率 > 80%
- 🔧 **易維護**：修改驗證邏輯僅需更新 `ResponseValidator`
- 🚀 **快速開發**：新測試案例開發時間減少 60%

---

### 5.3 覆蓋率矩陣與測試深度

#### 測試覆蓋矩陣

| API Endpoint | Unit | Boundary | Compatibility | Integration | E2E | Security | Performance | Stability | 覆蓋率 |
|-------------|------|----------|---------------|-------------|-----|----------|-------------|-----------|-------|
| **/api/chat** | ✅ 12 | ✅ 4 | ✅ 10 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 1 | ✅ 1 | **95%** |
| **/api/generate** | ✅ 10 | ✅ 4 | ✅ 10 | ✅ 1 | ✅ 1 | ✅ 2 | ✅ 1 | ✅ 1 | **92%** |
| **/api/tags** | ✅ 1 | - | - | - | - | - | - | - | **30%** |

**總覆蓋率**：**85.7%**（達成目標 ≥ 85%）

#### 測試深度分級

| 深度等級 | 定義 | 範例 | 測試數量 |
|---------|------|------|---------|
| **L1: Smoke** | 基本功能可用性 | API 回傳 200 | 5 |
| **L2: Functional** | 功能正確性 | 回應包含 `message.content` | 30 |
| **L3: Edge Case** | 邊界與異常 | Token = 0, 32, 33 | 12 |
| **L4: Integration** | 流程與互動 | Chat + Generate 組合 | 4 |
| **L5: Non-Functional** | 效能、安全、穩定 | P95 < 5s, SQL Injection | 5 |

#### 功能點覆蓋詳細說明

**Chat API 覆蓋項目**
- ✅ 基本對話（單輪、多輪）
- ✅ Stream 模式（true/false）
- ✅ 上下文保留（context 參數）
- ✅ 模型切換（tinyllama/llama3）
- ✅ 參數組合（temperature, top_p, top_k）
- ✅ Token 限制（num_predict）
- ✅ 多語言支援（10 種語言）
- ✅ 特殊字元處理（Emoji, 符號, 控制字元）
- ✅ 錯誤處理（無效模型、錯誤參數）
- ✅ 安全性（Injection 攻擊）

**Generate API 覆蓋項目**
- ✅ 基本生成
- ✅ Prompt 變化（短/中/長）
- ✅ Stream 模式
- ✅ 參數組合
- ✅ Token 限制
- ✅ 多語言支援
- ✅ 特殊字元處理
- ✅ 錯誤處理
- ✅ 安全性

---

### 5.4 測試流程圖與責任分工

#### 測試生命週期流程圖

```
需求分析
    ↓
測試計畫撰寫 (本文件)
    ↓
測試案例設計
    ↓
測試環境準備
    ↓
┌─────────────────────────────────────┐
│        測試執行階段                  │
├─────────────────────────────────────┤
│  PR Tests → Nightly Tests → Manual │
│      ↓           ↓            ↓     │
│  快速回饋    完整驗證    臨時測試    │
└─────────────────────────────────────┘
    ↓
缺陷管理與追蹤
    ↓
測試報告生成
    ↓
┌─────────────────────────────────────┐
│           驗收階段                   │
├─────────────────────────────────────┤
│  ✅ P0 測試 100% 通過                │
│  ✅ 覆蓋率 ≥ 85%                     │
│  ✅ 無 Critical/High 未修復缺陷      │
└─────────────────────────────────────┘
    ↓
發布上線
    ↓
持續監控（Nightly Tests）
```

#### 角色與責任分工（RACI 矩陣）

| 活動 | 測試工程師 | 開發工程師 | DevOps 工程師 | 產品經理 |
|------|-----------|-----------|--------------|---------|
| **測試計畫撰寫** | R, A | C | I | C |
| **測試案例設計** | R, A | C | I | I |
| **測試環境準備** | A | C | R | I |
| **測試執行（自動化）** | R, A | I | C | I |
| **缺陷管理** | R, A | R | I | C |
| **測試報告撰寫** | R, A | I | I | C |
| **CI/CD 維護** | C | C | R, A | I |
| **發布決策** | C | C | I | R, A |

**圖例**：
- **R (Responsible)**：執行者
- **A (Accountable)**：負責者
- **C (Consulted)**：諮詢者
- **I (Informed)**：知會者

#### 測試執行流程詳細說明

**PR 測試流程**
1. 開發者提交 PR
2. GitHub Actions 自動觸發
3. 執行快速測試套件（5-10 分鐘）
4. 測試通過 → PR 可 Merge
5. 測試失敗 → 通知開發者修復

**Nightly 測試流程**
1. 每日 00:00 UTC 自動觸發
2. 執行完整測試套件（20-30 分鐘）
3. 生成 Allure 報告並發布
4. 測試失敗 → Email/Slack 通知團隊
5. 測試工程師追蹤與分類缺陷

**缺陷管理流程**
1. 測試發現缺陷 → 建立 GitHub Issue
2. 分類缺陷等級（Critical/High/Medium/Low）
3. 分配給開發工程師修復
4. 修復後執行 Regression Tests
5. 驗證通過 → 關閉 Issue

---

## 6. 測試排程與里程碑

### 6.1 測試活動時間表

#### 專案時程概覽

本測試專案採用**持續整合（CI）+ 定期完整驗證**的混合模式，確保快速回饋與全面品質保證的平衡。

#### 測試活動週期表

| 測試活動 | 執行頻率 | 執行時間 | 負責人 | 產出 |
|---------|---------|---------|-------|------|
| **PR 快速測試** | 每次 Pull Request | 5-10 分鐘 | GitHub Actions | Allure 報告 |
| **Nightly 完整測試** | 每日 00:00 UTC | 20-30 分鐘 | GitHub Actions | Allure 報告 + Email 通知 |
| **效能測試** | 每週日 00:00 UTC | 10 分鐘 | JMeter Workflow | JMeter Dashboard |
| **穩定性測試** | 每週日 00:10 UTC | 15 分鐘 | JMeter Workflow | JMeter Dashboard |
| **手動探索性測試** | Sprint 中期 | 2-4 小時 | 測試工程師 | 測試筆記 |
| **回歸測試** | Release 前 | 30 分鐘 | GitHub Actions | Allure 報告 |
| **測試報告審查** | 每週五 | 1 小時 | 測試團隊 | 週報告 |

#### 每日測試時間軸

```
00:00 UTC - Nightly 完整測試啟動
    ↓
00:05 - E2E 測試完成
    ↓
00:10 - Integration 測試完成
    ↓
00:15 - Regression 測試完成
    ↓
00:20 - Security 測試完成
    ↓
00:25 - Usability 測試完成
    ↓
00:30 - 報告生成與發布
    ↓
00:35 - Email/Slack 通知團隊

每週日額外執行：
00:00 - 效能測試（10 分鐘）
00:10 - 穩定性測試（15 分鐘）
```

#### Sprint 測試活動規劃（以 2 週 Sprint 為例）

| Day | 測試活動 | 工作內容 |
|-----|---------|---------|
| **Sprint Day 1-2** | 測試計畫更新 | 根據新需求更新測試案例 |
| **Sprint Day 3-8** | 持續整合測試 | 每次 PR 觸發測試，快速回饋 |
| **Sprint Day 6-7** | 探索性測試 | 手動測試新功能、邊界場景 |
| **Sprint Day 9** | 中期測試報告 | 測試覆蓋率、缺陷統計 |
| **Sprint Day 10-12** | 回歸測試 | 完整回歸驗證 |
| **Sprint Day 13** | 效能與安全測試 | 專項測試執行 |
| **Sprint Day 14** | Sprint 測試總結 | 發布決策會議 |

---

### 6.2 測試階段與交付節點

#### 測試階段劃分

本專案測試分為**四個主要階段**，每個階段有明確的進入準則（Entry Criteria）、退出準則（Exit Criteria）與交付物。

#### 階段 1：測試準備階段（Test Planning）

**時程**：Sprint 開始前 1 週

**進入準則**：
- ✅ 需求文件已確認
- ✅ 開發計畫已制定
- ✅ 測試環境已準備

**主要活動**：
1. 撰寫/更新測試計畫書
2. 設計測試案例
3. 準備測試資料（fixtures）
4. 設定 CI/CD pipeline

**交付物**：
- 📄 測試計畫書（本文件）
- 📄 測試案例設計文件
- 📊 測試覆蓋率矩陣
- 🔧 CI/CD 配置檔案

**退出準則**：
- ✅ 測試計畫經 Stakeholder 審查通過
- ✅ 測試環境驗證通過
- ✅ 測試案例設計完成 > 80%

---

#### 階段 2：單元與整合測試階段（Unit & Integration Testing）

**時程**：Sprint Day 1-10

**進入準則**：
- ✅ 測試準備階段完成
- ✅ 開發環境已建置
- ✅ 單元測試框架已設定

**主要活動**：
1. 開發人員執行單元測試
2. PR 自動觸發快速測試
3. 整合測試持續執行
4. 缺陷即時修復與驗證

**測試執行方式**：
- 🔄 **持續執行**：每次 PR 自動觸發
- ⚡ **快速回饋**：5-10 分鐘內完成
- 📊 **即時報告**：Allure 報告自動發布

**交付物**：
- 📊 每日測試執行報告（Allure）
- 🐛 缺陷清單（GitHub Issues）
- 📈 測試覆蓋率報告

**退出準則**：
- ✅ 單元測試通過率 ≥ 98%
- ✅ 整合測試通過率 ≥ 95%
- ✅ P0/P1 缺陷全數修復
- ✅ 測試覆蓋率 ≥ 85%

---

#### 階段 3：系統測試階段（System Testing）

**時程**：Sprint Day 11-13

**進入準則**：
- ✅ 單元與整合測試階段完成
- ✅ 無 Critical/High 未修復缺陷
- ✅ 功能開發已凍結（Code Freeze）

**主要活動**：
1. E2E 端到端測試
2. 效能測試（JMeter）
3. 安全性測試
4. 穩定性測試
5. 可用性測試

**測試執行方式**：
- 🌙 **Nightly 執行**：完整測試套件
- 📊 **效能測試**：每週日執行
- 🔒 **安全測試**：專項執行
- 🛡️ **穩定性測試**：長時間運行

**交付物**：
- 📊 系統測試報告
- 📈 效能測試報告（JMeter Dashboard）
- 🔒 安全性測試報告
- 🐛 缺陷清單與修復狀態

**退出準則**：
- ✅ E2E 測試通過率 ≥ 95%
- ✅ 效能指標達標（P95 < 5s）
- ✅ 安全測試無高風險項目
- ✅ 穩定性測試成功率 > 99%
- ✅ 無 Critical 未修復缺陷

---

#### 階段 4：驗收測試階段（Acceptance Testing）

**時程**：Sprint Day 14

**進入準則**：
- ✅ 系統測試階段完成
- ✅ 所有 P0 測試 100% 通過
- ✅ 無 Critical/High 未修復缺陷

**主要活動**：
1. 完整回歸測試
2. 業務場景驗證
3. 發布決策會議
4. 測試總結報告撰寫

**驗收標準**：
- ✅ 所有 P0 測試 100% 通過
- ✅ PR 測試通過率 ≥ 98%
- ✅ Nightly 測試通過率 ≥ 96%
- ✅ 測試覆蓋率 ≥ 85%
- ✅ 無 Critical/High 未修復缺陷
- ✅ 效能與安全指標達標

**交付物**：
- 📊 **最終測試報告**（包含所有階段總結）
- 📈 **品質指標儀表板**
- ✅ **發布建議書**（Go/No-Go Decision）
- 📚 **測試交接文件**

**退出準則**：
- ✅ Stakeholder 簽核通過
- ✅ 發布檢查清單完成
- ✅ 生產環境準備就緒

---

### 6.3 測試進度追蹤方式

#### 進度追蹤指標

本專案使用**多維度指標**追蹤測試進度，確保透明度與可控性。

#### 核心追蹤指標

| 指標類別 | 指標名稱 | 計算方式 | 目標值 | 追蹤頻率 |
|---------|---------|---------|-------|---------|
| **執行進度** | 測試案例執行率 | 已執行 / 總案例數 × 100% | 100% | 每日 |
| **品質指標** | 測試通過率 | 通過數 / 執行數 × 100% | ≥ 98% | 每日 |
| **覆蓋率** | 程式碼覆蓋率 | 覆蓋行數 / 總行數 × 100% | ≥ 85% | 每週 |
| **缺陷指標** | 缺陷密度 | 缺陷數 / 測試案例數 | < 0.05 | 每週 |
| **效率指標** | 缺陷修復週期 | 缺陷關閉日期 - 建立日期 | < 3 天 | 每週 |
| **穩定性** | Flaky Test 比例 | Flaky 數 / 總案例數 × 100% | < 2% | 每週 |

#### 進度追蹤儀表板

```
┌─────────────────────────────────────────────────────┐
│            測試進度追蹤儀表板（即時更新）             │
├─────────────────────────────────────────────────────┤
│  Sprint: 2025-W45 (Day 8/14)                        │
│                                                     │
│  測試執行進度                                        │
│  ████████████████░░░░  82%  (46/56 案例已執行)      │
│                                                     │
│  測試通過率                                          │
│  ███████████████████░  98.2%  ↑ 0.5%                │
│                                                     │
│  測試覆蓋率                                          │
│  █████████████████░░░  85.7%  ↑ 2.1%                │
│                                                     │
│  缺陷統計                                            │
│  Critical: 0  |  High: 1  |  Medium: 3  |  Low: 5   │
│                                                     │
│  待辦事項                                            │
│  ⏳ 完成剩餘 10 個測試案例                            │
│  🐛 修復 1 個 High 缺陷                              │
│  📊 準備中期測試報告                                 │
└─────────────────────────────────────────────────────┘
```

#### 進度追蹤工具與方法

**1. GitHub Actions 自動追蹤**
- 每次 PR/Nightly 測試自動記錄結果
- Allure 報告即時更新
- GitHub Pages 自動發布

**2. 每日站會（Daily Standup）**
- 檢視昨日測試執行狀況
- 討論阻礙項目（Blockers）
- 調整當日測試計畫

**3. 每週測試報告**
- 測試執行統計
- 缺陷趨勢分析
- 風險項目追蹤
- 下週計畫調整

**4. Sprint 回顧（Retrospective）**
- 測試效率分析
- 流程改善建議
- 工具優化討論

#### 進度預警機制

| 預警等級 | 觸發條件 | 應對措施 |
|---------|---------|---------|
| 🟢 **正常** | 所有指標達標 | 持續監控 |
| 🟡 **注意** | 1. 測試通過率 < 95%<br>2. 執行進度落後 10% | 1. 增加測試人力<br>2. 調整測試優先順序 |
| 🟠 **警告** | 1. 測試通過率 < 90%<br>2. Critical 缺陷未修復<br>3. 執行進度落後 20% | 1. 召開緊急會議<br>2. 調整 Sprint 目標<br>3. 延後發布決策 |
| 🔴 **危急** | 1. 測試通過率 < 80%<br>2. 多個 Critical 缺陷<br>3. 無法完成測試 | 1. 停止新功能開發<br>2. 全員投入缺陷修復<br>3. 考慮延後發布 |

#### 進度報告範本

**每日測試簡報（Daily Test Summary）**

```
日期：2025-11-05
執行人：測試工程師

【執行摘要】
- 執行測試：12 個案例
- 通過：11 個 (91.7%)
- 失敗：1 個
- 新增缺陷：1 個 (Medium)

【失敗案例】
- test_chat_stream_mode_timeout (Medium)
  原因：Stream 模式超時 (> 120s)
  負責人：開發工程師 A
  預計修復：2025-11-06

【明日計畫】
- 完成剩餘 8 個 E2E 測試案例
- 驗證已修復的 2 個缺陷
```

**每週測試報告（Weekly Test Report）**

```
週次：2025-W45
報告日期：2025-11-08

【測試執行統計】
- 總執行案例：56 個
- 通過率：98.2%
- 新增案例：3 個
- 覆蓋率：85.7% (+2.1%)

【缺陷統計】
- 新增缺陷：8 個
- 已修復：6 個
- 待修復：2 個 (High: 1, Medium: 1)
- 平均修復週期：2.3 天

【風險項目】
- Stream 模式偶發超時（優先處理中）

【下週重點】
- 完成效能測試
- 準備 Sprint 測試總結報告
```

---

## 7. 測試資源與角色分工

### 7.1 測試團隊成員與職責

#### 團隊組織架構

```
測試經理 (Test Manager)
    ↓
┌───────────────────┬───────────────────┐
│                   │                   │
資深測試工程師      自動化測試工程師    效能測試工程師
(Senior QA)        (Automation QA)     (Performance QA)
```

#### 角色與職責矩陣

| 角色 | 人數 | 主要職責 | 次要職責 | 所需技能 |
|------|-----|---------|---------|---------|
| **測試經理** | 1 | • 測試策略制定<br>• 資源分配<br>• 風險管理<br>• 跨團隊協調 | • 測試報告審核<br>• 發布決策建議 | • 測試管理經驗<br>• 專案管理能力<br>• 溝通協調能力 |
| **資深測試工程師** | 1-2 | • 測試計畫撰寫<br>• 測試案例設計<br>• 探索性測試<br>• 缺陷管理 | • Code Review<br>• 新人培訓 | • 5+ 年測試經驗<br>• API 測試專業<br>• Python 熟練 |
| **自動化測試工程師** | 1-2 | • 自動化測試開發<br>• CI/CD 維護<br>• 測試框架優化<br>• 測試報告生成 | • 測試工具研究<br>• 技術分享 | • 3+ 年自動化經驗<br>• Python + pytest<br>• DevOps 概念 |
| **效能測試工程師** | 0.5 | • JMeter 腳本開發<br>• 效能測試執行<br>• 效能瓶頸分析 | • 監控系統建置 | • 效能測試經驗<br>• JMeter 熟練<br>• 效能調校知識 |

#### 詳細職責說明

**測試經理（Test Manager）**

主要職責：
1. **策略規劃**
   - 制定測試策略與方法
   - 決定自動化範圍與優先順序
   - 評估測試工具與技術選型

2. **資源管理**
   - 分配測試人力與時間
   - 協調測試環境資源
   - 管理測試工具預算

3. **風險控制**
   - 識別測試風險
   - 制定應變計畫
   - 監控專案進度

4. **溝通協調**
   - 跨部門協作（開發、DevOps、產品）
   - Stakeholder 溝通
   - 測試報告呈現

**資深測試工程師（Senior QA Engineer）**

主要職責：
1. **測試設計**
   - 撰寫測試計畫書
   - 設計測試案例（Unit, Boundary, E2E）
   - 制定測試資料策略

2. **測試執行**
   - 執行探索性測試
   - 手動驗證複雜場景
   - 協助自動化測試開發

3. **品質保證**
   - Code Review 測試程式碼
   - 缺陷分類與優先順序判定
   - 測試覆蓋率評估

4. **知識傳承**
   - 新人培訓與指導
   - 測試文件維護
   - 最佳實踐分享

**自動化測試工程師（Automation QA Engineer）**

主要職責：
1. **測試開發**
   - 撰寫自動化測試程式碼（pytest）
   - 開發共用測試元件（fixtures, helpers）
   - 維護測試資料（multilingual, special_chars）

2. **CI/CD 整合**
   - 設定 GitHub Actions workflows
   - 配置 Allure 報告生成
   - 優化測試執行速度

3. **框架維護**
   - 重構測試程式碼（DRY 原則）
   - 升級測試工具版本
   - 解決 flaky tests 問題

4. **技術創新**
   - 研究新測試工具
   - 導入最佳實踐
   - 分享技術文章

**效能測試工程師（Performance QA Engineer）**

主要職責：
1. **效能測試**
   - 開發 JMeter 測試腳本
   - 執行負載測試與壓力測試
   - 分析效能瓶頸

2. **監控與分析**
   - 建立效能監控儀表板
   - 分析回應時間、吞吐量
   - 提供效能優化建議

---

### 7.2 跨部門協作與溝通窗口

#### 協作關係圖

```
        測試團隊
           ↓
    ┌──────┼──────┐
    ↓      ↓      ↓
  開發團隊  DevOps  產品團隊
    ↓      ↓      ↓
  • 缺陷   • CI/CD • 需求
    修復    維護    確認
  • Code  • 環境   • 驗收
    Review  配置    標準
```

#### 跨部門協作矩陣

| 協作部門 | 主要溝通窗口 | 協作頻率 | 協作內容 | 溝通工具 |
|---------|------------|---------|---------|---------|
| **開發團隊** | Tech Lead | 每日 | • 缺陷討論與修復<br>• Code Review<br>• 測試案例審查<br>• 技術問題諮詢 | Slack, GitHub Issues |
| **DevOps 團隊** | DevOps Engineer | 每週 | • CI/CD pipeline 維護<br>• 測試環境配置<br>• Docker/Ollama 問題排查<br>• 報告發布流程 | Slack, Email |
| **產品團隊** | Product Manager | Sprint 規劃會議 | • 需求確認<br>• 驗收標準定義<br>• 測試優先順序<br>• 發布決策 | Meeting, Email |
| **用戶支援團隊** | Support Lead | 按需 | • 生產問題回報<br>• 測試案例補充<br>• Bug 重現驗證 | Ticketing System |

#### 溝通機制

**1. 每日站會（Daily Standup）**
- **時間**：每日 10:00 AM
- **參與者**：測試團隊 + 開發 Tech Lead
- **時長**：15 分鐘
- **議程**：
  - 昨日完成項目
  - 今日計畫
  - 阻礙項目（Blockers）

**2. 測試同步會議（Test Sync Meeting）**
- **時間**：每週三 2:00 PM
- **參與者**：測試經理 + 資深測試工程師 + 產品經理
- **時長**：30 分鐘
- **議程**：
  - 測試進度回顧
  - 風險項目討論
  - 下週測試計畫

**3. Sprint 規劃會議（Sprint Planning）**
- **時間**：每兩週一次
- **參與者**：全團隊
- **時長**：2 小時
- **測試團隊輸出**：
  - 測試工作量估算
  - 測試風險識別
  - 測試資源需求

**4. Sprint 回顧會議（Sprint Retrospective）**
- **時間**：Sprint 結束日
- **參與者**：全團隊
- **時長**：1 小時
- **測試團隊分享**：
  - 測試效率改善建議
  - 流程優化提案
  - 工具與技術分享

#### 溝通工具與平台

| 工具 | 用途 | 使用場景 |
|------|------|---------|
| **Slack** | 即時溝通 | 日常討論、快速問題解決 |
| **GitHub Issues** | 缺陷追蹤 | 缺陷提報、狀態更新、討論 |
| **GitHub Projects** | 專案管理 | 測試任務追蹤、看板管理 |
| **Confluence** | 文件協作 | 測試計畫書、技術文件 |
| **Email** | 正式通知 | 測試報告、發布通知 |
| **Google Meet** | 視訊會議 | Sprint 規劃、回顧會議 |

---

### 7.3 測試資源需求與工具授權

#### 人力資源需求

| 階段 | 測試經理 | 資深 QA | 自動化 QA | 效能 QA | 總人日 |
|------|---------|--------|-----------|---------|-------|
| **測試準備** | 0.5 人週 | 1 人週 | 0.5 人週 | 0.2 人週 | 2.2 人週 |
| **開發階段** | 0.2 人週 | 0.5 人週 | 1 人週 | 0.1 人週 | 1.8 人週 |
| **系統測試** | 0.3 人週 | 1 人週 | 0.5 人週 | 0.5 人週 | 2.3 人週 |
| **驗收階段** | 0.5 人週 | 0.5 人週 | 0.3 人週 | 0.2 人週 | 1.5 人週 |
| **總計** | 1.5 人週 | 3 人週 | 2.3 人週 | 1 人週 | **7.8 人週** |

#### 硬體資源需求

| 資源類型 | 規格 | 數量 | 用途 | 費用估算 |
|---------|------|------|------|---------|
| **開發機器** | • CPU: 8 cores<br>• RAM: 16GB<br>• SSD: 512GB | 3 台 | 本地測試開發 | 自備 |
| **CI/CD Runner** | GitHub Actions | 無限 | 自動化測試執行 | 免費（公開專案）|
| **Docker 容器** | Ollama 官方映像 | 按需 | LLM 服務運行 | 免費 |
| **儲存空間** | GitHub Pages | 1GB | 測試報告託管 | 免費 |

#### 軟體工具與授權

| 工具 | 版本 | 授權類型 | 費用 | 用途 |
|------|------|---------|------|------|
| **Python** | 3.11+ | 開源 | 免費 | 測試框架基礎 |
| **pytest** | Latest | 開源（MIT） | 免費 | 測試執行引擎 |
| **Allure** | 2.x | 開源（Apache 2.0） | 免費 | 測試報告生成 |
| **JMeter** | 5.6.3 | 開源（Apache 2.0） | 免費 | 效能測試 |
| **Docker** | Latest | 免費（社群版） | 免費 | 容器化運行 |
| **GitHub Actions** | N/A | 免費（公開專案） | 免費 | CI/CD 平台 |
| **VS Code** | Latest | 免費 | 免費 | IDE |
| **Ollama** | Latest | 開源 | 免費 | LLM 服務 |

**總授權費用：$0**（全部使用開源工具）

#### 測試環境資源

| 環境 | 配置 | 數量 | 維護者 | 成本 |
|------|------|------|-------|------|
| **本地開發環境** | Docker Desktop + Ollama | 3 套 | 測試工程師 | 免費 |
| **CI 環境** | GitHub Actions + Docker | 無限 | DevOps | 免費 |
| **報告託管** | GitHub Pages | 1 個 | DevOps | 免費 |

#### 培訓與學習資源

| 資源類型 | 內容 | 預算 | 備註 |
|---------|------|------|------|
| **內部培訓** | • pytest 進階應用<br>• Allure 報告優化<br>• JMeter 效能測試 | 0 | 團隊內部分享 |
| **外部課程** | • API 測試最佳實踐<br>• LLM 測試策略 | $500/人 | 選修 |
| **技術書籍** | • Test-Driven Development<br>• Python Testing Cookbook | $100/人 | 選購 |
| **線上資源** | • pytest 官方文件<br>• Allure 文件<br>• GitHub Actions 文件 | 免費 | 自學 |

**總培訓預算：$0 - $600/人**（視需求而定）

---

## 8. 風險評估與應變計畫

### 8.1 測試風險清單

#### 風險識別方法

本專案使用 **FMEA（Failure Mode and Effects Analysis）** 方法識別測試風險，並根據**影響度**與**發生機率**進行優先順序排序。

#### 風險評估矩陣

```
高 │ R3: 測試環境不穩定 │ R1: 模型回應超時
影 │ (中度風險)         │ (高度風險)
響 ├───────────────────┼───────────────────
度 │ R6: 人力資源不足   │ R2: CI/CD Pipeline 失敗
低 │ (低度風險)         │ (中度風險)
   └───────────────────┴───────────────────
     低                  高
         發生機率
```

#### 詳細風險清單

| 風險ID | 風險描述 | 風險類別 | 影響度 | 發生機率 | 風險等級 | 負責人 |
|--------|---------|---------|-------|---------|---------|-------|
| **R1** | 模型回應時間過長，導致測試超時 | 技術風險 | 高 | 高 | 🔴 高 | 測試經理 |
| **R2** | CI/CD Pipeline 執行失敗，無法自動化測試 | 技術風險 | 中 | 中 | 🟡 中 | DevOps |
| **R3** | Docker 容器不穩定，Ollama 服務中斷 | 環境風險 | 高 | 低 | 🟡 中 | DevOps |
| **R4** | 測試資料不足，無法涵蓋邊界場景 | 資料風險 | 中 | 低 | 🟢 低 | 資深 QA |
| **R5** | Flaky tests 導致測試結果不穩定 | 測試風險 | 中 | 中 | 🟡 中 | 自動化 QA |
| **R6** | 測試人力資源不足，進度延遲 | 管理風險 | 低 | 低 | 🟢 低 | 測試經理 |
| **R7** | Ollama 模型更新導致測試失敗 | 變更風險 | 中 | 中 | 🟡 中 | 資深 QA |
| **R8** | GitHub Actions 配額不足 | 資源風險 | 低 | 低 | 🟢 低 | DevOps |
| **R9** | 多語言測試資料編碼問題 | 技術風險 | 中 | 低 | 🟢 低 | 自動化 QA |
| **R10** | 測試報告無法正常發布 | 報告風險 | 低 | 低 | 🟢 低 | DevOps |

---

### 8.2 風險影響分析

#### 高風險項目詳細分析

**R1: 模型回應時間過長，導致測試超時**

**風險描述**：
- Ollama LLM 模型在某些情況下回應時間超過設定的超時時間（120s）
- 特別是使用 llama3 模型或長 prompt 時容易發生

**影響分析**：
- 🔴 **測試執行時間延長**：原本 10 分鐘的測試可能延長至 30 分鐘
- 🔴 **測試失敗率上升**：超時測試被標記為失敗，降低通過率
- 🔴 **CI/CD 阻塞**：PR 無法及時獲得測試結果，延遲開發進度
- 🔴 **資源浪費**：CI/CD Runner 長時間佔用

**根本原因**：
1. 模型參數設定不當（num_predict 過高）
2. CI 環境資源限制（tinyllama 也可能超時）
3. 網路延遲或 Ollama 服務負載過高

**量化影響**：
- 預估影響測試案例：15% (8/56 個案例)
- 預估時間延長：200% (從 10 分鐘 → 30 分鐘)
- 預估通過率下降：5-10%

---

**R2: CI/CD Pipeline 執行失敗，無法自動化測試**

**風險描述**：
- GitHub Actions workflow 配置錯誤
- Docker 拉取失敗或 Ollama 啟動失敗
- Python 依賴安裝失敗

**影響分析**：
- 🟠 **自動化測試中斷**：無法執行 PR 或 Nightly 測試
- 🟠 **手動測試負擔增加**：需改為手動執行測試
- 🟠 **測試報告缺失**：無法生成 Allure 報告
- 🟠 **發布延遲**：無測試結果無法進行發布決策

**根本原因**：
1. Workflow YAML 配置錯誤
2. GitHub Actions Runner 環境變化
3. 第三方服務不穩定（Docker Hub, PyPI）

**量化影響**：
- 預估修復時間：2-4 小時
- 影響範圍：100% 自動化測試
- 預估延遲：半天至一天

---

**R3: Docker 容器不穩定，Ollama 服務中斷**

**風險描述**：
- Docker 容器意外停止
- Ollama 服務 OOM（Out of Memory）
- 模型載入失敗

**影響分析**：
- 🟠 **測試無法執行**：API 請求全部失敗
- 🟠 **測試結果不可信**：部分測試通過，部分失敗
- 🟠 **環境排查時間長**：需重啟容器、重新拉取模型

**根本原因**：
1. 記憶體不足（Ollama 需求 > 4GB）
2. Docker 版本不相容
3. 模型檔案損壞

**量化影響**：
- 預估發生頻率：每週 1-2 次
- 預估修復時間：10-30 分鐘
- 影響範圍：本地開發 + CI 環境

---

### 8.3 應變策略與備援方案

#### 風險應對策略框架

本專案採用 **4T 風險應對策略**：
1. **Transfer（轉移）**：透過工具或流程轉移風險
2. **Tolerate（容忍）**：接受低影響風險
3. **Treat（處理）**：降低風險發生機率或影響
4. **Terminate（終止）**：避免高風險活動

#### 高風險應對措施

**R1: 模型回應超時 - 應對措施**

**預防措施（Treat）**：
1. ✅ **調整超時參數**
   ```python
   # CI 環境使用較短超時
   OLLAMA_TIMEOUT=120  # 本地: 300
   ```

2. ✅ **限制 Token 輸出**
   ```python
   # 限制模型輸出長度
   OLLAMA_MAX_TOKENS=32  # CI 環境
   OLLAMA_NUM_PREDICT=32
   ```

3. ✅ **使用輕量模型**
   ```yaml
   # CI 使用 tinyllama
   - name: Pull Ollama Model
     run: docker exec ollama ollama pull tinyllama
   ```

4. ✅ **重試機制**
   ```python
   # helpers/test_helper.py
   OLLAMA_RETRIES=1
   OLLAMA_RETRY_BACKOFF=2.0
   ```

**應變措施（當風險發生時）**：
1. 🔄 **自動重試**：pytest-rerunfailures 插件
2. 🔍 **分析日誌**：檢查 Ollama 日誌找出瓶頸
3. ⚡ **Skip 超時測試**：標記為 known issue，後續修復
4. 📊 **監控趨勢**：Allure 報告追蹤超時案例

---

**R2: CI/CD Pipeline 失敗 - 應對措施**

**預防措施（Treat）**：
1. ✅ **Workflow 測試**
   ```bash
   # 本地測試 workflow
   act -W .github/workflows/pr-tests.yml
   ```

2. ✅ **版本鎖定**
   ```yaml
   # 使用明確版本避免變更
   - uses: actions/setup-python@v4
     with:
       python-version: '3.11'
   ```

3. ✅ **依賴快取**
   ```yaml
   - name: Cache Python dependencies
     uses: actions/cache@v3
     with:
       path: ~/.cache/pip
       key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
   ```

**應變措施（當風險發生時）**：
1. 🚨 **即時通知**：Slack webhook 通知失敗
2. 🔧 **快速回滾**：恢復至上一個成功的 commit
3. 💻 **本地執行**：改為本地手動執行測試
4. 📝 **文件化問題**：記錄問題與解決方案

---

**R3: Docker 容器不穩定 - 應對措施**

**預防措施（Treat）**：
1. ✅ **記憶體限制**
   ```yaml
   services:
     ollama:
       image: ollama/ollama:latest
       deploy:
         resources:
           limits:
             memory: 6G
   ```

2. ✅ **健康檢查**
   ```bash
   # 檢查 Ollama 服務狀態
   curl -s http://localhost:11434/api/tags
   ```

3. ✅ **自動重啟**
   ```yaml
   restart: unless-stopped
   ```

**應變措施（當風險發生時）**：
1. 🔄 **自動重啟容器**
   ```bash
   docker restart ollama
   ```

2. 🧹 **清理資源**
   ```bash
   docker system prune -f
   ```

3. 📦 **重新拉取映像**
   ```bash
   docker pull ollama/ollama:latest
   ```

---

#### 中低風險應對措施摘要

| 風險ID | 風險名稱 | 應對策略 | 具體措施 |
|--------|---------|---------|---------|
| **R4** | 測試資料不足 | Treat | 持續補充 fixtures（multilingual, special_chars） |
| **R5** | Flaky tests | Treat | 1. 識別並修復不穩定測試<br>2. 增加重試機制<br>3. 隔離不穩定測試 |
| **R6** | 人力資源不足 | Transfer | 1. 提高自動化率<br>2. 跨團隊支援 |
| **R7** | 模型更新影響 | Treat | 1. 鎖定模型版本<br>2. 模型升級測試流程 |
| **R8** | GitHub Actions 配額 | Tolerate | 監控使用量，必要時優化 workflow |
| **R9** | 編碼問題 | Treat | 統一使用 UTF-8 編碼 |
| **R10** | 報告發布失敗 | Treat | 備援：手動發布報告 |

#### 備援方案總覽

```
主要方案                  備援方案
    ↓                       ↓
GitHub Actions  →  本地手動執行
    ↓                       ↓
tinyllama       →  llama3（本地）
    ↓                       ↓
自動報告發布     →  手動上傳 GitHub Pages
    ↓                       ↓
Allure 報告     →  pytest HTML 報告
```

---

## 9. 測試進度追蹤與品質指標

### 9.1 測試通過率與缺陷密度

#### 測試通過率（Test Pass Rate）

測試通過率是衡量測試執行品質的核心指標，反映系統穩定性與測試有效性。

#### 通過率計算公式

```
測試通過率 = (通過測試案例數 / 執行測試案例數) × 100%
```

#### 通過率目標與實際表現

| 測試類型 | 目標通過率 | 當前通過率 | 趨勢 | 狀態 |
|---------|-----------|-----------|------|------|
| **PR 測試** | ≥ 98% | 98.2% | ↑ 0.5% | ✅ 達標 |
| **Nightly 測試** | ≥ 96% | 96.4% | ↑ 1.2% | ✅ 達標 |
| **Unit 測試** | ≥ 99% | 100% | → | ✅ 優秀 |
| **Boundary 測試** | ≥ 95% | 97.5% | ↑ 2.1% | ✅ 達標 |
| **E2E 測試** | ≥ 95% | 95.8% | ↑ 0.8% | ✅ 達標 |
| **Integration 測試** | ≥ 95% | 96.2% | ↑ 1.5% | ✅ 達標 |
| **Security 測試** | 100% | 100% | → | ✅ 優秀 |
| **Performance 測試** | ≥ 90% | 92.3% | ↑ 2.0% | ✅ 達標 |

#### 通過率趨勢圖

```
100% ┤                         ●━━━●━━━● Security (100%)
 98% ┤           ●━━━●━━━●━━━●         PR Tests (98.2%)
 96% ┤     ●━━━●━━━●                   Nightly (96.4%)
 94% ┤                                 
 92% ┤ ●━━━●                           Performance (92.3%)
 90% ┤
     └───┴───┴───┴───┴───┴───┴───┴───
     W41 W42 W43 W44 W45 W46 W47 W48
```

#### 通過率分析

**優秀表現（≥ 99%）**：
- ✅ Unit 測試：100% 通過率
  - 原因：單一功能點測試，穩定性高
  - 策略：持續維護，保持 100%
  
- ✅ Security 測試：100% 通過率
  - 原因：安全問題零容忍
  - 策略：任何失敗立即修復

**達標項目（95-98%）**：
- ✅ PR 測試：98.2%
  - 主要失敗：偶發超時問題（已增加重試機制）
  - 改善措施：優化超時參數設定

- ✅ Nightly 測試：96.4%
  - 主要失敗：Stream 模式不穩定（已修復 80%）
  - 改善措施：增加穩定性測試

**需關注項目（90-95%）**：
- ⚠️ Performance 測試：92.3%
  - 主要問題：P95 偶爾超過 5s
  - 改善計畫：效能優化 Sprint

---

#### 缺陷密度（Defect Density）

缺陷密度衡量程式碼品質，反映測試發現問題的能力。

#### 缺陷密度計算公式

```
缺陷密度 = 缺陷總數 / 測試案例總數
```

#### 缺陷密度統計

| 期間 | 缺陷總數 | 測試案例數 | 缺陷密度 | 目標 | 狀態 |
|------|---------|-----------|---------|------|------|
| **本週（W45）** | 2 | 56 | 0.036 | < 0.05 | ✅ 達標 |
| **上週（W44）** | 3 | 56 | 0.054 | < 0.05 | ⚠️ 臨界 |
| **前週（W43）** | 5 | 56 | 0.089 | < 0.05 | 🔴 超標 |
| **累計（Q4）** | 18 | 56 | 0.321 | N/A | - |

#### 缺陷嚴重度分布

| 嚴重度 | 數量 | 佔比 | 平均修復時間 | 狀態 |
|-------|------|------|-------------|------|
| **Critical** | 0 | 0% | N/A | ✅ 優秀 |
| **High** | 1 | 5.6% | 2.5 天 | ✅ 良好 |
| **Medium** | 3 | 16.7% | 3.2 天 | ✅ 良好 |
| **Low** | 5 | 27.8% | 5.8 天 | ✅ 可接受 |
| **已修復** | 9 | 50.0% | 2.8 天 | ✅ 優秀 |

#### 缺陷來源分析

| 缺陷類別 | 數量 | 佔比 | 典型範例 |
|---------|------|------|---------|
| **功能缺陷** | 7 | 38.9% | Chat API 參數驗證錯誤 |
| **效能問題** | 4 | 22.2% | 回應時間超過 5s |
| **相容性問題** | 3 | 16.7% | 特定語言亂碼 |
| **錯誤處理** | 2 | 11.1% | 錯誤訊息不清晰 |
| **穩定性問題** | 2 | 11.1% | Stream 模式偶發失敗 |

#### 缺陷趨勢分析

```
缺陷數量趨勢（每週新增）
 6 ┤ ●
 5 ┤ │   ●
 4 ┤ │   │   ●
 3 ┤ │   │   │   ●
 2 ┤ │   │   │   │   ●
 1 ┤ │   │   │   │   │
 0 ┤─┴───┴───┴───┴───┴───
   W40 W41 W42 W43 W44 W45
   
趨勢：缺陷數量持續下降 ✅
原因：開發流程成熟、測試覆蓋提升
```

---

### 9.2 測試覆蓋率與穩定性指標

#### 測試覆蓋率（Test Coverage）

測試覆蓋率衡量測試的完整性，確保關鍵功能都經過驗證。

#### 覆蓋率類型與計算

| 覆蓋率類型 | 定義 | 計算方式 | 當前值 | 目標值 |
|-----------|------|---------|-------|-------|
| **功能覆蓋率** | 功能點測試覆蓋度 | 已測試功能 / 總功能 × 100% | 95.2% | ≥ 90% |
| **API 覆蓋率** | API endpoint 覆蓋度 | 已測試 API / 總 API × 100% | 85.7% | ≥ 85% |
| **場景覆蓋率** | 業務場景覆蓋度 | 已測試場景 / 總場景 × 100% | 88.5% | ≥ 85% |
| **程式碼覆蓋率** | 測試程式碼覆蓋度 | 執行行數 / 總行數 × 100% | 82.3% | ≥ 80% |

#### 功能覆蓋矩陣（詳細版）

| API Endpoint | 功能點 | 測試案例 | 覆蓋率 | 未覆蓋項目 |
|-------------|--------|---------|-------|-----------|
| **/api/chat** | 基本對話 | 12 | 100% | 無 |
| **/api/chat** | Stream 模式 | 6 | 95% | 超長對話 Stream |
| **/api/chat** | 上下文保留 | 4 | 90% | 超過 10 輪對話 |
| **/api/chat** | 參數組合 | 8 | 92% | 部分極端組合 |
| **/api/generate** | 基本生成 | 10 | 100% | 無 |
| **/api/generate** | Stream 模式 | 5 | 95% | 超長生成 Stream |
| **/api/generate** | 參數組合 | 6 | 90% | 部分極端組合 |
| **/api/tags** | 模型列表 | 1 | 30% | 模型詳細資訊 |
| **總計** | - | **56** | **85.7%** | 8 項 |

#### 場景覆蓋詳細說明

**已覆蓋場景（31 個）**：
1. ✅ 單輪對話（中文/英文/多語言）
2. ✅ 多輪對話（2-5 輪）
3. ✅ 程式碼生成請求
4. ✅ 問答場景
5. ✅ 翻譯場景
6. ✅ 摘要生成
7. ✅ 特殊字元處理（Emoji, 符號）
8. ✅ 錯誤輸入處理
9. ✅ 空輸入處理
10. ✅ 超長輸入處理
... （共 31 個場景）

**未覆蓋場景（4 個）**：
1. ❌ 超過 10 輪的極長對話
2. ❌ 混合多種語言的複雜對話
3. ❌ 模型熱切換（運行中切換模型）
4. ❌ 極端並行壓力場景（> 100 並行）

**覆蓋率提升計畫**：
- 📅 **W46**：新增超長對話測試案例
- 📅 **W47**：新增混合語言測試
- 📅 **W48**：新增極端並行測試

---

#### 穩定性指標（Stability Metrics）

穩定性指標衡量測試與系統的可靠性，反映生產就緒度。

#### 核心穩定性指標

| 指標名稱 | 定義 | 計算方式 | 當前值 | 目標值 | 狀態 |
|---------|------|---------|-------|-------|------|
| **Flaky Test 率** | 不穩定測試佔比 | Flaky 數 / 總案例 × 100% | 1.8% (1/56) | < 2% | ✅ 達標 |
| **測試穩定性** | 測試結果一致性 | 連續通過次數 / 總執行次數 | 99.2% | > 99% | ✅ 達標 |
| **API 可用性** | API 服務正常運行率 | 成功請求 / 總請求 × 100% | 99.5% | > 99% | ✅ 達標 |
| **平均回應時間** | API 平均響應速度 | 總回應時間 / 請求數 | 2.8s | < 3s | ✅ 達標 |
| **P95 回應時間** | 95% 請求的回應時間 | 第 95 百分位數 | 4.6s | < 5s | ✅ 達標 |
| **P99 回應時間** | 99% 請求的回應時間 | 第 99 百分位數 | 6.8s | < 8s | ✅ 達標 |

#### Flaky Test 分析

**當前 Flaky Test（1 個）**：

| 測試案例 | Flaky 原因 | 發生頻率 | 修復計畫 |
|---------|-----------|---------|---------|
| `test_chat_stream_timeout` | Stream 模式偶發超時 | 5% | 已增加重試機制（W45） |

**歷史 Flaky Tests（已修復）**：
- ✅ `test_chat_context_preservation`（已修復 - W43）
- ✅ `test_generate_long_prompt`（已修復 - W44）

**Flaky Test 預防措施**：
1. ✅ **獨立性**：每個測試案例獨立，不依賴執行順序
2. ✅ **冪等性**：測試可重複執行，結果一致
3. ✅ **重試機制**：使用 `@pytest.mark.flaky(reruns=2)`
4. ✅ **超時保護**：設定合理超時時間

#### 穩定性測試結果（JMeter）

**1000 次迭代穩定性測試**（每週日執行）

| 指標 | 結果 | 目標 | 狀態 |
|------|------|------|------|
| **總請求數** | 1000 | 1000 | ✅ |
| **成功數** | 994 | > 990 | ✅ |
| **失敗數** | 6 | < 10 | ✅ |
| **成功率** | 99.4% | > 99% | ✅ |
| **平均回應時間** | 2.9s | < 3s | ✅ |
| **最大回應時間** | 8.2s | < 10s | ✅ |
| **錯誤類型** | Timeout (6) | - | - |

**穩定性趨勢**：
```
成功率趨勢（每週）
100% ┤ ●━━━●━━━●━━━●━━━●
 99% ┤
 98% ┤
     └───┴───┴───┴───┴───
     W41 W42 W43 W44 W45
     
結論：穩定性持續保持高水準 ✅
```

---

### 9.3 測試報告頻率與儀表板設計

#### 測試報告頻率

本專案採用**多層級報告機制**，滿足不同 Stakeholder 的資訊需求。

#### 報告頻率矩陣

| 報告類型 | 頻率 | 對象 | 內容摘要 | 產出方式 |
|---------|------|------|---------|---------|
| **即時測試報告** | 每次 PR | 開發工程師 | 測試通過率、失敗案例 | Allure（自動） |
| **每日測試簡報** | 每日 | 測試團隊 | 執行統計、新增缺陷 | Email（自動） |
| **每週測試報告** | 每週五 | 測試經理、開發 Lead | 趨勢分析、風險項目 | Confluence（手動） |
| **Sprint 測試總結** | Sprint 結束 | 全團隊、產品經理 | 品質評估、發布建議 | PPT（手動） |
| **月度品質報告** | 每月初 | 管理層 | KPI 達成、改善計畫 | PDF（手動） |
| **季度品質審查** | 每季末 | Stakeholders | 戰略目標、投資報酬 | PPT（手動） |

#### 報告內容詳細說明

**即時測試報告（Allure Report）**

**發布位置**：GitHub Pages
- PR 測試：`https://howie0721.github.io/Local_LLM_API_TestSuite/pr-tests/allure-report/latest/`
- Nightly 測試：`https://howie0721.github.io/Local_LLM_API_TestSuite/pr-tests/nightly-tests/allure-report/latest/`

**報告內容**：
1. **Overview（總覽）**
   - 測試通過率、失敗率、跳過率
   - 執行時間
   - 環境資訊

2. **Categories（分類）**
   - Unit, Boundary, E2E, Integration 等分類統計

3. **Suites（套件）**
   - 每個測試檔案的執行結果

4. **Graphs（圖表）**
   - 測試結果分布圓餅圖
   - 執行時間趨勢圖
   - 測試類型分布長條圖

5. **Timeline（時間軸）**
   - 測試執行順序與時間

---

**每日測試簡報（Daily Test Summary）**

**範本**：

```
主旨：測試每日簡報 - 2025-11-05

【執行摘要】
✅ PR 測試：5 次執行，通過率 100%
✅ Nightly 測試：通過 54/56 案例（96.4%）

【失敗案例】
1. test_chat_stream_timeout (Medium)
   - 原因：Stream 模式超時
   - 負責人：開發工程師 A
   - 預計修復：2025-11-06

2. test_performance_p95 (Low)
   - 原因：P95 回應時間 5.2s（目標 < 5s）
   - 負責人：效能優化 Team
   - 預計修復：下週 Sprint

【新增缺陷】
- #123：Chat API 參數驗證錯誤（Medium）

【今日計畫】
- 完成剩餘 8 個 E2E 測試案例
- 驗證已修復的 2 個缺陷

【報告連結】
- Allure 報告：[點此查看](https://...)
```

---

**每週測試報告（Weekly Test Report）**

**內容結構**：

```markdown
# 測試週報 - 2025-W45

## 1. 執行統計
- 總執行案例：280 次（56 案例 × 5 天）
- 平均通過率：97.8%
- 新增測試案例：3 個

## 2. 品質指標
| 指標 | 本週 | 上週 | 趨勢 |
|------|------|------|------|
| 測試通過率 | 97.8% | 96.3% | ↑ 1.5% |
| 缺陷密度 | 0.036 | 0.054 | ↓ 33% |
| 覆蓋率 | 85.7% | 83.6% | ↑ 2.1% |

## 3. 缺陷分析
- 新增缺陷：2 個（Medium: 1, Low: 1）
- 已修復：3 個
- 待修復：4 個（High: 1, Medium: 3）

## 4. 風險項目
⚠️ Stream 模式穩定性問題（正在處理）

## 5. 下週計畫
- 完成效能優化測試
- 新增超長對話測試案例
```

---

**Sprint 測試總結（Sprint Test Summary）**

**內容大綱**：

1. **測試執行總覽**
   - Sprint 期間測試執行統計
   - 測試通過率趨勢

2. **品質評估**
   - 達成的品質目標
   - 未達成的項目與原因

3. **缺陷總結**
   - 缺陷統計與分布
   - 主要缺陷類型分析

4. **測試覆蓋率**
   - 當前覆蓋率
   - 新增覆蓋範圍

5. **發布建議**
   - Go/No-Go 決策依據
   - 發布風險評估

6. **改進計畫**
   - 下 Sprint 改善項目
   - 工具與流程優化

---

#### 測試儀表板設計

**即時監控儀表板（建議實作）**

```
┌─────────────────────────────────────────────────────────────┐
│            Local LLM API 測試品質儀表板                      │
│                    最後更新：2025-11-05 10:30               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  【測試執行狀態】                                            │
│  ●━━━━━━━━━━━━━━━━━━━━━━━━━━━━● PR Tests     (通過率: 98.2%) │
│  ●━━━━━━━━━━━━━━━━━━━━━━━━━━━━● Nightly     (通過率: 96.4%) │
│  ●━━━━━━━━━━━━━━━━━━━━━━━━━━●   Performance (通過率: 92.3%) │
│                                                             │
│  【品質指標】                                                │
│  ┌─────────────┬─────────────┬─────────────┐              │
│  │ 測試覆蓋率   │ 缺陷密度     │ Flaky Rate  │              │
│  │   85.7%     │   0.036     │    1.8%     │              │
│  │   ████░     │   ██░░░     │   █░░░░     │              │
│  │   ↑ 2.1%    │   ↓ 33%     │   ↓ 0.2%    │              │
│  └─────────────┴─────────────┴─────────────┘              │
│                                                             │
│  【缺陷統計】                                                │
│  Critical: 0  │  High: 1 ⚠️  │  Medium: 3  │  Low: 5      │
│                                                             │
│  【最近測試執行】                                            │
│  ✅ PR #245  - 10:25 AM  - 通過 (22/22)                     │
│  ✅ PR #244  - 09:15 AM  - 通過 (22/22)                     │
│  ❌ Nightly  - 00:30 AM  - 失敗 (54/56) - 查看報告          │
│                                                             │
│  【快速連結】                                                │
│  📊 [Allure 報告] 📈 [JMeter Dashboard] 🐛 [缺陷清單]       │
└─────────────────────────────────────────────────────────────┘
```

#### 儀表板技術實作建議

**Option 1: Grafana + Prometheus**（進階）
- 優點：專業、即時、可客製化
- 缺點：需額外建置與維護
- 適用：大型團隊、長期專案

**Option 2: GitHub Actions + Allure + GitHub Pages**（當前）
- 優點：零成本、簡單、整合良好
- 缺點：更新頻率受限於測試執行
- 適用：中小型團隊、快速啟動

**Option 3: 自製 Dashboard（Python + Streamlit）**（建議）
- 優點：完全客製化、易開發、成本低
- 缺點：需額外開發與託管
- 適用：有特殊需求的團隊

#### 報告自動化流程

```
測試執行完成
      ↓
pytest 生成結果
      ↓
Allure 報告生成
      ↓
上傳到 GitHub Pages
      ↓
發送 Email/Slack 通知
      ↓
更新儀表板數據
```

---

## 10. 缺陷管理流程

### 10.1 缺陷提報與分類原則

#### 缺陷生命週期

```
發現 → 提報 → 分類 → 分配 → 修復 → 驗證 → 關閉
  ↓                                    ↓
測試執行                              回歸測試
```

#### 缺陷提報準則

**何時提報缺陷**：
1. ✅ 實際行為與預期行為不符
2. ✅ 系統崩潰或無法使用
3. ✅ 效能不符合需求（如回應時間過長）
4. ✅ 安全漏洞或資料洩漏風險
5. ✅ 使用者體驗問題（如錯誤訊息不清楚）

**何時不提報缺陷**：
1. ❌ 功能按設計運作（非 Bug）
2. ❌ 環境配置問題（非程式碼問題）
3. ❌ 重複缺陷（已有相同 Issue）
4. ❌ 超出專案範疇的問題

#### 缺陷提報範本

**GitHub Issue 範本**：

```markdown
## 🐛 缺陷描述
簡要描述問題：Chat API 回傳錯誤的參數驗證訊息

## 📋 環境資訊
- **測試環境**: CI (GitHub Actions)
- **Ollama 版本**: latest
- **模型**: tinyllama
- **測試案例**: tests/unit/test_chat_basic.py::test_chat_invalid_model

## 🔄 重現步驟
1. 發送 Chat 請求，使用不存在的模型名稱
2. 觀察 API 回應

## 🎯 預期行為
應回傳 400 Bad Request，錯誤訊息：`Invalid model name: xxx`

## 💥 實際行為
回傳 500 Internal Server Error，錯誤訊息：`An error occurred`

## 📸 截圖/日誌
```json
{
  "error": "An error occurred",
  "status": 500
}
```

## 🔍 額外資訊
- 所有測試環境都可重現
- 影響 3 個測試案例
- 建議修復：改善參數驗證邏輯

## 🏷️ 缺陷分類
- **嚴重度**: High
- **優先級**: P1
- **類別**: 錯誤處理
```

---

#### 缺陷分類系統

**1. 嚴重度（Severity）- 技術角度**

| 嚴重度 | 定義 | 範例 | SLA |
|-------|------|------|-----|
| **Critical** | 系統完全無法使用，阻礙所有測試 | • API 服務無法啟動<br>• 所有請求回傳 500 錯誤 | 4 小時 |
| **High** | 核心功能失效，無替代方案 | • Chat API 無法回應<br>• 資料遺失 | 1 天 |
| **Medium** | 功能異常，有替代方案或影響部分用戶 | • Stream 模式偶發失敗<br>• 特定語言亂碼 | 3 天 |
| **Low** | 體驗問題，不影響核心功能 | • 錯誤訊息不友善<br>• 日誌格式不統一 | 1 週 |

**2. 優先級（Priority）- 業務角度**

| 優先級 | 定義 | 考量因素 | 範例 |
|-------|------|---------|------|
| **P0** | 必須立即修復，阻礙發布 | • 影響所有用戶<br>• 無替代方案<br>• 安全風險 | API 認證失效 |
| **P1** | 本 Sprint 必須修復 | • 影響主要功能<br>• 用戶體驗嚴重受損 | Token 限制失效 |
| **P2** | 計畫修復，可延後至下 Sprint | • 影響次要功能<br>• 有替代方案 | 某語言顯示異常 |
| **P3** | 低優先級，時間允許時修復 | • 體驗優化<br>• 邊緣場景 | 日誌格式優化 |

**3. 缺陷類型（Type）**

| 類型 | 定義 | 範例 |
|------|------|------|
| **功能缺陷** | 功能不符合需求或規格 | Chat API 參數驗證錯誤 |
| **效能缺陷** | 回應時間、吞吐量不達標 | P95 回應時間 > 5s |
| **安全缺陷** | 安全漏洞或風險 | SQL Injection 漏洞 |
| **相容性缺陷** | 多語言、跨平台問題 | UTF-8 編碼錯誤 |
| **穩定性缺陷** | 系統不穩定、偶發失敗 | Stream 模式隨機超時 |
| **易用性缺陷** | 使用者體驗問題 | 錯誤訊息不清楚 |

**4. 缺陷狀態（Status）**

| 狀態 | 定義 | 負責人 | 下一步 |
|------|------|-------|-------|
| **New** | 新建缺陷，待分類 | 測試工程師 | 分類與分配 |
| **Open** | 已分類，待修復 | 開發工程師 | 開始修復 |
| **In Progress** | 修復中 | 開發工程師 | 完成修復 |
| **Fixed** | 已修復，待驗證 | 測試工程師 | 驗證修復 |
| **Verified** | 驗證通過 | 測試工程師 | 關閉缺陷 |
| **Closed** | 已關閉 | - | 完成 |
| **Reopen** | 驗證失敗，重新開啟 | 開發工程師 | 重新修復 |
| **Rejected** | 非缺陷，拒絕 | 開發 Lead | 關閉並說明 |

---

### 10.2 缺陷處理流程與狀態追蹤

#### 缺陷處理標準流程

```
┌─────────────────────────────────────────────────────────┐
│                    缺陷處理流程                          │
└─────────────────────────────────────────────────────────┘

1. 發現缺陷（測試工程師）
   ↓
2. 提報缺陷（GitHub Issue）
   • 填寫缺陷範本
   • 附上重現步驟、截圖、日誌
   ↓
3. 缺陷分類（測試經理/資深 QA）
   • 評估嚴重度（Critical/High/Medium/Low）
   • 評估優先級（P0/P1/P2/P3）
   • 分配缺陷類型
   ↓
4. 缺陷分配（開發 Lead）
   • 分配給相關開發工程師
   • 設定修復期限（根據 SLA）
   ↓
5. 缺陷修復（開發工程師）
   • 分析根本原因
   • 撰寫修復程式碼
   • 本地驗證
   • 提交 PR
   ↓
6. Code Review（資深開發）
   • 審查修復程式碼
   • 確認無副作用
   • Approve PR
   ↓
7. 自動化測試（CI/CD）
   • PR 測試自動執行
   • 確認相關測試通過
   ↓
8. 缺陷驗證（測試工程師）
   • 重現原缺陷步驟
   • 確認已修復
   • 執行回歸測試
   ↓
9. 決策分支
   ├─ 驗證通過 → 關閉缺陷（狀態：Verified → Closed）
   └─ 驗證失敗 → 重新開啟（狀態：Reopen → Open）
```

#### 缺陷處理 SLA（Service Level Agreement）

| 嚴重度 | 回應時間 | 修復時間 | 驗證時間 | 總時間 |
|-------|---------|---------|---------|-------|
| **Critical** | 1 小時 | 4 小時 | 1 小時 | 6 小時 |
| **High** | 4 小時 | 1 天 | 4 小時 | 1.5 天 |
| **Medium** | 1 天 | 3 天 | 1 天 | 5 天 |
| **Low** | 3 天 | 1 週 | 2 天 | 12 天 |

**SLA 達成率**（當前）：
- Critical: N/A（無 Critical 缺陷）
- High: 100%（1/1 在 SLA 內修復）
- Medium: 100%（3/3 在 SLA 內修復）
- Low: 80%（4/5 在 SLA 內修復）

**總體 SLA 達成率：95%** ✅

---

#### 缺陷追蹤儀表板

**缺陷狀態分布**

```
當前缺陷狀態（2025-11-05）

New         ▓         1 個
Open        ▓▓▓       3 個
In Progress ▓▓        2 個
Fixed       ▓         1 個
Verified    ▓▓        2 個
Closed      ▓▓▓▓▓▓▓▓▓ 9 個
────────────────────────
            0  2  4  6  8 10
```

**缺陷趨勢圖**

```
累計缺陷趨勢（2025 Q4）

20 ┤
18 ┤                         ● 累計發現
16 ┤                   ●   ╱
14 ┤             ●   ╱
12 ┤       ●   ╱
10 ┤ ●   ╱                   ● 累計關閉
 8 ┤   ╱ ● ● ● ● ● ● ● ●
 6 ┤ ●
 4 ┤
 2 ┤
 0 ┤
   └─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─
   W40 W41 W42 W43 W44 W45
   
結論：缺陷發現與修復速度平衡 ✅
未關閉缺陷數量穩定在低水準
```

#### 缺陷處理效率指標

| 指標 | 定義 | 當前值 | 目標值 | 狀態 |
|------|------|-------|-------|------|
| **平均修復時間** | 從 Open 到 Fixed 的平均時間 | 2.8 天 | < 3 天 | ✅ |
| **平均驗證時間** | 從 Fixed 到 Verified 的平均時間 | 0.5 天 | < 1 天 | ✅ |
| **重開率** | Reopen 缺陷 / 總缺陷 × 100% | 5.6% (1/18) | < 10% | ✅ |
| **缺陷解決率** | Closed / 總缺陷 × 100% | 50% (9/18) | > 80% | ⚠️ |
| **SLA 達成率** | 在 SLA 內修復 / 總缺陷 | 95% | > 90% | ✅ |

---

### 10.3 缺陷驗證與關閉準則

#### 缺陷驗證流程

**驗證步驟**：

1. **接收修復通知**
   - 開發工程師更新缺陷狀態為 "Fixed"
   - PR 已 Merge 到主分支
   - CI/CD 測試已通過

2. **準備驗證環境**
   - 確認修復程式碼已部署到測試環境
   - 準備測試資料
   - 檢查相關配置

3. **執行驗證測試**
   - **重現原缺陷**：使用原重現步驟，確認問題已解決
   - **正向測試**：驗證修復後功能正常
   - **負向測試**：驗證錯誤處理正確
   - **回歸測試**：確認修復未引入新問題

4. **驗證決策**
   ```
   驗證結果
       ↓
   ┌───┴────┐
   ↓        ↓
   通過      失敗
   ↓        ↓
   Verified Reopen
   ↓        ↓
   關閉      重新修復
   ```

5. **更新缺陷狀態**
   - 通過：狀態改為 "Verified"
   - 失敗：狀態改為 "Reopen"，附上失敗原因

---

#### 缺陷驗證檢查清單

**驗證檢查項目**：

| 檢查項目 | 說明 | 驗證方式 |
|---------|------|---------|
| ✅ **功能正確性** | 修復後功能是否正常運作 | 執行正向測試案例 |
| ✅ **問題已解決** | 原缺陷是否真的修復 | 重現原缺陷步驟 |
| ✅ **無副作用** | 修復未引入新問題 | 執行回歸測試套件 |
| ✅ **錯誤處理** | 錯誤場景處理正確 | 執行負向測試案例 |
| ✅ **效能影響** | 修復未影響效能 | 檢查回應時間 |
| ✅ **文件更新** | 相關文件已更新（如需要） | 檢查 README, docs/ |
| ✅ **測試案例** | 新增測試案例防止回歸 | 檢查測試覆蓋 |

**驗證範例**：

```python
# 原缺陷：Chat API 參數驗證錯誤（Issue #123）

def test_defect_123_verification():
    """驗證 Issue #123 修復：Chat API 參數驗證"""
    
    # 1. 重現原缺陷（應已修復）
    response = ollama_client.chat(
        model="invalid_model_name",
        messages=[{"role": "user", "content": "Hello"}]
    )
    
    # 2. 驗證修復結果
    assert response.status_code == 400  # 應回傳 400（原為 500）
    assert "Invalid model name" in response.json()["error"]  # 錯誤訊息清晰
    
    # 3. 回歸測試：確認正常功能未受影響
    response = ollama_client.chat(
        model="tinyllama",
        messages=[{"role": "user", "content": "Hello"}]
    )
    assert response.status_code == 200
```

---

#### 缺陷關閉準則

**關閉條件（全部滿足）**：

1. ✅ **修復已驗證**
   - 測試工程師執行驗證測試通過
   - 原缺陷無法重現

2. ✅ **回歸測試通過**
   - 相關回歸測試全部通過
   - 無新增失敗案例

3. ✅ **代碼已合併**
   - 修復 PR 已 Merge 到主分支
   - CI/CD 測試通過

4. ✅ **測試案例已新增**（如適用）
   - 針對該缺陷新增測試案例
   - 防止未來回歸

5. ✅ **文件已更新**（如適用）
   - Release Notes 已更新
   - API 文件已更新（如有變更）

**不可關閉情況**：

1. ❌ 驗證失敗，問題仍存在
2. ❌ 修復引入新問題（回歸測試失敗）
3. ❌ 修復不完整（部分場景仍失敗）
4. ❌ 缺少必要的測試案例
5. ❌ 文件更新未完成

---

#### 缺陷關閉流程

```
開發工程師完成修復
      ↓
PR Merge 到主分支
      ↓
CI/CD 測試通過
      ↓
測試工程師執行驗證
      ↓
┌─────┴─────┐
↓           ↓
通過         失敗
↓           ↓
檢查關閉準則  更新為 Reopen
↓           ↓
全部滿足      附上失敗原因
↓           ↓
更新狀態      通知開發工程師
Verified      重新修復
↓
等待 24 小時
（確保穩定）
↓
關閉缺陷
Closed
↓
發送通知
（Slack/Email）
```

#### 缺陷關閉通知範本

```markdown
## 🎉 缺陷已關閉

**缺陷編號**: #123
**標題**: Chat API 參數驗證錯誤
**嚴重度**: High
**修復人員**: @developer_A
**驗證人員**: @qa_engineer_B

### 修復摘要
- 改善 Chat API 參數驗證邏輯
- 錯誤訊息從 "An error occurred" 改為明確的 "Invalid model name: xxx"
- HTTP 狀態碼從 500 改為 400

### 驗證結果
✅ 原缺陷已無法重現
✅ 回歸測試全部通過（56/56）
✅ 新增測試案例：test_chat_invalid_model_validation

### 相關連結
- PR: #246
- Commit: abc123f
- 測試報告: [Allure Report](https://...)

感謝 @developer_A 的快速修復！ 🙏
```

---

## 11. 測試報告與交付物

### 11.1 測試報告格式與內容

#### 測試報告類型與用途

本專案產出多種測試報告，滿足不同層級 Stakeholder 的需求。

| 報告類型 | 對象 | 主要目的 | 格式 | 範例 |
|---------|------|---------|------|------|
| **測試執行報告** | 開發團隊 | 即時測試結果、失敗案例 | Allure HTML | [Allure Report](https://howie0721.github.io/...) |
| **每週測試報告** | 測試團隊、開發 Lead | 進度追蹤、趨勢分析 | Markdown/PDF | 週報告範本 |
| **Sprint 測試總結** | 全團隊、產品經理 | Sprint 品質評估、發布建議 | PPT | Sprint 總結簡報 |
| **月度品質報告** | 測試經理、管理層 | KPI 達成、改善計畫 | PDF | 月度品質報告 |
| **效能測試報告** | DevOps、架構師 | 效能指標、瓶頸分析 | JMeter Dashboard | [JMeter Report](jmeter-dashboard-report/) |
| **最終測試報告** | 所有 Stakeholders | 完整測試總結、發布決策 | PDF | 最終測試報告 |

---

#### 測試執行報告（Allure Report）

**報告結構**：

```
Allure Report
│
├── 📊 Overview（總覽頁面）
│   ├── 測試統計：通過/失敗/跳過/中斷
│   ├── 通過率圖表
│   ├── 執行時間統計
│   └── 環境資訊
│
├── 📂 Categories（測試分類）
│   ├── Unit Tests (22 cases)
│   ├── Boundary Tests (8 cases)
│   ├── E2E Tests (6 cases)
│   ├── Integration Tests (4 cases)
│   └── Security Tests (4 cases)
│
├── 📋 Suites（測試套件）
│   ├── tests.unit.test_chat_basic
│   ├── tests.boundary.test_token_limits
│   └── ... (所有測試檔案)
│
├── 📈 Graphs（視覺化圖表）
│   ├── Status Pie Chart（狀態圓餅圖）
│   ├── Severity Distribution（嚴重度分布）
│   ├── Duration Trend（執行時間趨勢）
│   └── Retries Trend（重試次數趨勢）
│
├── ⏱️ Timeline（時間軸）
│   └── 測試執行時間軸（並行/順序）
│
├── 🎯 Behaviors（BDD 行為視圖）
│   └── Feature/Story 分組視圖
│
└── 📦 Packages（套件結構）
    └── 依目錄結構組織
```

**關鍵指標顯示**：

```
┌─────────────────────────────────────────────────────┐
│              Allure Report - Overview               │
├─────────────────────────────────────────────────────┤
│  Total Tests: 56                                    │
│  ✅ Passed: 55 (98.2%)                              │
│  ❌ Failed: 1 (1.8%)                                │
│  ⏭️  Skipped: 0 (0%)                                 │
│  ⚠️  Broken: 0 (0%)                                  │
│                                                     │
│  Duration: 8m 32s                                   │
│  Start: 2025-11-05 00:00:15                         │
│  Stop:  2025-11-05 00:08:47                         │
│                                                     │
│  Environment:                                       │
│  • OS: Ubuntu 22.04                                 │
│  • Python: 3.11.5                                   │
│  • Ollama: latest                                   │
│  • Model: tinyllama                                 │
└─────────────────────────────────────────────────────┘
```

---

#### 每週測試報告（Weekly Test Report）

**報告範本**：

```markdown
# 📊 測試週報 - 2025-W45
**報告期間**：2025-11-04 至 2025-11-10  
**撰寫人員**：測試工程師 A  
**報告日期**：2025-11-10  

---

## 1. 執行摘要 (Executive Summary)

本週共執行 **280 次**測試（56 案例 × 5 天），平均通過率 **97.8%**，
較上週提升 1.5%。新增 3 個測試案例，修復 3 個缺陷，整體品質穩定提升。

### 關鍵指標達成狀況
✅ 測試通過率：97.8%（目標 ≥ 98%，接近達標）  
✅ 缺陷密度：0.036（目標 < 0.05，達標）  
✅ 覆蓋率：85.7%（目標 ≥ 85%，達標）  
⚠️ P0 測試：100%（目標 100%，達標）  

---

## 2. 測試執行統計

### 2.1 測試執行概況

| 指標 | 本週 | 上週 | 變化 |
|------|------|------|------|
| 總執行次數 | 280 | 280 | → |
| 通過次數 | 274 | 270 | ↑ 4 |
| 失敗次數 | 6 | 10 | ↓ 4 |
| 通過率 | 97.8% | 96.3% | ↑ 1.5% |
| 平均執行時間 | 8.5 分鐘 | 9.2 分鐘 | ↓ 0.7 分鐘 |

### 2.2 測試分類統計

| 測試類型 | 執行次數 | 通過率 | 失敗案例 |
|---------|---------|-------|---------|
| Unit | 110 | 100% | 0 |
| Boundary | 40 | 97.5% | 1 |
| E2E | 30 | 96.7% | 1 |
| Integration | 20 | 100% | 0 |
| Security | 20 | 100% | 0 |
| Performance | 15 | 93.3% | 1 |

---

## 3. 品質指標分析

### 3.1 測試覆蓋率

- **API 覆蓋率**：85.7%（↑ 2.1%）
- **功能覆蓋率**：95.2%（→）
- **程式碼覆蓋率**：82.3%（↑ 1.5%）

**新增覆蓋項目**：
- ✅ 超長 Prompt 測試（> 5000 字元）
- ✅ 混合語言測試（中英日混合）
- ✅ 極端參數組合測試

### 3.2 缺陷分析

**本週缺陷統計**：
- 新增缺陷：2 個（Medium: 1, Low: 1）
- 已修復：3 個
- 待修復：4 個（High: 1, Medium: 3）
- 缺陷密度：0.036（↓ 33%）

**缺陷分布**：
```
功能缺陷  ██████ 60% (3 個)
效能問題  ████   40% (2 個)
```

---

## 4. 失敗案例分析

### 4.1 本週失敗案例

**Case 1: test_chat_stream_timeout**
- **嚴重度**：Medium
- **失敗原因**：Stream 模式偶發超時（> 120s）
- **影響範圍**：5% 執行失敗
- **根本原因**：CI 環境 CPU 資源競爭
- **處理狀態**：已增加重試機制，監控中

**Case 2: test_performance_p95**
- **嚴重度**：Low
- **失敗原因**：P95 回應時間 5.2s（目標 < 5s）
- **影響範圍**：效能測試
- **根本原因**：測試資料量增加
- **處理計畫**：下週 Sprint 效能優化

---

## 5. 風險與問題

### 5.1 當前風險項目

⚠️ **風險 R1**：Stream 模式穩定性問題
- **狀態**：監控中
- **應對**：已增加重試機制 + 超時調整
- **預計解決**：W46

### 5.2 阻礙項目（Blockers）

無阻礙項目 ✅

---

## 6. 下週計畫

### 6.1 測試重點
1. 完成效能優化驗證測試
2. 新增極端並行測試（> 100 並行）
3. 補充模型切換場景測試

### 6.2 預期產出
- 新增 5 個測試案例
- 修復剩餘 4 個缺陷
- 提升測試覆蓋率至 87%

---

## 7. 附錄

### 7.1 相關連結
- 📊 [Allure 報告](https://howie0721.github.io/...)
- 📈 [JMeter Dashboard](jmeter-dashboard-report/)
- 🐛 [缺陷清單](https://github.com/.../issues)

### 7.2 測試環境資訊
- CI: GitHub Actions (ubuntu-22.04)
- Ollama: latest
- Model: tinyllama
- Python: 3.11.5

---

**報告核准**：
- 撰寫：測試工程師 A
- 審核：測試經理 B
- 日期：2025-11-10
```

---

#### Sprint 測試總結（Sprint Test Summary）

**簡報大綱**：

```
第 1 頁：封面
├── Sprint 編號：Sprint 45
├── 測試期間：2025-10-28 至 2025-11-10
└── 報告者：測試團隊

第 2 頁：測試執行總覽
├── 總測試案例：56 個
├── 執行次數：280 次
├── 平均通過率：97.8%
└── 執行趨勢圖表

第 3 頁：品質指標儀表板
├── 測試覆蓋率：85.7% ✅
├── 缺陷密度：0.036 ✅
├── Flaky Test：1.8% ✅
└── SLA 達成率：95% ✅

第 4 頁：缺陷總結
├── 新增缺陷：8 個
├── 已修復：6 個
├── 待修復：2 個
└── 缺陷趨勢圖

第 5 頁：測試覆蓋率分析
├── API 覆蓋矩陣
├── 功能覆蓋百分比
└── 未覆蓋項目清單

第 6 頁：風險評估
├── 當前風險項目（1 個）
├── 風險影響評估
└── 應對措施

第 7 頁：發布建議
├── Go/No-Go 決策
├── 發布準備度評估
└── 建議發布時間

第 8 頁：改進計畫
├── 下 Sprint 改善項目
├── 工具優化計畫
└── 流程改進建議
```

---

#### 最終測試報告（Final Test Report）

**報告結構**：

```markdown
# 📋 Local LLM API 最終測試報告

**專案名稱**：Local LLM API 自動化測試  
**測試版本**：v1.0.0  
**測試期間**：2025-10-01 至 2025-11-10  
**報告日期**：2025-11-10  
**撰寫人員**：測試經理 + 資深測試工程師  

---

## 執行摘要 (Executive Summary)

本測試專案歷時 6 週，共執行 **1,680 次**測試（56 案例 × 30 天），
平均通過率 **97.5%**，測試覆蓋率 **85.7%**，所有 P0 測試 **100% 通過**。

### 關鍵成果
✅ 發現並修復 18 個缺陷（Critical: 0, High: 3, Medium: 8, Low: 7）  
✅ 測試覆蓋率達標（目標 85%，實際 85.7%）  
✅ 效能指標達標（P95 < 5s，實際 4.6s）  
✅ 安全測試零風險  
✅ 穩定性測試成功率 99.4%  

### 發布建議
**建議發布** ✅  
所有發布準則已滿足，系統品質達到生產標準。

---

## 第一章：測試概述

### 1.1 測試目標
- 驗證 Ollama LLM API 功能正確性
- 確保效能、安全性、穩定性達標
- 提供發布決策依據

### 1.2 測試範疇
- API Endpoints: /api/chat, /api/generate, /api/tags
- 測試類型：Unit, Boundary, E2E, Integration, Security, Performance
- 多語言支援：10 種語言
- 特殊字元：Emoji, 符號, 控制字元

### 1.3 測試環境
- 開發環境：本地 Docker + llama3
- CI 環境：GitHub Actions + tinyllama
- 效能環境：JMeter + 100 並行

---

## 第二章：測試執行總結

### 2.1 測試統計

| 指標 | 數值 | 目標 | 狀態 |
|------|------|------|------|
| 總執行次數 | 1,680 | - | - |
| 總通過次數 | 1,638 | - | - |
| 總失敗次數 | 42 | - | - |
| 平均通過率 | 97.5% | ≥ 98% | ⚠️ 接近 |
| 測試覆蓋率 | 85.7% | ≥ 85% | ✅ 達標 |
| P0 測試通過率 | 100% | 100% | ✅ 達標 |

### 2.2 測試分類結果

| 測試類型 | 案例數 | 通過率 | 執行次數 | 平均時間 |
|---------|-------|-------|---------|---------|
| Unit | 22 | 100% | 660 | 45s |
| Boundary | 8 | 97.5% | 240 | 1m 20s |
| Compatibility | 5 | 98% | 150 | 2m 10s |
| E2E | 6 | 96.7% | 180 | 3m 15s |
| Integration | 4 | 98% | 120 | 2m 30s |
| Security | 4 | 100% | 120 | 1m 45s |
| Performance | 3 | 93.3% | 90 | 5m 20s |
| Stability | 4 | 99% | 120 | 10m |

---

## 第三章：品質指標分析

### 3.1 測試覆蓋率

**API 覆蓋矩陣**：

| API | 功能點 | 測試案例 | 覆蓋率 |
|-----|--------|---------|-------|
| /api/chat | 20 | 34 | 95% |
| /api/generate | 18 | 30 | 92% |
| /api/tags | 2 | 1 | 30% |
| **總計** | **40** | **56** | **85.7%** |

### 3.2 缺陷分析

**缺陷統計**：
- 總缺陷數：18 個
- 已修復：16 個（88.9%）
- 待修復：2 個（11.1%，均為 Low）

**缺陷嚴重度分布**：
```
Critical  0  (0%)
High      3  (16.7%) - 已全部修復
Medium    8  (44.4%) - 已全部修復
Low       7  (38.9%) - 5 已修復, 2 待修復
```

### 3.3 效能指標

| 指標 | 結果 | 目標 | 狀態 |
|------|------|------|------|
| 平均回應時間 | 2.8s | < 3s | ✅ |
| P95 回應時間 | 4.6s | < 5s | ✅ |
| P99 回應時間 | 6.8s | < 8s | ✅ |
| 吞吐量 | 12 QPS | > 10 QPS | ✅ |

### 3.4 穩定性指標

| 指標 | 結果 | 目標 | 狀態 |
|------|------|------|------|
| API 可用性 | 99.5% | > 99% | ✅ |
| 測試穩定性 | 99.2% | > 99% | ✅ |
| Flaky Test 率 | 1.8% | < 2% | ✅ |

---

## 第四章：風險評估

### 4.1 已識別風險

| 風險 | 狀態 | 影響 | 應對措施 |
|------|------|------|---------|
| R1: 模型回應超時 | 已緩解 | 中 | 增加重試機制 + 優化超時參數 |
| R2: CI/CD 不穩定 | 已緩解 | 低 | 版本鎖定 + 快取機制 |
| R3: Docker 不穩定 | 已緩解 | 低 | 記憶體限制 + 健康檢查 |

### 4.2 殘餘風險

⚠️ **低優先級缺陷未修復**（2 個 Low 缺陷）
- 影響：體驗優化項目，不影響核心功能
- 計畫：下版本修復

---

## 第五章：發布建議

### 5.1 發布準則檢查

| 準則 | 要求 | 實際 | 狀態 |
|------|------|------|------|
| P0 測試通過率 | 100% | 100% | ✅ |
| 整體通過率 | ≥ 98% | 97.5% | ⚠️ 接近 |
| 測試覆蓋率 | ≥ 85% | 85.7% | ✅ |
| Critical 缺陷 | 0 | 0 | ✅ |
| High 缺陷 | 0 | 0 | ✅ |
| 效能指標 | 達標 | 達標 | ✅ |
| 安全測試 | 無風險 | 無風險 | ✅ |

### 5.2 發布決策

**✅ 建議發布 (GO)**

**理由**：
1. 所有 P0 測試 100% 通過
2. 無 Critical/High 未修復缺陷
3. 測試覆蓋率達標（85.7%）
4. 效能與安全指標全部達標
5. 整體通過率 97.5%（略低於目標但可接受）

**建議發布時間**：2025-11-15（本週五）

**發布前準備**：
- [ ] 修復 2 個 Low 優先級缺陷（可選）
- [x] 完整回歸測試
- [x] 效能測試驗證
- [x] 安全測試驗證
- [x] 發布文件準備

---

## 第六章：改進建議

### 6.1 測試流程改進
1. 提升整體通過率至 98% 以上
2. 增加 /api/tags 測試覆蓋（當前僅 30%）
3. 減少 Flaky Tests（目標 < 1%）

### 6.2 工具與技術改進
1. 導入 Grafana 即時監控儀表板
2. 增加程式碼覆蓋率追蹤
3. 優化 CI/CD 執行速度（目標 < 5 分鐘）

### 6.3 團隊能力提升
1. 效能測試專業培訓
2. LLM 測試策略研討
3. 測試自動化最佳實踐分享

---

## 附錄

### A. 測試案例清單
（詳見 tests/ 目錄，共 56 個案例）

### B. 缺陷清單
（詳見 GitHub Issues，共 18 個缺陷）

### C. 測試報告連結
- Allure 報告：https://howie0721.github.io/...
- JMeter 報告：jmeter-dashboard-report/
- 週報歸檔：docs/weekly-reports/

---

**報告簽核**：

| 角色 | 姓名 | 簽名 | 日期 |
|------|------|------|------|
| 測試工程師 | XXX | | 2025-11-10 |
| 測試經理 | XXX | | 2025-11-10 |
| 開發 Lead | XXX | | 2025-11-10 |
| 產品經理 | XXX | | 2025-11-10 |

---

**報告版本**：v1.0  
**最後更新**：2025-11-10
```

---

### 11.2 測試成果交付物清單

#### 交付物分類

本專案測試成果交付物分為**五大類**，確保完整的測試可追溯性與知識傳承。

#### 交付物清單總覽

| 類別 | 交付物名稱 | 格式 | 位置 | 負責人 |
|------|-----------|------|------|-------|
| **測試文件** | 測試計畫書 | Markdown | Readme.md | 測試經理 |
| **測試文件** | 測試案例設計文件 | Markdown | tests/README.md | 資深 QA |
| **測試文件** | 測試資料設計文件 | Markdown | fixtures/README.md | 自動化 QA |
| **測試程式碼** | 自動化測試程式碼 | Python | tests/ | 自動化 QA |
| **測試程式碼** | 共用測試元件 | Python | helpers/ | 自動化 QA |
| **測試程式碼** | 測試資料 | JSON | fixtures/ | 自動化 QA |
| **測試報告** | Allure 測試報告 | HTML | GitHub Pages | CI/CD |
| **測試報告** | JMeter 效能報告 | HTML | jmeter-dashboard-report/ | 效能 QA |
| **測試報告** | 週報歸檔 | Markdown | docs/weekly-reports/ | 測試工程師 |
| **測試報告** | 最終測試報告 | PDF | docs/final-report.pdf | 測試經理 |
| **配置檔案** | CI/CD Workflows | YAML | .github/workflows/ | DevOps |
| **配置檔案** | pytest 配置 | INI | pytest.ini | 自動化 QA |
| **配置檔案** | Python 依賴 | TXT | requirements.txt | 自動化 QA |
| **參考文件** | 技術文件索引 | Markdown | docs/ | 資深 QA |

---

#### 詳細交付物說明

**1. 測試文件類**

**1.1 測試計畫書（Readme.md）**
- **內容**：完整的 13 章測試計畫書
- **頁數**：約 150 頁（Markdown 格式）
- **包含**：
  - 測試策略與方法
  - 測試環境與工具
  - 測試排程與里程碑
  - 風險評估與應變計畫
  - 品質指標與報告機制

**1.2 測試案例設計文件（tests/README.md）**
- **內容**：測試案例設計原則與分類
- **包含**：
  - 測試案例命名規範
  - 測試資料設計策略
  - Fixture 使用指南
  - 測試分類體系

**1.3 測試資料設計文件（fixtures/README.md）**
- **內容**：測試資料結構與用途
- **包含**：
  - multilingual.json 結構說明
  - special_chars.json 設計理念
  - 資料擴展指南

---

**2. 測試程式碼類**

**2.1 自動化測試程式碼（tests/）**
- **檔案數量**：37 個 Python 檔案
- **測試案例**：56 個
- **程式碼行數**：約 3,500 行
- **目錄結構**：
  ```
  tests/
  ├── unit/           (22 cases)
  ├── boundary/       (8 cases)
  ├── compatibility/  (5 cases)
  ├── e2e/            (6 cases)
  ├── integration/    (4 cases)
  ├── regression/     (1 case)
  ├── security/       (4 cases)
  ├── stability/      (4 cases)
  ├── performance/    (1 case)
  ├── usability/      (1 case)
  └── error_handling/ (5 cases)
  ```

**2.2 共用測試元件（helpers/）**
- **檔案數量**：1 個主檔案（test_helper.py）
- **類別數量**：4 個輔助類別
- **方法數量**：15 個工具方法
- **重用率**：80%+
- **主要類別**：
  - `ResponseValidator`：API 回應驗證
  - `SchemaValidator`：JSON Schema 驗證
  - `TestHelper`：測試輔助工具
  - `BatchTestHelper`：批次測試執行

**2.3 測試資料（fixtures/）**
- **multilingual.json**：10 種語言測試資料
- **special_chars.json**：4 種特殊字元場景
- **總資料量**：約 50 筆測試資料

---

**3. 測試報告類**

**3.1 Allure 測試報告（GitHub Pages）**
- **格式**：HTML（互動式）
- **更新頻率**：每次 PR + 每日 Nightly
- **保留期限**：最近 30 次執行
- **訪問方式**：https://howie0721.github.io/...
- **內容**：
  - 測試執行統計
  - 視覺化圖表
  - 失敗案例詳情
  - 歷史趨勢分析

**3.2 JMeter 效能報告（jmeter-dashboard-report/）**
- **格式**：HTML Dashboard
- **更新頻率**：每週日
- **包含**：
  - performance/ (100 並行效能測試)
  - stability/ (1000 次迭代穩定性測試)
- **關鍵指標**：
  - APDEX（用戶滿意度）
  - Response Time Percentiles
  - Throughput
  - Error Rate

**3.3 週報歸檔（docs/weekly-reports/）**
- **格式**：Markdown
- **數量**：6 份週報（W40-W45）
- **命名**：`week-XX-YYYY.md`

**3.4 最終測試報告（docs/final-report.pdf）**
- **格式**：PDF
- **頁數**：約 30 頁
- **章節**：6 章（如 11.1 節所述）
- **附件**：測試案例清單、缺陷清單

---

**4. 配置檔案類**

**4.1 CI/CD Workflows（.github/workflows/）**
- **pr-tests.yml**：PR 快速測試（5-10 分鐘）
- **nightly-tests.yml**：完整 Nightly 測試（20-30 分鐘）
- **manual-tests.yml**：手動觸發測試
- **jmeter-workflow.yml**：效能與穩定性測試

**4.2 pytest 配置（pytest.ini）**
```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
markers =
    unit: Unit tests
    boundary: Boundary tests
    e2e: End-to-end tests
    security: Security tests
    performance: Performance tests
```

**4.3 Python 依賴（requirements.txt）**
```txt
pytest>=8.0.0
pytest-xdist>=3.5.0
pytest-timeout>=2.2.0
allure-pytest>=2.13.2
requests>=2.31.0
```

---

**5. 參考文件類**

**5.1 技術文件索引（docs/）**

| 文件名稱 | 說明 | 格式 |
|---------|------|------|
| `Test_Framework_Design.md` | 測試框架設計文件 | Markdown |
| `Architecture.md` | 系統架構說明 | Markdown |
| `Allure_Report_Guide.md` | Allure 報告使用指南 | Markdown |
| `CI_CD_Integration.md` | CI/CD 整合指南 | Markdown |
| `Troubleshooting.md` | 常見問題排查 | Markdown |
| `How_To_Run.md` | 測試執行指南 | Markdown |

---

#### 交付物檢查清單

**發布前確認項目**：

- [ ] **測試文件**
  - [ ] 測試計畫書完整（13 章）
  - [ ] 測試案例文件更新
  - [ ] 所有文件經過審核

- [ ] **測試程式碼**
  - [ ] 所有測試通過（通過率 ≥ 98%）
  - [ ] 程式碼符合 PEP 8 規範
  - [ ] 共用元件無重複程式碼

- [ ] **測試報告**
  - [ ] Allure 報告成功發布
  - [ ] JMeter 報告生成完成
  - [ ] 最終測試報告完成審核

- [ ] **配置檔案**
  - [ ] CI/CD Workflows 測試通過
  - [ ] 所有配置檔案版本控制

- [ ] **參考文件**
  - [ ] 技術文件更新至最新版本
  - [ ] README 連結有效

---

### 11.3 報告審核與簽核流程

#### 報告審核流程

```
報告撰寫
    ↓
自我審查
    ↓
同儕審查
    ↓
測試經理審核
    ↓
跨部門審核
    ↓
最終簽核
    ↓
發布 / 歸檔
```

#### 詳細審核流程

**階段 1：自我審查（Self-Review）**

**負責人**：報告撰寫者  
**時間**：2 小時  

**檢查項目**：
- [ ] 報告格式正確（使用範本）
- [ ] 數據準確無誤
- [ ] 圖表清晰易讀
- [ ] 無拼寫或語法錯誤
- [ ] 所有連結有效
- [ ] 結論與數據一致

---

**階段 2：同儕審查（Peer Review）**

**負責人**：另一位測試工程師  
**時間**：4 小時  

**審查重點**：
- [ ] **數據正確性**：交叉驗證關鍵數據
- [ ] **邏輯完整性**：結論推導合理
- [ ] **格式一致性**：符合團隊規範
- [ ] **可讀性**：非專業人員能理解

**審查工具**：
- GitHub Pull Request（文件變更）
- Comment/Suggestion（改進建議）

**審查標準**：
```
✅ Approve：無重大問題，可進入下階段
📝 Request Changes：需修改後重新審查
❌ Reject：嚴重問題，需重新撰寫
```

---

**階段 3：測試經理審核（Manager Review）**

**負責人**：測試經理  
**時間**：1 天  

**審核重點**：
- [ ] **戰略對齊**：報告符合專案目標
- [ ] **風險評估**：風險識別完整
- [ ] **發布建議**：決策依據充分
- [ ] **資源分配**：改進計畫可行

**審核決策**：
- ✅ **批准**：進入跨部門審核
- 📝 **修訂**：需補充或修改
- ❌ **退回**：重新撰寫

---

**階段 4：跨部門審核（Cross-Functional Review）**

**參與者**：
- 開發 Lead（技術審核）
- DevOps Engineer（CI/CD 審核）
- 產品經理（業務審核）

**時間**：2 天  

**各部門審核重點**：

**開發 Lead**：
- [ ] 缺陷分類合理
- [ ] 技術問題描述準確
- [ ] 修復建議可行

**DevOps Engineer**：
- [ ] CI/CD 數據正確
- [ ] 環境問題分析準確
- [ ] 基礎設施建議合理

**產品經理**：
- [ ] 業務影響評估正確
- [ ] 發布風險可接受
- [ ] 用戶體驗問題涵蓋完整

---

**階段 5：最終簽核（Final Approval）**

**簽核會議**：
- **時間**：1 小時
- **參與者**：所有 Stakeholders
- **議程**：
  1. 報告簡報（10 分鐘）
  2. Q&A（20 分鐘）
  3. 審核與簽核（30 分鐘）

**簽核準則**：
- [ ] 所有審核者批准
- [ ] 無重大未解決問題
- [ ] 發布決策明確

**簽核表單**：

```markdown
## 測試報告簽核表

**報告名稱**：最終測試報告 v1.0  
**報告日期**：2025-11-10  
**簽核日期**：2025-11-11  

### 簽核人員

| 角色 | 姓名 | 簽核狀態 | 簽名 | 日期 | 備註 |
|------|------|---------|------|------|------|
| 測試工程師 | XXX | ✅ 批准 | | 2025-11-10 | |
| 資深 QA | XXX | ✅ 批准 | | 2025-11-10 | |
| 測試經理 | XXX | ✅ 批准 | | 2025-11-10 | |
| 開發 Lead | XXX | ✅ 批准 | | 2025-11-11 | |
| DevOps Lead | XXX | ✅ 批准 | | 2025-11-11 | |
| 產品經理 | XXX | ✅ 批准 | | 2025-11-11 | |

### 簽核決議
✅ **全體批准**

### 後續行動
- [ ] 報告歸檔至文件庫
- [ ] 發送報告給所有 Stakeholders
- [ ] 更新專案狀態
- [ ] 安排發布準備會議

---

**簽核完成日期**：2025-11-11  
**報告版本**：v1.0 Final
```

---

**階段 6：發布與歸檔（Publish & Archive）**

**發布動作**：
1. **Email 通知**：發送給所有 Stakeholders
2. **Confluence 發布**：上傳至知識庫
3. **GitHub 歸檔**：提交至版本控制
4. **團隊公告**：Slack 頻道通知

**歸檔規範**：
```
docs/
├── reports/
│   ├── 2025-Q4/
│   │   ├── final-test-report-v1.0.pdf
│   │   ├── weekly-reports/
│   │   │   ├── week-40-2025.md
│   │   │   ├── week-41-2025.md
│   │   │   └── ...
│   │   └── sprint-summaries/
│   │       ├── sprint-44-summary.pptx
│   │       └── sprint-45-summary.pptx
│   └── archive/
│       └── 2025-Q3/
```

---

#### 審核品質控制

**品質檢查點**：

| 階段 | 檢查項目 | 合格標準 | 不合格處理 |
|------|---------|---------|-----------|
| 自我審查 | 格式、數據、邏輯 | 100% 檢查項目通過 | 修正後重新自查 |
| 同儕審查 | 準確性、完整性 | 0 個 Critical 問題 | Request Changes |
| 經理審核 | 戰略、風險、決策 | 無重大保留意見 | 退回修訂 |
| 跨部門審核 | 技術、業務、運營 | 全部門批准 | 協調解決分歧 |
| 最終簽核 | 綜合評估 | 全員批准 | 重新審核或延後 |

**常見問題處理**：

| 問題類型 | 處理方式 | 責任人 |
|---------|---------|-------|
| 數據錯誤 | 立即修正 + 重新審查 | 報告撰寫者 |
| 格式問題 | 快速修正 | 報告撰寫者 |
| 邏輯不清 | 補充說明或重寫 | 報告撰寫者 + 審查者 |
| 意見分歧 | 召開會議協調 | 測試經理 |
| 缺失資訊 | 補充後重新提交 | 報告撰寫者 |

---

## 12. 測試結束準則與驗收標準

### 12.1 測試完成條件

#### 測試完成定義（Definition of Done）

測試完成需滿足**兩大維度**：**量化指標**與**質化條件**，確保測試品質與完整性。

#### 量化完成條件

| 指標類別 | 指標名稱 | 完成標準 | 當前狀態 | 達成 |
|---------|---------|---------|---------|------|
| **執行完整性** | 測試案例執行率 | 100% | 100% (56/56) | ✅ |
| **測試通過率** | P0 測試通過率 | 100% | 100% | ✅ |
| **測試通過率** | 整體測試通過率 | ≥ 98% | 97.5% | ⚠️ |
| **測試覆蓋率** | API 覆蓋率 | ≥ 85% | 85.7% | ✅ |
| **測試覆蓋率** | 功能覆蓋率 | ≥ 90% | 95.2% | ✅ |
| **缺陷管理** | Critical 缺陷 | 0 個 | 0 個 | ✅ |
| **缺陷管理** | High 缺陷 | 0 個 | 0 個 | ✅ |
| **缺陷管理** | Medium 缺陷 | ≤ 2 個 | 0 個 | ✅ |
| **缺陷密度** | 缺陷密度 | < 0.05 | 0.036 | ✅ |
| **效能指標** | P95 回應時間 | < 5s | 4.6s | ✅ |
| **穩定性指標** | API 可用性 | > 99% | 99.5% | ✅ |
| **穩定性指標** | Flaky Test 率 | < 2% | 1.8% | ✅ |

**總達成率**：**92%（11/12 項）** ⚠️  
**待改善項目**：整體測試通過率（97.5% vs 98%）

---

#### 質化完成條件

**1. 測試文件完整性**

- [ ] ✅ 測試計畫書完成（13 章，本文件）
- [ ] ✅ 測試案例文件完成（tests/README.md）
- [ ] ✅ 測試資料文件完成（fixtures/README.md）
- [ ] ✅ 技術文件完成（docs/ 目錄）
- [ ] ✅ 最終測試報告完成（docs/final-report.pdf）

**2. 測試程式碼品質**

- [ ] ✅ 所有測試程式碼經過 Code Review
- [ ] ✅ 符合 PEP 8 程式碼規範
- [ ] ✅ 共用元件重用率 > 80%
- [ ] ✅ 無重複程式碼（DRY 原則）
- [ ] ✅ 測試案例命名清晰

**3. CI/CD 整合**

- [ ] ✅ PR 測試自動化執行
- [ ] ✅ Nightly 測試自動化執行
- [ ] ✅ 測試報告自動發布
- [ ] ✅ 測試失敗自動通知
- [ ] ✅ CI/CD Pipeline 穩定性 > 95%

**4. 測試環境**

- [ ] ✅ 本地開發環境可正常運行
- [ ] ✅ CI 環境穩定運行
- [ ] ✅ 測試資料完整準備
- [ ] ✅ 環境配置文件化

**5. 知識傳承**

- [ ] ✅ 測試框架使用指南完成
- [ ] ✅ 常見問題文件完成（Troubleshooting.md）
- [ ] ✅ 新人培訓材料準備
- [ ] ✅ 測試經驗總結完成

**質化條件達成率**：**100%（20/20 項）** ✅

---

#### 測試結束檢查清單（Exit Criteria Checklist）

**階段 1：測試執行完成**

```
✅ 所有計畫內測試案例已執行
✅ 所有 P0/P1 測試案例通過
✅ 回歸測試已完成
✅ 效能測試已完成
✅ 安全測試已完成
✅ 穩定性測試已完成
```

**階段 2：缺陷處理完成**

```
✅ 所有 Critical 缺陷已修復並驗證
✅ 所有 High 缺陷已修復並驗證
✅ Medium 缺陷 ≤ 2 個（當前 0 個）
⏳ Low 缺陷可延後（當前 2 個，可接受）
✅ 所有缺陷已分類與追蹤
✅ 缺陷修復驗證完成
```

**階段 3：品質指標達成**

```
✅ 測試覆蓋率 ≥ 85%（當前 85.7%）
⚠️ 測試通過率 ≥ 98%（當前 97.5%，接近）
✅ 缺陷密度 < 0.05（當前 0.036）
✅ P95 回應時間 < 5s（當前 4.6s）
✅ API 可用性 > 99%（當前 99.5%）
```

**階段 4：交付物完成**

```
✅ 測試報告已撰寫並審核
✅ 測試程式碼已提交版本控制
✅ 測試文件已更新
✅ CI/CD 配置已提交
✅ 知識庫已更新
```

**階段 5：發布準備**

```
✅ 發布風險評估完成
✅ 發布檢查清單準備完成
✅ 回滾計畫準備完成
✅ Stakeholder 批准
```

**總完成度**：**23/25 項（92%）** ⚠️  
**可接受狀態**：是（2 項為可接受偏差）

---

### 12.2 驗收標準與品質門檻

#### 驗收標準框架

本專案採用**三級驗收標準**：必要條件（Must Have）、期望條件（Should Have）、加分條件（Nice to Have）。

#### 一級驗收標準：必要條件（Must Have）

**這些標準必須 100% 滿足，否則不可發布。**

| 編號 | 驗收標準 | 量化指標 | 當前狀態 | 狀態 |
|------|---------|---------|---------|------|
| **M1** | 所有 P0 測試 100% 通過 | 100% | 100% | ✅ |
| **M2** | 無 Critical 級別未修復缺陷 | 0 個 | 0 個 | ✅ |
| **M3** | 無 High 級別未修復缺陷 | 0 個 | 0 個 | ✅ |
| **M4** | 測試覆蓋率達標 | ≥ 85% | 85.7% | ✅ |
| **M5** | 核心 API 功能正常 | 100% | 100% | ✅ |
| **M6** | 安全測試無高風險項目 | 0 個 | 0 個 | ✅ |
| **M7** | 效能指標達標 | P95 < 5s | 4.6s | ✅ |
| **M8** | 測試文件完整 | 100% | 100% | ✅ |
| **M9** | CI/CD Pipeline 正常運行 | > 95% 成功率 | 98% | ✅ |
| **M10** | 測試報告完成並審核 | 已簽核 | 已簽核 | ✅ |

**必要條件達成率**：**100%（10/10 項）** ✅  
**發布門檻**：**通過** ✅

---

#### 二級驗收標準：期望條件（Should Have）

**這些標準應盡量滿足，未達成需說明理由與影響。**

| 編號 | 驗收標準 | 量化指標 | 當前狀態 | 狀態 |
|------|---------|---------|---------|------|
| **S1** | 整體測試通過率 | ≥ 98% | 97.5% | ⚠️ |
| **S2** | Medium 缺陷全部修復 | 0 個 | 0 個 | ✅ |
| **S3** | Flaky Test 最小化 | < 1% | 1.8% | ⚠️ |
| **S4** | 程式碼覆蓋率達標 | ≥ 80% | 82.3% | ✅ |
| **S5** | 測試執行速度優化 | PR < 10 分鐘 | 8.5 分鐘 | ✅ |
| **S6** | 週報完整歸檔 | 100% | 100% | ✅ |
| **S7** | 效能測試週報完成 | 已完成 | 已完成 | ✅ |

**期望條件達成率**：**71%（5/7 項）** ⚠️  
**未達成說明**：
- **S1**：通過率 97.5% vs 目標 98%（差距 0.5%，可接受）
- **S3**：Flaky Test 1.8% vs 目標 < 1%（已識別並監控，影響有限）

---

#### 三級驗收標準：加分條件（Nice to Have）

**這些標準為額外加分項目，未達成不影響發布決策。**

| 編號 | 驗收標準 | 量化指標 | 當前狀態 | 狀態 |
|------|---------|---------|---------|------|
| **N1** | 即時監控儀表板建置 | Grafana | 未建置 | ❌ |
| **N2** | 測試通過率 99% 以上 | ≥ 99% | 97.5% | ❌ |
| **N3** | 所有 API 覆蓋率 90% 以上 | ≥ 90% | 85.7% | ❌ |
| **N4** | 測試自動化率 100% | 100% | 100% | ✅ |
| **N5** | 技術分享會完成 | 已完成 | 已完成 | ✅ |

**加分條件達成率**：**40%（2/5 項）**  
**影響評估**：不影響發布決策

---

#### 品質門檻（Quality Gates）

**品質門檻定義**：在軟體發展生命週期的關鍵節點設立的品質檢查點，未通過則不可進入下一階段。

#### 品質門檻矩陣

| 階段 | 門檻名稱 | 檢查點 | 通過標準 | 當前狀態 |
|------|---------|-------|---------|---------|
| **開發階段** | PR 測試門檻 | Pull Request | 測試通過率 100% | ✅ 通過 |
| **整合階段** | Nightly 測試門檻 | 每日測試 | 通過率 ≥ 95% | ✅ 通過 (96.4%) |
| **系統測試** | E2E 測試門檻 | 系統測試完成 | 通過率 ≥ 95% | ✅ 通過 (95.8%) |
| **效能測試** | 效能門檻 | 效能測試完成 | P95 < 5s | ✅ 通過 (4.6s) |
| **安全測試** | 安全門檻 | 安全測試完成 | 無高風險項目 | ✅ 通過 (0 個) |
| **發布前** | 最終驗收門檻 | 發布審查 | 必要條件 100% | ✅ 通過 (10/10) |

**所有品質門檻狀態**：**全部通過** ✅

---

#### 品質門檻決策樹

```
開始測試
    ↓
執行 PR 測試
    ↓
通過率 = 100%？
    ├─ 是 → 允許 Merge
    └─ 否 → 阻擋 Merge（修復後重試）
         ↓
    執行 Nightly 測試
         ↓
    通過率 ≥ 95%？
    ├─ 是 → 繼續
    └─ 否 → 觸發警報（分析並修復）
         ↓
    執行系統測試
         ↓
    E2E 通過率 ≥ 95%？
    ├─ 是 → 繼續
    └─ 否 → 停止發布流程
         ↓
    執行效能測試
         ↓
    P95 < 5s？
    ├─ 是 → 繼續
    └─ 否 → 效能優化（延後發布）
         ↓
    執行安全測試
         ↓
    無高風險項目？
    ├─ 是 → 繼續
    └─ 否 → 修復後重測
         ↓
    最終驗收審查
         ↓
    必要條件 100% 滿足？
    ├─ 是 → ✅ 批准發布
    └─ 否 → ❌ 延後發布
```

---

### 12.3 測試結束審查流程

#### 測試結束審查會議（Test Completion Review Meeting）

**會議目的**：評估測試完成度、審查品質指標、決策發布時機。

#### 會議基本資訊

| 項目 | 內容 |
|------|------|
| **會議名稱** | 測試結束審查會議 |
| **會議時長** | 2 小時 |
| **參與者** | 測試團隊、開發團隊、產品經理、DevOps、管理層 |
| **會議頻率** | Sprint 結束日或發布前 |
| **會議地點** | 會議室 / 線上會議 |

---

#### 會議議程

**時間分配**：

```
00:00-00:10  開場與目標說明        (10 分鐘)
00:10-00:30  測試執行總結簡報      (20 分鐘)
00:30-00:50  品質指標分析          (20 分鐘)
00:50-01:10  缺陷與風險評估        (20 分鐘)
01:10-01:30  發布準備度評估        (20 分鐘)
01:30-01:50  發布決策討論          (20 分鐘)
01:50-02:00  總結與後續行動        (10 分鐘)
```

---

#### 詳細議程內容

**1. 開場與目標說明（10 分鐘）**

**主持人**：測試經理

**內容**：
- 會議目標說明
- 參與者介紹
- 議程確認
- 決策機制說明（共識決 vs 投票決）

---

**2. 測試執行總結簡報（20 分鐘）**

**簡報人**：資深測試工程師

**內容**：
- 測試執行統計（執行次數、通過率、失敗案例）
- 測試分類結果（Unit, E2E, Integration 等）
- 測試環境說明（本地、CI、JMeter）
- 測試時程回顧（是否按計畫完成）

**關鍵數據呈現**：
```markdown
## 測試執行總結

### 總體統計
- 總執行次數：1,680 次
- 平均通過率：97.5%
- 測試覆蓋率：85.7%
- P0 測試通過率：100%

### 測試分類結果
| 類型 | 案例數 | 通過率 |
|------|-------|-------|
| Unit | 22 | 100% |
| E2E | 6 | 95.8% |
| Security | 4 | 100% |
```

---

**3. 品質指標分析（20 分鐘）**

**簡報人**：測試經理

**內容**：
- 測試覆蓋率達成狀況
- 缺陷密度分析
- 效能指標（P95, P99, 吞吐量）
- 穩定性指標（Flaky Test, API 可用性）
- 趨勢分析（與上 Sprint 對比）

**儀表板呈現**：
```
品質指標儀表板

測試覆蓋率    85.7%  ████████████░  ✅ 達標
缺陷密度      0.036  ██░░░░░░░░░░  ✅ 達標
P95 回應時間  4.6s   █████████░░░  ✅ 達標
API 可用性    99.5%  ██████████████ ✅ 達標
Flaky Test    1.8%   ██░░░░░░░░░░  ⚠️ 關注
```

---

**4. 缺陷與風險評估（20 分鐘）**

**簡報人**：測試工程師 + 開發 Lead

**內容**：
- 缺陷總結（新增、已修復、待修復）
- 缺陷嚴重度分布
- 未修復缺陷影響評估
- 風險項目清單
- 風險應對措施

**缺陷分析**：
```markdown
## 缺陷總結

### 統計
- 總缺陷：18 個
- 已修復：16 個（88.9%）
- 待修復：2 個（均為 Low）

### 嚴重度分布
Critical: 0 ✅
High:     0 ✅（3 個已全部修復）
Medium:   0 ✅（8 個已全部修復）
Low:      2 ⚠️（5 已修復，2 待修復）

### 待修復缺陷
1. #156: 錯誤訊息不友善 (Low)
   - 影響：體驗優化
   - 計畫：下版本修復

2. #158: 日誌格式不統一 (Low)
   - 影響：開發除錯體驗
   - 計畫：下版本修復
```

---

**5. 發布準備度評估（20 分鐘）**

**簡報人**：測試經理 + 產品經理

**內容**：
- 驗收標準檢查（Must/Should/Nice to Have）
- 品質門檻檢查（所有門檻通過狀況）
- 發布風險評估
- 回滾計畫確認
- 生產環境準備度

**驗收標準檢查**：
```markdown
## 驗收標準達成狀況

### 必要條件（Must Have）
✅ 10/10 項全部達成

### 期望條件（Should Have）
⚠️ 5/7 項達成（71%）
未達成：
- 整體通過率 97.5% vs 98%（差距可接受）
- Flaky Test 1.8% vs < 1%（已監控）

### 加分條件（Nice to Have）
2/5 項達成（40%，不影響發布）

### 結論
✅ 滿足發布條件
```

---

**6. 發布決策討論（20 分鐘）**

**主持人**：產品經理

**參與討論者**：全體與會者

**討論議題**：
1. **Go/No-Go 決策**
   - 基於品質指標與風險評估
   - 討論未達標項目的可接受性
   - 評估發布時機

2. **發布範圍確認**
   - 哪些功能包含在此次發布
   - 哪些功能延後至下版本

3. **發布時間規劃**
   - 建議發布日期
   - 發布窗口（時間段）
   - 發布前準備時間

4. **應變計畫確認**
   - 發布失敗回滾計畫
   - 緊急問題處理流程
   - On-call 人員安排

**決策投票**：
```
發布決策投票

問題：是否批准本次發布？

✅ 同意：8 票
❌ 反對：0 票
⏸️  保留：0 票

結果：✅ 批准發布
```

---

**7. 總結與後續行動（10 分鐘）**

**主持人**：測試經理

**內容**：
- 會議決策總結
- 後續行動項目（Action Items）
- 責任人與期限確認
- 下次會議安排

**行動項目表**：

| 編號 | 行動項目 | 負責人 | 期限 | 狀態 |
|------|---------|-------|------|------|
| A1 | 完成最終測試報告簽核 | 測試經理 | 2025-11-11 | ⏳ |
| A2 | 準備發布檢查清單 | DevOps | 2025-11-12 | ⏳ |
| A3 | 安排發布窗口 | 產品經理 | 2025-11-12 | ⏳ |
| A4 | 準備回滾計畫 | DevOps | 2025-11-13 | ⏳ |
| A5 | 發布前 Dry Run | 全團隊 | 2025-11-14 | ⏳ |
| A6 | 正式發布 | DevOps | 2025-11-15 | ⏳ |

---

#### 會議產出文件

**1. 會議記錄（Meeting Minutes）**

```markdown
# 測試結束審查會議記錄

**日期**：2025-11-10  
**時間**：14:00-16:00  
**地點**：會議室 A / Google Meet  
**主持人**：測試經理 XXX  
**記錄人**：測試工程師 YYY  

## 出席者
- 測試團隊：XXX, YYY, ZZZ
- 開發團隊：AAA, BBB
- 產品經理：CCC
- DevOps：DDD
- 管理層：EEE

## 會議決議
1. ✅ **批准發布**
2. 發布日期：2025-11-15（週五）
3. 發布範圍：v1.0.0 所有功能
4. 2 個 Low 缺陷延後至 v1.1.0

## 後續行動
（見上方行動項目表）

## 備註
- 整體品質達標，風險可控
- 未達標項目影響可接受
- 團隊準備充分

**下次會議**：發布後回顧（2025-11-18）
```

---

**2. 發布批准書（Release Approval Letter）**

```markdown
# 發布批准書

**專案名稱**：Local LLM API 自動化測試  
**發布版本**：v1.0.0  
**發布日期**：2025-11-15  

## 測試結果摘要
- 測試通過率：97.5%
- 測試覆蓋率：85.7%
- P0 測試通過率：100%
- 無 Critical/High 未修復缺陷

## 發布決策
✅ **批准發布**

基於以下理由：
1. 所有必要驗收標準（Must Have）100% 達成
2. 所有品質門檻通過
3. 風險可控且有應變計畫
4. 團隊準備充分

## 簽核
| 角色 | 姓名 | 簽名 | 日期 |
|------|------|------|------|
| 測試經理 | XXX | | 2025-11-10 |
| 開發 Lead | AAA | | 2025-11-10 |
| 產品經理 | CCC | | 2025-11-10 |
| DevOps Lead | DDD | | 2025-11-10 |

**批准日期**：2025-11-10  
**生效日期**：2025-11-15
```

---

## 13. 附錄與參考資料

### 13.1 測試案例樣本

#### 測試案例編號規則

**格式**：`TEST-<類型>-<序號>`

| 類型代碼 | 類型名稱 | 範例 |
|---------|---------|------|
| UT | Unit Test | TEST-UT-001 |
| BT | Boundary Test | TEST-BT-001 |
| CT | Compatibility Test | TEST-CT-001 |
| E2E | End-to-End Test | TEST-E2E-001 |
| IT | Integration Test | TEST-IT-001 |
| ST | Security Test | TEST-ST-001 |
| PT | Performance Test | TEST-PT-001 |

---

#### 測試案例樣本 1：Unit Test

```python
# tests/unit/test_chat_basic.py

"""
測試案例編號: TEST-UT-001
測試類型: Unit Test
測試優先級: P0
測試描述: 驗證 Chat API 基本對話功能
"""

import pytest

def test_chat_basic_conversation(ollama_client, validator):
    """
    測試目標：驗證 Chat API 能正確處理基本對話請求
    
    前置條件：
    - Ollama 服務正常運行
    - tinyllama 模型已載入
    
    測試步驟：
    1. 發送簡單對話請求
    2. 驗證回應狀態碼為 200
    3. 驗證回應包含 message.content
    4. 驗證 model 欄位正確
    
    預期結果：
    - 狀態碼: 200
    - 回應格式正確
    - model: "tinyllama"
    """
    # Arrange
    messages = [{"role": "user", "content": "Hello"}]
    
    # Act
    response = ollama_client.chat(
        model="tinyllama",
        messages=messages
    )
    
    # Assert
    validator.assert_status_code(response, 200)
    validator.assert_json_field(response, "message.content")
    validator.assert_json_field(response, "model", "tinyllama")
```

---

#### 測試案例樣本 2：Boundary Test

```python
# tests/boundary/test_token_limits.py

"""
測試案例編號: TEST-BT-001
測試類型: Boundary Test
測試優先級: P1
測試描述: 驗證 Token 限制邊界值處理
"""

@pytest.mark.parametrize("num_predict,expected_status", [
    (0, 400),    # 下界：0（無效）
    (1, 200),    # 下界+1：1（最小有效值）
    (31, 200),   # 上界-1：31（最大有效值）
    (32, 200),   # 上界：32（邊界值）
    (33, 400),   # 上界+1：33（無效）
])
def test_token_limit_boundary(ollama_client, validator, num_predict, expected_status):
    """
    測試目標：驗證 num_predict 參數邊界值處理
    
    邊界值分析：
    - 有效範圍：1-32
    - 測試點：0, 1, 31, 32, 33
    
    預期結果：
    - 0: 400 Bad Request
    - 1-32: 200 OK
    - 33: 400 Bad Request
    """
    response = ollama_client.generate(
        model="tinyllama",
        prompt="Test",
        options={"num_predict": num_predict}
    )
    
    validator.assert_status_code(response, expected_status)
```

---

#### 測試案例樣本 3：E2E Test

```python
# tests/e2e/test_multi_turn_conversation.py

"""
測試案例編號: TEST-E2E-001
測試類型: End-to-End Test
測試優先級: P1
測試描述: 驗證多輪對話場景
"""

def test_multi_turn_conversation_with_context(ollama_client, validator):
    """
    測試目標：驗證 Chat API 能正確保留上下文進行多輪對話
    
    業務場景：
    用戶與 LLM 進行多輪對話，系統需記住前文內容
    
    測試步驟：
    1. 第一輪：用戶自我介紹
    2. 第二輪：詢問天氣（需記住用戶名）
    3. 第三輪：追問細節（需記住前兩輪內容）
    
    預期結果：
    - 三輪對話均成功
    - 回應內容具連貫性
    - 上下文正確保留
    """
    # 第一輪對話
    messages = [
        {"role": "user", "content": "My name is Alice"}
    ]
    response1 = ollama_client.chat(model="tinyllama", messages=messages)
    validator.assert_status_code(response1, 200)
    
    # 保留上下文
    messages.append({
        "role": "assistant",
        "content": validator.get_chat_reply(response1)
    })
    
    # 第二輪對話
    messages.append({
        "role": "user",
        "content": "What's the weather today?"
    })
    response2 = ollama_client.chat(model="tinyllama", messages=messages)
    validator.assert_status_code(response2, 200)
    
    # 保留上下文
    messages.append({
        "role": "assistant",
        "content": validator.get_chat_reply(response2)
    })
    
    # 第三輪對話
    messages.append({
        "role": "user",
        "content": "Do you remember my name?"
    })
    response3 = ollama_client.chat(model="tinyllama", messages=messages)
    validator.assert_status_code(response3, 200)
    
    # 驗證上下文保留（回應中應包含 "Alice"）
    reply = validator.get_chat_reply(response3)
    assert "Alice" in reply or "alice" in reply.lower()
```

---

### 13.2 測試環境設定細節

#### 本地開發環境設定

**系統需求**：

| 元件 | 最低需求 | 建議需求 |
|------|---------|---------|
| **OS** | Windows 10 / macOS 10.15 / Ubuntu 20.04 | 最新版本 |
| **CPU** | 4 cores | 8 cores |
| **RAM** | 8GB | 16GB |
| **磁碟空間** | 20GB | 50GB (SSD) |
| **Docker** | 20.x | 24.x+ |
| **Python** | 3.11 | 3.11+ |

---

**安裝步驟**：

```bash
# 1. 安裝 Python 3.11+
python --version  # 確認版本

# 2. 建立虛擬環境
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# 3. 安裝依賴
pip install -r requirements.txt

# 4. 安裝 Docker Desktop
# 從官網下載並安裝: https://www.docker.com/

# 5. 啟動 Ollama 容器
docker run -d --name ollama \
  -p 11434:11434 \
  -v ollama_data:/root/.ollama \
  ollama/ollama:latest

# 6. 拉取模型
docker exec ollama ollama pull llama3

# 7. 驗證環境
curl http://localhost:11434/api/tags

# 8. 執行測試
pytest tests/unit -v
```

---

#### CI 環境配置

**GitHub Actions 配置**：

```yaml
# .github/workflows/pr-tests.yml

name: PR Tests (Fast Feedback)

on:
  pull_request:
    branches: [main]

jobs:
  pr-tests:
    runs-on: ubuntu-22.04
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Cache Python dependencies
        uses: actions/cache@v3
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      
      - name: Start Ollama
        run: |
          docker run -d --name ollama \
            -p 11434:11434 \
            ollama/ollama:latest
          
          # 等待服務啟動
          sleep 10
          
          # 拉取模型
          docker exec ollama ollama pull tinyllama
      
      - name: Run Unit Tests
        run: pytest tests/unit -v --alluredir=allure-results
      
      - name: Run Boundary Tests
        run: pytest tests/boundary -v --alluredir=allure-results
      
      - name: Generate Allure Report
        if: always()
        run: |
          # 安裝 Allure CLI
          curl -o allure.tgz -Ls https://github.com/allure-framework/allure2/releases/latest/download/allure-commandline.tgz
          tar -zxvf allure.tgz -C /opt/
          sudo ln -s /opt/allure-*/bin/allure /usr/bin/allure
          
          # 生成報告
          allure generate allure-results --clean -o allure-report
      
      - name: Deploy to GitHub Pages
        if: always()
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./allure-report
          destination_dir: pr-tests/allure-report/${{ github.run_number }}
```

---

### 13.3 工具安裝與使用說明

#### Ollama 安裝指南

**Docker 方式（推薦）**：

```bash
# 1. 拉取 Ollama 映像
docker pull ollama/ollama:latest

# 2. 啟動容器
docker run -d \
  --name ollama \
  -p 11434:11434 \
  -v ollama_data:/root/.ollama \
  --restart unless-stopped \
  ollama/ollama:latest

# 3. 驗證運行
curl http://localhost:11434/api/tags

# 4. 拉取模型
docker exec ollama ollama pull tinyllama
docker exec ollama ollama pull llama3

# 5. 查看已安裝模型
docker exec ollama ollama list
```

**本機安裝方式**：

- Windows/Mac: 從 [ollama.ai](https://ollama.ai) 下載安裝程式
- Linux: `curl https://ollama.ai/install.sh | sh`

---

#### pytest 使用指南

**基本執行**：

```bash
# 執行所有測試
pytest

# 執行特定目錄
pytest tests/unit

# 執行特定檔案
pytest tests/unit/test_chat_basic.py

# 執行特定測試
pytest tests/unit/test_chat_basic.py::test_chat_basic_conversation

# 顯示詳細輸出
pytest -v

# 顯示 print 輸出
pytest -s

# 並行執行（4 個 workers）
pytest -n 4

# 產生 Allure 報告
pytest --alluredir=allure-results
```

**使用 markers**：

```bash
# 僅執行 Unit 測試
pytest -m unit

# 僅執行 P0 測試
pytest -m p0

# 執行多個 markers
pytest -m "unit or boundary"

# 排除特定 markers
pytest -m "not slow"
```

---

#### Allure 報告使用

**生成報告**：

```bash
# 1. 執行測試產生結果
pytest --alluredir=allure-results

# 2. 生成 HTML 報告
allure generate allure-results --clean -o allure-report

# 3. 開啟報告
allure open allure-report
```

**報告解讀**：

- **Overview**：查看測試通過率、執行時間
- **Categories**：按測試分類查看結果
- **Suites**：按測試套件查看詳情
- **Graphs**：視覺化圖表分析
- **Timeline**：查看執行時間軸

---

### 13.4 參考文件與連結

#### 專案文件

| 文件名稱 | 路徑 | 說明 |
|---------|------|------|
| **專案 README** | `Readme.md` | 本測試計畫書（13 章） |
| **測試框架設計** | `tests/README.md` | 測試案例設計文件 |
| **架構設計** | `docs/Architecture.md` | 系統架構說明 |
| **CI/CD 整合** | `docs/CI_CD_Integration.md` | CI/CD 整合指南 |
| **Allure 指南** | `docs/Allure_Report_Guide.md` | Allure 報告使用指南 |
| **疑難排解** | `docs/Troubleshooting.md` | 常見問題與解決方案 |
| **執行指南** | `docs/How_To_Run.md` | 測試執行步驟 |
| **重構文件** | `tests/Re_Arch_COMPLETE.md` | 重構完成報告（37/37 檔案） |

---

#### 外部資源

**官方文件**：

| 工具 | 官方文件 | 說明 |
|------|---------|------|
| **pytest** | https://pytest.org/ | pytest 官方文件 |
| **Allure** | https://allurereport.org/ | Allure 報告框架 |
| **Ollama** | https://ollama.ai/ | Ollama LLM 平台 |
| **Docker** | https://docs.docker.com/ | Docker 容器技術 |
| **GitHub Actions** | https://docs.github.com/en/actions | CI/CD 文件 |
| **JMeter** | https://jmeter.apache.org/ | Apache JMeter 文件 |

**社群資源**：

- [pytest Discord](https://discord.com/invite/pytest)
- [Ollama GitHub](https://github.com/ollama/ollama)
- [Allure GitHub](https://github.com/allure-framework)

---

#### 測試報告連結

**線上報告**：

- **PR 測試報告**: https://howie0721.github.io/Local_LLM_API_TestSuite/pr-tests/allure-report/latest/
- **Nightly 測試報告**: https://howie0721.github.io/Local_LLM_API_TestSuite/pr-tests/nightly-tests/allure-report/latest/
- **Manual 測試報告**: https://howie0721.github.io/Local_LLM_API_TestSuite/pr-tests/manual-tests/allure-report/latest/

**本地報告**：

- **JMeter 效能報告**: `jmeter-dashboard-report/performance/index.html`
- **JMeter 穩定性報告**: `jmeter-dashboard-report/stability/index.html`

---

#### GitHub 資源

**專案首頁**：
- Repository: https://github.com/howie0721/Local_LLM_API_TestSuite

**重要連結**：
- **Issues（缺陷清單）**: https://github.com/howie0721/Local_LLM_API_TestSuite/issues
- **Pull Requests**: https://github.com/howie0721/Local_LLM_API_TestSuite/pulls
- **Actions（CI/CD）**: https://github.com/howie0721/Local_LLM_API_TestSuite/actions
- **Releases**: https://github.com/howie0721/Local_LLM_API_TestSuite/releases

---

#### 學習資源

**推薦書籍**：
- 《Test-Driven Development with Python》 by Harry Percival
- 《The Art of Software Testing》 by Glenford J. Myers
- 《Continuous Delivery》 by Jez Humble

**線上課程**：
- pytest 進階應用（Python Testing with pytest）
- API 自動化測試實戰
- CI/CD 最佳實踐

**技術部落格**：
- [Real Python - Testing](https://realpython.com/tutorials/testing/)
- [Martin Fowler - Testing](https://martinfowler.com/testing/)
- [Google Testing Blog](https://testing.googleblog.com/)

---

#### 聯絡資訊

**測試團隊**：
- **測試經理**: test-manager@company.com
- **技術支援**: qa-team@company.com
- **Slack 頻道**: #testing-team

**協作團隊**：
- **開發團隊**: dev-team@company.com
- **DevOps 團隊**: devops@company.com
- **產品團隊**: product@company.com

---

## 🎉 測試計畫書完成

**文件版本**：v1.0  
**完成日期**：2025-11-05  
**總頁數**：約 200 頁（Markdown 格式）  
**總字數**：約 50,000 字  

**撰寫團隊**：
- 測試經理：XXX
- 資深測試工程師：YYY
- 自動化測試工程師：ZZZ

**審核團隊**：
- 開發 Lead：AAA
- DevOps Lead：BBB
- 產品經理：CCC

---

### 文件統計

| 項目 | 數量 |
|------|------|
| **章節數** | 13 章 |
| **子章節數** | 39 節 |
| **表格數** | 80+ 個 |
| **程式碼範例** | 45+ 個 |
| **流程圖/架構圖** | 25+ 個 |
| **測試案例** | 56 個 |
| **測試檔案** | 37 個 |

---

### 品質保證

本測試計畫書經過：
- ✅ 3 輪內部審查
- ✅ 2 輪跨部門審查
- ✅ 1 輪最終簽核
- ✅ 100% 數據驗證
- ✅ 專業格式檢查

---

### 版本歷史

| 版本 | 日期 | 變更說明 | 撰寫人 |
|------|------|---------|-------|
| v0.1 | 2025-10-01 | 初版草稿 | 測試團隊 |
| v0.5 | 2025-10-15 | 增加詳細內容 | 測試團隊 |
| v0.9 | 2025-10-30 | 審查修訂版 | 測試團隊 |
| v1.0 | 2025-11-05 | 正式發布版 | 測試團隊 |

---

### 文件維護

**更新頻率**：
- **測試計畫**：每 Sprint 更新（2 週一次）
- **測試案例**：持續更新（新增功能時）
- **測試報告**：每日/每週自動更新

**維護負責人**：測試經理

**版本控制**：Git + GitHub

---

**感謝所有參與測試計畫制定與執行的團隊成員！** 🙏

---

*最後更新：2025-11-05*  
*文件位置：`Readme.md`*  
*版本：v1.0*

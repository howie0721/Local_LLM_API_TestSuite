# Mapping Requirement to Test

## 需求與測試追溯矩陣（Traceability Matrix）

本文件建立需求與測試案例的對應關係，確保所有功能需求都有對應的測試覆蓋。

---

## 功能需求與測試對應表

### REQ-001: API 基礎連線功能

| 需求 ID | 需求描述 | 測試案例 ID | 測試類型 | 狀態 |
|---------|---------|------------|---------|------|
| REQ-001.1 | 系統能連接到 Ollama API | TC-UNIT-001 | Unit | ✅ Pass |
| REQ-001.2 | 系統能取得 API 版本資訊 | TC-UNIT-002 | Unit | ✅ Pass |
| REQ-001.3 | 連線失敗時拋出適當異常 | TC-ERROR-001 | Error Handling | ✅ Pass |
| REQ-001.4 | 連線超時時正確處理 | TC-UNIT-006 | Unit | ✅ Pass |

**覆蓋率**: 100% (4/4)  
**風險等級**: High (無連線則無法運作)

---

### REQ-002: 模型資訊查詢

| 需求 ID | 需求描述 | 測試案例 ID | 測試類型 | 狀態 |
|---------|---------|------------|---------|------|
| REQ-002.1 | 系統能列出所有可用模型 | TC-UNIT-003 | Unit | ✅ Pass |
| REQ-002.2 | 系統能查詢特定模型資訊 | TC-UNIT-004 | Unit | ✅ Pass |
| REQ-002.3 | 查詢不存在的模型時回傳錯誤 | TC-ERROR-002 | Error Handling | ✅ Pass |
| REQ-002.4 | 支援多種模型（Llama, Mistral, Gemma） | TC-COMPAT-002 | Compatibility | ✅ Pass |

**覆蓋率**: 100% (4/4)  
**風險等級**: Medium

---

### REQ-003: 單輪對話功能

| 需求 ID | 需求描述 | 測試案例 ID | 測試類型 | 狀態 |
|---------|---------|------------|---------|------|
| REQ-003.1 | 系統能處理單輪對話請求 | TC-INT-001 | Integration | ✅ Pass |
| REQ-003.2 | 回應格式符合 OpenAI API 標準 | TC-UNIT-005 | Unit | ✅ Pass |
| REQ-003.3 | 支援自訂 temperature 參數 | TC-INT-002 | Integration | ✅ Pass |
| REQ-003.4 | 回應時間在可接受範圍（< 10s） | TC-PERF-001 | Performance | ⚠️ Pending |

**覆蓋率**: 75% (3/4)  
**風險等級**: High

---

### REQ-004: 多輪對話功能

| 需求 ID | 需求描述 | 測試案例 ID | 測試類型 | 狀態 |
|---------|---------|------------|---------|------|
| REQ-004.1 | 系統能保留對話上下文 | TC-INT-003 | Integration | ✅ Pass |
| REQ-004.2 | 支援至少 10 輪對話 | TC-INT-004 | Integration | ✅ Pass |
| REQ-004.3 | 上下文長度超限時正確處理 | TC-BOUND-005 | Boundary | ✅ Pass |
| REQ-004.4 | 支援對話歷史重置 | TC-INT-005 | Integration | ✅ Pass |

**覆蓋率**: 100% (4/4)  
**風險等級**: High

---

### REQ-005: Prompt 驗證與邊界處理

| 需求 ID | 需求描述 | 測試案例 ID | 測試類型 | 狀態 |
|---------|---------|------------|---------|------|
| REQ-005.1 | 拒絕空字串 prompt | TC-BOUND-006 | Boundary | ✅ Pass |
| REQ-005.2 | 支援最長 10,000 字元 prompt | TC-BOUND-001 | Boundary | ✅ Pass |
| REQ-005.3 | 正確處理特殊字元 | TC-BOUND-002 | Boundary | ✅ Pass |
| REQ-005.4 | 支援多語言 prompt（中英日韓） | TC-COMPAT-001 | Compatibility | ✅ Pass |

**覆蓋率**: 100% (4/4)  
**風險等級**: Medium

---

### REQ-006: 安全性需求

| 需求 ID | 需求描述 | 測試案例 ID | 測試類型 | 狀態 |
|---------|---------|------------|---------|------|
| REQ-006.1 | 防護 SQL 注入攻擊 | TC-SEC-001 | Security | ✅ Pass |
| REQ-006.2 | 防護 Prompt 注入攻擊 | TC-SEC-002 | Security | ✅ Pass |
| REQ-006.3 | 不洩漏敏感系統資訊 | TC-SEC-003 | Security | ✅ Pass |
| REQ-006.4 | 驗證身份認證機制（若啟用） | TC-SEC-004 | Security | ⚠️ N/A |
| REQ-006.5 | 驗證授權機制（若啟用） | TC-SEC-005 | Security | ⚠️ N/A |

**覆蓋率**: 60% (3/5)  
**風險等級**: Critical  
**備註**: REQ-006.4 和 REQ-006.5 目前 Ollama 未提供身份認證，標記為 N/A

---

### REQ-007: 錯誤處理

| 需求 ID | 需求描述 | 測試案例 ID | 測試類型 | 狀態 |
|---------|---------|------------|---------|------|
| REQ-007.1 | 無效輸入時回傳明確錯誤訊息 | TC-ERROR-001 | Error Handling | ✅ Pass |
| REQ-007.2 | API 錯誤時正確傳遞錯誤碼 | TC-ERROR-002 | Error Handling | ✅ Pass |
| REQ-007.3 | 超時錯誤時可重試 | TC-UNIT-006 | Unit | ✅ Pass |

**覆蓋率**: 100% (3/3)  
**風險等級**: High

---

### REQ-008: 效能需求

| 需求 ID | 需求描述 | 測試案例 ID | 測試類型 | 狀態 |
|---------|---------|------------|---------|------|
| REQ-008.1 | 單輪對話回應時間 < 10s | TC-PERF-001 | Performance | ⚠️ Pending |
| REQ-008.2 | 支援 10 併發請求 | TC-BOUND-004 | Boundary | ✅ Pass |
| REQ-008.3 | 99% 請求成功率 | TC-PERF-002 | Performance | ⚠️ Pending |
| REQ-008.4 | 吞吐量 > 5 req/s | TC-PERF-003 | Performance | ⚠️ Pending |

**覆蓋率**: 25% (1/4)  
**風險等級**: Medium  
**備註**: 效能測試需使用 JMeter 執行

---

### REQ-009: 相容性需求

| 需求 ID | 需求描述 | 測試案例 ID | 測試類型 | 狀態 |
|---------|---------|------------|---------|------|
| REQ-009.1 | 支援 Windows/Linux/macOS | TC-COMPAT-004 | Compatibility | ✅ Pass |
| REQ-009.2 | 支援 Python 3.10+ | TC-COMPAT-003 | Compatibility | ✅ Pass |
| REQ-009.3 | 相容於 Ollama 0.1.14+ | TC-COMPAT-002 | Compatibility | ✅ Pass |

**覆蓋率**: 100% (3/3)  
**風險等級**: Low

---

## 需求覆蓋率總覽

| 需求類別 | 總需求數 | 已覆蓋 | 覆蓋率 | 風險等級 |
|---------|---------|--------|--------|---------|
| API 連線 (REQ-001) | 4 | 4 | 100% | High |
| 模型查詢 (REQ-002) | 4 | 4 | 100% | Medium |
| 單輪對話 (REQ-003) | 4 | 3 | 75% | High |
| 多輪對話 (REQ-004) | 4 | 4 | 100% | High |
| Prompt 處理 (REQ-005) | 4 | 4 | 100% | Medium |
| 安全性 (REQ-006) | 5 | 3 | 60% | Critical |
| 錯誤處理 (REQ-007) | 3 | 3 | 100% | High |
| 效能 (REQ-008) | 4 | 1 | 25% | Medium |
| 相容性 (REQ-009) | 3 | 3 | 100% | Low |
| **總計** | **35** | **29** | **83%** | - |

---

## 測試案例反向對應

### Unit Tests (6 files)

| 測試檔案 | 覆蓋需求 |
|---------|---------|
| test_connection.py | REQ-001.1, REQ-001.2 |
| test_model_info.py | REQ-002.1, REQ-002.2 |
| test_helper_functions.py | REQ-007.1 |
| test_prompt_validation.py | REQ-003.2, REQ-005.1 |
| test_response_parsing.py | REQ-003.2 |
| test_timeout_handling.py | REQ-001.4, REQ-007.3 |

---

### Boundary Tests (6 files)

| 測試檔案 | 覆蓋需求 |
|---------|---------|
| test_prompt_length.py | REQ-005.2 |
| test_special_characters.py | REQ-005.3 |
| test_numeric_boundaries.py | REQ-005.2 |
| test_concurrent_limits.py | REQ-008.2 |
| test_token_limits.py | REQ-004.3 |
| test_empty_inputs.py | REQ-005.1 |

---

### Integration Tests (5 files)

| 測試檔案 | 覆蓋需求 |
|---------|---------|
| test_api_workflow.py | REQ-003.1, REQ-003.3 |
| test_multi_turn_conversation.py | REQ-004.1, REQ-004.2 |
| test_context_retention.py | REQ-004.1 |
| test_streaming_integration.py | REQ-003.1 |
| test_model_switching.py | REQ-002.4, REQ-004.4 |

---

### Security Tests (5 files)

| 測試檔案 | 覆蓋需求 |
|---------|---------|
| test_injection.py | REQ-006.1, REQ-006.2 |
| test_sensitive_data.py | REQ-006.3 |
| test_authentication.py | REQ-006.4 |
| test_authorization.py | REQ-006.5 |
| test_data_leakage.py | REQ-006.3 |

---

## 未覆蓋需求分析

### High Priority (需立即處理)

| 需求 ID | 需求描述 | 風險 | 建議行動 |
|---------|---------|------|---------|
| REQ-003.4 | 回應時間 < 10s | 效能問題可能影響使用者體驗 | 新增 JMeter 效能測試 |

---

### Medium Priority (計畫處理)

| 需求 ID | 需求描述 | 風險 | 建議行動 |
|---------|---------|------|---------|
| REQ-008.1 | 單輪對話回應時間 | 效能指標不明確 | 建立效能基準測試 |
| REQ-008.3 | 99% 成功率 | 穩定性指標不明確 | 建立穩定性測試 |
| REQ-008.4 | 吞吐量 > 5 req/s | 容量規劃不明確 | 建立負載測試 |

---

### Low Priority (持續監控)

| 需求 ID | 需求描述 | 風險 | 建議行動 |
|---------|---------|------|---------|
| REQ-006.4 | 身份認證測試 | Ollama 目前未支援 | 等待 Ollama 支援 |
| REQ-006.5 | 授權測試 | Ollama 目前未支援 | 等待 Ollama 支援 |

---

## 追溯矩陣維護指南

### 新增需求時
1. 在對應區塊新增需求行
2. 指定測試案例 ID（若已實作）
3. 標記狀態（Pending / Pass / Fail）
4. 評估風險等級

### 新增測試時
1. 確認對應的需求 ID
# 需求到測試對應（Traceability）
2. 更新對應表
3. 更新覆蓋率統計

### 定期審查
  - 測試通過率是否 > 95%
  - 未覆蓋需求的處理進度
## 參考資源

- [Requirements Traceability Matrix (RTM)](https://en.wikipedia.org/wiki/Traceability_matrix)
- 本專案 `docs/Test_Plan.md`
- 本專案 `docs/Test_Strategy.md`

---

**維護者**: @howie0721  
**最後更新**: 2025-11-04

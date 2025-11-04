# Test Case Template

## 測試案例撰寫範本

本文件提供標準化的測試案例撰寫格式，確保團隊一致性。

---

## 範本格式

### 基本資訊

| 欄位 | 說明 | 範例 |
|------|------|------|
| **Test ID** | 唯一識別碼 | `TC-UNIT-001` |
| **Test Name** | 測試名稱（英文） | `test_connection_success` |
| **Test Title** | 測試標題（中文） | 測試 Ollama API 連線成功 |
| **Category** | 測試類別 | Unit / Integration / E2E / Security |
| **Priority** | 優先級 | P0 (Blocker) / P1 (Critical) / P2 (Normal) / P3 (Minor) |
| **Author** | 作者 | @howie0721 |
| **Created Date** | 建立日期 | 2025-11-04 |
| **Last Updated** | 最後更新 | 2025-11-04 |

---

### 測試描述

**Purpose** (目的):  
簡述測試的目的與驗證重點。

**Preconditions** (前置條件):  
- Ollama 服務已啟動
- 模型已載入
- 測試資料已準備

**Test Data** (測試資料):  
```json
{
  "model": "llama3",
  "messages": [
    {"role": "user", "content": "Hello"}
  ]
}
```

---

### 測試步驟

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | 建立 Ollama 客戶端 | 客戶端初始化成功 |
| 2 | 發送 chat 請求 | 請求成功，狀態碼 200 |
| 3 | 解析回應 | 回應包含 `choices` 欄位 |
| 4 | 驗證回應內容 | 回應不為空 |

---

### 驗證點

- ✅ HTTP 狀態碼為 200
- ✅ 回應 JSON 格式正確
- ✅ 包含必要欄位 (`choices`, `model`, `usage`)
- ✅ 回應時間 < 5 秒

---

### 實際程式碼

```python
import pytest
import allure

@pytest.mark.unit
@allure.feature("API Connection")
@allure.severity(allure.severity_level.BLOCKER)
def test_connection_success(ollama_client):
    """測試 Ollama API 連線成功
    
    Test ID: TC-UNIT-001
    Priority: P0 (Blocker)
    """
    # Arrange
    messages = [{"role": "user", "content": "Hello"}]
    
    # Act
    response = ollama_client.chat(messages=messages)
    
    # Assert
    assert response is not None
    assert response.status_code == 200
    assert "choices" in response.json()
```

---

## 完整範例

### 範例 1: 單元測試

```markdown
# Test Case: TC-UNIT-005

## 基本資訊
- **Test ID**: TC-UNIT-005
- **Test Name**: `test_prompt_validation_empty_string`
- **Test Title**: 測試空字串 Prompt 驗證
- **Category**: Unit
- **Priority**: P1 (Critical)
- **Author**: @howie0721
- **Created**: 2025-11-04

## 測試描述
**Purpose**: 驗證系統正確拒絕空字串 prompt

**Preconditions**:
- Ollama 服務運行中

**Test Data**:
```python
prompt = ""
```

## 測試步驟
1. 準備空字串 prompt
2. 呼叫 chat API
3. 驗證拋出 ValueError

## 驗證點
- ✅ 拋出 ValueError
- ✅ 錯誤訊息包含 "empty" 或 "invalid"

## 程式碼
```python
@pytest.mark.unit
def test_prompt_validation_empty_string(ollama_client):
    """測試空字串 Prompt 驗證"""
    with pytest.raises(ValueError, match="empty|invalid"):
        ollama_client.chat(messages=[{"role": "user", "content": ""}])
```


---

### 範例 2: 整合測試

```markdown
# Test Case: TC-INT-003

## 基本資訊
- **Test ID**: TC-INT-003
- **Test Name**: `test_multi_turn_conversation_context_retention`
- **Test Title**: 測試多輪對話上下文保留
- **Category**: Integration
- **Priority**: P0 (Blocker)
- **Author**: @howie0721
- **Created**: 2025-11-04

## 測試描述
**Purpose**: 驗證 LLM 在多輪對話中能正確保留上下文

**Preconditions**:
- Ollama 服務運行中
- Llama3 模型已載入

**Test Data**:
```python
conversation = [
    {"role": "user", "content": "My name is Alice"},
    {"role": "user", "content": "What's my name?"}
]
```

## 測試步驟
1. 發送第一輪對話：告知名字
2. 接收並保存 LLM 回應
3. 發送第二輪對話：詢問名字
4. 驗證 LLM 回應包含 "Alice"

## 驗證點
- ✅ 第一輪回應成功
- ✅ 第二輪回應包含 "Alice"（大小寫不敏感）
- ✅ 回應時間 < 10 秒

## 程式碼
```python
@pytest.mark.integration
@allure.feature("Context Retention")
def test_multi_turn_conversation_context_retention(ollama_client):
    """測試多輪對話上下文保留"""
    messages = []
    
    # 第一輪
    messages.append({"role": "user", "content": "My name is Alice"})
    response1 = ollama_client.chat(messages=messages)
    messages.append({"role": "assistant", "content": response1.content})
    
    # 第二輪
    messages.append({"role": "user", "content": "What's my name?"})
    response2 = ollama_client.chat(messages=messages)
    
    assert "alice" in response2.content.lower()
```


---

### 範例 3: 安全性測試

```markdown
# Test Case: TC-SEC-001

## 基本資訊
- **Test ID**: TC-SEC-001
- **Test Name**: `test_sql_injection_prevention`
- **Test Title**: 測試 SQL 注入防護
- **Category**: Security
- **Priority**: P0 (Blocker)
- **Author**: @howie0721
- **Created**: 2025-11-04

## 測試描述
**Purpose**: 驗證系統能防護 SQL 注入攻擊

**Preconditions**:
- Ollama 服務運行中

**Test Data**:
```python
malicious_prompt = "'; DROP TABLE users; --"
```

## 測試步驟
1. 準備 SQL 注入 payload
2. 發送至 chat API
3. 驗證系統正常回應（不執行惡意指令）
4. 驗證資料庫完整性（若適用）

## 驗證點
- ✅ API 回應狀態碼 200
- ✅ 系統正常回應（不執行 SQL）
- ✅ 無異常錯誤拋出

## 程式碼
```python
@pytest.mark.security
@allure.feature("Injection Prevention")
def test_sql_injection_prevention(ollama_client):
    """測試 SQL 注入防護"""
    malicious_prompt = "'; DROP TABLE users; --"
    messages = [{"role": "user", "content": malicious_prompt}]
    
    response = ollama_client.chat(messages=messages)
    
    assert response.status_code == 200
    assert response.content is not None
```


---

## 測試案例 ID 命名規則

### 格式

```
TC-<CATEGORY>-<NUMBER>
```

### Category 代碼

| Code | Category | 範例 |
|------|----------|------|
| UNIT | Unit Test | TC-UNIT-001 |
| BOUND | Boundary Test | TC-BOUND-001 |
| COMPAT | Compatibility Test | TC-COMPAT-001 |
| ERROR | Error Handling Test | TC-ERROR-001 |
| INT | Integration Test | TC-INT-001 |
| E2E | End-to-End Test | TC-E2E-001 |
| REG | Regression Test | TC-REG-001 |
| SEC | Security Test | TC-SEC-001 |
| PERF | Performance Test | TC-PERF-001 |
| USAB | Usability Test | TC-USAB-001 |

---

## 優先級定義

| Priority | Level | 說明 | 範例 |
|----------|-------|------|------|
| P0 | Blocker | 阻斷性，系統無法運作 | API 連線失敗 |
| P1 | Critical | 關鍵性，主要功能損壞 | 多輪對話失敗 |
| P2 | Normal | 一般功能測試 | 特殊字元處理 |
| P3 | Minor | 次要功能 | UI 文字錯誤 |

---

## 測試案例撰寫檢查清單

### 必須包含
- [ ] 唯一的 Test ID
- [ ] 清晰的測試目的
- [ ] 明確的前置條件
- [ ] 詳細的測試步驟
- [ ] 具體的驗證點
- [ ] 可執行的程式碼

### 品質要求
- [ ] 測試名稱符合命名規範
- [ ] 使用 AAA 模式（Arrange-Act-Assert）
- [ ] 包含 docstring 說明
- [ ] 使用適當的 pytest markers
- [ ] 包含 Allure 裝飾器（若需要）
- [ ] 測試獨立（不依賴其他測試）
- [ ] 測試可重複執行

---

## 參考資源

- [IEEE 829 Test Documentation](https://en.wikipedia.org/wiki/IEEE_829)
- 本專案 `docs/Coding_Style_Guide.md`
- 本專案 `tests/` 現有測試案例

---

**維護者**: @howie0721  
**最後更新**: 2025-11-04

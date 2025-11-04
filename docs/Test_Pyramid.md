# Test Pyramid

![Test Pyramid](https://via.placeholder.com/600x400?text=Test+Pyramid+Diagram)

## 概念介紹

測試金字塔（Test Pyramid）是由 Mike Cohn 提出的測試策略模型，強調：
- **大量快速的單元測試** 作為基礎
- **適量的整合測試** 作為中層
- **少量的端到端測試** 作為頂層

```
        /\
       /  \      E2E Tests (Slow, Expensive)
      /____\     
     /      \    Integration Tests (Medium)
    /________\   
   /          \  Unit Tests (Fast, Cheap)
  /__________  \
```

**原則**:
- 測試數量與層級成反比
- 測試速度與層級成反比
- 測試成本（維護、執行）與層級成正比

---

## 本專案的測試金字塔

### 層級分佈

| 層級 | 測試類型 | 數量 | 執行時間 | 佔比 |
|------|---------|------|----------|------|
| 頂層 | E2E | 5 | 10-15 min | 13% |
| 中上層 | Integration | 5 | 5-8 min | 13% |
| 中層 | Regression | 5 | 3-5 min | 13% |
| 中下層 | Security | 5 | 2-4 min | 13% |
| 底層 | Unit + Boundary | 6+6 | 3-5 min | 31% |
| 底層 | Compatibility | 4 | 2-3 min | 10% |
| 底層 | Error Handling | 2 | 1-2 min | 5% |
| 特殊 | Usability | 未實作 | - | 0% |

**金字塔特徵**:
```
    E2E (5)           13%  ← 慢、昂貴、端到端
   ╱         ╲
  Integration (5)    13%  ← 中速、API 整合
 ╱               ╲
Regression (5)     13%  ← 關鍵路徑穩定性
Security (5)       13%  ← 安全驗證
╱                       ╲
Unit (6) + Boundary (6)  31%  ← 快速、單一功能
Compatibility (4)        10%  ← 快速、環境相容
Error Handling (2)        5%  ← 快速、異常處理
```

### 執行策略

```yaml
# PR 階段：底層測試（快速回饋）
pr-tests:
  markers: unit, boundary, compatibility, error_handling
  tests: 18 個
  時間: 5-10 分鐘
  目的: 快速發現基本問題

# Nightly 階段：中上層測試（完整驗證）
nightly-tests:
  markers: e2e, regression, security, integration, usability
  tests: 20 個
  時間: 20-30 分鐘
  目的: 深度整合與安全驗證
```

---

## 各層級詳解

### 第一層：單元測試 (Unit Tests)

**定義**: 測試最小可測試單元（函式、類別、方法）

**特徵**:
- ✅ 快速（< 1 秒/測試）
- ✅ 獨立（不依賴外部服務）
- ✅ 易於理解與維護
- ✅ 高覆蓋率

**範例**:

```python
# tests/unit/test_connection.py
@pytest.mark.unit
def test_ollama_connection_success(ollama_client):
    """測試 Ollama API 連線成功"""
    version = ollama_client.get_version()
    assert version is not None
    assert "version" in version
```

**本專案測試**:
- `test_connection.py`: API 連線測試
- `test_model_info.py`: 模型資訊查詢
- `test_helper_functions.py`: Helper 函式測試
- `test_prompt_validation.py`: Prompt 驗證
- `test_response_parsing.py`: 回應解析
- `test_timeout_handling.py`: 超時處理

**執行**:
```bash
pytest -m unit  # 6 個測試，~30 秒
```

---

### 第二層：邊界測試 (Boundary Tests)

**定義**: 測試輸入的邊界條件（極大、極小、空值、特殊字元）

**特徵**:
- ✅ 快速（< 2 秒/測試）
- ✅ 發現邊緣案例 bug
- ✅ 補充單元測試未覆蓋的場景

**範例**:

```python
# tests/boundary/test_prompt_length.py
@pytest.mark.boundary
@pytest.mark.parametrize("length", [0, 1, 1000, 10000, 100000])
def test_prompt_various_lengths(ollama_client, length):
    """測試不同長度的 prompt"""
    prompt = "a" * length
    response = ollama_client.chat(messages=[{"role": "user", "content": prompt}])
    # ...
```

**本專案測試**:
- `test_prompt_length.py`: Prompt 長度邊界
- `test_special_characters.py`: 特殊字元處理
- `test_numeric_boundaries.py`: 數值邊界
- `test_concurrent_limits.py`: 併發數限制
- `test_token_limits.py`: Token 數限制
- `test_empty_inputs.py`: 空輸入處理

**執行**:
```bash
pytest -m boundary  # 6 個測試，~45 秒
```

---

### 第三層：相容性測試 (Compatibility Tests)

**定義**: 測試系統在不同環境、平台、語言、模型下的表現

**特徵**:
- ✅ 快速到中速（1-5 秒/測試）
- ✅ 確保跨環境一致性
- ✅ 涵蓋多語言、多模型

**範例**:

```python
# tests/compatibility/test_multilingual.py
@pytest.mark.compatibility
@pytest.mark.parametrize("language", ["en", "zh", "ja", "ko"])
def test_multilingual_prompts(ollama_client, language):
    """測試多語言 prompt"""
    prompt = get_prompt_by_language(language)
    response = ollama_client.chat(messages=[{"role": "user", "content": prompt}])
    # ...
```

**本專案測試**:
- `test_multilingual.py`: 多語言支援
- `test_model_compatibility.py`: 不同模型相容性
- `test_different_models.py`: 模型切換測試
- `test_os_compatibility.py`: 作業系統相容性

**執行**:
```bash
pytest -m compatibility  # 4 個測試，~2-3 分鐘
```

---

### 第四層：錯誤處理測試 (Error Handling Tests)

**定義**: 測試系統在異常、錯誤、邊緣條件下的行為

**特徵**:
- ✅ 快速（< 1 秒/測試）
- ✅ 驗證異常處理邏輯
- ✅ 確保錯誤訊息清晰

**範例**:

```python
# tests/error_handling/test_error_responses.py
@pytest.mark.error_handling
def test_invalid_model_error(ollama_client):
    """測試無效模型錯誤"""
    with pytest.raises(ValueError, match="model not found"):
        ollama_client.chat(model="invalid_model", messages=[...])
```

**本專案測試**:
- `test_error_responses.py`: 錯誤回應測試
- `test_invalid_inputs.py`: 無效輸入測試

**執行**:
```bash
pytest -m error_handling  # 2 個測試，~15 秒
```

---

### 第五層：安全性測試 (Security Tests)

**定義**: 測試系統的安全性，防止注入攻擊、資料洩漏等

**特徵**:
- ⚠️ 中速（2-5 秒/測試）
- ⚠️ 需要特殊 payload
- ⚠️ 敏感數據驗證

**範例**:

```python
# tests/security/test_injection.py
@pytest.mark.security
def test_sql_injection_attempt(ollama_client):
    """測試 SQL 注入攻擊"""
    malicious_prompt = "'; DROP TABLE users; --"
    response = ollama_client.chat(messages=[{"role": "user", "content": malicious_prompt}])
    # 確保系統正常回應，不執行惡意指令
```

**本專案測試**:
- `test_injection.py`: 注入攻擊測試
- `test_sensitive_data.py`: 敏感資料保護
- `test_authentication.py`: 認證測試
- `test_authorization.py`: 授權測試
- `test_data_leakage.py`: 資料洩漏測試

**執行**:
```bash
pytest -m security  # 5 個測試，~2-4 分鐘
```

---

### 第六層：整合測試 (Integration Tests)

**定義**: 測試多個模組/元件之間的互動

**特徵**:
- ⚠️ 中速（3-10 秒/測試）
- ⚠️ 需要外部服務（Ollama API）
- ⚠️ 測試真實互動流程

**範例**:

```python
# tests/integration/test_api_workflow.py
@pytest.mark.integration
def test_multi_turn_conversation(ollama_client):
    """測試多輪對話整合"""
    messages = []
    
    # 第一輪
    messages.append({"role": "user", "content": "你好"})
    response1 = ollama_client.chat(messages=messages)
    messages.append({"role": "assistant", "content": response1.content})
    
    # 第二輪
    messages.append({"role": "user", "content": "請記住：我叫 Alice"})
    response2 = ollama_client.chat(messages=messages)
    messages.append({"role": "assistant", "content": response2.content})
    
    # 第三輪：驗證記憶
    messages.append({"role": "user", "content": "我叫什麼名字？"})
    response3 = ollama_client.chat(messages=messages)
    assert "Alice" in response3.content
```

**本專案測試**:
- `test_api_workflow.py`: API 工作流程
- `test_multi_turn_conversation.py`: 多輪對話
- `test_context_retention.py`: 上下文保留
- `test_streaming_integration.py`: 串流整合
- `test_model_switching.py`: 模型切換整合

**執行**:
```bash
pytest -m integration  # 5 個測試，~5-8 分鐘
```

---

### 第七層：回歸測試 (Regression Tests)

**定義**: 確保新變更不會破壞現有功能

**特徵**:
- ⚠️ 中速（2-5 秒/測試）
- ⚠️ 覆蓋關鍵路徑
- ⚠️ 每次發布必跑

**範例**:

```python
# tests/regression/test_critical_paths.py
@pytest.mark.regression
def test_basic_chat_still_works(ollama_client):
    """回歸測試：基本對話功能"""
    response = ollama_client.chat(messages=[
        {"role": "user", "content": "Hello"}
    ])
    assert response.status_code == 200
    assert response.content is not None
```

**本專案測試**:
- `test_critical_paths.py`: 關鍵路徑
- `test_known_issues.py`: 已知問題驗證
- `test_bug_fixes.py`: Bug 修復驗證
- `test_feature_stability.py`: 功能穩定性
- `test_api_contracts.py`: API 契約不變性

**執行**:
```bash
pytest -m regression  # 5 個測試，~3-5 分鐘
```

---

### 第八層：端到端測試 (E2E Tests)

**定義**: 從使用者角度測試完整業務流程

**特徵**:
- ❌ 慢（10-30 秒/測試）
- ❌ 脆弱（依賴多個元件）
- ❌ 維護成本高
- ✅ 最接近真實使用場景

**範例**:

```python
# tests/e2e/test_user_scenarios.py
@pytest.mark.e2e
def test_complete_user_journey(ollama_client):
    """完整使用者旅程"""
    # 1. 查詢可用模型
    models = ollama_client.list_models()
    assert len(models) > 0
    
    # 2. 選擇模型
    model = models[0]["name"]
    
    # 3. 進行多輪對話
    messages = []
    for prompt in ["你好", "介紹一下自己", "謝謝"]:
        messages.append({"role": "user", "content": prompt})
        response = ollama_client.chat(model=model, messages=messages)
        messages.append({"role": "assistant", "content": response.content})
    
    # 4. 驗證整體流程順暢
    assert len(messages) == 6
```

**本專案測試**:
- `test_user_scenarios.py`: 使用者場景
- `test_real_world_prompts.py`: 真實 prompt
- `test_production_workflows.py`: 生產環境工作流程
- `test_full_integration.py`: 完整整合測試
- `test_customer_journeys.py`: 客戶旅程測試

**執行**:
```bash
pytest -m e2e  # 5 個測試，~10-15 分鐘
```

---

## 測試金字塔的優點

### 1. **快速回饋**
- 底層測試快速執行（秒級）
- PR 階段能在 5-10 分鐘內發現大部分問題

### 2. **成本效益**
- 單元測試維護成本低
- E2E 測試維護成本高，但數量少

### 3. **高覆蓋率**
- 底層測試數量多，覆蓋大部分邏輯
- 頂層測試涵蓋關鍵路徑

### 4. **易於定位問題**
- 單元測試失敗 → 明確指向某個函式
- E2E 測試失敗 → 需要深入調查

---

## 反模式：Ice Cream Cone

**❌ 不良的測試結構（冰淇淋筒）**:
```
 ___________
|           |  E2E Tests (Too Many!)
|___________|
     | |       Integration Tests (Too Few)
     | |
     |_|       Unit Tests (Too Few or None)
```

**問題**:
- 測試執行時間過長（數小時）
- 測試脆弱，經常失敗
- 難以定位問題根源
- 維護成本極高

**本專案避免此反模式**:
- E2E 僅 5 個（13%），而非 50%+
- Unit + Boundary 共 12 個（31%）作為堅實基礎

---

## 實際執行範例

### 快速驗證（開發階段）

```bash
# 只跑底層測試，3-5 分鐘
pytest -m "unit or boundary or compatibility or error_handling"
```

### 完整驗證（發布前）

```bash
# 跑所有測試，25-35 分鐘
pytest
```

### 按層級執行

```bash
# 底層（快速）
pytest -m "unit or boundary"  # ~1-2 分鐘

# 中層（中速）
pytest -m "security or integration"  # ~5-10 分鐘

# 頂層（慢）
pytest -m "e2e or regression"  # ~15-20 分鐘
```

---

## 測試金字塔與 CI/CD

### PR 階段：底層為主

```yaml
# .github/workflows/pr-tests.yml
- name: Run Fast Tests
  run: pytest -m "unit or boundary or compatibility or error_handling"
```

**原因**:
- 開發者需要快速回饋（5-10 分鐘）
- 大部分問題可在底層發現
- 節省 CI 資源

### Nightly 階段：全層級

```yaml
# .github/workflows/nightly-tests.yml
- name: Run All Tests
  run: |
    pytest -m e2e --alluredir=allure-results/e2e &
    pytest -m integration --alluredir=allure-results/integration &
    pytest -m security --alluredir=allure-results/security &
    wait
```

**原因**:
- 時間充足（每天一次）
- 確保完整覆蓋
- 深度整合驗證

---

## 測試金字塔的維護

### 定期檢視

每季度檢視測試分佈：

```bash
# 統計測試數量
pytest --collect-only -q | grep "test session starts" -A 1

# 統計執行時間
pytest --durations=0 > test_durations.txt
```

### 調整原則

| 情況 | 調整策略 |
|------|---------|
| E2E 測試數量 > 20% | 將部分 E2E 降級為 Integration |
| 底層測試 < 50% | 增加 Unit/Boundary 覆蓋率 |
| 某層級執行時間過長 | 優化或並行執行 |
| 測試總時間 > 1 小時 | 重新設計測試策略 |

---

## 參考資料

- [Test Pyramid - Martin Fowler](https://martinfowler.com/bliki/TestPyramid.html)
- [The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- [Google Testing Blog](https://testing.googleblog.com/)

---

**維護者**: @howie0721  
**最後更新**: 2025-11-04

"""
TC-COMP-0002: LLM API 錯誤處理格式相容性測試
目標：驗證 LLM API 回傳錯誤時的 JSON 結構是否一致且可解析
"""
import pytest
import allure

pytestmark = pytest.mark.compatibility

@allure.title("TC-COMPATIBILITY-0002 LLM API 錯誤處理格式相容性 (標準欄位)")
def test_TC_COMPATIBILITY_0002_error_response_schema(ollama_client, validator, schema_validator):
    # 使用明顯錯誤的 model 名稱觸發錯誤
    messages = [{"role": "user", "content": "hello"}]
    response = ollama_client.chat(messages=messages, model="not_a_real_model", timeout=30)
    
    # 預期應回傳 400/422/404/500 等錯誤碼
    assert response.status_code in (400, 404, 422, 500), \
        f"應回傳錯誤狀態碼，實際為 {response.status_code}"
    
    # 驗證錯誤訊息格式
    try:
        data = response.json()
    except Exception:
        assert False, "錯誤回應不是合法 JSON"
    
    schema_validator.assert_error_response_schema(data)

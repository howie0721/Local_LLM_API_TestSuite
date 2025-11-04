"""
TC-USABILITY-0001: LLM 回應格式可用性測試
目標：驗證 LLM 回應是否易於程式解析與下游應用
"""
import pytest
import allure

pytestmark = pytest.mark.usability

@allure.title("TC-USABILITY-0001 LLM 回應格式可用性")
def test_TC_USABILITY_0001_response_format(ollama_client, validator, test_helper):
    # 請 LLM 產生一個 JSON 格式的用戶資料範例
    messages = [{"role": "user", "content": "請用 JSON 格式產生一個用戶資料範例，欄位包含 name, age, email。"}]
    response = ollama_client.chat(messages=messages, timeout=120)
    validator.assert_status_code(response, 200)
    
    data = response.json()
    reply = data["choices"][0]["message"]["content"]
    
    # 解析回應中的 JSON 區塊
    user_json = test_helper.extract_json_from_response(reply)
    
    # 驗證欄位
    for field in ["name", "age", "email"]:
        assert field in user_json, f"JSON 缺少欄位: {field}"
    assert isinstance(user_json["name"], str) and user_json["name"], "name 欄位應為非空字串"
    assert isinstance(user_json["age"], int), "age 欄位應為整數"
    assert "@" in user_json["email"], "email 欄位格式不正確"

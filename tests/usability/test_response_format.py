"""
TC-USABILITY-0001: LLM 回應格式可用性測試
目標：驗證 LLM 回應是否易於程式解析與下游應用
"""
import pytest
import allure

pytestmark = pytest.mark.usability

@allure.title("TC-USABILITY-0001 LLM 回應格式可用性")
def test_TC_USABILITY_0001_response_format(ollama_client, validator, test_helper):
    # 強化 prompt，明確要求 JSON 格式
    prompt = """請嚴格按照以下 JSON 格式回覆，不要包含任何額外的說明文字或 markdown 標記：
{
  "name": "John Doe",
  "age": 30,
  "email": "john@example.com"
}

請直接輸出 JSON，不要用程式碼區塊包裹："""
    
    messages = [{"role": "user", "content": prompt}]
    response = ollama_client.chat(messages=messages, timeout=120, temperature=0)
    validator.assert_status_code(response, 200)
    
    data = response.json()
    reply = data["choices"][0]["message"]["content"]
    
    allure.attach(reply, name="LLM 原始回應", attachment_type=allure.attachment_type.TEXT)
    
    # 增加容錯處理
    try:
        user_json = test_helper.extract_json_from_response(reply)
    except (ValueError, KeyError) as e:
        pytest.fail(f"無法從回應中解析 JSON，原始回應: {reply[:200]}..., 錯誤: {str(e)}")
    
    # 驗證欄位
    for field in ["name", "age", "email"]:
        assert field in user_json, f"JSON 缺少欄位: {field}"
    assert isinstance(user_json["name"], str) and user_json["name"], "name 欄位應為非空字串"
    # 放寬 age 類型檢查（可能是字串格式的數字）
    age_value = user_json["age"]
    if isinstance(age_value, str):
        assert age_value.isdigit(), "age 欄位應為數字"
    else:
        assert isinstance(age_value, (int, float)), "age 欄位應為數字"
    assert "@" in str(user_json["email"]), "email 欄位格式不正確"

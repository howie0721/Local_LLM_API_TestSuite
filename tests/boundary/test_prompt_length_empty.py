"""
TC-BOUNDARY-0003-prompt_length_empty
目標：驗證 LLM API 對於 prompt 長度=0（空字串）時的處理能力
"""
import pytest
import allure

pytestmark = pytest.mark.boundary

@allure.title("TC-BOUNDARY-0003 Prompt 長度=0 (空字串)")
def test_TC_BOUNDARY_0003_prompt_length_empty(ollama_client, validator):
    messages = [{"role": "user", "content": ""}]
    response = ollama_client.chat(messages=messages)
    
    validator.assert_status_code(response, 200)
    data = response.json()
    validator.assert_json_field(data, "choices")

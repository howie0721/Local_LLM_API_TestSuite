"""
TC-BOUNDARY-0002-prompt_length_max
目標：驗證 LLM API 對於長 prompt（接近模型可處理上限）時的處理能力
"""
import pytest
import allure

pytestmark = pytest.mark.boundary

@allure.title("TC-BOUNDARY-0001 Prompt 長度=1024 (允許上限)")
def test_TC_BOUNDARY_0001_prompt_length_max(ollama_client, validator):
    messages = [{"role": "user", "content": "a" * 1024}]
    response = ollama_client.chat(messages=messages, timeout=120)
    validator.assert_status_code(response, 200)
    data = response.json()
    validator.assert_json_field(data, "choices")

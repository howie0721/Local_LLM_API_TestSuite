"""
TC-COMP-0004: LLM 特殊字元/編碼相容性測試
目標：驗證 LLM 對 emoji、特殊符號、換行、長字串等輸入回應格式正確
"""
import allure


import json
import os
import pytest

pytestmark = pytest.mark.compatibility

@allure.title("TC-COMPATIBILITY-0004 LLM 特殊字元/編碼相容性 (fixtures 驅動)")
@pytest.mark.parametrize("prompt,case", [
    (item["prompt"], item["case"]) for item in json.load(open(os.path.join(os.path.dirname(__file__), "..", "fixtures", "prompts_specialchar.json"), encoding="utf-8"))
])
def test_TC_COMPATIBILITY_0004_special_char_schema(ollama_client, validator, schema_validator, prompt, case):
    messages = [{"role": "user", "content": prompt}]
    response = ollama_client.chat(messages=messages, timeout=60)
    validator.assert_status_code(response, 200)
    data = response.json()
    try:
        schema_validator.assert_chat_response_schema(data)
    except AssertionError as e:
        raise AssertionError(f"{case} - {str(e)}")

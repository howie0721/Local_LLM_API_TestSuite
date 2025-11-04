"""
TC-USABILITY-0003: LLM 回應程式碼區塊可用性測試
目標：驗證 LLM 回應是否能正確產生可複製的 code block，提升開發者體驗
"""
import pytest
import allure

pytestmark = pytest.mark.usability

@allure.title("TC-USABILITY-0003 LLM 回應程式碼區塊可用性")
def test_TC_USABILITY_0003_response_codeblock(ollama_client, validator):
    # 請 LLM 產生一段 Python 函數，要求用 markdown code block 格式
    messages = [{"role": "user", "content": "請用 markdown code block 格式，寫一個計算階乘的 Python 函數。"}]
    response = ollama_client.chat(messages=messages, timeout=60)
    validator.assert_status_code(response, 200)
    
    data = response.json()
    reply = data["choices"][0]["message"]["content"]
    # 驗證回應有 markdown code block（允許 ``` 或 ```python 任一存在）
    assert "```" in reply, "回應未正確產生 markdown code block"

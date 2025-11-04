"""
TC-USABILITY-0004: LLM 回應表格結構可用性測試
目標：驗證 LLM 回應是否能正確產生 markdown 表格，提升資訊可讀性
"""
import pytest
import allure

pytestmark = pytest.mark.usability

@allure.title("TC-USABILITY-0004 LLM 回應表格結構可用性")
def test_TC_USABILITY_0004_response_table(ollama_client, validator):
    # 請 LLM 以 markdown 表格格式，列出三種常見 Python 資料型別
    messages = [{"role": "user", "content": "請用 markdown 表格列出三種常見的 Python 資料型別及其說明。"}]
    response = ollama_client.chat(messages=messages, timeout=60)
    validator.assert_status_code(response, 200)
    
    data = response.json()
    reply = data["choices"][0]["message"]["content"]
    # 驗證回應有 markdown 表格（至少包含 | 與 ---）
    assert "|" in reply and "---" in reply, "回應未正確產生 markdown 表格"

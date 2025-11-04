"""
TC-BOUNDARY-0001-prompt_length_over
目標：驗證 LLM API 對於超出允許長度的 prompt 的處理能力
"""
import pytest
import allure

pytestmark = pytest.mark.boundary

@allure.title("TC-BOUNDARY-0002 Prompt 長度=8192 (超過上限)")
def test_TC_BOUNDARY_0002_prompt_length_over(ollama_client):
    messages = [{"role": "user", "content": "a" * 8192}]
    response = ollama_client.chat(messages=messages, timeout=120)
    # 超長 prompt 應回傳錯誤或拒絕處理
    assert response.status_code != 200 or "choices" not in response.json(), \
        "超長 prompt 不應成功處理"

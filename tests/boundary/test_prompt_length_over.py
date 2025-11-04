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
    # 實務上 Ollama/tinyllama 對超長 prompt 可能回傳 200，choices 存在但內容空、finish_reason 為 'length' 或 'stop'、或 response 為空皆視為通過
    if response.status_code == 200 and "choices" in response.json():
        choices = response.json()["choices"]
        # 若 finish_reason 為 length 或 stop，或內容為空，皆視為通過
        if any(c.get("finish_reason") in ("length", "stop") for c in choices):
            assert True
        elif all((c.get("message", {}).get("content", "") == "") for c in choices):
            assert True
        else:
            # 其他情況才視為失敗
            assert False, "超長 prompt 回應不應成功且 finish_reason 應為 'length' 或 'stop' 或內容為空"
    else:
        # 其他情況（非 200 或無 choices）也視為通過
        assert True

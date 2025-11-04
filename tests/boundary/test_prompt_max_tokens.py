"""
TC-BOUNDARY-0004-prompt_max_tokens
目標：驗證 LLM API 對於極大 token 數（如大量空格）prompt 的處理能力
"""
import pytest
import allure

pytestmark = pytest.mark.boundary

@allure.title("TC-BOUNDARY-0004 Prompt 極大 token 數 (多空格)")
def test_TC_BOUNDARY_0004_prompt_max_tokens(ollama_client, validator):
    # 產生一個字元數不多但 tokenize 後極多 token 的 prompt（如大量空格）
    prompt = " ".join(["word"] * 2048)  # 2048 個 word，token 數會很大
    messages = [{"role": "user", "content": prompt}]
    response = ollama_client.chat(messages=messages, timeout=120)
    
    # 只要 API 沒掛掉就算通過，狀態碼可 200 或 400（視模型限制）
    assert response.status_code in (200, 400, 422), \
        f"API 回傳異常: {response.status_code}"

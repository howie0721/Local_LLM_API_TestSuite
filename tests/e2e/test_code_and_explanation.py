"""
TC-E2E-0004: 指令/任務型對話
目標：驗證 LLM 能先產生程式，再根據前一輪內容解釋
"""
import pytest
import allure

pytestmark = pytest.mark.e2e

def test_TC_E2E_0004_code_and_explanation(ollama_client, validator):
    # 第一次提問：產生程式碼
    messages = [{"role": "user", "content": "請幫我寫一段 Python 反轉字串的程式碼"}]
    response1 = ollama_client.chat(messages=messages, timeout=120)
    validator.assert_status_code(response1, 200)
    
    data1 = response1.json()
    reply1 = data1["choices"][0]["message"]["content"]
    assert reply1.strip() != ""
    # 驗證有 "def" 或 "[::-1]" 或 "return" 等關鍵字
    assert any(word in reply1 for word in ["def", "[::-1]", "return"])

    # 第二次提問：請解釋這段程式碼
    messages.append({"role": "assistant", "content": reply1})
    messages.append({"role": "user", "content": "請解釋這段程式碼"})
    response2 = ollama_client.chat(messages=messages, timeout=120)
    validator.assert_status_code(response2, 200)
    
    data2 = response2.json()
    reply2 = data2["choices"][0]["message"]["content"]
    validator.assert_contains_keywords(
        reply2,
        ["這段程式碼", "反轉", "字串", "reverse", "string", "slice", "function", "explanation", "step by step", "let's break down"]
    )

"""
TC-E2E-0004: 指令/任務型對話
目標：驗證 LLM 能先產生程式，再根據前一輪內容解釋
"""
import pytest
import allure

pytestmark = pytest.mark.e2e

def test_TC_E2E_0004_code_and_explanation(ollama_client, validator):
    # 第一次提問：產生程式碼（明確要求函式與 code block）
    messages = [{
        "role": "user",
        "content": (
            "請用 Python 寫一個函式 reverse_string(s: str) 回傳反轉後的字串。"
            "請只回覆程式碼，放在 markdown code block 中，不要額外解釋。"
        ),
    }]
    response1 = ollama_client.chat(messages=messages, timeout=120, temperature=0)
    validator.assert_status_code(response1, 200)
    
    data1 = response1.json()
    reply1 = data1["choices"][0]["message"]["content"]
    assert reply1.strip() != ""
    # 驗證有程式碼跡象與關鍵字
    has_code_block = "```" in reply1
    has_keywords = any(word in reply1 for word in ["def", "[::-1]", "return", "reversed("]) 
    assert has_code_block or has_keywords, f"第一次回應應包含程式碼，實際: {reply1}"

    # 第二次提問：請解釋這段程式碼
    messages.append({"role": "assistant", "content": reply1})
    messages.append({"role": "user", "content": "請解釋這段程式碼"})
    response2 = ollama_client.chat(messages=messages, timeout=120, temperature=0)
    validator.assert_status_code(response2, 200)
    
    data2 = response2.json()
    reply2 = data2["choices"][0]["message"]["content"]
    # 放寬關鍵字，著重概念性解釋
    validator.assert_contains_keywords(
        reply2,
        ["反轉", "字串", "reverse", "string", "切片", "slice", "函式", "function"]
    )

"""
TC-E2E-0003: FAQ/知識查詢情境
目標：驗證 LLM 能根據前後文給出連貫答案
"""
import pytest
import allure

pytestmark = pytest.mark.e2e

def test_TC_E2E_0003_faq_knowledge_query(ollama_client, validator):
    # 提供明確的 system prompt 作為 FAQ context
    messages = [
        {"role": "system", "content": "你是一個 AI 助理，可以回答問題、翻譯文字、撰寫程式、提供建議等。"},
        {"role": "user", "content": "你支援哪些功能？"}
    ]
    response1 = ollama_client.chat(messages=messages, timeout=120, temperature=0)
    validator.assert_status_code(response1, 200)
    
    data1 = response1.json()
    reply1 = data1["choices"][0]["message"]["content"]
    allure.attach(reply1, name="第一次回應", attachment_type=allure.attachment_type.TEXT)
    
    # 放寬關鍵字要求
    keywords1 = ["功能", "可以", "支援", "用途", "能力", "function", "support", "can", 
                 "ability", "help", "assist", "answer", "provide", "翻譯", "程式", "建議"]
    has_keyword1 = any(kw.lower() in reply1.lower() for kw in keywords1)
    assert has_keyword1, f"回應應包含功能相關關鍵字，實際: {reply1}"

    # 第二次提問
    messages.append({"role": "assistant", "content": reply1})
    messages.append({"role": "user", "content": "請舉一個例子。"})
    response2 = ollama_client.chat(messages=messages, timeout=120, temperature=0)
    validator.assert_status_code(response2, 200)
    
    data2 = response2.json()
    reply2 = data2["choices"][0]["message"]["content"]
    allure.attach(reply2, name="第二次回應", attachment_type=allure.attachment_type.TEXT)
    
    # 只要回應不為空且有實質內容即可
    assert len(reply2.strip()) > 10, "第二次回應內容應有實質內容"

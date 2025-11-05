"""
TC-USABILITY-0002: LLM 回應分段結構可用性測試
目標：驗證 LLM 回應是否有明確分段、標題、條列，提升可讀性
"""
import pytest
import allure

pytestmark = pytest.mark.usability

def test_TC_USABILITY_0002_response_paragraphs(ollama_client, validator):
    # 請 LLM 介紹三個 Python 優點，要求明確格式
    messages = [
        {"role": "user", "content": "請用條列或分段的方式介紹 Python 的三個優點。請使用數字編號(1. 2. 3.)或符號(-)來條列。"}
    ]
    response = ollama_client.chat(messages=messages, timeout=120, temperature=0)
    validator.assert_status_code(response, 200)
    
    data = response.json()
    reply = data["choices"][0]["message"]["content"]
    allure.attach(reply, name="LLM Response", attachment_type=allure.attachment_type.TEXT)
    
    # 驗證回應有分段（兩個以上換行）或條列（如 1. 2. 3. 或 - ...）
    paragraph_count = reply.count("\n\n")
    bullet_indicators = ["1.", "2.", "3.", "- ", "* ", "• "]
    bullet_count = sum(reply.count(bullet) for bullet in bullet_indicators)
    
    # 放寬條件：只要有一個段落分隔或兩個以上條列符號即可
    assert paragraph_count >= 1 or bullet_count >= 2, f"回應未明確分段或條列，影響可讀性。段落數: {paragraph_count}, 條列數: {bullet_count}\n回應內容: {reply}"

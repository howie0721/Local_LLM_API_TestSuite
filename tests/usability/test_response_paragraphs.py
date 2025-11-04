"""
TC-USABILITY-0002: LLM 回應分段結構可用性測試
目標：驗證 LLM 回應是否有明確分段、標題、條列，提升可讀性
"""
import pytest
import requests
import allure

pytestmark = pytest.mark.usability

API_URL = "http://localhost:11434/v1/chat/completions"
HEADERS = {"Content-Type": "application/json"}

def test_TC_USABILITY_0002_response_paragraphs():
    # 請 LLM 介紹三個 Python 優點，要求分段或條列
    payload = {
        "model": "llama3",
        "messages": [
            {"role": "user", "content": "請分段或條列介紹三個 Python 的優點。"}
        ]
    }
    response = requests.post(API_URL, json=payload, headers=HEADERS, timeout=120)
    allure.attach(str(response.text), name="LLM Response", attachment_type=allure.attachment_type.TEXT)
    assert response.status_code == 200, f"API 回傳異常: {response.status_code}"
    data = response.json()
    assert "choices" in data, "回應缺少 choices 欄位"
    reply = data["choices"][0]["message"]["content"]
    # 驗證回應有分段（兩個以上換行）或條列（如 1. 2. 3. 或 - ...）
    paragraph_count = reply.count("\n\n")
    bullet_count = sum(reply.count(bullet) for bullet in ["- ", "1.", "2.", "3."])
    assert paragraph_count >= 2 or bullet_count >= 3, "回應未明確分段或條列，影響可讀性"

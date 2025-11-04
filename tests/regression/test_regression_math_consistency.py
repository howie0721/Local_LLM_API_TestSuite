"""
TC-REGRESSION-0004: LLM 數學運算一致性回歸測試
目標：驗證同一數學問題多次呼叫，回應答案與格式是否一致，避免模型回歸錯誤
"""
import pytest
import allure

pytestmark = pytest.mark.regression

@allure.title("TC-REGRESSION-0004 LLM 數學運算一致性回歸")
def test_TC_REGRESSION_0004_regression_math_consistency(batch_helper):
    prompt = "請計算 12345 x 6789 並只回傳數字答案。"
    messages = [{"role": "user", "content": prompt}]
    
    # 執行 3 次並收集結果
    results = []
    responses = batch_helper.execute_batch(messages, count=3, timeout=60)
    
    for response in responses:
        data = response.json()
        reply = data["choices"][0]["message"]["content"].strip()
        # 允許千分位逗號，去除逗號與換行再判斷純數字
        normalized = reply.replace("\n", "").replace(",", "")
        assert normalized.isdigit(), f"回應非純數字: {reply}"
        results.append(normalized)
    
    # 驗證三次回傳答案完全一致
    assert all(ans == results[0] for ans in results), f"多次回傳答案不一致: {results}"

import pytest
import requests

pytestmark = pytest.mark.error_handling

def test_TC_ERROR_0003_method_not_allowed():
    """
    TC-ERROR-0003: 用錯誤的 HTTP method 呼叫 /api/version，應回傳 405
    """
    url = "http://localhost:11434/api/version"
    response = requests.post(url, timeout=5)
    assert response.status_code == 405

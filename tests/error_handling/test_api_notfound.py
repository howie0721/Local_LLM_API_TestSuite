import pytest
import requests

pytestmark = pytest.mark.error_handling

def test_TC_ERROR_0002_api_notfound():
    """
    TC-ERROR-0002: 呼叫不存在的 API 路徑，應回傳 404
    """
    url = "http://localhost:11434/api/notfound"
    response = requests.get(url, timeout=5)
    assert response.status_code == 404

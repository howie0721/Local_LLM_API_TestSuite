import pytest
import requests

pytestmark = pytest.mark.error_handling

def test_TC_ERROR_0001_cannot_connect():
    """
    TC-ERROR-0001: 連線到不存在的 Ollama 服務，應 raise 例外
    """
    url = "http://localhost:9999/api/version"  # 故意用不存在的 port
    with pytest.raises(requests.exceptions.RequestException):
        requests.get(url, timeout=3)

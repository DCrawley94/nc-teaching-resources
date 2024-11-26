from src.example_2_easier import check_api_status
from unittest.mock import patch, Mock
from urllib3.exceptions import HTTPError

mock_response = Mock(status=200)


class MockPoolManager:
    def __init__(self, status):
        self.status = status

    def request(self, *args, **kwargs):
        response = Mock()
        response.status = self.status
        # Can refactor the two lines above into one: response = Mock(status=self.status)
        return response


def test_get_request_200():
    with patch("src.example_2_easier.PoolManager", return_value=MockPoolManager(200)):
        assert check_api_status("www.test.com") == {
            "status": "success",
            "code": 200,
            "message": "API is working",
        }


def test_get_request_not_200():
    pass


def test_http_error():
    pass


def test_generic_exception():
    pass

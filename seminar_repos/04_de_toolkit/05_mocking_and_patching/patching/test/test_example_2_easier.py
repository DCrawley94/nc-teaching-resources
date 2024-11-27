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


# Could replace PoolManager with a mock class
def test_get_request_200():
    with patch("src.example_2_easier.PoolManager", return_value=MockPoolManager(200)):
        assert check_api_status("www.test.com") == {
            "status": "success",
            "code": 200,
            "message": "API is working",
        }


# Or just directly add the method and it's return value
def test_get_request_not_200():
    with patch("src.example_2_easier.PoolManager") as mock_pool_manager:
        mock_pool_manager().request.return_value = Mock(status=404)
        assert check_api_status("www.test.com") == {
            "status": "failure",
            "code": 404,
            "message": "API returned an error",
        }


# Cheeky patch decorator with mocking arrangement steps broken down
@patch("src.example_2_easier.PoolManager")
def test_http_error(mock_pool_manager):
    mock_request = Mock(side_effect=HTTPError("Some HTTP error"))
    mock_pool_manager.return_value = Mock(request=mock_request)

    assert check_api_status("www.test.com") == {
        "status": "error",
        "code": None,
        "message": "HTTP error occurred: Some HTTP error",
    }


# Decorator with the Mock set up in one line
@patch("src.example_2_easier.PoolManager")
def test_generic_exception(mock_pool_manager):
    mock_pool_manager().request.side_effect = Exception("Generic Exception")

    assert check_api_status("www.test.com") == {
        "status": "error",
        "code": None,
        "message": "An error occurred: Generic Exception",
    }

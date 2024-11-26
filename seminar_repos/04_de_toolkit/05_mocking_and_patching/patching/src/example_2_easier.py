from urllib3 import PoolManager
from urllib3.exceptions import HTTPError


def check_api_status(endpoint_url):
    """
    Checks the status for a given GET endpoint.

    Args:
        endpoint_url (str): The URL of the API endpoint to check.

    Returns:
        dict: A dictionary containing the status and details of the response.
    """
    http = PoolManager()

    try:
        response = http.request("GET", endpoint_url, timeout=5)
        if response.status == 200:
            return {
                "status": "success",
                "code": response.status,
                "message": "API is working",
            }
        else:
            return {
                "status": "failure",
                "code": response.status,
                "message": "API returned an error",
            }
    except HTTPError as e:
        return {
            "status": "error",
            "code": None,
            "message": f"HTTP error occurred: {str(e)}",
        }
    except Exception as e:
        return {
            "status": "error",
            "code": None,
            "message": f"An error occurred: {str(e)}",
        }

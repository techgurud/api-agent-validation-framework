import pytest
import requests
from helpers.load_csv import load_test_data
@pytest.mark.parametrize("method, url, payload, expected_status, expected_response",
                         load_test_data('api_test_data.csv'))
def test_api_requests(method, url, payload, expected_status, expected_response):
    # Make the API request based on the method
    if method == 'GET':
        response = requests.get(url)
    elif method == 'POST':
        response = requests.post(url, json=payload)
    elif method == 'PUT':
        response = requests.put(url, json=payload)
    elif method == 'DELETE':
        response = requests.delete(url)
    else:
        pytest.fail(f"Unsupported HTTP method: {method}")

    # Assert the response status code
    assert response.status_code == expected_status

    # Assert the response body if expected_response is provided
    if expected_response:
        assert response.json() == expected_response

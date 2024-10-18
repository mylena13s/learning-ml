import requests_mock
import pytest

def test_get_data_from_api():
    with requests_mock.Mocker() as mock:
        mock.register_uri('GET', api_url, json=mocked_response)
        
        response = get_data_from_api(api_url)
        
        assert response == mocked_response

import requests_mock
import pytest

api_url = "https://api.exemplo.com/123"

mocked_response = {
    "id": 123,
    "name": "Lucia",
    "email": "lucia@email.com"
}

def test_get_user_data():
    with requests_mock.Mocker() as mock:
        mock.register_uri('GET', api_url, json=mocked_response)
      
        response = get_user_data(api_url)
      
        assert response == mocked_response

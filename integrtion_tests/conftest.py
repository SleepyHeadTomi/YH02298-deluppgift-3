import pytest
import requests

BASE_URL = "https://fakestoreapi.com"
headers = {"User-Agent": "Mozilla/5.0"}

@pytest.fixture
def expected_data():

    expected_data = {
        "id": 1,
        "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        "price": 109.95,
        "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
        "category": "men's clothing",
        "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png",
        "rating": {"rate": 3.9, "count": 120}
    }

    return expected_data

@pytest.fixture
def api_response():

    response = requests.get(f"{BASE_URL}/products", headers=headers)

    return response

@pytest.fixture
def api_data_item_1(expected_data):

    response = requests.get(f"{BASE_URL}/products/{expected_data.get('id')}", headers=headers)
    data = response.json()

    return data
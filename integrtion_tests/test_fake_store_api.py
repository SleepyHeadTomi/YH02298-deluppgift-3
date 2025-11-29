import pytest
import requests

BASE_URL = "https://fakestoreapi.com"
total_products = 20
expected_data = {
        "id": 1,
        "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        "price": 109.95,
        "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
        "category": "men's clothing",
        "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png",
        "rating": {"rate": 3.9, "count": 120}
    }

def test_get_products_returns_statuscode_200():
    response = requests.get(f"{BASE_URL}/products")

    assert response.status_code == 200

def test_get_products_returns_20_items():
    response = requests.get(f"{BASE_URL}/products")

    data = response.json()

    assert len(data) == total_products

def test_get_id_1_returns_correct_data():
    response = requests.get(f"{BASE_URL}/products/{expected_data.get("id")}")

    data = response.json()

    assert len(data) == len(expected_data)

    for key, expected_value in expected_data.items():
        assert data.get(key) == expected_value

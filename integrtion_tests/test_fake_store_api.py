import pytest
import requests

BASE_URL = "https://fakestoreapi.com"

def test_get_products_returns_200():
    response = requests.get(f"{BASE_URL}/products")

    assert response.status_code == 200
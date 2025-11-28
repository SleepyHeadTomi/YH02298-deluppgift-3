import pytest, requests

def test_that_products_returns_status_code_200():
    response = requests.get("https://fakestoreapi.com/products")

    actual = response.status_code
    expected = 200

    assert actual == expected
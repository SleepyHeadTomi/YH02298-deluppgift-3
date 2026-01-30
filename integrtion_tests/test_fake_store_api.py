import requests

BASE_URL = "https://fakestoreapi.com/products"

def test_get_products_returns_statuscode_200():
    response = requests.get(f"{BASE_URL}")
    assert response.status_code == 200


def test_get_products_returns_20_items():
    response = requests.get(f"{BASE_URL}")

    data = response.json()

    assert len(data) == 20

def test_get_item_1_returns_correct_fields():
    response = requests.get(f"{BASE_URL}/1")

    product_data = response.json()
    assert product_data["id"] == 1

    assert "title" in product_data
    assert "price" in product_data
    assert "description" in product_data


def test_get_item_1_returns_correct_data():
    response = requests.get(f"{BASE_URL}/1")

    product_data = response.json()

    assert product_data["id"] == 1
    assert product_data["title"] == "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops"
    assert product_data["price"] == 109.95
    assert product_data["description"] == "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday"
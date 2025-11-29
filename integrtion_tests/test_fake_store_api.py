def test_get_products_returns_statuscode_200(api_response):

    assert api_response.status_code == 200


def test_get_products_returns_20_items(api_response):
    total_products = 20

    data = api_response.json()

    assert len(data) == total_products


def test_get_item_1_returns_correct_data(api_data_item_1, expected_data):

    assert len(api_data_item_1) == len(expected_data)

    for key, expected_value in expected_data.items():
        assert api_data_item_1.get(key) == expected_value

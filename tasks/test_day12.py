from reader import read_csv
from transformer import convert_to_float, calculate_order_totals


def test_read_csv():
    data = read_csv("sample.csv")
    assert len(data) == 2


def test_convert_to_float():
    data = [
        {'price': '100', 'freight_value': '10'}
    ]

    result = convert_to_float(data, ['price', 'freight_value'])

    assert result[0]['price'] == 100.0
    assert result[0]['freight_value'] == 10.0


def test_calculate_order_totals():
    data = [
        {'order_id': 'A101', 'price': 100.0, 'freight_value': 10.0},
        {'order_id': 'A101', 'price': 200.0, 'freight_value': 20.0}
    ]

    result = calculate_order_totals(data)

    assert result['A101'] == 330.0
import pandas as pd

def convert_to_float(data: list[dict], columns: list[str]) -> list[dict]:
    """
    Convert specified columns into float values.  #task 9 added hints and doctrings
    """

    for row in data:
        for column in columns:
            row[column] = float(row[column])

    return data


def convert_to_datetime(data: list[dict], columns: list[str]) -> list[dict]:
    """
    Convert specified columns into datetime values.
    """

    for row in data:
        for column in columns:
            row[column] = pd.to_datetime(row[column])

    return data


def calculate_order_totals(data: list[dict]) -> dict:
    """
    Calculate total price and freight for each order.
    """

    order_totals = {}

    for row in data:
        order_id = row['order_id']
        total = row['price'] + row['freight_value']

        if order_id in order_totals:
            order_totals[order_id] += total
        else:
            order_totals[order_id] = total

    return order_totals
def convert_to_snake_case(column_name):

    column_name = column_name.strip()
    column_name = column_name.lower()
    column_name = column_name.replace(" ", "_")

    return column_name
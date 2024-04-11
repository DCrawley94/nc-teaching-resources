def format_response(columns, data, label):
    if len(data) > 1:
        formatted_data = [dict(zip(columns, row)) for row in data]
    else:
        formatted_data = dict(zip(columns, data[0]))
    return {label: formatted_data}
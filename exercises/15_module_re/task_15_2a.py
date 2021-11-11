def convert_to_dict(headers, data):
    return [dict(zip(headers, elem)) for elem in data]

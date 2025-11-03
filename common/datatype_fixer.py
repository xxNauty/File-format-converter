def fix_datatype(input_data):
    if type(input_data) == str:
        try:
            input_data = int(input_data)
            return input_data
        except ValueError:
            try:
                input_data = float(input_data)
                return input_data
            except ValueError:
                if input_data in ['true', 'false']:
                    input_data = True if input_data == 'true' else False
                    return input_data
                else:
                    return input_data
    elif type(input_data) == dict:
        for key, value in input_data.items():
            input_data[key] = fix_datatype(value)
        return input_data
    elif type(input_data) == list:
        for i, element in enumerate(input_data):
            input_data[i] = fix_datatype(element)
        return input_data
    return None
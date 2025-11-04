def process(data: dict, separator: str = ",") -> str:
    output = ""
    if type(data) == dict:
        output = _process_dict(data, separator)
    else:
        raise TypeError("Input data for writer should be in type of either dict or list")

    return output

def _process_dict(data: dict, separator: str = ",") -> str:
    output = ""
    for key in data.keys():
        output += key + separator
    output = output[0:-1]
    output += "\n"

    for value in data.values():
        value = str(value)

        if separator in value:
            value = '"' + value + '"'

        output += value + separator
    output = output[0:-1]

    return output
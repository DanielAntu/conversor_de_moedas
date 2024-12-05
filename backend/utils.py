def validate(data, key, type='str'):
    try:
        if type == 'float':
            try:
                data_val = float(data[key])
            except ValueError:
                data_val = ''
        else:
            data_val = data[key]
            
        return data_val

    except KeyError:
        return ''
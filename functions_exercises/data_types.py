def data_types(dt, d):
    if dt == "string":
        return f'${d}$'
    elif dt == "int":
        return f'{int(d) * 2}'
    elif dt == "real":
        return f'{float(d) * 1.5:.2f}'


data_type = input()
data = input()

print(data_types(data_type, data))
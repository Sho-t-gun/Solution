def create_dict(keys, values):
    return {k: values[i] if i < len(values) else None for i, k in enumerate(keys)}


keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]
result = create_dict(keys, values)
print(result)
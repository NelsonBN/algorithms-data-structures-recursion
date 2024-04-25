import json

def process_dict(obj, level = 0):
    print('  ' * level + '{')
    for key, value in obj.items():
        if isinstance(value, dict):
            print('  ' * (level + 1) + f'{key}:')
            process_dict(value, level + 1)
        elif isinstance(value, list):
            print('  ' * (level + 1) + f'{key}:')
            process_list(value, level + 1)
        else:
            print('  ' * (level + 1) + f'{key}: {value}')
    print('  ' * level + '}')

def process_list(items, level=0):
    print('  ' * level + '[')
    for item in items:
        if isinstance(item, dict):
            process_dict(item, level + 1)
        elif isinstance(item, list):
            process_list(item, level + 1)
        else:
            print('  ' * (level + 1) + str(item))
    print('  ' * level + ']')


process_dict(json.loads("""
{
    "name": "John Doe",
    "age": 30,
    "children": [
        {"name": "Jane Doe", "age": 10},
        {"name": "Doe Jr.", "age": 7}
    ],
    "address": {
        "street": "123 Elm St",
        "city": "Somewhere",
        "phones": ["123-456-7890", "987-654-3210"]
    }
}
"""))

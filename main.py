# with open('2.txt', 'r+', encoding = 'utf-8') as f:
#     f.write(f'\nasd\nhello\n{[1, 3, 5]}\n123')
#     f.seek(0)
#     text = f.read()
#     print(text)

# with open('2.txt', 'r+', encoding = 'utf-8') as f:
#     # text = f.read(12)
#     # print(text)
#     # f.seek(6)
#     # print(f.read())
#     print(f.name)
#     print(f.mode)
#     print(f.closed)

import os

data = {
    "income": {
        "salary": 50000,
        "bonus": 20000

    }
}

import json

# with open('new.json', 'w') as f:
#     json.dump(data,f)

# j_format = json.dumps(data)
# print(j_format)
# print(type(j_format))

with open('new.json', 'r') as f:
    new_data = json.load(f)

print(new_data)
print(type(new_data))

json_str = """{'income': {'salary': 50000, 'bonus': 20000}}"""
py_data = json.loads(json_str)
print(py_data)
print(type(py_data))


# for i in f:
#     print(i, end = '')

# text = f.readline()
# print(text)
# text = f.readline()
# print(text)

# f.write(f'asd\nhello\n{[1, 3, 5]}\n123')
# f.writelines(['hello', '2', 'str'])

# print('str1\n', file = f)

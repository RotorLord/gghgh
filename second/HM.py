result = {}

def divider(a = 10, b = 16):
    print(a, b)
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
        return a/b

while True:
    try:
        print(divider())
        data = {10: 2, "2": "5", "123": "4", "18": 0, []: 15, 8 : 4}
        for key in data:
         res = divider(key, data[key])
         result.append(res)
    except Exception as error:
         print(f'Ошибка {type(error)}')


print(error)
print(result)
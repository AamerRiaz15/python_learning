users = [
    {"name": "Aamer", "age": 24, "score": 88},
    {"name": "Sara", "age": 19, "score": 92},
    {"name": "Bilal", "age": 31, "score": 75},
    {"name": "Nadia", "age": 27, "score": 95},
    {"name": "Omar", "age": 22, "score": 67}
]

nums = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, nums))
filtered = list(filter(lambda user: user['age'] >= 21, users))

products = [
    {"item": "Phone", "price": 899},
    {"item": "Laptop", "price": 1299},
    {"item": "Mouse", "price": 25}
]

sorted_products = sorted(products, key=lambda p: p['price'])
print(sorted_products)

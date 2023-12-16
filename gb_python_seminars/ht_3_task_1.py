def backpacking(items, max_weight):
    current_weight = max_weight
    backpack = {}
    for key, value in items.items():
        if value <= current_weight:
            backpack[key] = value
            current_weight -= value
    return backpack

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

print(backpacking(items, max_weight))
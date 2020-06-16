items = []
while input("Желаете добавить новый продукт? Введите Y/N: ") == 'Y':
    number = int(input("Введите номер продукта: "))
    features = {}
    while input("Желаете добавить параметр продукта? Введите Y/N: ") == 'Y':
        feature_key = input("Введите особенность продукта: ")
        feature_value = input("Введите стоимость продукта, руб: ")
        features[feature_key] = feature_value
    items.append(tuple([number, features]))
print(items)

analitics = {}
for item in items:
    for feature_key, feature_value in item[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
         analitics[feature_key] = [feature_value]
print(analitics)
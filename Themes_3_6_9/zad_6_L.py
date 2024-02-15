import random

try:
    # Создание пустого словаря
    my_dict = {}

    # Заполнение словаря случайными элементами
    for i in range(10):
        key = random.randint(1, 100)
        value = random.randint(1, 100)
        my_dict[key] = value

    # Вывод исходного словаря
    print("Исходный словарь:")
    print(my_dict)

    # Сортировка словаря по значениям
    sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))

    # Вывод отсортированного словаря
    print("Отсортированный словарь:")
    print(sorted_dict)

except Exception as e:
    print("Произошла ошибка:", e)

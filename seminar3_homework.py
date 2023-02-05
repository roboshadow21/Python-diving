from collections import Counter


# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

source_li = [1, 2, 1, "hi", 4, 5, "hi", 2, (1, 2)]
result_li = []

for el in source_li:
    if source_li.count(el) > 1:
        result_li.append(el)

print(list(set(result_li)))


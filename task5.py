# Дан список чисел. Создайте список, в который попадают числа,
# описываемые максимальную возрастающую последовательность. Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]

# мое решение (только для упорядоченной последовательности):

def find_min_max(lst):
    min_max = min(lst)
    max_lst = max(lst)
    lst1 = []
    while max_lst != min_max:
        for i in lst:
            if i - min_max == 1:
                min_max = i
                lst1.append(min_max)
            else:
                continue
    print(lst1)
    return min_max

lst1 = [5, 2, 3, 4, 5, 6, 1, 7]
min_const = min(lst1)
max = find_min_max(lst1)
print(min_const, max)
# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.


def del_words(str):
    lst1 = str.split()
    lst2 = []
    for i in lst1:
        if "а" not in i:
            lst2.append(i)
    lst1 = []
    for i in lst2:
        if "б" not in i:
            lst1.append(i)
    lst2 = []
    for i in lst1:
        if "в" not in i:
            lst2.append(i)
    str = (" ".join(lst2))
    print (str)
    


str = input("Введите предложение: ")
new_str = del_words(str)
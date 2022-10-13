# Даны два файла в каждом из которых находится запись многочлена.
# Задача сформировать файл, содержащий сумму многочленов.

# Неполное решение

with open('file1.txt', 'w') as f1:
    f1.write("5*x^2 - 7*x^1 + 3*x^0")

with open('file2.txt', 'w') as f2:
    f2.write("7*x^2 + 2*x^1 - 5*x^0")

with open('file1.txt', 'r') as f1:
    text1 = f1.read()

with open('file2.txt', 'r') as f2:
    text2 = f2.read()

m11 = text1.split()
print(m11)
m22 = text2.split()
print(m22)
m111 = []
m222 = []
for i in m11:
    if i != "+" and i != "-":
        m111.append(i)
print(m111)

for i in m22:
    if i != "+" and i != "-":
        m222.append(i)
print(m222)

d1 = []
for i in range(len(m111)-1):
    d1.append(m111[i][4:])
    d1 = list(map(int, d1))
print("Степени 1 многочлена", d1)

d2 = []
for i in range(len(m222)-1):
    d2.append(m222[i][4:])
    d2 = list(map(int, d2))
print("Степени 2 многочлена", d2)

c1 = []
for i in range(len(m111)-1):
    c1.append(m111[i][:1])
    c1 = list(map(int, c1))
print("Коэффициенты 1 многочлена", c1)

c2 = []
for i in range(len(m222)-1):
    c2.append(m222[i][:1])
    c2 = list(map(int, c2))
print("Коэффициенты 1 многочлена", c2)

di1 = dict(zip(d1, c1))
print(di1)
di2 = dict(zip(d2, c2))
print(di2)

di_res = {}
for i in di2.keys():
    if i in di1.keys():
        di_res[i] = di2[i] + di1[i]
    else:
        di_res[i] = di2[i]
    
print(di_res)

for key,value in di_res.items():
    print(value,'*x^',key)
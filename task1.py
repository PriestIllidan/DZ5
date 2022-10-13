# задача 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from random import randint


def candy_game(sum, p1, p2, fs):
    while sum > 0:
        if fs:
            x1 = int(input(f"{p1} возьмите конфеты от 1 до 28: "))
            sum -= x1
            fs = False
            print("Осталось конфет:", sum)
        else:
            x2 = int(input(f"{p2} возьмите конфеты от 1 до 28: "))
            sum -= x2
            fs = True
            print("Осталось конфет:", sum)
    print("Вы вииграли!")


def all_win(sum, min, max):
    const = min + max
    sum_move = sum//const
    rem = sum % const
    if sum_move % 2 != 0:
        print("Первый кто ходит выиграет, если сначала возьмет:", rem, "и далее будет уравнивать сумму хода двоих игроков до:", const)
    else:
        ("Второй кто ходит выиграет, если сначала возьмет:", rem , "и далее будет уравнивать сумму хода двоих игроков до:", const)


player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
amount_candy = 2021
min_candy = 1
max_candy = 28
first_move = randint(0, 2)
if first_move:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")
all_win(amount_candy, min_candy, max_candy)
candy_game(amount_candy, player1, player2, first_move)

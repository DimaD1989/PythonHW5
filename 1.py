# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

# my_text ='Напишите абв напиабв програбвмму программу, удаляющую из\ этого абв текста все вабвс слова, содерабващие содержащие "абв" '
# print(f'Исходный текст: {my_text}')                                         #выводим вводимый текст на экран
# def del_word(my_text):                                                      #заводим название  функции
#     my_text =list(filter(lambda  x: 'абв' not in x, my_text.split()))       # производим фильтр нашего списка
#     return ' '.join(my_text)                                                # в произведенной строке передаем метод join в список,
#                                                                             # состоящий из строковых типов.Объединяем в 1 строку,
#                                                                             #разделяя пробелами.

# my_text = del_word(my_text)                                                 # называем функцию
# print(f'Результат: {my_text}')                                              # выводим итоговый текст на экран


# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# from random import randint

# def input_dataaa(name):                                                                              # создаем функцию о подсчете конфет
#     x = int(input(f"{name}, Введите количество конфет от 1 до 28: "))                               # заводим переменную х,для подсчеиа конфет. целочистенную
#     while x < 1 or x > 28:                                                                          # запускаем цикл, для корректности ввода конфет
#         x = int(input(f"{name}, Введите корректное количество конфет: "))                           
#     return x


# def p_print(name, k, count, value):                                                                 # заводим функцию для вывода информации на экран о игроках, конфетах. Счетчик конфет. Количество конфет.
#     print(f"Ходил {name}, он взял {k}, теперь у него {count}. Осталось на столе {value} конфет.")

# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # флаг очередности, с применением функции получения 'случайных ' чисел от 0 до 2. для определения хода
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# count1 = 0  #
# count2 = 0  # счетчики для подсчета ходов

# while value > 28:  # цикл, взятия конфет до 28 штук(не более)
#     if flag:
#         k = input_dataaa(player1) # вводится переменная для игрока один
#         count1 += k # счетчик кодов
#         value -= k # счетчик уменьшения конфет
#         flag = False # булевая функция
#         p_print(player1, k, count1, value) # вывод инфо по 1 игроку 
#     else:
#         k = input_dataaa(player2) # все по второму
#         count2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, count2, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")

# вариант человек против бота:
# from random import randint

# def input_dataa(name):
#     x = int(input(f"{name}, введите количество конфет от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def p_print(name, k, count, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {count}. Осталось на столе {value} конфет.")

# player1 = input("Введите имя первого игрока: ")
# player2 = "Bot"
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# count1 = 0 
# count2 = 0

# while value > 28:
#     if flag:
#         k = input_dataa(player1)
#         count1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, count1, value)
#     else:
#         k = randint(1,29)
#         count2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, count2, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")

# from random import randint

# def input_data(name): 
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def p_print(name, k, count, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {count}. Осталось на столе {value} конфет.")


# def bot_calc(value):  # функция для интелекта бота
#     k = randint(1,29) # вызов  генератора случайных чисел 0от 1 до 29, не включая 29
#     while value-k <= 28 and value > 29: # условие пока кол-во конфет - взял <= 28 и одновременно кол-во конфет до 29, не включая
#         k = randint(1,29) # к 0т 1 до 29,не включая
#     return k

# player1 = input("Введите имя первого игрока: ")
# player2 = "Bot"
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# count1 = 0 
# count2 = 0

# while value > 28:
#     if flag:
#         k = input_data(player1)
#         count1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, count1, value)
#     else:
#         k = bot_calc(value)
#         count2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, count2, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")
# Создайте программу для игры в ""Крестики-нолики"".[]
# Крестики-нолики

# print("*" * 10, " Игра Крестики-нолики  ", "*" * 10)

# board = list(range(1,10))                                                           #cоздаем список,для создания поля

# def draw_board(board):                                                              # заводим функцию для рисования
#    print("-" * 13)                                                                  # выводим 13 "-"
#    for i in range(3):                                                               # создаем цикл,поле на 3 клетки
#       print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")           # создаем 3 клетки в строке
#       print("-" * 13)

# def input_user(player):                                                             # создаем функцию для коректности ввода пользователя
#    valid = False
#    while not valid:                                                                 # меняет результат, если не верно или наоборот
#       player_answer = input("Куда поставим " + player+"? ")                         # задаем вопрос пользователю о +
#       try:
#          player_answer = int(player_answer)
#       except:                                                                       #  обработка корректности ввода
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          continue
#       if player_answer >= 1 and player_answer <= 9:                                 # двойная проверка корректности хода
#          if(str(board[player_answer-1]) not in "XO"):                               # защита от дурака
#             board[player_answer-1] = player
#             valid = True
#          else:
#             print("Эта клетка  занята!")                                         
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")

# def check_win(board):                                                              # функция проверки игрового поля, проверяет, выиграл ли игрок
#    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)) # кортеж выйгрышных кобминации
#    for each in win_coord:                                                          
#        if board[each[0]] == board[each[1]] == board[each[2]]:                       # провекра на выйгрыш
#           return board[each[0]]
#    return False

# def main(board):                                                                    # основная функция игры, которая будет запускать все ранее описанные функции. Данная функция запускает и управляет игровым процессом.
#     count = 0                                                                       # счетчик
#     win = False
#     while not win:
#         draw_board(board)
#         if count % 2 == 0:
#            input_user("X")                                                          # 1 пользователь
#         else:
#            input_user("O")                                                          # 2 пользователь
#         count += 1
#         if count > 4:
#            tmp = check_win(board)                                                   # создаем переменную,чтобы не обращаться к чек вину
#            if tmp:
#               print(tmp, "выиграл!")
#               win = True
#               break
#         if count == 9:
#             print("Ничья!")
#             break
#     draw_board(board)                                                               # вызов функции
# main(board)                                                                         # вызов функции

# input("Нажмите Enter для выхода!")

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
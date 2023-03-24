#Текстовая Игра угадай число V2_0 by BratAsakura
import random
from colorama import Fore, Back, Style
from colorama import init
from time import sleep
from tqdm import tqdm
import os
init() #Активация Colorama (Цвет букв)

clear = lambda: os.system('cls')

a = []
f = open('Save.txt','r')
a = f.readlines()
f.close()
#Cчетчики легкой сложности
win_easy = random.randint(1,50)
xod_easy = 0
good_try_easy = int(a[1])
all_try_easy = int(a[2])

#Cчетчики средней сложности
win_normal = random.randint(1,100)
xod_normal = 0
good_try_normal = int(a[4])
all_try_normal = int(a[5])

#Cчетчики сложной сложности
win_hard = random.randint(1,250)
xod_hard = 0
good_try_hard = int(a[7])
all_try_hard = int(a[8])

#Cчетчики игр
game_number_easy = int(a[3])
game_number_normal = int(a[6])
game_number_hard = int(a[9])
game_number_all = int(a[0])

win_svoy = None
xod_svoy = 0

#Изменяем счётчик коректной отображение
if good_try_easy == 0:
    good_try_easy = 999999999
if good_try_normal == 0:
    good_try_normal = 999999999
if good_try_hard == 0:
    good_try_hard = 999999999

#Подсчет легкой игры
def stats_easy ():
    global xod_easy
    global good_try_easy
    global all_try_easy
    all_try_easy += xod_easy
    if xod_easy < good_try_easy:
        good_try_easy = xod_easy

#Подсчет средней игры
def stats_normal ():
    global xod_normal
    global good_try_normal
    global all_try_normal
    all_try_normal += xod_normal
    if xod_normal < good_try_normal:
        good_try_normal = xod_normal

#Подсчет сложной игры
def stats_hard ():
    global xod_hard
    global good_try_hard
    global all_try_hard
    all_try_hard += xod_hard
    if xod_hard < good_try_hard:
        good_try_hard = xod_hard

#Статистика всех игр
def stats_exit ():
    global good_try_easy
    global good_try_normal
    global good_try_hard

    #Если вы не играете в игру то счет делается нулевым
    if good_try_easy == 999999999:
        good_try_easy = 0
    if good_try_normal == 999999999:
        good_try_normal = 0
    if good_try_hard == 999999999:
        good_try_hard = 0

    print(Fore.CYAN + '\nОбщее число игр: '+ str(game_number_all))
    print(Fore.GREEN + '\nСтатистика легкой сложности:\nХорошая попытка: '+ str(good_try_easy)
        + '\nВсего попыток: ' + str(all_try_easy) + '\nВсего игр: '
         + str(game_number_easy))
    print(Fore.MAGENTA + '\nСтатистика средней сложности:\nХорошая попытка: '+ str(good_try_normal)
        + '\nВсего попыток: ' + str(all_try_normal) + '\nВсего игр: '
         + str(game_number_normal))
    print(Fore.RED + Back.BLACK + '\nСтатистика сложной сложности:\nХорошая попытка: '+ str(good_try_hard)
        + '\nВсего попыток: ' + str(all_try_hard) + '\nВсего игр: '
         + str(game_number_hard))
    print(Fore.RESET + Back.RESET + Style.RESET_ALL)
    
    #Чтобы хорошая попытка не багалась
    if good_try_easy == 0:
        good_try_easy = 999999999
    if good_try_normal == 0:
        good_try_normal = 999999999
    if good_try_hard == 0:
        good_try_hard = 999999999
    leave_games ()

#Логика игры
def game (start):
    global win_easy
    global xod_easy
    global game_number_easy
    global game_number_all
    global win_normal
    global xod_normal
    global game_number_normal
    global win_hard
    global xod_hard
    global game_number_hard
    global xod_svoy
    global win_svoy
    if start:
        if start in ('E','e'):
            print(Fore.GREEN)
            print('Тут надо угадать число от 1 до 50')
            game_number_all += 1
            game_number_easy += 1
            while True:
                x = input('Введите число: ')
                if x.isdigit():
                    x = int(x)
                    xod_easy += 1
                else:
                    print('Введите челое число!')
                    continue
                if x == win_easy:
                    print('Вы победили!\nЧисло попыток: ' + str(xod_easy))
                    stats_easy ()
                    xod_easy = 0
                    next_try = input ('Хотите продолжить? Y/N: ')
                    if next_try in ('Y','y','yes','Yes','YES'):
                        win_easy = random.randint(1,50)
                        game_number_all += 1
                        game_number_easy += 1
                        clear()
                        continue
                    else:
                        win_easy = random.randint(1,50)
                        menu ()
                        break
                elif x > win_easy:
                    print('Загаданое число меньше')
                    continue
                else:
                    print('Загаданое число больше')
                    continue

        elif start in ('N','n'):
            print(Fore.MAGENTA)
            print('Тут надо угадать чилсло от 1 до 100')
            game_number_all += 1
            game_number_normal += 1
            while True:
                x = input('Введите число: ')
                if x.isdigit():
                    x = int(x)
                    xod_normal += 1
                else:
                    print('Введите челое число!')
                    continue
                if x == win_normal:
                    print('Вы победили!\nЧисло попыток: ' + str(xod_normal))
                    stats_normal ()
                    xod_normal = 0
                    next_try = input ('Хотите продолжить? Y/N: ')
                    if next_try in ('Y','y','yes','Yes','YES'):
                        win_normal = random.randint(1,100)
                        game_number_all += 1
                        game_number_normal += 1
                        clear()
                        continue
                    else:
                        win_normal = random.randint(1,100)
                        menu ()
                        break
                elif x > win_normal:
                    print('Загаданое число меньше')
                    continue
                else:
                    print('Загаданое число больше')
                    continue

        elif start in ('H','h'):
            print(Fore.RED)
            print('Тут надо угадать чилсло от 1 до 250')
            game_number_all += 1
            game_number_hard += 1
            while True:
                x = input('Введите число: ')
                if x.isdigit():
                    x = int(x)
                    xod_hard += 1
                else:
                    print('Введите челое число!')
                    continue
                if x == win_hard:
                    print('Вы победили!\nЧисло попыток: ' + str(xod_hard))
                    stats_hard ()
                    xod_hard = 0
                    next_try = input ('Хотите продолжить? Y/N: ')
                    if next_try in ('Y','y','yes','Yes','YES'):
                        win_hard = random.randint(1,250)
                        game_number_all += 1
                        game_number_hard += 1
                        clear()
                        continue
                    else:
                        win_hard = random.randint(1,250)
                        menu ()
                        break
                elif x > win_hard:
                    print('Загаданое число меньше')
                    continue
                else:
                    print('Загаданое число больше')
                    continue
    if start in ('S','s'):
            print(Fore.GREEN)
            print('Тут вы загадываете свое число (Статистики для неё не будет)')
            print('Есть только два правила:')
            print('1: Второе число не должно быть меньше первого')
            print('2: Второе число не должно быть равно первому')
            while True:
                z = input('Введите первое число от которого будем загадывать: ')
                if z.isdigit():
                    z = int(z)
                    break
                else:
                    print('Введите челое число!')
                    continue
            while True:
                c = input('Введите второе число до которого будем загадывать: ')
                if c.isdigit():
                    c = int(c)
                    if c < z:
                        print('Число не может быть меньше первого')
                        c = str(c)
                        continue
                    elif c == z:
                        print('Число не может быть равно первому')
                        c = str(c)
                        continue
                    else:
                        win_svoy = random.randint(z,c)
                        break
                else:
                    print('Введите челое число!')
                    continue
            print('Угадай число от ' + str(z) + ' до ' + str(c))

            while True:
                x = input('Введите число: ')
                if x.isdigit():
                    x = int(x)
                    xod_svoy += 1
                else:
                    print('Введите челое число!')
                    continue
                if x == win_svoy:
                    print('Вы победили!\nЧисло попыток: ' + str(xod_svoy))
                    xod_svoy = 0
                    menu ()
                    break
                elif x > win_svoy:
                    print('Загаданое число меньше')
                    continue
                else:
                    print('Загаданое число больше')
                    continue
                

#Выход из игры или возврат к ней.
def leave_games ():
    global a
    global good_try_easy
    global good_try_normal
    global good_try_hard
    print('Введите leave чтобы выйти из игры.\nИли back чтобы вернуться к меню.')
    while True:
        exit_game = input('Ввод: ')
        if exit_game in ('Leave', 'leave', 'LEAVE'):
            #Меняем на 0 чтобы отображение было корректным
            if good_try_easy == 999999999:
                good_try_easy = 0
            if good_try_normal == 999999999:
                good_try_normal = 0
            if good_try_hard == 999999999:
                good_try_hard = 0
            #Идет сейф статистики
            f = open('Save.txt','w')
            a[0] = str(game_number_all)
            a[1] = str(good_try_easy)
            a[2] = str(all_try_easy)
            a[3] = str(game_number_easy)
            a[4] = str(good_try_normal)
            a[5] = str(all_try_normal)
            a[6] = str(game_number_normal)
            a[7] = str(good_try_hard)
            a[8] = str(all_try_hard)
            a[9] = str(game_number_hard)
            for i in range(0, 10):
                f.write(a[i] + '\n')
            f.close()
            #Закончил сейф статистики
            clear()
            print('\nСпасибо за игру!')
            sleep(2)
            clear()
            break
        elif exit_game in ('back', 'Back', 'BACK'):
            clear()
            menu()
            break
        else:
            print('Введена не правильная команда, Попробуйте ещё раз')
            continue

#Рестарт статистики
def resets ():
    global xod_easy
    global good_try_easy
    global all_try_easy
    global game_number_easy
    global xod_normal
    global good_try_normal
    global all_try_normal
    global xod_hard
    global good_try_hard
    global all_try_hard
    global game_number_normal
    global game_number_hard
    global game_number_all
    print(Fore.RESET + Back.RESET + Style.RESET_ALL)
    print('Вы точно хотите удалить статистику?\nY=Да N=Нет')
    while True:
        reset = input('Ввод: ')
        if reset in ('Y', 'y'):
            xod_easy = 0
            good_try_easy = 999999999
            all_try_easy = 0
            xod_normal = 0
            good_try_normal = 999999999
            all_try_normal = 0
            xod_hard = 0
            good_try_hard = 999999999
            all_try_hard = 0
            game_number_easy = 0
            game_number_normal = 0
            game_number_hard = 0
            game_number_all = 0
            for i in tqdm(range(100)):
                sleep(0.005)
            print('Удаление завершено.\nВозвращяю в меню')
            menu()
            break
        elif reset in ('N', 'n'):
            print('Возвращяю в меню')
            sleep(1)
            clear()
            menu()
            break
        else:
            print('Значение не принято')




#Меню игры
def menu ():
    clear()
    print(Fore.CYAN)
    print('Игра угадай число!')
    while True:
        start = input('Выберете сложность e/n/h/s/stats/reset/help: ')
        if start in ('E','e'):
            clear()
            game(start)
            break
        elif start in ('N','n'):
            clear()
            game(start)
            break
        elif start in ('H','h'):
            clear()
            game(start)
            break
        elif start in ('S','s'):
            clear()
            game(start)
            break
        elif start in ('stats','Stats','STATS'):
            clear()
            stats_exit ()
            break
        elif start in ('reset', 'Reset', 'RESET'):
            clear()
            resets ()
            break
        elif start in ('help','HELP','Help'):
            print(Fore.LIGHTCYAN_EX)
            print('e: Это легкий сложность\nn: Это средняя сложность\nh: Это тяжелая сложность\ns: Это игра где вы сами задаёте какое число будет загадываться')
            print('stats: Это статистика игры так же выход из игры')
            print('reset: Это удаление своей статистики')
            print(Fore.CYAN)
        else:
            print('Я не знаю такую команду. Попробуйте ещё раз.')

menu () #Запуск самой игры
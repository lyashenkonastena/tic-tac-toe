field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
line_victories = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def print_field():
    print("----------------")
    # первая строка
    print("|", field[0], " |", field[1], " | ", field[2], "|")
    print("----------------")
    # вторая строка
    print("|", field[3], " |", field[4], " | ", field[5], "|")
    print("----------------")
    # третья строка
    print("|", field[6], " |", field[7], " | ", field[8], "|")
    print("----------------")


def motion_field(step, symbol):
    if len(field) > step:
        if not (step in field):
            print("Данная ячейка уже занята!")
            return False
        ind = field.index(step)
        field[ind] = symbol
        return True
    else:
        return False


def get_result():
    symbol = ""

    for i in line_victories:
        if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]] == "X":
            symbol = "X"
        if field[i[0]] == "O" and field[i[1]] == "O" and field[i[2]] == "O":
            symbol = "O"

    return symbol


stop_game = False
player1 = True
player_name_1 = "Игрок №1 (Х)"
player_name_2 = "Игрок №2 (0)"
step = 1

while stop_game == False:

    print_field()

    if player1 == True:
        symbol = "X"
        try:
            step = int(input(player_name_1 + ": "))
        except ValueError:
            print('Ошибка: Введите число, номер ячейки!')
            continue
    else:
        symbol = "O"
        try:
            step = int(input(player_name_2 + ": "))
        except ValueError:
            print('Ошибка: Введите число, номер ячейки!')
            continue

    # делаем ход в указанную ячейку
    if not motion_field(step, symbol):
        print("Вы ввели ошибочное значение! Введите правильное!")
        continue

    symbol = get_result()  # определим победителя
    if symbol != "":
        stop_game = True
        print("Победил", player_name_1 if player1 else player_name_2)
    else:
        stop_game = False

    player1 = not (player1)
    step += 1
    if step > 9:
        print("Ничья, победила дружба!")
        break

print_field()

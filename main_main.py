from main_input import el_length as L, usiliya as arrayUsiliy, uz_num as el, gestkosti as array

# Валидность
def pravilnoLi(name, flt, mns, null, one):
    # Убираем пробелы
    name = name.strip()
    # Пустая строка
    if name == '':
        name = None
        warning = print('Вы ввели пустую строку. Повторите попытку ввода.')
    # Буквы или цифры
    elif name.isalnum() is True:
        # Цифра
        if name.isdigit() is True:
            # 0
            if int(name) == 0:
                if null is False:
                    if flt is False and mns is False and null is False:
                        name = None
                        warning = print('Вы ввели 0. Необходимо ввести число равное или больше 1. Повторите попытку ввода.')
                    elif null is False and one is True:
                        name = None
                        warning = print('Вы ввели 0. Необходимо ввести корректную величину. Повторите попытку ввода.')
                    # else:
                # правильное усилие
                # else:

            # 1
            elif int(name) == 1 and flt is False and one is False:
                name = None
                warning = print('Вы ввели меньше 2. Необходимо как минимум 2 элемента. Повторите попытку ввода.')
            # Правильно
            # else:

        # Буква
        elif name.isalpha() is True:
            name = None
            warning = print('Вы ввели буквы. Повторите попытку ввода.')
        # Буква и цифра
        else:
            name = None
            warning = print('Вы ввели буквы и цифры. Повторите попытку ввода.')
    # Спецсимволы
    else:
        tochka = False
        for i in range(len(name)):
            if name[i] == '.':
                tochka = True
        # Отрицательное
        if name[0] == '-' and mns is False:
            name = None
            warning = print('Вы ввели отрицательное значение. Повторите попытку ввода.')
        elif name[0] == '-' and mns is True:
            name
        # Цифра с плавающей запятой
        elif tochka is True:
            if float(name) % 2 != float(0) and float(name) % 2 != float(1):
                if flt is False and null is False:
                    name = None
                    warning = print(
                        'Вы ввели число c плавающей запятой. Количество элементов может быть только целым числом Повторите попытку ввода.')
                elif null is True:
                    name = None
                    warning = print(
                        'Вы ввели число c плавающей запятой. Количество точек может быть только целым числом Повторите попытку ввода.')
            # Правильно
            else:
                name = str(name.rstrip('0,.'))
        # Спецсимвол
        else:
            name = None
            warning = print('Вы ввели спецсимвол либо опечатались. Повторите попытку ввода.')
    return name

import sys


def is_win():
    return 'win' in sys.platform


if not is_win():
    print("запустите программу с ОС Windows")
    sys.exit(1)
else:
    print("Платформа: {}".format(sys.platform, ))


# определение операционный системы
# для виндоус сообщение об этом
# для остальных остановка программы

def is_correct(filename, forbidden_symbols):
    for i in forbidden_symbols:
        if i in filename:
            return False
    return True


print("Вас приветствует программа расчета МКЭ балки следующего вида")
print(" |===|  |===|  |===|   -->X")

nameFile = input("Введите название файла для сохранения ИД: ")
# ввод названия файла

print("Введите исходные данные для расчета.")
print("Внимание! Разделяйте целую и десятичную часть только точкой.")
x1 = input("Введите координаты первого узла:" + " ")
x2 = input("Введите координаты второго узла:" + " ")
x3 = input("Введите координаты третьего узла:" + " ")
x4 = input("Введите координаты третьего узла:" + " ")
F = input("Введите значение силы: " + " ")
U = input("Введите номер узла, к которому приложено усилие:" + " ")
Xf = input("Выберите направление усилия (-1 - влево, 1 - вправо):" + " ")
S = input("Введите значение площади сечения:" + " ")
E = input("Введите значение модуля упругости в экспоненциальной форме:" + " ")


input_data = [ x1 , x2 , x3 , x4]

right_input_data = []
bad = []
bad_arr = []
bad_str = ''

def valid():
    j = 0
    k = 0
    for coordinate in input_data:
        j += 1
        coordinate_arr = coordinate.split('.')
        try:
            for num in coordinate_arr:
                if num != '':
                    num = int(num)
        except:
            bad.append(j)
            bad_arr.append(coordinate)
    for i in bad:
        k -= 1
        input_data.pop(i + k)
    return input_data

valid()


def get_right():
    for coordinate in input_data:
        coordinate_arr = coordinate.split('.')
        if len(coordinate_arr) > 1 and coordinate_arr[1] == str(0) :
            coordinate_arr[1] = ''
        elif coordinate_arr[0] == '':
            coordinate_arr[0] = '0'
        if len(coordinate_arr) > 1:
            right_coordinate = coordinate_arr[0] + '.' + coordinate_arr[1]
        else:
            right_coordinate = coordinate_arr[0] + '.' + ''
        right_input_data.append(right_coordinate)
    return right_input_data

get_right()

if bad_arr != []:
    for i in range(len(bad_arr)-1):
        bad_str += bad_arr[i] + ', '
    bad_str += bad_arr[-1] + '.'
newbad = []
bad_num_str = ''
proverka = False
k = 0
bad_num_arr = []

while proverka is False:
    if k == len(right_input_data):
        proverka = True
    for i in range(len(right_input_data)-1, 0 , -1):
        if float(right_input_data[i]) < float(right_input_data[i - 1]):
            bad_num_arr.append(right_input_data[i])
            right_input_data.pop(i)
    k = len(right_input_data)


if bad_num_arr != []:
    for i in range(len(bad_num_arr)-1):
        bad_num_str += bad_num_arr[i] + ', '
    bad_num_str += bad_num_arr[-1] + '.'


grid_arr = []
grid_str = []

def make_grid():
    for i in range(len(right_input_data)):
        grid_num = str(i)
        for j in range(16-len(grid_num)):
            grid_num += ' '
        grid_x_coordinate = right_input_data[i]
        for j in range(8-len(grid_x_coordinate)):
            grid_x_coordinate += ' '
        grid_str = 'GRID    ' + grid_num + grid_x_coordinate + '0.      0.              3456'
        grid_arr.append(grid_str)
    return grid_arr

make_grid()

if (is_correct(nameFile, "\\|/*<>?:")):
    # набор запрещенных символов символов для Windows
    file = open(nameFile + ".txt", "w+")
    # задание нового файла, перезапись существующего
    # имя вводить без тхт
    file.write("$    FILENAME - " + nameFile + ".txt\n")
    file.write("$\n")
    file.write("ID LINEAR," + nameFile + "\n")
    file.write("SOL 101\n")
    file.write("TIME 2\n")
    file.write("CEND\n")

    file.write("\n\n\n\n\n")
    file.write("TITLE = LINEAR STATICS USER'S SAMPLE INPUT FILE\n")
    file.write("SUBTITLE = TRUSS STRUCTURE\n")
    file.write("LABEL = POINT LOAD AT GRID POINT 4\n")
    file.write("LOAD = 10\n")
    file.write("SPC = 11\n")
    file.write("DISPLACEMENT = ALL\n")
    file.write("ELFORCE = ALL\n")
    file.write("ELSTRESS = ALL")

    file.write("\n\n\n\n\n")
    file.write("BEGIN BULK\n")
    file.write("$\n")
    file.write("$ THE GRID POINTS LOCATIONS\n")
    file.write("$ DESCRIBE THE GEOMETRY\n")
    file.write("$\n")
    for i in range(len(right_input_data)):
        file.writelines(grid_arr[i] + "\n")

    file.write("$ раздел CROD не используется в нашем решателе \n")
    file.write("$ MEMBERS ARE MODELED USING\n")
    file.write("$ ROD ELEMENTS\n")
    file.write("$\n")
    file.write("\n\n\n\n\n")

    file.write("$\n")
    file.write("$ PROPERTIES  OF ROD ELEMENTS\n")
    file.write("$\n")
    file.write("PROD    21      22      " + S + "\n")

    file.write("$\n")
    file.write("$ MATERIAL PROPERTIES\n")
    file.write("$\n")
    file.write("MAT1    22      " + E + "\n")

    file.write("$\n")
    file.write("$ POINT LOAD\n")
    file.write("$\n")
    file.write("FORCE   10      " + U + "               " + F + "   " + Xf + ".      -1.     0.")

    file.close()
else:
    print('Введите корректное название файла.')
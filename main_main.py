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

def hotiteLi(text):
    m = ''
    while m != '1' and m != '0' and m.lower() != 'да' and m.lower() != 'нет':
        m = input(text)
    return m


def roundNum(num, kolZnakPoslZap):
    num = round(num * 10 ** int(kolZnakPoslZap))/(10 ** int(kolZnakPoslZap))
    return num

balka = []

def chertezUzlov():
    print('Предварительный чертеж балки, включите воображение')
    for i in range(len(array) * 2 + 1):
        if i % 2 == 0:
            balka.append('F' + str(round(i / 2 + 1)))
        else:
            balka.append('----')
    print('F1' + ' и ' + 'F' + str(round(i / 2 + 1)) + '- заделки')
    return balka


chertezUzlov()
print(balka, ' --> X', '\n')
# masiveLength()
# masiveYsiliy()
# вывод массивов
print('Массив жесткостей элементов EF\n', array, '\n')
print('Массив длин элементов L\n', L, '\n')
print('Массив узловых усилий F\n', arrayUsiliy, '\n')

balkaM = []


def chertezUzlovM():
    print('Чертеж балки в масштабе с узловыми усилиями')
    for i in range(len(array) * 2 + 1):
        if i % 2 == 0:
            balkaM.append(arrayUsiliy[round(i / 2)])
        else:
            balkaM.append(('-' * int(L[round((i - 1) / 2)])))
    balkaM[0] = 'F1'
    balkaM[-1] = 'F' + str(round(i / 2 + 1))
    print('F1' + ' и ' + 'F' + str(round(i / 2 + 1)) + '- заделки')
    return balkaM


chertezUzlovM()

print(balkaM, ' --> X', '\n')

# обьявление вспомогательной матрицы
arrayG = [[1, -1],
          [-1, 1]]

# формируем заготовку для массива матриц жесткостей
arrayGes = []
for i in range(len(array)):
    arrayGes.append([])
    for j in range(len(arrayG)):
        arrayGes[i].append([])


# на выходе получим [  [ [], [] ],  [ [], [] ],
#                      [ [], [] ],  [ [], [] ]  ]

# считаем матрицу жесткостей элементов
def makeMatricaGestcosti():
    for i in range(len(array)):
        for j in range(len(arrayG)):
            for k in range(len(arrayG[j])):
                arrayGes[i][j].append(float(array[i]) * float(arrayG[j][k]))
    return arrayGes



makeMatricaGestcosti()


# выводим матрицы жесткостей элементов
def vivod(arrayGes):
    k = 0
    for i in range(len(arrayGes)):
        for j in range(len(arrayGes[i])):
            if k % 2 == 0:
                print('Матрица жесткости ', i + 1, '-го элемента: \n', arrayGes[i][j])
                k += 1
            else:
                print('', arrayGes[i][j])
        k = 0


vivod(arrayGes)
print('')

# формируем заготовку для матрицу жесткости системы
matGes = []
for i in range(len(array) + 1):
    matGes.append([])


# считаем матрицу жесткости системы
def makeMatricaGestcostiSistemi():
    matGes[0].append(arrayGes[0][0][0])
    for i in range(len(array) + 1):
        for j in range(len(array) + 1):
            if i == j and i != 0 and i != len(array):
                matGes[i].append(arrayGes[i][0][0] + arrayGes[i - 1][0][0])
            elif j == i - 1 and i != 0 and i != len(array) + 1:
                matGes[i].append(arrayGes[i - 1][0][1])
            elif j == i + 1 and i != len(array) + 1:
                matGes[i].append(arrayGes[i][0][1])
            elif j != i and j != -1 and i != -1:
                matGes[i].append(0)
    matGes[-1].append(arrayGes[-1][0][0])
    return matGes


makeMatricaGestcostiSistemi()

print('Матрица жесткости системы')
for i in range(len(matGes)):
    print(matGes[i])
print('')


def vvodGranichnihUsloviy():
    for i in range(len(matGes)):
        for j in range(len(matGes[i])):
            if j == 0 or j == len(matGes) - 1 or i == 0 or i == len(matGes) - 1:
                matGes[i][j] = 0
    matGes[0][0] = 1
    matGes[-1][-1] = 1
    return matGes


vvodGranichnihUsloviy()

print('Матрица жесткости системы с граничными условиями')
for i in range(len(matGes)):
    print(matGes[i])
print('')

arrayUzlovihPeremesheniy = []


def matrichnoeUravnenie():
    for i in range(len(array) + 1):
        arrayUzlovihPeremesheniy.append('U' + str(i + 1))
        print(str(matGes[i]) + ' * ' + str(arrayUzlovihPeremesheniy[i]) + ' = ' + str(arrayUsiliy[i]))


print('Матричное уравнение')
matrichnoeUravnenie()
print('')

arrayReshenie = []
arr1 = []
arr = []
for i in range(len(arrayUsiliy) - 2):
    arr.append([])



def makeArr():
    for i in range(1, len(arrayUsiliy) - 1):
        for j in range(1, len(arrayUsiliy) - 1):
            for k in range(1):
                arr[i - 1].append(matGes[i][j])
    return arr


makeArr()

arrU = []


def makeArrU():
    for i in range(1, len(arrayUsiliy) - 1):
        arrU.append(arrayUsiliy[i])
    return arrU


makeArrU()

print('Убираем лишнее')
for i in range(len(arr)):
    print(str(arr[i]) + ' = ' + str(arrU[i]))
print('')


def mnogitel(i, elem):
    for j in range(len(elem)):
        if i == j:
            m = elem[i - 1][j] / elem[i][j]
    return m


okr = False
m = hotiteLi('Хотите округлить результаты? ')
if m == '1' or m.lower() == 'да':
    okr = True
    kolZnakPoslZap = None
    while kolZnakPoslZap == None:
        kolZnakPoslZap = input('Сколько знаков оставить после запятой? ')
        kolZnakPoslZap = pravilnoLi(kolZnakPoslZap, False, False, False, True)


def triangleArray():
    for i in range(len(arr) - 1, 0, -1):
        mn = mnogitel(i, arr)
        b = float(arrU[i - 1]) - float(arrU[i]) * mn
        if okr is True:
            b = roundNum(b, kolZnakPoslZap)
        arrU[i - 1] = b
        for j in range(len(arr[i]) - 1, -1, -1):
            a = arr[i - 1][j] - arr[i][j] * mn
            if okr is True:
                a = roundNum(a, kolZnakPoslZap)
            arr[i - 1][j] = a
    return arr


triangleArray()

print('Приводим к диагональному виду')
for i in range(len(arr)):
    print(str(arr[i]) + ' = ' + str(arrU[i]))
print('')


def intU():
    for i in range(len(arrU)):
        arrU[i] = float(arrU[i])
    return arrU


intU()

resh = 0
uLoc = 0
U = []


def reshenieSlay():
    arrayReshenie.append(0)
    for i in range(len(arrU)):
        for j in range(len(arrU)):
            if i == j and i == 0:
                resh = arrU[i] / arr[i][j]
                if okr is True:
                    resh = roundNum(resh, kolZnakPoslZap)
                uLoc = resh
            elif i == j:
                resh = (arrU[i] - uLoc * arr[i][j - 1]) / arr[i][j]
                if okr is True:
                    resh = roundNum(resh, kolZnakPoslZap)
                uLoc = resh
        arrayReshenie.append(resh)
    arrayReshenie.append(0)
    return arrayReshenie


U = reshenieSlay()
print('Столбец возможных перемещений')
print(U)
print('')

N = []

for i in range(len(array)):
    N.append([])

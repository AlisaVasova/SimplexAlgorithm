def print_table(basis, bdr, array, n, m, cel_func, delts):
    # выводим красивенькую таблицу, 8|6
    # верх над таблицей
    for i in range(1, 20):
        print(" ", end='')
    for i in range(1, n + 1):
        print(" %7.3f  " % cel_func[i - 1], end='')
    print("")

    for i in range(1, 20 + 10 * n):
        print("_", end='')
    print("")

    # заголовок
    print(" Базис  |   БДР   |", end='')
    for i in range(1, n + 1):
        if i > 9:
            print("   x%d   |" % i, end='')
        else:
            print("   x%d    |" % i, end='')
    print("")

    for i in range(1, 20 + 10 * n):
        print("_", end='')
    print("")

    for j in range(1, m + 1):
        if bdr[j - 1] == 0:
            bdr[j - 1] = 0
        for i in range(1, n + 1):
            if array[j - 1][i - 1] == 0:
                array[j - 1][i - 1] = 0

    # строки базиса
    for j in range(1, m + 1):
        if j > 9:
            print("   x%d  | %7.3f |" % (basis[j - 1], bdr[j - 1]), end='')
        else:
            print("   x%d   | %7.3f |" % (basis[j - 1], bdr[j - 1]), end='')
        for i in range(1, n + 1):
            print(" %7.3f |" % array[j - 1][i - 1], end='')
        print("")

        for i in range(1, 20 + 10 * n):
            print("_", end='')
        print("")

    # нижняя строка
    delt0 = 0
    for j in range(1, m + 1):
        delt0 += cel_func[basis[j - 1] - 1] * bdr[j - 1]

    print("   Z    | %7.3f |" % delt0, end='')

    for i in range(1, n + 1):
        delts[i - 1] = 0
        for j in range(1, m + 1):
            delts[i - 1] += cel_func[basis[j - 1] - 1] * array[j - 1][i - 1]
        delts[i - 1] -= cel_func[i - 1]
        print(" %7.3f |" % delts[i - 1], end='')

    print("")

    for i in range(1, 20 + 10 * n):
        print("_", end='')
    print("")

def decision(m, n, bdr, array, basis, cel_func, delts):
    print_table(basis, bdr, array, n, m, cel_func, delts)

    isThereSolution = True
    while True:
        flag = True
        for i in range(1, n + 1):
            if delts[i - 1] > 0:
                flag = False
                break
        if flag == True:
            break

        max = 0
        ved_stolb = -1
        for i in range(1, n + 1):
            if delts[i - 1] > max:
                max = delts[i - 1]
                ved_stolb = i

        isThereSolution = False
        for j in range(1, m + 1):
            if array[j - 1][ved_stolb - 1] > 0:
                isThereSolution = True
        if isThereSolution == False:
            break

        min = 0
        ved_str = -1
        for j in range(1, m + 1):
            if array[j - 1][ved_stolb - 1] > 0:
                if ved_str == -1 or (bdr[j - 1] / array[j - 1][ved_stolb - 1]) < min:
                    min = bdr[j - 1] / array[j - 1][ved_stolb - 1]
                    ved_str = j

        basis[ved_str - 1] = ved_stolb
        preobr(ved_str, ved_stolb, array, m, n, bdr, cel_func, delts, basis)

    if isThereSolution == False:
        print("Целевая функция не ограничена, нет решения")
        return False
    else:
        print("Решение:")
        for i in range(1, n + 1):
            if i in basis:
                print("x" + str(i) + " = " + str(bdr[basis.index(i)]))
            else:
                print("x" + str(i) + " = 0")
        return True

def find_basis(m, n, ogr):
    basis = [0] * m # какие переменные входят в базис
    for k in range(1, m + 1): # для каждой строки базиса
        for i in range(1, n + 1): # для каждой переменной
            flag = False
            for j in range(1, m + 1): # для каждого ограничения
                if j != k:
                    if ogr[j - 1][i - 1] != 0:
                        flag = True
                        break
                else:
                    if ogr[j - 1][i - 1] != 1:
                        flag = True
                        break
            if flag == True:
                continue;
            else:
                basis[k - 1] = i
                break
    return basis

def preobr(ved_str, ved_stolb, array, m, n, bdr, cel_func, delts, basis):
    new_array = []
    for j in range(1, m + 1):
        new_array.append([0] * n)

    new_bdr = [0] * m

    for j in range(1, m + 1):
        if j != ved_str:
            for i in range(1, n + 1):
                new_array[j - 1][i - 1] = (array[j - 1][i - 1] * array[ved_str - 1][ved_stolb - 1] - array[ved_str - 1][i - 1] * array[j - 1][ved_stolb - 1]) / array[ved_str - 1][ved_stolb - 1]
        
            new_bdr[j - 1] = (bdr[j - 1] * array[ved_str - 1][ved_stolb - 1] - bdr[ved_str - 1] * array[j - 1][ved_stolb - 1]) / array[ved_str - 1][ved_stolb - 1]
        else:
            for i in range(1, n + 1):
                new_array[j - 1][i - 1] = array[j - 1][i - 1] / array[ved_str - 1][ved_stolb - 1]
            new_bdr[j - 1] = bdr[j - 1] / array[ved_str - 1][ved_stolb - 1]

    for j in range(1, m + 1):
        for i in range(1, n + 1):
            array[j - 1][i - 1] = new_array[j - 1][i - 1]
        bdr[j - 1] = new_bdr[j - 1]
    print_table(basis, bdr, array, n, m, cel_func, delts)

# ввод данных
print("Введите количество переменных: ", end='')
n = int(input())
print("Введите количество ограничений: ", end='')
m = int(input())

cel_func = []

print("Введите коэффициенты при переменных целевой функции:")
for i in range(1, n + 1):
    print("x" + str(i) + ": ", end='')
    cel_func.append(float(input()))

ogr = []

for j in range(1, m + 1):
    print("Введите коэффициенты при переменных ограничения " + str(j) + ":")
    ogr.append([0] * (n + 1))
    for i in range(1, n + 1):
        print("x" + str(i) + ": ", end='')
        ogr[j - 1][i - 1] = float(input())
    print("Введите значение правой части ограничения " + str(j) + ": ", end='')
    ogr[j - 1][n] = float(input())


print("Получившаяся мат. модель:")
print("Целевая функция: ", end='')
for i in range(1, n + 1):
    if cel_func[i-1] < 0:
        if i != 1:
            print("- ", end='')
        else:
            print("-", end='')
    else:
        if i != 1:
            print("+ ", end='')
    print(str(abs(cel_func[i-1])) + "x" + str(i) + " ", end='')
print("-> min")

print("Ограничения:")
for j in range(1, m + 1):
    for i in range(1, n + 1):
        if ogr[j - 1][i - 1] < 0:
            if i != 1:
                print("- ", end='')
            else:
                print("-", end='')
        else:
            if i != 1:
                print("+ ", end='')
        print(str(abs(ogr[j - 1][i - 1])) + "x" + str(i) + " ", end='')
    print("= " + str(ogr[j - 1][n]))

# поиск базиса
basis = find_basis(m, n, ogr)

c = 0 # сколько переменных не хватает в базисе
for i in range(0, m):
    if basis[i] == 0:
        c += 1

if (c == 0):    
    # стобец БДР
    bdr = []
    for j in range(1, m + 1):
        bdr.append(ogr[j - 1][n])
    # матрица коэффициентов
    array = [] # aij
    for j in range(1, m + 1):
        array.append([0] * n)
        for i in range(1, n + 1):
            array[j - 1][i - 1] = ogr[j - 1][i - 1]
    # оценки
    delts = [0] * n
    decision(m, n, bdr, array, basis, cel_func, delts)
else:
    print('Поиск базиса с помощью метода искусственного базиса.')
    print('Добавляем переменных: ' + str(c))
    n_dop = n + c
    m_dop = m
    cel_func_dop = []
    array_dop = []
    # новые ограничения
    q = 0 # сколько переменных внесли
    for i in range(0, m): # для каждого ограничения
        array_dop.append([0] * (n_dop + 1))
        for j in range(0, n):
            array_dop[i][j] = ogr[i][j]
        for j in range(0, c):
            if (basis[i] == 0 and j == q):
                array_dop[i][n + j] = 1
                q += 1
                basis[i] = n + j + 1
            else:
                array_dop[i][n + j] = 0
    # новая целевая функция
    for i in range (0, n):
        cel_func_dop.append(0)
    for i in range(0, c):
        cel_func_dop.append(1)
    # строим стобец БДР
    bdr_dop = []
    for j in range(1, m + 1):
        bdr_dop.append(ogr[j - 1][n])
    basis_dop = find_basis(m_dop, n_dop, array_dop)
    # оценки
    delts_dop = [0] * n_dop

    # решаем вспомогательную задачу
    if (decision(m_dop, n_dop, bdr_dop, array_dop, basis_dop, cel_func_dop, delts_dop) == True):
        # проверяем получившееся решение
        basis = basis_dop

        print("Заменяем искусственные переменные.")
        # заменяем искусственные переменные
        for l in range(0, m):
            if basis[l] > m:
                for k in range(1,n+1):
                    if k not in basis:
                        ved_str = l + 1
                        ved_stolb = k
                        basis[ved_str - 1] = ved_stolb
                        preobr(ved_str, ved_stolb, array_dop, m_dop, n_dop, bdr_dop, cel_func_dop, delts_dop, basis)
                        break;

        bdr = bdr_dop

        # матрица коэффициентов
        array = [] # aij
        for j in range(1, m + 1):
            array.append([0] * n)
            for i in range(1, n + 1):
                array[j - 1][i - 1] = array_dop[j - 1][i - 1]

        # оценки
        delts = [0] * n

        # решаем исходную задачу
        decision(m, n, bdr, array, basis, cel_func, delts)
    


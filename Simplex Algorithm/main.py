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

def artificial_basis(c, n, m, ogr, basis):
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

    return m_dop, n_dop, bdr_dop, array_dop, basis_dop, cel_func_dop, delts_dop

def reverse_transition(n, m, ved_str, ved_stolb, array_dop, m_dop, n_dop, bdr_dop, cel_func_dop, delts_dop, basis):
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

    return m, n, bdr, array, basis, cel_func, delts

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
    m_dop, n_dop, bdr_dop, array_dop, basis_dop, cel_func_dop, delts_dop = artificial_basis(c, n, m, ogr, basis)

    # решаем вспомогательную задачу
    if (decision(m_dop, n_dop, bdr_dop, array_dop, basis_dop, cel_func_dop, delts_dop) == True):
        m, n, bdr, array, basis, cel_func, delts = reverse_transition(n, m, ved_str, ved_stolb, array_dop, m_dop, n_dop, bdr_dop, cel_func_dop, delts_dop, basis)

        # решаем исходную задачу
        decision(m, n, bdr, array, basis, cel_func, delts)
    

import decision

def find_basis(m, n, array):
    basis = [0] * m # какие переменные входят в базис
    for k in range(0, m): # для каждой строки базиса
        for i in range(0, n): # для каждой переменной
            flag = False
            for j in range(0, m): # для каждого ограничения
                if j != k:
                    if array[j][i] != 0:
                        flag = True
                        break
                else:
                    if array[j][i] != 1:
                        flag = True
                        break
            if flag == True:
                continue;
            else:
                basis[k] = i + 1
                break
    return basis

def artificial_basis(c, n, m, array, basis):
    print('Поиск базиса с помощью метода искусственного базиса.')
    print('Добавляем переменных: ' + str(c))
    n_dop = n + c
    cel_func_dop = []
    array_dop = []
    # новые ограничения
    q = 0 # сколько переменных внесли
    for i in range(0, m): # для каждого ограничения
        array_dop.append([0] * (n_dop))
        for j in range(0, n):
            array_dop[i][j] = array[i][j]
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

    return n_dop, array_dop, cel_func_dop

def reverse_transition(n, m, array_dop, n_dop, bdr_dop, basis_dop):
    # проверяем получившееся решение
    basis = basis_dop
    array = []
    bdr = []
    for i in range(0, m): # для каждого ограничения
        array.append([0] * (n))
        for j in range(0, n):
            array[i][j] = array_dop[i][j]
        bdr.append(bdr_dop[i])

    print("Заменяем искусственные переменные.")
    # заменяем искусственные переменные
    for l in range(0, m):
        if basis[l] > m:
            for k in range(1,n+1):
                if k not in basis:
                    ved_str = l
                    ved_stolb = k - 1
                    basis[ved_str] = k
                    array, bdr = decision.preobr(ved_str, ved_stolb, array_dop, m, n_dop, bdr_dop)
                    break;

    return bdr, array, basis

def count_mis_vars(basis):
    c = 0 # сколько переменных не хватает в базисе
    for b in basis:
        if b == 0:
            c += 1
    return c

def input_model():
    error_str = "Ошибка ввода. Попробуйте еще раз."
    # ввод данных
    while True:
        print("Введите количество переменных: ", end='')
        try:
            n = int(input())
            if n < 1:
                print(error_str)
            else:
                break
        except ValueError:
            print(error_str)

    while True:
        print("Введите количество ограничений: ", end='')
        try:
            m = int(input())
            if m < 1:
                print(error_str)
            else:
                break
        except ValueError:
            print(error_str)

    while True:
        try:
            cel_func = []

            print("Введите коэффициенты при переменных целевой функции:")
            for i in range(1, n + 1):
                print("x" + str(i) + ": ", end='')
                cel_func.append(float(input()))
            break
        except ValueError:
            print(error_str)

    while True:
        try:
            array = []
            bdr = []

            for j in range(1, m + 1):
                print("Введите коэффициенты при переменных ограничения " + str(j) + ":")
                array.append([0] * (n))
                for i in range(1, n + 1):
                    print("x" + str(i) + ": ", end='')
                    array[j - 1][i - 1] = float(input())
                print("Введите значение правой части ограничения " + str(j) + ": ", end='')
                bdr.append(float(input()))

            break
        except ValueError:
            print(error_str)

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
            if array[j - 1][i - 1] < 0:
                if i != 1:
                    print("- ", end='')
                else:
                    print("-", end='')
            else:
                if i != 1:
                    print("+ ", end='')
            print(str(abs(array[j - 1][i - 1])) + "x" + str(i) + " ", end='')
        print("= " + str(bdr[j - 1]))

    return n, m, cel_func, array, bdr

def main():
    n, m, cel_func, array, bdr = input_model()
    # поиск базиса
    basis = find_basis(m, n, array)

    c = count_mis_vars(basis)

    if (c == 0):    
        # оценки
        delts = [0] * n
        flag, bdr_dec, basis_dec = decision.decision(m, n, bdr, array, basis, cel_func, delts)
    else:
        n_dop, array_dop, cel_func_dop = artificial_basis(c, n, m, array, basis)
        basis_dop = find_basis(m, n_dop, array_dop)
        delts_dop = [0] * n_dop

        # решаем вспомогательную задачу
        flag, bdr_dec, basis_dec = decision.decision(m, n_dop, bdr, array_dop, basis_dop, cel_func_dop, delts_dop)
        if (flag == True):
            bdr, array, basis = reverse_transition(n, m, array_dop, n_dop, bdr, basis_dop)

            # решаем исходную задачу
            delts = [0] * n
            flag, bdr_dec, basis_dec = decision.decision(m, n, bdr, array, basis, cel_func, delts)

    return flag, bdr_dec, basis_dec

if __name__ == "__main__":
    main()


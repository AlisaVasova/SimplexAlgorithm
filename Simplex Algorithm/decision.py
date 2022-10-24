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

def is_there_solution(m, array, ved_stolb):
    for j in range(1, m + 1):
            if array[j - 1][ved_stolb - 1] > 0:
                return True
    return False
    
def ved_stolbec(delts, n):
    max = 0
    ved_st = -1
    for i in range(1, n + 1):
        if delts[i - 1] > max:
            max = delts[i - 1]
            ved_st = i

    return ved_st

def ved_stroka(array, ved_stolb, bdr, m):
    min = 0
    ved_s = -1
    for j in range(1, m + 1):
        if array[j - 1][ved_stolb - 1] > 0:
            if ved_s == -1 or (bdr[j - 1] / array[j - 1][ved_stolb - 1]) < min:
                min = bdr[j - 1] / array[j - 1][ved_stolb - 1]
                ved_str = j

    return ved_s

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

        ved_stolb = ved_stolbec(delts, n)

        if is_there_solution(m, array, ved_stolb) == False:
            break
        
        ved_str = ved_stroka(array, ved_stolb, bdr, m)

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


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
        if basis[j - 1] > 9:
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

    return True

def is_there_solution(array, ved_stolb):
    for stroka in array:
        if stroka[ved_stolb] > 0:
            return True
    return False
    
def ved_stolbec(delts, n):
    max_st = 0
    ved_st = -1
    if n < 1 or len(delts) < n:
        return None
    for i in range(0, n):
        if delts[i] > max_st:
            max_st = delts[i]
            ved_st = i

    return ved_st

def ved_stroka(array, ved_stolb, bdr, m):
    min_s = 0
    ved_s = -1

    if m < 1 or len(array) < m or len(bdr) < m:
        return None
    for j in range(0, m):
        if array[j][ved_stolb] > 0:
            if ved_s == -1 or (bdr[j] / array[j][ved_stolb]) < min_s:
                min_s = bdr[j] / array[j][ved_stolb]
                ved_s = j

    return ved_s

def decision(m, n, bdr, array, basis, cel_func, delts):
    print_table(basis, bdr, array, n, m, cel_func, delts)

    is_there_solution_flag = True
    while True:
        flag = True
        for i in range(0, n):
            if delts[i] > 0:
                flag = False
                break
        if flag == True:
            break

        ved_stolb = ved_stolbec(delts, n)

        if is_there_solution(array, ved_stolb) == False: 
            is_there_solution_flag = False
            break
        
        ved_str = ved_stroka(array, ved_stolb, bdr, m)

        basis[ved_str] = ved_stolb + 1
        array, bdr = preobr(ved_str, ved_stolb, array, m, n, bdr)
        print_table(basis, bdr, array, n, m, cel_func, delts)

    if is_there_solution_flag == False:
        print("Целевая функция не ограничена, нет решения")
        return False, bdr, basis, array
    else:
        print("Решение:")
        for i in range(1, n + 1):
            if i in basis:
                print("x" + str(i) + " = " + str(bdr[basis.index(i)]))
            else:
                print("x" + str(i) + " = 0")
        return True, bdr, basis, array

def preobr(ved_str, ved_stolb, array, m, n, bdr):
    new_array = []
    for j in range(0, m):
        new_array.append([0] * n)

    new_bdr = [0] * m

    for j in range(0, m):
        if j != ved_str:
            for i in range(0, n):
                new_array[j][i] = (array[j][i] * array[ved_str][ved_stolb] - array[ved_str][i] * array[j][ved_stolb]) / array[ved_str][ved_stolb]
        
            new_bdr[j] = (bdr[j] * array[ved_str][ved_stolb] - bdr[ved_str] * array[j][ved_stolb]) / array[ved_str][ved_stolb]
        else:
            for i in range(0, n):
                new_array[j][i] = array[j][i] / array[ved_str][ved_stolb]
            new_bdr[j] = bdr[j] / array[ved_str][ved_stolb]

    print_table([0]*m, new_bdr, new_array, n, m, [0]*n, [0]*n)
    return new_array, new_bdr


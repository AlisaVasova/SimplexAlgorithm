# Тесты

## Блочные тесты
Функция: is_there_solution(array, ved_stolb) - проверяет, есть ли решение для данной задачи

Аргументы: array - массив с коэффициентами переменных при ограничениях, ved_stolb - ведущий столбец

 1. Тест ```test_is_sol``` (когда есть решение)
  - Входные данные: array = [[1, 1],[0,0]], ved_stolb = 1
  - Ожидаемый результат: True
  
 2. Тест ```test_is_not_sol``` (когда нет решения)
  - Входные данные:array = [[-1, -1],[-2,-2]], ved_stolb = 1
  - Ожидаемый результат: False
  
Функция: print_table(basis, bdr, array, n, m, cel_func, delts) - печатает таблицу

Аргументы: basis - номера переменных, входящие в базис, bdr - столбец БДР, array - массив с коэффициентами переменных при ограничениях, n - количество переменных, m - количество органичений, cel_func - коэффициенты переменных при целевой функции, delts - строка оценок

 1. Тест ```test_print_table``` (проверяет функцию печати таблицы)
  - Входные данные: basis = [2, 4], bdr = [4, 14], array = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], n = 10, m = 2, cel_func = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], delts = [0,0,0,0,0,0,0,0,0,0]
  - Ожидаемый результат: True
  
Функция: ved_stroka(array, ved_stolb, bdr, m) - находит ведущую строку

Аргументы: array - массив с коэффициентами переменных при ограничениях, ved_stolb - ведущий столбец, bdr - столбец БДР, m - количество ограничений

 1. Тест ```test_is_ved_str_some_otr``` - когда в ведущем столбце некоторые числа положительные, а некоторые отрицательные
  - Входные данные: array = [[3, -2],[3,3]], ved_stolb = 1, bdr = [2,2], m = 2
  - Ожидаемый результат: 1
  
 2. Тест ```test_is_not_ved_str``` - когда в ведущем столбце все числа отрицательные
  - Входные данные: array = [[3, -2],[3,-3]], ved_stolb = 1, bdr = [2,2], m = 2
  - Ожидаемый результат: -1
  
 3. Тест ```test_is_ved_str``` - когда в ведущем столбце все числа положительные
  - Входные данные: array = [[3, 2],[3,3]], ved_stolb = 1, bdr = [2,2], m = 2
  - Ожидаемый результат: 0
  
 4. Тест ```test_neg_ved_str``` - когда некоторые данные неверны
  - Входные данные: array = [], ved_stolb = -1, bdr = [2,2], m = 2
  - Ожидаемый результат: None
  
 Функция: ved_stolbec(delts, n) - находит ведущий столбец

Аргументы: delts - строка оценок, n - количество переменных

 1. Тест ```test_is_ved_st_some_otr``` - когда в строке оценок некоторые числа положительные, а некоторые отрицательные
  - Входные данные: delts = [1,-2], n = 2
  - Ожидаемый результат: 0
  
 2. Тест ```test_is_not_ved_st``` - когда в строке оценок все числа отрицательные
  - Входные данные: delts = [-1,-2], n = 2
  - Ожидаемый результат: -1
  
 3. Тест ```test_is_ved_st``` - когда в строке оценок все числа положительные
  - Входные данные: delts = [2,3], n = 2
  - Ожидаемый результат: 1
  
 4. Тест ```test_neg_ved_st``` - когда некоторые данные неверны
  - Входные данные: delts = [], n = 2
  - Ожидаемый результат: None
  
Функция: preobr(ved_str, ved_stolb, array, m, n, bdr) - преобразует матрицу по Жордано-Гауссу

Аргументы: ved_str - ведущая строка, ved_stolb - ведущий столбец, array - массив с коэффициентами переменных при ограничениях, n - количество переменных, m - количество органичений, bdr - столбец БДР

 1. Тест ```test_preobr``` (проверяет функция преобразования Жордана-Гаусса)
  - Входные данные: ved_str = 0, ved_stolb = 2, array = [[1, 0, 2, 1],[4, 1, 6, 0]], m = 2, n = 4, bdr = [4,14]
  - Ожидаемый результат: [[0.5,0,1,0.5],[1,1,0,-3]], [2,2]
  
Функция: input_model() - считывает модель, введенную пользователем

 1. Тест ```test_input``` (когда пользователь вводит все правильно)
  - Входные данные: ["4", "2", "1", "2", "3", "4", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
  - Ожидаемый результат: 4, 2, [1, 2, 3, 4], [[1, 2, 3, 4], [6, 7, 8, 9]], [5, 10]
  
 2. Тест ```test_wrong_input``` (когда пользователь вводит с ошибками)
  - Входные данные: ["-1", "0", "", "4", "-1", "0", " ", "2", "", "-1", "2", "-3", "4", "a","1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
  - Ожидаемый результат: 4, 2, [-1, 2, -3, 4], [[1, 2, 3, 4], [6, 7, 8, 9]], [5, 10]
  
Функция: find_basis(m, n, array) - находит базис по ограничениям
 
Аргументы: array - массив с коэффициентами переменных при ограничениях, n - количество переменных, m - количество органичений
 
 1. Тест ```test_full_basis``` (полный базис)
  - Входные данные: m = 2, n = 4, array = [[6, 1, 2, 0], [-2, 0, 3, 1]]
  - Ожидаемый результат: [2, 4]
  
 2. Тест ```test_not_full_basis``` (полный базис)
  - Входные данные: m = 2, n = 3, array = [[1, 2, 5], [0, 3, 1]]
  - Ожидаемый результат: [1, 0]
  
 2. Тест ```test_negativ_basis``` (неверные данные)
  - Входные данные: m = 2, n = 3, array = []
  - Ожидаемый результат: None
  
Функция: artificial_basis(c, n, m, array, basis) - вводит в модель переменные для метода искусственного базиса

Аргументы: array - массив с коэффициентами переменных при ограничениях, n - количество переменных, m - количество органичений, с - количество переменных, которых не хватает, basis - номера переменных, входящие в базис

1. Тест ```test_art_basis``` (проверяет введение новых переменных)
 - Входные данные: c = 1, n = 6, m = 3, array = [[1,0,0,1,0,6],[3,1,-4,0,0,2],[1,2,0,0,1,2]], basis = [4, 0, 5]
 - Ожидаемый результат: 7, [[1,0,0,1,0,6,0],[3,1,-4,0,0,2,1],[1,2,0,0,1,2,0]], [0,0,0,0,0,0,1]
 
Функция: reverse_transition(n, m, array_dop, n_dop, bdr_dop, basis_dop) - переход от искусственных переменных к начальным

Аргументы: array_dop - массив с коэффициентами переменных при ограничениях, n_dop - количество переменных c искусственными, n - количество переменных без искусственных, m - количество органичений, basis_dop - номера переменных, входящие в базис, bdr_dop - столбец БДР

1. Тест ```test_reverse_in_basis_not_art``` (когда в базисе нет искусственных переменных)
 - Входные данные: n = 4, m = 3, array_dop = [[0,1,0,0,2,-1],[0,0,1,-1,-4,3],[1,0,0,1,-3,2]], n_dop = 6, bdr_dop = [0,5,2], basis_dop = [2,3,1]
 - Ожидаемый результат: [0,5,2], [[0,1,0,0],[0,0,1,-1],[1,0,0,1]], [2,3,1]
 
2. Тест ```test_reverse_in_basis_is_art``` (когда в базисе есть искусственные переменные)
 - Входные данные: n = 3, m = 2, array_dop = [[2,0,1,1],[6,1,4,0]], n_dop = 4, bdr_dop = [4,14], basis_dop = [4,2]
 - Ожидаемый результат: [2,2], [[1,0,0.5,0.5],[0,1,1,-3]], [1,2]

Функция: count_mis_vars(basis) - подсчитывает, сколько переменных не хватает в базисе

Аргументы: basis_dop - номера переменных, входящие в базис

 1. Тест ```test_is_mis_var``` (есть недостающие переменные)
  - Входные данные: basis = [2, 0, 0]
  - Ожидаемый результат: 2
  
 2. Тест ```test_is_not_mis_var``` (нет недостающих переменных)
  - Входные данные: basis = [2, 1, 3]
  - Ожидаемый результат: 0
  
 3. Тест ```test_all_mis_var``` (все недостающие переменные)
  - Входные данные: basis = [0, 0, 0]
  - Ожидаемый результат: 3

## Интеграционные тесты 

Функция decision() вызывает функции is_there_solution(), ved_stolbec(), ved_stroka(), preobr()

Аргументы: basis - номера переменных, входящие в базис, bdr - столбец БДР, array - массив с коэффициентами переменных при ограничениях, n - количество переменных, m - количество органичений, cel_func - коэффициенты переменных при целевой функции, delts - строка оценок

1. Тест ```test_is_decision``` (есть решение для данной задачи)
  - Входные данные: basis = [2, 4], bdr = [4, 14], array = [[1, 0, 2, 1],[4, 1, 6, 0]], n = 4, m = 2, cel_func = [1, 2, 0, 3], delts = [0,0,0,0]
  - Ожидаемый результат: True
  
2. Тест ```test_is_not_decision``` (нет решения для данной задачи)
  - Входные данные: basis = [2, 4], bdr = [10, 40], array = [[1, -1, 1, 0],[2, 0, 0, 1]], n = 4, m = 2, cel_func = [-1, -2, 0, 0], delts = [0,0,0,0]
  - Ожидаемый результат: False, [1, 2], [3, 1], [[0,-0.5,1,2],[1,1,0,-3]]

Функция reverse_transition() вызывает функцию preobr():

Аргументы: array_dop - массив с коэффициентами переменных при ограничениях, n_dop - количество переменных c искусственными, n - количество переменных без искусственных, m - количество органичений, basis_dop - номера переменных, входящие в базис, bdr_dop - столбец БДР

1. Тест ```test_intgr_reverse_in_basis_not_art``` (когда в базисе нет искусственных переменных)
 - Входные данные: n = 4, m = 3, array_dop = [[0,1,0,0,2,-1],[0,0,1,-1,-4,3],[1,0,0,1,-3,2]], n_dop = 6, bdr_dop = [0,5,2], basis_dop = [2,3,1]
 - Ожидаемый результат: [0,5,2], [[0,1,0,0],[0,0,1,-1],[1,0,0,1]], [2,3,1]
 
2. Тест ```test_intgr_reverse_in_basis_is_art``` (когда в базисе есть искусственные переменные)
 - Входные данные: n = 3, m = 2, array_dop = [[2,0,1,1],[6,1,4,0]], n_dop = 4, bdr_dop = [4,14], basis_dop = [4,2]
 - Ожидаемый результат: [2,2], [[1,0,0.5,0.5],[0,1,1,-3]], [1,2]

Функция main() вызывает функции input_model(), find_basis(), count_mis_vars(), decision(), artificial_basis(), reverse_transition():

1. Тест ```test_main_with_art_basis``` - когда используется метод искусственного базиса
 - Входные данные: ["4", "3", "3", "1", "1", "0", "1", "2", "0", "1", "2", "-2", "-1", "1", "-3", "1", "2", "3", "0", "2", "4"]
 - Ожидаемый результат: в базисе находятся переменные 2,3,4; им соответствуют значения БДР 0,7,2

2. Тест ```test_main'`` - когда не используется метод искусственного базиса
 - Входные данные: ["4", "2", "1", "2", "0", "3", "1", "0", "2", "1", "4", "4", "1", "6", "0", "14"]
 - Ожидаемый результат: в базисе находятся переменные 1,3; им соответствуют значения БДР 2,1

## Аттестационные тесты 

1. Тест 1 - проверка запуска программы
 - Действия: пользователь запускает программу
 - Ожидаемый результат: программа запрашивает количество переменных
 
2. Тест 2 - проверка ввода количества переменных и ограничений (положительная)
 - Действия: пользователь вводит целое число > 0
 - Ожидаемый результат: программа запрашивает следующее число

3. Тест 3 - проверка ввода количества переменных и ограничений (отрицательная)
 - Действия: пользователь вводит не число, нецелое число или целое число <= 0
 - Ожидаемый результат: программа выводит сообщение об ошибке и запрашивает данные еще раз

4. Тест 4 - проверка ввода коэффициентов ограничений (положительная)
 - Действия: пользователь вводит число
 - Ожидаемый результат: программа запрашивает следующее число

5. Тест 5 - проверка ввода коэффициентов ограничений (отрицательная)
 - Действия: пользователь вводит не число
 - Ожидаемый результат: программа выводит сообщение об ошибке и запрашивает данные еще раз
 
6. Тест 6 - проверка нахождения решения
  - Действия: пользователь вводит "4", "3", "3", "1", "1", "0", "1", "2", "0", "1", "2", "-2", "-1", "1", "-3", "1", "2", "3", "0", "2", "4"
  - Ожидаемый результат: программа выводит процесс решения в таблицах и находит решение: в базисе находятся переменные 2,3,4; им соответствуют значения БДР 0,7,2

7. Тест 7 - проверка отсутствия решения
  - Действия: пользователь вводит "4", "2", "1", "-1", "1", "0", "10", "2", "0", "0", "1", "40"
  - Ожидаемый результат: программа выводит процесс решения в таблицах и то, что нет решения

import decision

def test_is_sol():
   assert decision.is_there_solution(2, [[1, 1],[0,0]], 1) == True

def test_is_not_sol():
   assert decision.is_there_solution(2, [[-1, -1],[-2,-2]], 1) == False

def test_print_table():
    n = 4
    m = 2
    cel_func = [1, 2, 0, 3]
    array = [[1, 0, 2, 1],[4, 1, 6, 0]]
    bdr = [4, 14]
    basis = [2, 4]
    delts = [0,0,0,0]
    assert decision.print_table(basis, bdr, array, n, m, cel_func, delts) == True
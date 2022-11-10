import decision

def test_is_sol():
   assert decision.is_there_solution([[1, 1],[0,0]], 0) == True

def test_is_not_sol():
   assert decision.is_there_solution([[-1, -1],[-2,-2]], 0) == False

def test_print_table():
    n = 4
    m = 2
    cel_func = [1, 2, 0, 3]
    array = [[1, 0, 2, 1],[4, 1, 6, 0]]
    bdr = [4, 14]
    basis = [2, 4]
    delts = [0,0,0,0]
    assert decision.print_table(basis, bdr, array, n, m, cel_func, delts) == True

def test_is_ved_st():
   assert decision.ved_stolbec([2,3], 2) == 1

def test_is_not_ved_st():
   assert decision.ved_stolbec([-1,-2], 2) == -1

def test_preobr():
    n = 4
    m = 2
    array = [[1, 0, 2, 1],[4, 1, 6, 0]]
    bdr = [4, 14]
    ved_str = 1
    ved_stolb = 2
    
    array, bdr = decision.preobr(ved_str, ved_stolb, array, m, n, bdr)

def test_is_decision():
    n = 4
    m = 2
    cel_func = [1, 2, 0, 3]
    array = [[1, 0, 2, 1],[4, 1, 6, 0]]
    bdr = [4, 14]
    basis = [2, 4]
    delts = [0,0,0,0]
    assert decision.decision(m, n, bdr, array, basis, cel_func, delts) == True

def test_is_not_decision():
    n = 4
    m = 2
    cel_func = [-1, -2, 0, 0]
    array = [[1, -1, 1, 0],[2, 0, 0, 1]]
    bdr = [10, 40]
    basis = [3, 4]
    delts = [0,0,0,0]
    assert decision.decision(m, n, bdr, array, basis, cel_func, delts) == False
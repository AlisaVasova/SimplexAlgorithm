import decision

def test_is_sol():
   assert decision.is_there_solution([[1, 1],[0,0]], 0) == True

def test_is_not_sol():
   assert decision.is_there_solution([[-1, -1],[-2,-2]], 0) == False

def test_print_table():
    n = 10
    m = 2
    cel_func = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    array = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    bdr = [4, 14]
    basis = [2, 10]
    delts = [0]*10
    assert decision.print_table(basis, bdr, array, n, m, cel_func, delts) == True

def test_is_ved_st():
   assert decision.ved_stolbec([2,3], 2) == 1

def test_is_not_ved_st():
   assert decision.ved_stolbec([-1,-2], 2) == -1

def test_is_ved_st_some_otr():
   assert decision.ved_stolbec([1,-2], 2) == 0

def test_neg_ved_st():
   assert decision.ved_stolbec([], 2) == None

def test_is_ved_str_some_otr():
    assert decision.ved_stroka([[3, -2],[3,3]], 1, [2,2], 2) == 1

def test_is_not_ved_str():
    assert decision.ved_stroka([[3, -2],[3,-3]], 1, [2,2], 2) == -1

def test_is_ved_str():
    assert decision.ved_stroka([[3, 3],[3,2]], 1, [2,2], 2) == 0

def test_neg_ved_str():
    assert decision.ved_stroka([], -1, [2,2], 2) == None

def test_preobr():
    n = 4
    m = 2
    array = [[1, 0, 2, 1],[4, 1, 6, 0]]
    bdr = [4, 14]
    ved_str = 0
    ved_stolb = 2
    
    array, bdr = decision.preobr(ved_str, ved_stolb, array, m, n, bdr)
    assert array == [[0.5,0,1,0.5],[1,1,0,-3]]
    assert bdr == [2,2]

def test_is_decision():
    n = 4
    m = 2
    cel_func = [1, 2, 0, 3]
    array = [[1, 0, 2, 1],[4, 1, 6, 0]]
    bdr = [4, 14]
    basis = [2, 4]
    delts = [0,0,0,0]
    flag, bdr_dec, basis_dec, array_dec = decision.decision(m, n, bdr, array, basis, cel_func, delts)
    assert flag  == True
    assert (bdr_dec == [1, 2]) and (basis_dec == [3, 1])
    assert array_dec == [[0,-0.5,1,2],[1,1,0,-3]]
    
def test_is_not_decision():
    n = 4
    m = 2
    cel_func = [-1, -2, 0, 0]
    array = [[1, -1, 1, 0],[2, 0, 0, 1]]
    bdr = [10, 40]
    basis = [3, 4]
    delts = [0,0,0,0]
    assert decision.decision(m, n, bdr, array, basis, cel_func, delts)[0] == False
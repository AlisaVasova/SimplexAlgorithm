from unittest.mock import call
from unittest.mock import patch
import main

class MockInputFunction:
    def __init__(self, return_value=None, side_effect=None):
        self.return_value = return_value
        self.side_effect = side_effect
        self.mock_calls = []
        self._orig_input_fn = __builtins__['input']

    def _mock_input_fn(self, prompt=None):
        return_value = self.return_value\
            if self.side_effect is None\
            else self.side_effect[len(self.mock_calls)]
        self.mock_calls.append(call(prompt))
        print(str(return_value))
        return return_value

    def __enter__(self):
        __builtins__['input'] = self._mock_input_fn

    def __exit__(self, type, value, traceback):
        __builtins__['input'] = self._orig_input_fn

def test_input():
    with MockInputFunction(side_effect=["4", "2", "1", "2", "3", "4", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]):
        n, m, cel_func, array, bdr = main.input_model()
    assert n == 4
    assert m == 2
    assert cel_func == [1, 2, 3, 4]
    assert array == [[1, 2, 3, 4], [6, 7, 8, 9]]
    assert bdr == [5, 10]

def test_wrong_input():
    with MockInputFunction(side_effect=["-1", "0", "", "4", "-1", "0", " ", "2", "", "-1", "2", "-3", "4", "a","1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]):
        n, m, cel_func, array, bdr = main.input_model()
    assert n == 4
    assert m == 2
    assert cel_func == [-1, 2, -3, 4]
    assert array == [[1, 2, 3, 4], [6, 7, 8, 9]]
    assert bdr == [5, 10]

def test_full_basis():
    basis = main.find_basis(2, 4, [[6, 1, 2, 0], [-2, 0, 3, 1]])
    assert basis == [2, 4]

def test_not_full_basis():
    basis = main.find_basis(2, 3, [[1, 2, 5], [0, 3, 1]])
    assert basis == [1, 0]

def test_negativ_basis():
    basis = main.find_basis(2, 3, [])
    assert basis == None

def test_art_basis():
   c = 1
   n = 6
   m = 3
   array = [[1,0,0,1,0,6],[3,1,-4,0,0,2],[1,2,0,0,1,2]]
   basis = [4, 0, 5]
   n_dop, array_dop, cel_func_dop = main.artificial_basis(c, n, m, array, basis)
   assert n_dop == 7 
   assert array_dop == [[1,0,0,1,0,6,0],[3,1,-4,0,0,2,1],[1,2,0,0,1,2,0]]
   assert cel_func_dop == [0,0,0,0,0,0,1]

def test_reverse_in_basis_not_art():
   n = 4
   m = 3
   array_dop = [[0,1,0,0,2,-1],[0,0,1,-1,-4,3],[1,0,0,1,-3,2]]
   n_dop = 6
   bdr_dop = [0,5,2]
   basis_dop = [2,3,1]
   with patch('decision.preobr', side_effect=[(None,None)]) as preobr:
       bdr, array, basis = main.reverse_transition(n, m, array_dop, n_dop, bdr_dop, basis_dop)
   assert bdr == [0,5,2]
   assert array == [[0,1,0,0],[0,0,1,-1],[1,0,0,1]]
   assert basis == [2,3,1]
    
def test_reverse_in_basis_is_art():
   n = 3
   m = 2
   array_dop = [[2,0,1,1],[6,1,4,0]]
   n_dop = 4
   bdr_dop = [4,14]
   basis_dop = [4,2]
   with patch('decision.preobr', side_effect=[([[1,0,0.5,0.5],[0,1,1,-3]],[2,2])]) as preobr:
       bdr, array, basis = main.reverse_transition(n, m, array_dop, n_dop, bdr_dop, basis_dop)
   assert bdr == [2,2]
   assert array == [[1,0,0.5,0.5],[0,1,1,-3]]
   assert basis == [1,2]

def test_is_mis_var():
    basis = [2, 0, 0]
    assert main.count_mis_vars(basis) == 2

def test_is_not_mis_var():
    basis = [2, 1, 3]
    assert main.count_mis_vars(basis) == 0

def test_all_mis_var():
    basis = [0, 0, 0]
    assert main.count_mis_vars(basis) == 3

def test_intgr_reverse_in_basis_not_art():
   n = 4
   m = 3
   array_dop = [[0,1,0,0,2,-1],[0,0,1,-1,-4,3],[1,0,0,1,-3,2]]
   n_dop = 6
   bdr_dop = [0,5,2]
   basis_dop = [2,3,1]
   bdr, array, basis = main.reverse_transition(n, m, array_dop, n_dop, bdr_dop, basis_dop)
   assert bdr == [0,5,2]
   assert array == [[0,1,0,0],[0,0,1,-1],[1,0,0,1]]
   assert basis == [2,3,1]
    
def test_intgr_reverse_in_basis_is_art():
   n = 3
   m = 2
   array_dop = [[2,0,1,1],[6,1,4,0]]
   n_dop = 4
   bdr_dop = [4,14]
   basis_dop = [4,2]
   bdr, array, basis = main.reverse_transition(n, m, array_dop, n_dop, bdr_dop, basis_dop)
   assert bdr == [2,2]
   assert array == [[1,0,0.5,0.5],[0,1,1,-3]]
   assert basis == [1,2]


def test_main_with_art_basis():
    with MockInputFunction(side_effect=["4", "3", "3", "1", "1", "0", "1", "2", "0", "1", "2", "-2", "-1", "1", "-3", "1", "2", "3", "0", "2", "4"]):
        flag, bdr, basis = main.main()
    assert flag == True    
    assert (2 in basis) and (3 in basis) and (4 in basis)    
    assert bdr[basis.index(2)] == 0
    assert bdr[basis.index(3)] == 7
    assert bdr[basis.index(4)] == 2

def test_main():
    with MockInputFunction(side_effect=["4", "2", "1", "2", "0", "3", "1", "0", "2", "1", "4", "4", "1", "6", "0", "14"]):
        flag, bdr, basis = main.main()
    assert flag == True    
    assert (1 in basis) and (3 in basis)   
    assert bdr[basis.index(1)] == 2
    assert bdr[basis.index(3)] == 1
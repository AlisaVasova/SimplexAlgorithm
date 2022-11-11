from unittest.mock import call
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
    with MockInputFunction(side_effect=["4", "2", "1", "2", "3", "4", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", ""]):
        n, m, cel_func, array, bdr = main.input_model()
    assert n == 4
    assert m == 2
    assert cel_func == [1, 2, 3, 4]
    assert array == [[1, 2, 3, 4], [6, 7, 8, 9]]
    assert bdr == [5, 10]

def test_full_basis():
    basis = main.find_basis(2, 3, [[1, 2, 0], [0, 3, 1]])
    assert basis == [1, 3]

def test_not_full_basis():
    basis = main.find_basis(2, 3, [[1, 2, 5], [0, 3, 1]])
    assert basis == [1, 0]

def test_art_basis():
   c = 1
   n = 6
   m = 3
   array = [[1,0,0,1,0,6],[3,1,-4,0,0,2],[1,2,0,0,1,2]]
   bdr = [9, 2, 6]
   basis = [4, 0, 5]
   n_dop, array_dop, cel_func_dop, delts_dop = artificial_basis(c, n, m, array, bdr, basis)
   assert n_dop == 7 
   assert array_dop == [[1,0,0,1,0,6,0],[3,1,-4,0,0,2,1],[1,2,0,0,1,2,0]]
   assert cel_func_dop == [0,0,0,0,0,0,1]
   assert delts_dop == [0,0,0,0,0,0,0]

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
        n, m, cel_func, ogr = main.input_model()
    assert n == 4
    assert m == 2
    assert cel_func == [1, 2, 3, 4]
    assert ogr == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
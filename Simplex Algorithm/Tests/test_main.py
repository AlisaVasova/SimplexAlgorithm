import main
from unittest.mock import patch
from unittest.mock import call

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
        if prompt:
            print(prompt + str(return_value))
        else:
            print(str(return_value))
        return return_value

    def __enter__(self):
        __builtins__['input'] = self._mock_input_fn

    def __exit__(self, type, value, traceback):
        __builtins__['input'] = self._orig_input_fn

def some_func():
    input()
    binstr = input()
    changes= 1
    # Clever stuff
    return changes


def test_case1():
    with MockInputFunction(side_effect=["","1101110"]):
        changes = some_func()
    print(changes)

    assert changes == 1
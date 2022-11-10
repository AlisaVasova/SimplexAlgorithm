import main
from unittest.mock import patch

def test_input():
    with patch('__builtin__.input', side_effect = [4, 2, 1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) as input:
        n, m, cel_func, ogr = main.input_model()
        assert n == 4
        assert m == 2
        assert cel_func == [1, 2, 3, 4]
        assert ogr == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
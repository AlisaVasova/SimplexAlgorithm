import math

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5


import sys

sys.path.insert(1, '../decision')
import decision

def test_one():
   assert decision.is_there_solution(2, [[1, 1],[0,0]], 1) == True
import math

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

import decision

def test_1():
   assert decision.is_there_solution(2, [[1, 1],[0,0]], 1) == True
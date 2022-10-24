import math

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('../')
import decision

def test_one():
   assert decision.is_there_solution(2, [[1, 1],[0,0]], 1) == True
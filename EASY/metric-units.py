# https://www.codingame.com/ide/puzzle/metric-units
import sys
import re

value1, value2 = input().split('+')  # the expression to calculate
unit1 = re.sub(r'\d','',value1)
unit2 = re.sub(r'\d','',value2)

value1 = int(re.sub(r'[a-z]*','',value1))
value2 = int(re.sub(r'[a-z]*','',value2))

print("value1",value1,"unit1",unit1,"unit2",unit2,"value2",value2, file=sys.stderr, flush=True)

print("1cm")

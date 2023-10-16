import math
from decimal import Decimal

#NaN(nota a number)
a = float("NaN")
print(f"a: {a}")

#modulo math
a = float("nan")
print(f"Es de tipo Nan(not a number)?: {math.isnan(a)}")

#modulo decimal
a = Decimal("NaN")
print(f"Es de tipo Nan(not a number)?: {math.isnan(a)}")
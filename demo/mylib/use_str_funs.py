import str_funs as sf
from str_funs import has_digit
import sys

# Modify module search path
sys.path.append(r"d:\classroom\aug11\demo\stlib")
print(sys.path)

import num_funs as nf

print(has_digit('Abc'))
print(sf.count_upper('Abc'))
print(nf.iseven(10))

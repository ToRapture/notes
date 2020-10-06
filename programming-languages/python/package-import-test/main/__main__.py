import sys
print(sys.path)

from .pk import bar

from .relative import *
print(x)

try:
    import relative
    raise Exception('Not supposed to get here')
except ModuleNotFoundError:
    pass

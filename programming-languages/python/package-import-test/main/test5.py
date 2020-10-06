from pkg.pk1.pk2.pk3.pk4 import *  # pk4 is package
"""
If __all__ is not defined, the statement from pkg.pk1.pk2.pk3.pk4 import * does not import all submodules
from the package pkg.pk1.pk2.pk3.pk4 into the current namespace; it only ensures that the package
pkg.pk1.pk2.pk3.pk4 has been imported (possibly running any initialization code in __init__.py) and then imports
whatever names are defined in the package.
This includes any names defined (and submodules explicitly loaded) by __init__.py.
"""

assert 'foo' not in dir()  # foo is module
assert 'x' in dir()  # x is variable
assert 'func1' in dir()  # func1 is function

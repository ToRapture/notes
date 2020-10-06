from pkg.pk1.pk2 import *
"""
The import statement uses the following convention:
if a package’s __init__.py code defines a list named __all__,
it is taken to be the list of module names that should be imported when from package import * is encountered.
"""

assert 'foo' in dir()  # foo is module
assert 'x' not in dir()  # x is variable
assert 'y' in dir()  # y is a variable

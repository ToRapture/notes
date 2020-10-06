print('pk4 init')

x = 'defined in pk4'

"""
You can also write relative imports, with the from module import name form of import statement.
These imports use leading dots to indicate the current and parent packages involved in the relative import.
"""


def func1():
    from . import foo
    from .foo import foo as foo_func
    assert foo.foo == foo_func


def func2():
    from ... import pk3
    from ....pk2 import pk3 as pk2_pk3
    assert pk3 == pk2_pk3


def func3():
    from ....pk2 import foo
    from ...foo import foo as foo_func
    assert foo.foo == foo_func

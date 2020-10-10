# coding: utf-8


def foo(x, y):
    return x + y


def bar(self, x, y):
    print(self)
    return x + y


class F:
    pass


def main():
    # For objects, the machinery is in object.__getattribute__() which transforms b.x into type(b).__dict__['x'].__get__(b, type(b)).
    # The implementation works through a precedence chain that gives data descriptors priority over instance variables,
    # instance variables priority over non-data descriptors, and assigns lowest priority to __getattr__() if provided.
    # The full C implementation can be found in PyObject_GenericGetAttr() in Objects/object.c.
    f = F()
    f.foo = foo
    assert f.foo(1, 2) == 3

    F.bar = bar
    assert f.bar(3, 4) == 7


if __name__ == '__main__':
    main()

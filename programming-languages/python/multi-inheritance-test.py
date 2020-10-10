class X:
    def __init__(self):
        super().__init__()
        print('X init')


class A:
    def __init__(self, word):
        super().__init__()
        print('A init word: %s' % word)


class Y(A):
    def __init__(self):
        super().__init__('hello')
        print('Y init')


class Z:
    def __init__(self):
        print('Z init')


# super() return a proxy object that delegates method calls to a parent or sibling class of type.
# This is useful for accessing inherited methods that have been overridden in a class.
# The object-or-type determines the method resolution order to be searched.
# The search starts from the class right after the type.

# For example, if __mro__ of object-or-type is D -> B -> C -> A -> object and the value of type is B,
# then super() searches C -> A -> object.

# The __mro__ attribute of the object-or-type lists the method resolution search order used by both getattr() and super().
# The attribute is dynamic and can change whenever the inheritance hierarchy is updated.


class F(X, Y, Z):
    def __init__(self):
        # The zero argument form only works inside a class definition,
        # as the compiler fills in the necessary details to correctly retrieve the class being defined,
        # as well as accessing the current instance for ordinary methods.
        super().__init__()  # This does the same thing as: super(F, self).__init__()
        print('F init')


if __name__ == '__main__':
    f = F()
    assert F.__mro__ == (F, X, Y, A, Z, object)
    from IPython import embed
    embed()

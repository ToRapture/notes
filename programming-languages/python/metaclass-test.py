class MetaClass(type):
    # Once the class namespace has been populated by executing the class body,
    # the class object is created by calling metaclass(name, bases, namespace, **kwds)
    def __new__(cls, name, bases, namespace, **kwargs):
        print('MetaClass.__new__: cls[%s], name[%s], bases[%s], namespace[%s], kwargs[%s]' % (cls, name, bases, namespace, kwargs))

        namespace['foo'] = 'added in __new__'
        for k, v in kwargs.items():
            namespace[k] = v

        return super().__new__(cls, name, bases, namespace)

    def __init__(self, name, bases, namespace, **kwargs):
        print('MetaClass.__init__: self[%s], name[%s], bases[%s], namespace[%s], kwargs[%s]' % (self, name, bases, namespace, kwargs))
        self.bar = 'added in __init__'
        super().__init__(name, bases, namespace, **kwargs)


class F(metaclass=MetaClass, hello='world', say='one day'):
    pass


class Foo:
    # Called to create a new instance of class cls. __new__() is a static method (special-cased so you need not
    # declare it as such) that takes the class of which an instance was requested as its first argument.
    # The remaining arguments are those passed to the object constructor expression (the call to the class).
    # The return value of __new__() should be the new object instance (usually an instance of cls).

    # Typical implementations create a new instance of the class by invoking the superclass’s __new__() method
    # using super().__new__(cls[, ...]) with appropriate arguments and then modifying the newly-created
    # instance as necessary before returning it.
    def __new__(cls, *args, **kwargs):
        print(cls, args, kwargs)
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        self.bar = 'added in __init__'


if __name__ == '__main__':
    assert issubclass(type, type)
    assert isinstance(type, type)

    assert issubclass(object, object)
    assert isinstance(object, object)

    assert issubclass(type, object)
    assert not issubclass(object, type)

    assert isinstance(type, object)
    assert isinstance(object, type)

    Foo('hello')
    Foo(1, 2, 3, hello='world')

    assert issubclass(Foo, Foo)
    assert isinstance(F, MetaClass)
    assert F.__mro__ == (F, object)
    assert MetaClass.__mro__ == (MetaClass, type, object)

    assert F.foo == 'added in __new__'
    assert F.bar == 'added in __init__'
    assert F.hello == 'world'
    assert F.say == 'one day'

    from IPython import embed
    embed()

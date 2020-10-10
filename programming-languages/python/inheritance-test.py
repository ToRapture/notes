class A:
    def __init__(self):
        super().__init__()
        print('A init')


class B(A):
    def __init__(self, x):
        super().__init__()
        print('B init, x: %s' % x)


class C(B):
    def __init__(self):
        super().__init__(233)
        print('C init')


class D(C):
    def __init__(self):
        super().__init__()
        print('D init')


class E(D):
    pass


class F(D):
    def __init__(self):
        print('F init')


if __name__ == '__main__':
    E()
    print('-----------------')
    F()

import pkg.pk1.pk2.pk3.pk4.foo  # foo is module

assert 'foo' not in dir()
assert 'foo' not in dir(pkg.pk1.pk2)  # pk2 has module foo

assert 'pkg' in dir()
assert 'pk1' in dir(pkg)
assert 'pk2' in dir(pkg.pk1)
assert 'pk3' in dir(getattr(getattr(pkg, 'pk1'), 'pk2'))
assert 'pk4' in dir(getattr(getattr(getattr(pkg, 'pk1'), 'pk2'), 'pk3'))

assert '__path__' in dir(pkg.pk1.pk2.pk3.pk4)  # pk4 is package
assert '__path__' not in dir(pkg.pk1.pk2.pk3.pk4.foo)  # foo is module

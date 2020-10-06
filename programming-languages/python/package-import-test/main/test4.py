import pkg.pk1.pk2

assert 'foo' not in dir(pkg.pk1.pk2)  # foo is module
assert 'x' in dir(pkg.pk1.pk2)  # x is variable

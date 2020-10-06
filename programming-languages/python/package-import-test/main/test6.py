import pkg.pk1.pk2

assert 'foo' not in dir(pkg.pk1.pk2)  # foo is module
assert 'pk3' not in dir(pkg.pk1.pk2)  # pk3 is package

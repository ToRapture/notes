import pk.bar  # pk.bar is a module which contains relative import

try:
    import relative  # relative is a module which contains relative import
    raise Exception('Not supposed to get here')
except ImportError:
    pass

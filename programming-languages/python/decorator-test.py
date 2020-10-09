import functools
import time


def bad(func):
    def wrapper_bad(*args, **kwargs):
        print(f'before {func.__name__} in bad called')
        value = func(*args, **kwargs)
        print(f'after {func.__name__} in bad called, return value is: {value}')
        return value

    return wrapper_bad


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        print(f'before {func.__name__} in decorator called')
        value = func(*args, **kwargs)
        print(f'after {func.__name__} in decorator called, return value is: {value}')
        return value

    return wrapper_decorator


@bad
def foo(x, y, *args, **kwargs):
    print(x, y, args, kwargs)
    return x + y


@decorator
def bar(x, y, *args, **kwargs):
    print(x, y, args, kwargs)
    return x + y


def after(seconds):
    def decorator_after(func):
        @functools.wraps(func)
        def wrapper_after(*args, **kwargs):
            time.sleep(seconds)
            value = func(*args, **kwargs)
            return value

        return wrapper_after

    return decorator_after


@after(seconds=3)
def hello(word):
    print(word)


class C:
    FOO = 'bar'

    @after(seconds=1)
    def __init__(self):
        pass

    @after(seconds=1)
    def say(self):
        print('I am %s' % self)


if __name__ == '__main__':
    assert foo(1, 2) == 3
    assert bar(3, 4) == 7
    assert foo.__name__ == 'wrapper_bad'
    assert bar.__name__ == 'bar'

    # use IPython to test the after decorator
    from IPython import embed
    embed()

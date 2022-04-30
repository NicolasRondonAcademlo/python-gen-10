import functools
class DecoratorClass:

    @classmethod
    def print_mensaje(cls, file_name):
        def outer(func):
            @functools.wraps(func)
            def inner(*args, **kwargs):
                with open(file_name, 'r') as r:
                    print(r)
                return func(*args, **kwargs)
            return inner
        return outer
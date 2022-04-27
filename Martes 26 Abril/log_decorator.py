import logging


def log(func):

    def wrap_log(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(f'{name}.log')
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        
        logger.info(f'Running function {name}')
        result = func(*args, **kwargs)
        logger.info(f"Result: {result}")
        return func
    return wrap_log


@log
def double_function(x):
    return x * 2

@log 
def suma(x, y):
    return x + y

value = double_function(2)
suma  = suma(4,8)




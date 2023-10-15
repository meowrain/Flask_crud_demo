import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 装饰器的额外行为
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def my_function():
    """这是一个被装饰函数的文档字符串。"""
    pass

print(my_function.__name__)  # 输出: my_function
print(my_function.__doc__)   # 输出: 这是一个被装饰函数的文档字符串。


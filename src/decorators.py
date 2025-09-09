import functools


def log(filename=None):  # type: ignore
    """декоратор для лога выполнения функции"""

    def decorator(func):  # type: ignore
        @functools.wraps(func)
        def wrapper(*args, **kwargs):  # type: ignore
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                _write_log(message, filename)
                return result
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                _write_log(message, filename)
                raise

        return wrapper

    return decorator


def _write_log(message, filename):  # type: ignore
    """запись лог в файл или консоль"""
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    else:
        print(message)


@log(filename="mylog.txt")  # type: ignore
def add(x, y):  # type: ignore
    return x + y

from src.decorators import log


@log(filename="mylog.txt")
def add(x, y):
    return x + y


@log()  # Без файла - в консоль
def divide(a, b):
    return a / b


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)

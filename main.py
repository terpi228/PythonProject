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

# Тестируем
# add(1, 2)        # Запишет "add ok" в mylog.txt
# divide(10, 2)    # Выведет "divide ok" в консоль
# divide(10, 0)    # Выведет ошибку в консоль
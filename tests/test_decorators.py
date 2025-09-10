from src.decorators import log


def test_basic():  # type: ignore
    """Просто проверяем что декоратор работает"""

    @log()
    def test_func(x):  # type: ignore
        return x * 2

    result = test_func(5)
    assert result == 10  # Если выполнилось - значит ок


def test_with_file():  # type: ignore
    """Проверяем что с файлом тоже работает"""

    @log(filename="tmp.log")
    def test_func(x):  # type: ignore
        return x + 1

    result = test_func(10)
    assert result == 11  # Работает - значит все ок

import colorama
from inspect import getmembers, isclass, isfunction


def inspect_colorama():
    print(f"Интроспекция библиотеки: {colorama.__name__}")
    print(f"Версия: {colorama.__version__}")
    print("-" * 30)

    attributes = dir(colorama)

    for attr in attributes:
        value = getattr(colorama, attr)

        if not attr.startswith("_"):
            print(f"Имя: {attr} | Тип: {type(value)}")


if __name__ == "__main__":
    inspect_colorama()

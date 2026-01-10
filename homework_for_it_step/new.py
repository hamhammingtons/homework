class simple:
    def __init__(self, stop_value):
        self.stop_value = stop_value

    def __iter__(self):
        def generator():
            current = 0
            while current < self.stop_value:
                yield f"Step {current}"
                current += 1

        return generator()


# task 2


def safe_calculator(func):
    def wrapper(expression):
        try:
            # We check if the input is actually a string to avoid basic errors
            if not isinstance(expression, str):
                raise ValueError("введите str")

            result = func(expression)
            return f"результат: {result}"
        except ZeroDivisionError:
            return "Error: нельзя делить на 0"
        except SyntaxError:
            return "Error: не правильное математическое дейтсвие"
        except NameError:
            return "Error: нужны только числа и операнды"
        except Exception as e:
            return f"Error: {e}"

    return wrapper


@safe_calculator
def calculate(expression):
    return eval(expression)


def run_calculator_tests():
    print(calculate("10 + 5 * 2"))

    print(calculate("10 / 0"))

    print(calculate("hello + 5"))


if __name__ == "__main__":
    run_calculator_tests()

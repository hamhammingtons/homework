import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"запушено {func.__name__} за {end - start:.4f} секунд")
        return result

    return wrapper


class Sims:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.is_alive = True

    @timer_decorator
    def work(self):
        print(f"{self.name} is working...")
        time.sleep(0.2)
        self.energy -= 20
        return self.energy

    @timer_decorator
    def rest(self):
        print(f"{self.name} is resting...")
        time.sleep(0.1)
        self.energy += 10
        return self.energy


def calculate_runtime(function_to_run, *args):
    start_time = time.time()
    function_to_run(*args)
    end_time = time.time()
    return end_time - start_time


def run_tests():
    character = Sims("Bob")

    work_duration = calculate_runtime(character.work)
    assert work_duration >= 0.2

    rest_duration = calculate_runtime(character.rest)
    assert rest_duration >= 0.1

    assert character.energy == 90

    print("done")


if __name__ == "__main__":
    run_tests()

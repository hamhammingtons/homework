import os


class Console:
    def __init__(self) -> None:
        self.comms = {}

    def toRegister(self, name, uid, params_allowed):
        def wrapper(func):
            func.uid = uid
            func.name = name
            func.params_allowed = params_allowed
            self.comms[name] = func
            return func

        return wrapper

    def specifically_for_os_module(self, func):
        def wrapper(self, user_args):
            # self  -> Console instance
            # user_args -> list of strings from the user

            if not user_args:
                print("err: path missing")
                return

            USER_PATH = os.path.abspath(user_args[0])

            try:
                if not os.path.exists(USER_PATH):
                    print(f"Invalid path: {USER_PATH}")
                else:
                    return func(self, user_args)
            except Exception as ex:
                print(f"Error: {ex}")

        return wrapper

    def to_run(self):
        while True:
            user_input = input("> ").lower().split()
            if not user_input:
                continue

            name, params = user_input[0], user_input[1:]

            if name in ["exit", "quit"]:
                break

            if name in self.comms:
                func = self.comms[name]

                if len(params) < func.params_allowed:
                    print(f"Err: {name} needs {func.params_allowed} args")
                else:
                    # Pass self AND params
                    func(self, params)
            else:
                print("Unknown command")


new = Console()


@new.toRegister(name="echo", uid=3, params_allowed=0)
def echo(self, listothings: list):
    print(" ".join(listothings))


@new.toRegister(name="ls", uid=4, params_allowed=1)
@new.specifically_for_os_module
def listdir(self, listothings: list):
    print(os.listdir(listothings[0]))


new.to_run()

# TODO: remove this ai slop and make the function yourslef
# i hate how it did the os module wrapper

import os
import shlex  # 1 use case, which is ai written too. i dont know this module.


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
        def wrapper(self, user_args):  # user_args == params READ BELOW PLZ
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
            user_input = shlex.split(  # BIG FIX
                input("> ")
            )  # this is where this comes in handy, idk how to use it though. it was suggested by ai. so its just
            # for so when we do ls "OneDrive/Рабочий стол" it gets "Рабочий стол" instead of "Рабочий ".
            if not user_input:
                continue

            name = user_input[0]
            params = user_input[1:]

            if name in ["exit", "quit"]:
                break

            if name in self.comms:
                func = self.comms[name]

                if len(params) < func.params_allowed:
                    print(f"Err: {name} needs {func.params_allowed} args")
                else:
                    func(self, params)
            else:
                print("Unknown command")


new = Console()

os.chdir(os.environ["USERPROFILE"])
# not really that important but we can use it if we want to go to home directly


@new.toRegister(name="echo", uid=3, params_allowed=0)
def echo(self, listothings: list):
    print(" ".join(listothings))


@new.toRegister(name="ls", uid=4, params_allowed=1)
@new.specifically_for_os_module
def listdir(self, listothings: list):
    print(os.listdir(listothings[0]))


new.to_run()

""" this was heinous to do but i guess it works 
main things to note:
please for the love of god never use indirect indexing it is really hard to do and debug
^ it isnt evil exactly but its recomended to not use this 
i mean this crap:

name = user_input[0]
params = user_input[1:]

Use something like making these parameters global by adding them to the object itself
self.name = user_input[0] 
...

^ btw not recomended, just dont mix up this part:
func(self, params)
parameters = what the user typed, idk why i used user_input it made it way confusing

OR also you can do 
name, *params = input("> ").split() to not use indirect indexing
"""
# --- exceptions ---
"""""
FOR MAKING EXCEPTIONS (such as what i used for the os module)

Please use (self, function) first and then whatever you want
because if were doing not the manual way of doing something, we will need to first execute the exceptions things 
and then run the uid or store them in like a data base or whatever. I mean attaching metadata. 

"""

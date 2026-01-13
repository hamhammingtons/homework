import datetime
import socket  # using this we'll get the user and thats it, i dont know the things inside it so well output it fully.

# we will make a console for a person to echo something first. lets make a class i think


class Console:
    def __init__(self) -> None:
        self.user = socket.gethostname()
        self.commands = {
            "echo": (
                self.echo_func,
                1,
                12,
            )  # where 1 is the ammount of params, 12 is unqique id
        }
        self.cur_command = ""  # we will set it as an index of self commands some time

    def echo_func(self, arg_list, unique_id):
        print(" ".join(arg_list))

    def to_run(self):
        while True:
            user_input = input("> ").split()  # list
            name = user_input[0]  # name of func
            args = user_input[1:]  # its arguments

            if name == "exit":  # exceptions
                break
            elif not user_input:
                continue

            if name in self.commands:
                assigned_func = self.commands[
                    name
                ]  # we find that func [ 1 use case unfortuanetly]
                func, params_allowed, uid = assigned_func
                try:
                    if len(args) != params_allowed:
                        print(
                            f"ERR_T: 2, func {name} exceeds parameters fit in found func: {func.__name__}, \n\t {func.__name__} takes {params_allowed} {"pararameters" if params_allowed > 1 else "parameter"}, not {args}"
                        )  # ^^^ fixed the object at... problem with func.__name__ dunder method
                    else:
                        func(arg_list=args, unique_id=uid)
                except Exception as ex:
                    return "fatal eerro: ", ex
            else:
                print(
                    f"ERR_T: 1, func {user_input} with params {user_input[1:]} not found. "
                )


new_c = Console()
new_c.to_run()

def tosum():
    pass


tosum.uid = 12  # type: ignore
print(tosum.uid)  # type: ignore
print(tosum.__dict__)  # uid is now in a secret dict


# techincally mentioning i could refactor my code which is the console_project.py to have metadata instead of dict{key: [tuple values]}
# we will make a console for a person to echo something first. lets make a class i think


class Console:
    def __init__(self) -> None:
        self.comms = {}

    def toRegister(self, name, uid, params_allowed):
        def wrapper(
            func,
        ):  # remember dont pass func in the outer body only in the wrapper thank you
            func.uid = uid
            func.name = name
            func.params_allowed = params_allowed

            self.comms[name] = func
            return func

        return wrapper

    def to_run(self):
        while True:
            user_input = input(f"> ").lower().split()
            if not user_input:
                continue

            name, args = user_input[0], user_input[1:]
            if name in ["exit", "quit"]:
                break

            if name in self.comms:
                func = self.comms[name]

                if len(args) < func.params_allowed:
                    print(f"Err: {name} needs {func.params_allowed} args")
                else:
                    func(args)
            else:
                print("Unknown command")


new = Console()


@new.toRegister(
    name="echo", uid=3, params_allowed=0
)  # refactored thing is pretty weird but cool and much more readable.
def echo(listothings: list):
    print(" ".join(listothings))


new.to_run()

# TODO: i no longer need this todo, i did what i wanted to do.

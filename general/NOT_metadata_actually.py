def tosum():
    pass


tosum.uid = 12  # type: ignore
print(tosum.uid)  # type: ignore
print(tosum.__dict__)  # uid is now in a secret dict

# techincally mentioning i could refactor my code which is the console_project.py to have metadata instead of dict{key: [tuple values]}
# we will make a console for a person to echo something first. lets make a class i think


class Console:
    def __init__(self) -> None:
        self.commands = {"echo": {"func": self.echo_func, "uid": 12, "prm_req": 0}}

    def echo_func(self, arg_list, uid):
        if not arg_list:
            print("err fatal, arg list not provided.")
        else:
            print(f"uid: {uid}, returned: {" ".join(arg_list)}")

    def to_run(self):
        while True:
            user_str = input("> ").lower().split()
            if not user_str:
                continue

            name = user_str[0]

            if name in [
                "exit" or "quit"
            ]:  # used to be if 'name == "exit" or "quit" ' -> quit will be always true unless we do the machinacions again, because str = true
                break

            args = user_str[1:]

            if name in self.commands:
                found_func = self.commands[name]
                func = found_func["func"]
                uid = found_func["uid"]
                prm_req = found_func["prm_req"]

                if len(args) < prm_req:
                    print(
                        f"err: parameters must be at least {prm_req} in {func.__name__}"
                    )
                else:
                    func(args, uid)
            else:
                print(f"err: unknown command, expression: \n{user_str}")


clasic = Console()
clasic.to_run()


# ^^^ this isnt really metadata, this is just "Data Placement".
# if wed like to assign metadata we would actually do metadata

"""
console bla bla bla:
    def __init__(self):
        self.some_func.uid = 12
        self.some_func.prm_allowed = 1
        
        then we atually map it out 
        
        commands = {
        "echo": some_func (already has __dict__ inside it and has uid and prm allowed, you can check.)
        }
          --btw means hidden dict inside func (metadata -like a label)
            also dont forget a function is an object thats why we can assign dicts to it like that...

        def to_run(self):
            while True:
                ...
                func = commands[name] 
                uid = func.uid
                prm_req = func.prm_req -- again because it has __dict__
                ...
        """

# TODO: I forgot to say but actually we can use a decorator here to not do the manual thing where we assign values!:
# self.some_func.uid = 12
# self.some_func.prm_allowed = 1
# ... --- SO ill need to learn how to do decorators based of this!

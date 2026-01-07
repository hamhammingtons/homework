def tosort(dic: dict):
    match dic:
        case {"type": "message", "sender": sender, "content": content}:
            return f"message from {sender}: {content}"
        case {"type": "login", "user": user}:
            return f"User logged in {user}"
        case {"type": "err", "code": Code}:
            return "err", Code
        case _:
            return "idk figure it out sir"

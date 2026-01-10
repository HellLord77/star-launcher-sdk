from hashlib import md5
from json import dumps
from time import time


def to_train(snake: str) -> str:
    kebab = snake.replace("_", "-")
    return kebab.title()


def get_auth_header(data: str, game_id: str, version: str, salt: str) -> str:
    head = {"game_tag": game_id, "time": int(time()), "version": version}
    sign_str = f"{dumps(head, separators=(',', ':'))}{data or ''}{salt}"
    sign = md5(sign_str.encode(), usedforsecurity=False).hexdigest()
    authorization = {"head": head, "sign": sign}
    return dumps(authorization, separators=(",", ":"))

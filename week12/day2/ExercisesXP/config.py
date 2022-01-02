import random
import string


def rand_key(num1: int, num2: int):
    # staring range from num1 to num2.
    key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(num1, num2))
    return key


class Config:
    SECRET_KEY = rand_key(0, 256)
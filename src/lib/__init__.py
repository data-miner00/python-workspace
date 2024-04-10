import random
import string


def generate_random_uppercase_string(length: int) -> str:
    return "".join(random.choices(string.ascii_uppercase, k=length))

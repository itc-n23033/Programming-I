import random
import string

name = "kaito"

while True:
    random_name = "".join(random.sample(string.ascii_lowercase, len(name)))
    print(random_name)

    if random_name == name:
        break

import random
import string

def get_random_string(length):
    # Random string with the combination of lower and upper case
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

f = open("j.txt", "w")
n = random.randint(30, 100)
f.write(str(n) + "\n")

for i in range(n):
    s = get_random_string(random.randint(1, 5))
    f.write(s + " ")

f.write("\n")
f.write("mubeenkodvavi")
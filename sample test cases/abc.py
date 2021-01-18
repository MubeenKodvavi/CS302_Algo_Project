from random import seed
from random import randint

# alphabets = ["M", "U", "B", "E", "E", "N", "K", "O", "D", "V", "A", "V", "I"]
alphabets = ["M", "O", "E", "I", "Z", "A", "D", "I", "L"]
alpha_l = len(alphabets)
n = randint(30, 100)

string1 = ""
string2 = ""

for i in range(n):
    j = randint(0, alpha_l - 1)
    k = randint(0, alpha_l - 1)
    string1 = string1 + str(alphabets[j])
    string2 = string2 + str(alphabets[k])

f = open("abc10.txt", "w")
f.write(string1 + "\n")
f.write(string2 + "\n")

f.close()
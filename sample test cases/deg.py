from random import randint

f = open("deg10.txt", "w")

n = randint(30, 100)
f.write(str(n) + "\n")

array = []
for i in range(n):
    array.append(randint(1, 100))
    f.write(str(array[i]) + " ")

f.write("\n")
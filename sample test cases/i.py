from random import randint

f = open("i.txt", "w")

n = randint(30, 100)
f.write(str(n) + "\n")

array = []
for i in range(n):
    array.append(randint(0, 100))
    f.write(str(array[i]) + " ")

f.write("\n")

f.write("198")
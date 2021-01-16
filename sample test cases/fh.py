from random import randint

n = randint(10, 100)
f = open("fh.txt", "w")
f.write(str(n) + "\n")
weights = []
values = []
for i in range(n):
    weights.append(randint(1, 100))
    f.write(str(weights[i]) + " ")
f.write("\n")

for i in range(n):
    values.append(randint(1, 100))
    f.write(str(values[i]) + " ")
f.write("\n")

f.write("198")

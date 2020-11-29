# 4. Найти значение минимального элемента списка

import random

n = int(input("Input list size:\n"))

A = []
for i in range(n):
    A.append(random.randint(0, 99))

print(A)
B = set(A)
A = list(B)
print(A[0])

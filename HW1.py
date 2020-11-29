# 12. Есть натуральное двузначное число n. Верно ли, что среди его цифр есть 1 или 9?

import random

n = random.randint(10, 99)

print('Our number is '+str(n))

a = n % 10
b = n - a

if a == 9 or a == 1:
    print('There is 1 or 9 in our number digits!')
elif b == 9 or b == 1:
    print('There is 1 or 9 in our number digits!')
else:
    print('There is no 1 or 9 in our number digits!')

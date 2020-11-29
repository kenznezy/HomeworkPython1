# 1. Шестизначный автобусный билет считается удачным, если сумма его цифр делится на 7.
# Могут ли два билета подряд быть удачными?

A = []

for i in range(1000000):
    A = [int(x) for x in str(i)]
#   print(A)
    if sum(A) % 7 == 0:
        if (sum(A)+1) % 7 == 0:
            print(A)
    else:
        print('It is not possible')

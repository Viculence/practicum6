n = int(input())

if n == 1:
    print(0)
elif n <= 10:
    print(n - 1)
elif n <= 190:
    pos_in_double = n - 11
    number = 10 + pos_in_double // 2
    if pos_in_double % 2 == 0:
        print(number // 10)
    else:
        print(number % 10)
else:
    pos_in_triple = n - 191
    number = 100 + pos_in_triple // 3
    digit_pos = pos_in_triple % 3
    if digit_pos == 0:
        print(number // 100)
    elif digit_pos == 1:
        print((number // 10) % 10)
    else:
        print(number % 10)
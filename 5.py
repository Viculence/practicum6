s = input()

letter_from = s[0]
digit_from = int(s[1])
letter_to   = s[3]
digit_to   = int(s[4])

if letter_from == 'a': x1 = 1
elif letter_from == 'b': x1 = 2
elif letter_from == 'c': x1 = 3
elif letter_from == 'd': x1 = 4
elif letter_from == 'e': x1 = 5
elif letter_from == 'f': x1 = 6
elif letter_from == 'g': x1 = 7
else: x1 = 8

if letter_to == 'a': x2 = 1
elif letter_to == 'b': x2 = 2
elif letter_to == 'c': x2 = 3
elif letter_to == 'd': x2 = 4
elif letter_to == 'e': x2 = 5
elif letter_to == 'f': x2 = 6
elif letter_to == 'g': x2 = 7
else: x2 = 8

dx = x2 - x1
dy = digit_to - digit_from

if (dx == 1 and dy == 2) or (dx == 2 and dy == 1) or \
   (dx == -1 and dy == 2) or (dx == -2 and dy == 1) or \
   (dx == 1 and dy == -2) or (dx == 2 and dy == -1) or \
   (dx == -1 and dy == -2) or (dx == -2 and dy == -1):
    print("верно")
else:
    print("ошибка")
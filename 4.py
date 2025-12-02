s = input()
if (ord(s[0]) - ord('a') + 1 + int(s[1])) % 2 == 0:
    print("черный")
else:
    print("белый")
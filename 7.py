k = int(input())

if k % 5 == 0:
    print('да')
elif (k - 7) >= 0 and (k - 7) % 5 == 0:
    print('да')
elif (k - 14) >= 0 and (k - 14) % 5 == 0:
    print('да')
elif (k - 21) >= 0 and (k - 21) % 5 == 0:
    print('да')
elif (k - 28) >= 0 and (k - 28) % 5 == 0:
    print('да')
elif (k - 35) >= 0 and (k - 35) % 5 == 0:
    print('да')
elif (k - 42) >= 0 and (k - 42) % 5 == 0:
    print('да')
elif (k - 49) >= 0 and (k - 49) % 5 == 0:
    print('да')
else:
    print('нет')
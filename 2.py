a, b = map(float, input().strip().split('х'))
c, d, e = map(float, input().strip().split('х'))

if a > b:
    a, b = b, a

min1 = c
if d < min1:
    min1 = d
if e < min1:
    min1 = e

if min1 == c:
    if d <= e:
        min2 = d
    else:
        min2 = e
elif min1 == d:
    if c <= e:
        min2 = c
    else:
        min2 = e
else:
    if c <= d:
        min2 = c
    else:
        min2 = d

if min1 <= a and min2 <= b:
    print('да')
else:
    print('нет')
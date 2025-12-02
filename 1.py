a, b = map(float, input().strip().split('х'))

r = 6.5
d = 2 * r

d_squared = d * d
diagonal_squared = a**2 + b**2

if diagonal_squared <= d_squared:
    print('да')
else:
    print('нет')

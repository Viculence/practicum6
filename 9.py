import math

x1, y1, r1 = map(float, input().split())
x2, y2, r2 = map(float, input().split())

d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

sum_r = r1 + r2
diff_r = abs(r1 - r2)

if d > sum_r:
    print('Окружности лежат одна вне другой, не касаясь')
elif d == sum_r:
    print('Окружности имеют внешнее касание')
elif diff_r < d < sum_r:
    print('Окружности пересекаются')
elif d == diff_r:
    print('Окружности имеют внутреннее касание')
else:
    print('Одна окружность лежит внутри другой, не касаясь')

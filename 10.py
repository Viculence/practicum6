x1, y1, x2, y2 = map(float, input().split())

x3, y3, x4, y4 = map(float, input().split())

left = max(x1, x3)
right = min(x2, x4)
top = max(y1, y3)
bottom = min(y2, y4)

if left < right and top < bottom:
    print('Прямоугольники имеют пересечение')
elif left == right or top == bottom:
    print('Прямоугольники имеют касание')
elif (x1 > x3 and y1 > y3 and x2 < x4 and y2 < y4) or \
     (x3 > x1 and y3 > y1 and x4 < x2 and y4 < y2):
    print('Один прямоугольник лежит внутри другого, не касаясь')
else:
    print('Прямоугольники лежат вне друг друга, не касаясь')
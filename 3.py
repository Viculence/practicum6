n, m = map(int, input().strip().split('x'))
k = int(input())

if k % m == 0 and 1 <= k // m < n:
    print('успешно')
elif k % n == 0 and 1 <= k // n < m:
    print('успешно')
else:
    print('неосуществимо')
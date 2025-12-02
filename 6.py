n, k, m = map(int, input().split())

total_rides = 2 * n

if total_rides % k == 0:
    seansov = total_rides // k
else:
    seansov = total_rides // k + 1

time = seansov * m

print(time)
N = int(input())
coordinates = [0] * N
for n in range(N):
    x, y = map(int, input().split())
    coordinates[n] = (x, y)
coordinates.sort(key=lambda x: (x[0], x[1]))
for coordinate in coordinates:
    print(f'{coordinate[0]} {coordinate[1]}')
N = int(input())
coordinates = [0] * N
for n in range(N):
    x, y = map(int, input().split())
    coordinates[n] = (x, y)
coordinates.sort(key=lambda c: (c[1], c[0]))
for c in coordinates:
    print(f'{c[0]} {c[1]}')
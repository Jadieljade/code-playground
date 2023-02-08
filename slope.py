from math import gcd
from collections import defaultdict

points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]


points.sort()
print(points)
slope = defaultdict(int)
M = 0
for i, (x1, y1) in enumerate(points):
    slope.clear()
    for x2, y2 in points[i + 1:]:
        difx, dify = x2 - x1, y2 - y1
        print(difx, dify)

        G = gcd(difx, dify)

        m = (difx//G, dify//G)

        slope[m] += 1
        if slope[m] > M:
            M = slope[m]

print(M + 1)

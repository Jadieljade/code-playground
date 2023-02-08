trust = [[1, 3], [2, 3], [3, 1]]
N = 3
Trusted = [0] * (N+1)
print(Trusted)

for (a, b) in trust:
    print(a, b)
    Trusted[a] -= 1
    Trusted[b] += 1
    print(Trusted)

for i in range(1, len(Trusted)):
    if Trusted[i] == N-1:
        print(i)
    else:
        print(-1)

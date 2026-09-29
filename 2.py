n = int(input())
f = [0] + list(map(int, input().split()))

for i in range(1, n + 1):
    if f[f[f[i]]] == i:
        print("YES")
        break
else:
    print("NO")
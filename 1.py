n = int(input())
p = [0] * (n + 1)
for i in range(1, n + 1):
    p[i] = int(input())

depth = [0] * (n + 1)

def get_depth(i):
    if depth[i] != 0:
        return depth[i]
    if p[i] == -1:
        depth[i] = 1
    else:
        depth[i] = get_depth(p[i]) + 1
    return depth[i]

ans = 0
for i in range(1, n + 1):
    ans = max(ans, get_depth(i))

print(ans)

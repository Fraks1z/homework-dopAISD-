import sys

sys.setrecursionlimit(200000)


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    a = [0] + list(map(int, input().split()))

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)

    ans = 0

    def dfs(v, parent, cnt):
        nonlocal ans
        if a[v] == 1:
            cnt += 1
        else:
            cnt = 0

        if cnt > m:
            return

        is_leaf = True
        for u in adj[v]:
            if u != parent:
                is_leaf = False
                dfs(u, v, cnt)

        if is_leaf:
            ans += 1

    dfs(1, 0, 0)
    print(ans)


if __name__ == "__main__":
    main()
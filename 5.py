import sys
import heapq


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, w = map(int, input().split())
        adj[a].append((b, w))
        adj[b].append((a, w))

    INF = float('inf')
    dist = [INF] * (n + 1)
    prev = [0] * (n + 1)
    dist[1] = 0

    pq = [(0, 1)]  # (расстояние, вершина)

    while pq:
        d, v = heapq.heappop(pq)
        if d > dist[v]:
            continue
        for u, w in adj[v]:
            nd = d + w
            if nd < dist[u]:
                dist[u] = nd
                prev[u] = v
                heapq.heappush(pq, (nd, u))

    if dist[n] == INF:
        print(-1)
        return

    # Восстановление пути
    path = []
    v = n
    while v != 0:
        path.append(v)
        v = prev[v]
    path.reverse()

    print(' '.join(map(str, path)))


if __name__ == "__main__":
    main()
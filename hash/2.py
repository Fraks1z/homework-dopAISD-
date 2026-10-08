import sys


def main():
    input = sys.stdin.readline
    t = int(input())
    out = []

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        freq = {}
        ans = 0

        for i in range(n):
            b = a[i] - (i + 1)  # i+1, так как индексация с 1
            cnt = freq.get(b, 0)
            ans += cnt
            freq[b] = cnt + 1

        out.append(str(ans))

    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    main()
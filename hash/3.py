import sys


def main():
    input = sys.stdin.readline
    t = int(input())
    out = []

    MOD1 = 10 ** 9 + 7
    MOD2 = 10 ** 9 + 9
    BASE1 = 137
    BASE2 = 139
    MAXN = 200005

    pow1 = [1] * MAXN
    pow2 = [1] * MAXN
    for i in range(1, MAXN):
        pow1[i] = (pow1[i - 1] * BASE1) % MOD1
        pow2[i] = (pow2[i - 1] * BASE2) % MOD2

    for _ in range(t):
        n = int(input())
        s = input().strip()

        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)
        for i in range(n):
            c = ord(s[i])
            h1[i + 1] = (h1[i] * BASE1 + c) % MOD1
            h2[i + 1] = (h2[i] * BASE2 + c) % MOD2

        seen = set()

        for i in range(n - 1):
            len_suf = n - i - 2

            pref1 = h1[i]
            pref2 = h2[i]

            suf1 = (h1[n] - h1[i + 2] * pow1[n - i - 2]) % MOD1
            suf2 = (h2[n] - h2[i + 2] * pow2[n - i - 2]) % MOD2

            res1 = (pref1 * pow1[len_suf] + suf1) % MOD1
            res2 = (pref2 * pow2[len_suf] + suf2) % MOD2

            seen.add((res1, res2))

        out.append(str(len(seen)))

    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    main()
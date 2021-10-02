#!/usr/bin/env python3
import sys


def solve(N: int, S: "List[int]", T: "List[int]"):
    INF = 10 ** 9
    S = S * 2
    times = [INF] * (2 * N)
    tn = []
    for i in range(N):
        tn.append((T[i], i))
    tn.sort()
    for tt, i in tn:
        if times[i] <= tt:
            continue
        times[i] = tt
        for j in range(1, 2 * N - i):
            next = S[i + j - 1] + times[i + j - 1]
            if times[i + j] <= next:
                break
            times[i + j] = next
    for i in range(N):
        print(min(times[i], times[i + N]))
    # print(*times[:N], sep="\n")
            





    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    T = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, S, T)

if __name__ == '__main__':
    main()
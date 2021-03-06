#!/usr/bin/env python3
import sys


def solve(N: int, K: int, a: "List[int]"):
    p, q = divmod(K, N)
    nums = [p] * N
    l = []
    for i in range(N):
        l.append((a[i],i))
    l.sort()
    for i in range(q):
        nums[l[i][1]] += 1
    print(*nums, sep="\n")


    return


# Generated by 2.5.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, a)

if __name__ == '__main__':
    main()

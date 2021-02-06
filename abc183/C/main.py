#!/usr/bin/env python3
import sys
import itertools

def solve(N: int, K: int, T: "List[List[int]]"):
    l = [i for i in range(1, N)]
    ans = 0
    for v in itertools.permutations(l):
        p = [0] + list(v) + [0]
        sum = 0
        for i in range(len(p) - 1):
            sum += T[p[i]][p[i + 1]]
        if sum == K :
            ans += 1
    print(ans)

    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    T = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, K, T)

if __name__ == '__main__':
    main()

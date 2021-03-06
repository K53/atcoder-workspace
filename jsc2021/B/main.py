#!/usr/bin/env python3
import sys


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    nums = [0] * (10 ** 3 + 1)
    for aa in A:
        nums[aa] = 1
    for bb in B:
        nums[bb] ^= 1
    ans = []
    for n in range(10 ** 3 + 1):
        if nums[n]:
            ans.append(n) 
    if len(ans) == 0:
        print()
    else:
        print(*ans, sep=" ")
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, A, B)

if __name__ == '__main__':
    main()

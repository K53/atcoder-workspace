#!/usr/bin/env python3
import sys


def solve(N: int, M: int, A: "List[int]", B: "List[int]", K: int, C: "List[int]", D: "List[int]"):
    res = 0
    for i in range(2 ** K):
        nums = [False] * 101
        for b in range(K):
            if i >> b & 1:
                nums[C[b]] = True
            else:
                nums[D[b]] = True
        ans = 0
        for aa, bb in zip(A, B):
            if nums[aa] & nums[bb]:
                ans += 1
        res = max(res, ans)
    print(res)
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
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    K = int(next(tokens))  # type: int
    C = [int()] * (K)  # type: "List[int]"
    D = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        C[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(N, M, A, B, K, C, D)

if __name__ == '__main__':
    main()

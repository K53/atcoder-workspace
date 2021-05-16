#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]", B: "List[int]"):
    diff = 0
    sums = []
    for aa, bb in zip(A, B):
        diff += aa
        sums.append(2 * aa + bb)
    sums.sort(reverse=True)
    count = 0
    for s in sums:
        count += 1
        diff -= s
        if diff < 0:
            print(count)
            return
    return




# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    nums = [0] * (N + 1)
    for aa in A:
        nums[aa] += 1
    all = 0
    for i in nums:
        all += i * (i - 1) // 2
    for aa in A:
        print(all - (nums[aa] - 1))

# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()

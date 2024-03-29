#!/usr/bin/env python3
import sys


def solve(N: int, M: int, l: "List[int]", r: "List[int]"):
    nums = [0] * (M + 1 + 1)
    for ll, rr in zip(l, r):
        nums[ll] += 1
        nums[rr + 1] -= 1
    for i in range(1, M + 1 + 1):
        nums[i] += nums[i - 1]
    nums = nums[:-1]
    print(nums)
    for i in range(1, M + 1):
        ans = 0
        for j in range(0, M + 1, i):
            ans += nums[j]
        print(ans)
    return


# Generated by 2.8.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    l = [int()] * (N)  # type: "List[int]"
    r = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
    solve(N, M, l, r)

if __name__ == '__main__':
    main()

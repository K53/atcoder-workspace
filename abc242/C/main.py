#!/usr/bin/env python3
import sys

MOD = 998244353  # type: int

# 0 -> number 1

def solve(N: int):
    nums = [1] * 9
    for _ in range(N - 1):
        # print(nums)
        new = [(nums[0] + nums[1]) % MOD]
        for i in range(0,7):
            new.append((nums[i] + nums[i + 1] + nums[i + 2]) % MOD)
        new.append((nums[7] + nums[8]) % MOD)
        nums = new
    print(sum(nums) % MOD)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
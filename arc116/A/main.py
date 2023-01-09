#!/usr/bin/env python3
import sys


def solve(T: int, case: "List[int]"):
    for c in case:
        if c % 2 == 1:
            print("Odd")
            continue
        if (c - 2) % 4 == 0:
            print("Same")
            continue
        print("Even")
    return

# 奇数 * 奇数
# 奇数 * 偶数
# 偶数 * 偶数

# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    T = int(next(tokens))  # type: int
    case = [int(next(tokens)) for _ in range(T)]  # type: "List[int]"
    solve(T, case)

if __name__ == '__main__':
    main()

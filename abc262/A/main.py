#!/usr/bin/env python3
import sys


def solve(Y: int):
    for i in range(4):
        if (Y + i) % 4 == 2:
            print(Y + i) 
            return
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    Y = int(next(tokens))  # type: int
    solve(Y)

if __name__ == '__main__':
    main()

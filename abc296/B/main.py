#!/usr/bin/env python3
import sys

k = "abcdefgh"

def solve(S: "List[str]"):
    for i in range(8):
        for j in range(8):
            if S[i][j] == "*":
                print(k[j] + str(8 - i))
                return
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = [next(tokens) for _ in range(8)]  # type: "List[str]"
    solve(S)

if __name__ == '__main__':
    main()
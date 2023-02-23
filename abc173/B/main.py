#!/usr/bin/env python3
import sys
from collections import Counter

def solve(N: int, S: "List[str]"):
    l = Counter(S)
    print(f"AC x {l['AC']}")
    print(f"WA x {l['WA']}")
    print(f"TLE x {l['TLE']}")
    print(f"RE x {l['RE']}")
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)

if __name__ == '__main__':
    main()

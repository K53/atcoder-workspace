#!/usr/bin/env python3
import sys


def solve(S: str):
    from itertools import groupby
    def runLengthEncode(S: str) -> "List[tuple(str, int)]":
        grouped = groupby(S)
        res = []
        for k, v in grouped:
            res.append((k, int(len(list(v)))))
        return res
    print(len(runLengthEncode(S)) - 1)
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)

if __name__ == '__main__':
    main()

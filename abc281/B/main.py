#!/usr/bin/env python3
import sys


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(S: str):
    if len(S) != 8:
        print(NO)
        return
    if not (S[0].isupper() and S[-1].isupper()):
        print(NO)
        return
    try:
        if len(str(int(S[1:-1]))) == 6:
            print(YES)
            return
        else:
            print(NO)
            return
    except:
        print(NO)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
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

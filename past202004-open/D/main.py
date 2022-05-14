#!/usr/bin/env python3
import sys

def solve(S: str):
    T = set()
    for i in range(len(S) - 2):
        target = S[i:(i + 3)]
        if target in T:
            continue
        T.add(target)
        T.add("...")
        T.add("." + target[1:])
        T.add(target[0] + "." + target[-1])
        T.add(target[:-1] + ".")
        T.add(".." + target[-1])
        T.add("." + target[1] + ".")
        T.add(target[0] + "..")
    # print(T)
    T2 = set()
    for i in range(len(S) - 1):
        target = S[i:(i + 2)]
        if target in T2:
            continue
        T.add(target)
        T.add("..")
        T.add("." + target[-1])
        T.add(target[0] + ".")
    # print(T2)
    T1l = len(set(S)) + 1
    print(T1l + len(T2) + len(T))
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
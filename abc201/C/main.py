#!/usr/bin/env python3
import sys
import itertools

def solve(S: str):
    must = []
    cand = []
    for i in range(10):
        if S[i] == "o":
            must.append(i)
        elif S[i] == "?":
            cand.append(i)
    if len(must) > 4:
        print(0)
        return
    cand.extend(must)
    lest = 4 - len(must)
    ans = set()
    for l in itertools.combinations_with_replacement(cand, lest):
        ans |= set(itertools.permutations(must + list(l)))
    print(len(ans))
    
    return


# Generated by 2.3.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
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
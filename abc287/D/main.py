#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(S: str, T: str):
    # S = "a?"
    # T = "a"
    ngs = set()
    ans = []
    lt = len(T)
    Szz = S[-lt:]
    for i in range(lt):
        ss, tt = Szz[i], T[i]
        if not (ss == "?" or tt == "?" or ss == tt):
            ngs.add(i)
    # print(ngs)
    if len(ngs) == 0:
        ans.append(YES)
    else:
        ans.append(NO)

    for i in range(lt):
        # e = Szz[i]
        a = S[i]
        # if e == a:
        #     ans.append(ans[-1])
        #     continue
        if a == "?" or T[i] == "?" or a == T[i]:
            if i in ngs:
                ngs.remove(i)
            if len(ngs) == 0:
                ans.append(YES)
            else:
                ans.append(NO)
        else:
            ngs.add(i)
            ans.append(NO)
            
    print(*ans, sep="\n")

        
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    solve(S, T)

if __name__ == '__main__':
    main()
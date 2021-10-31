#!/usr/bin/env python3
import sys


def solve(N: int, H: int, a: "List[int]", b: "List[int]"):
    ma = max(a)
    b.sort(reverse=True)
    ans = 0
    for bb in b:
        if bb < ma:
            break
        H -= bb
        ans += 1
        if H <= 0:
            print(ans)
            return
    p, q = divmod(H, ma)
    if q > 0:
        p += 1
    ans += p
    print(ans)
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, H, a, b)

if __name__ == '__main__':
    main()

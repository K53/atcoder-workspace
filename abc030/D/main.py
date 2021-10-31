#!/usr/bin/env python3
import sys

def solve(N: int, a: int, k: int, b: "List[int]"):
    l = []
    s = [-1] * N
    now = a - 1
    count = 0
    for _ in range(N):
        if s[b[now] - 1] == -1:
            l.append(b[now] - 1)
            s[b[now] - 1] = count
            count += 1
            now = b[now] - 1
        else:
            break
    cycle = l[s[b[now] - 1]:]
    c = len(l)
    # print(l)
    # print(cycle)
    # print(s[b[now] - 1])
    if k - 1 < s[b[now] - 1]:
        print(l[k - 1] + 1)
        return
    rest = (k - 1 - s[b[now] - 1]) % c
    print(cycle[rest] + 1)
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = int(next(tokens))  # type: int
    k = int(next(tokens))  # type: int
    b = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a, k, b)

if __name__ == '__main__':
    main()

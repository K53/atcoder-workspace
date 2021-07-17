#!/usr/bin/env python3
import sys

def solve(N: int, K: int, c: "List[int]"):
    from collections import defaultdict
    d = defaultdict(int)
    # N = 1
    # K = 1
    # c = [1]
    now = len(set(c[:K]))
    ans = now
    for i in c[:K]:
        d[i] += 1
    # for i in d.items():
    #     print(i)
    # print("###")
    for i in range(N - K):
        if d[c[K + i]] == 0:
            now += 1
        d[c[K + i]] += 1
        d[c[i]] -= 1
        if d[c[i]] == 0:
            now -= 1
        ans = max(ans, now)
        # print(c[i], c[K + i])
        # for i in d.items():
        #     print(i)
        # print("###")
        # print(ans)
    print(ans)
    return


# Generated by 2.5.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    c = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, c)

if __name__ == '__main__':
    main()

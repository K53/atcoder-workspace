#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, K: int, A: "List[int]", Q: int, l: "List[int]", r: "List[int]"):
    l = [i - 1 for i in l]
    r = [i - 1 for i in r]
    d = [0] * K
    for i in range(N):
        d[i % K] += A[i]
    print(d)
    for i in range(Q):
        print(d[(l[i] + 1) % K])
        print(d[r[i] % K])
    return
    # A = [-16 ,4 ,21, 21]
    # N = 4
    # K = 4
    # Q = 1
    # l = [1]
    # r = [4]
    l = [i - 1 for i in l]
    r = [i - 1 for i in r]
    # from collections import defaultdict
    # lr = sorted([(ll - 1, rr - 1) for ll, rr in zip(l, r)])
    # d = defaultdict(list)
    # for k, v in lr:
    #     d[k].append(v)

    # for st, query in d.items():

    #     target = A[st]
    #     for kk in range(K):
    #         A[st + kk] -= target
    for i in range(Q):
        pp = 0
        for kk in range(N):
            if r[i] - K * kk < l[i]:
                break
            pp += A[r[i] - K * kk]
        print(pp)
        qq = 0
        for kk in range(N):
            if l[i] + K * kk > r[i]:
                break
            qq += A[l[i] + K * kk]
        print(qq)
        if pp == qq:
            print(YES)
        else:
            print(NO)

    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    Q = int(next(tokens))  # type: int
    l = [int()] * (Q)  # type: "List[int]"
    r = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
    solve(N, K, A, Q, l, r)

if __name__ == '__main__':
    main()

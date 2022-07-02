#!/usr/bin/env python3
from bisect import bisect_left
from itertools import accumulate
import sys

MOD = 1  # type: int


def solve(N: int, Q: int, X: int, W: "List[int]", K: "List[int]"):
    acc = list(accumulate(W))
    # print(acc)
    l = [-1]
    nums = []
    search = X
    exists = set()
    prefix = -1
    for _ in range(N * 2):
        idx = bisect_left(acc, search)
        if idx in exists:
            # print("#", idx, l.index(idx))
            if idx - l[-1] == 0:
                nums.append(N)
            else:
                nums.append(idx + N - l[-1] if idx - l[-1] < 0 else idx - l[-1])
            l.append(idx)
            prefix = l.index(idx)
            break
        # print(idx, acc[idx])
        nums.append(idx + N - l[-1] if idx - l[-1] < 0 else idx - l[-1])
        l.append(idx)
        exists.add(idx)
        search = acc[idx] + X
        search %= acc[-1]
        # print("search", search)
    # print(l)
    # print(nums)

    # 先頭削除 -1 しない 個数なので
    # loop -= 1
    loop = nums[prefix:]
    itr = len(loop)
    # print(prefix)
    # print(itr)
    # print(loop)

    for kk in K:
        kk -= 1
        if kk >= prefix:
            kk -= prefix
            kk %= itr
            # print(kk, "#")
            print(loop[kk])
        else:
            # print(kk, "##")
            print(nums[kk])


    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    W = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    K = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, Q, X, W, K)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import sys


def solve(M: int, a: "List[int]", b: "List[int]", p: "List[int]"):
    for i in range(1, 10):
        if not i in p:
            emp = i
            break
    from itertools import permutations
    d = dict()
    for i, pp in enumerate(permutations(p + [emp])):
        d[tuple(pp)] = i
    # print(d[tuple(p + [emp])])
    change = [[] for _ in range(9)]
    for i in range(M):
        change[a[i] - 1].append(b[i] - 1)
        change[b[i] - 1].append(a[i] - 1)

    # print(change)
    from collections import deque
    from copy import deepcopy
    INF = 10 ** 16
    q = deque()
    dist = [INF] * 362880
    q.append(p + [emp])
    dist[d[tuple(p + [emp])]] = 0
    while q:
        now_l = q.popleft()
        num = now_l.index(emp)
        # print(num)
        for next_num in change[num]:
            # print(next_num)
            now_copy_l = [i for i in now_l]
            now_copy_l[num], now_copy_l[next_num] = now_copy_l[next_num], now_copy_l[num]
            next_d = d[tuple(now_copy_l)]
            now_d = d[tuple(now_l)]
            if dist[next_d] != INF:
                continue
            q.append(now_copy_l)
            dist[next_d] = dist[now_d] + 1
    ans = dist[d[(1,2,3,4,5,6,7,8,9)]]
    print(-1 if ans == INF else ans)
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    M = int(next(tokens))  # type: int
    u = [int()] * (M)  # type: "List[int]"
    v = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    p = [int(next(tokens)) for _ in range(8)]  # type: "List[int]"
    solve(M, u, v, p)

if __name__ == '__main__':
    main()
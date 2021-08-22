#!/usr/bin/env python3
import sys


def solve(n: int, m: int, s: int, t: int, u: "List[int]", v: "List[int]", a: "List[int]", b: "List[int]"):
    import heapq
    INF = 10 ** 18       # *2
    def dijkstra(edges: "List[List[(cost, to)]]", start_node: int) -> list:
        hq = []
        heapq.heapify(hq)
        # Set start info
        dist = [INF] * len(edges)
        heapq.heappush(hq, (0, start_node))
        dist[start_node] = 0            # *1
        # dijkstra
        while hq:
            min_cost, now = heapq.heappop(hq)
            if min_cost > dist[now]:
                continue
            for cost, next in edges[now]:
                if dist[next] > dist[now] + cost:
                    dist[next] = dist[now] + cost
                    heapq.heappush(hq, (dist[next], next))
        return dist
    Gy = [[] for _ in range(n)]
    Gs = [[] for _ in range(n)]
    for uu, vv, aa, bb in zip(u, v, a, b):
        Gy[uu - 1].append((aa, vv - 1))
        Gy[vv - 1].append((aa, uu - 1))
        Gs[uu - 1].append((bb, vv - 1))
        Gs[vv - 1].append((bb, uu - 1))
    dy = dijkstra(Gy, s - 1)
    ds = dijkstra(Gs, t - 1)
    ans = []
    least = INF
    for change in reversed(range(n)):
        k = dy[change] + ds[change]
        if least < k:
            ans.append(10 ** 15 - least)
        else:
            ans.append(10 ** 15 - k)
            least = k
    print(*ans[::-1], sep="\n")
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    m = int(next(tokens))  # type: int
    s = int(next(tokens))  # type: int
    t = int(next(tokens))  # type: int
    u = [int()] * (m)  # type: "List[int]"
    v = [int()] * (m)  # type: "List[int]"
    a = [int()] * (m)  # type: "List[int]"
    b = [int()] * (m)  # type: "List[int]"
    for i in range(m):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(n, m, s, t, u, v, a, b)

if __name__ == '__main__':
    main()

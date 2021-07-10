#!/usr/bin/env python3



# Generated by 2.5.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    INF = 10 ** 16
    def bfs(edges: "List[to]", start_node: int) -> list:
        q = set()
        dist = [INF] * len(edges)
        q.add(start_node)
        dist[start_node] = 0
        while len(q) != 0:
            now = q.pop()
            for next in edges[now]:
                if dist[next] != INF:
                    continue
                q.add(next)
                dist[next] = (dist[now] + 1) % 2
        return dist
    
    N, Q = map(int, input().split())
    nodes = [[] for _ in range(N)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        nodes[a - 1].append(b - 1)
        nodes[b - 1].append(a - 1)
    f = bfs(nodes, 0)
    # print(f)

    for i in range(Q):
        c, d = map(int, input().split())
        print("Town" if f[c-1] == f[d-1] else "Road")


if __name__ == '__main__':
    main()

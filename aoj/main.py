#!/usr/bin/env python3
INF = 10 ** 9

def bellmanFord(edges: "List[(from, to, to)]", vertex: int, start_node: int) -> list:
    # Initialize
    costs = [INF] * vertex
    costs[start_node] = 0
    for i in range(vertex * 2):
        for f, t, c in edges:
            if costs[f] != INF and costs[t] > costs[f] + c:
                # 始点/終点ともに到達可能な負の閉路がある。
                # if i == vertex - 1 and t == vertex - 1:
                #      return None
                # 始点/終点ともに到達可能な負の閉路がある。
                if i >= vertex - 1:
                    costs[t] = -INF
                # 始点から到達する負の閉路(終点に至るかはこの時点では不明)
                # if i == vertex - 1:
                #     return None
                else:
                    costs[t] = costs[f] + c
    return costs


def main():    
    V, E, r = map(int, input().split())
    edges = []
    for _ in range(E):
        s, t, d = map(int, input().split())
        edges.append((s, t, d))
    costs = bellmanFord(edges, V, r)
    
    if -INF in costs:
        print("NEGATIVE CYCLE")
        return
    
    for c in costs:
        print("INF" if c == INF else c)

if __name__ == '__main__':
    main()
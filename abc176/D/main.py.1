#!/usr/bin/env python3

def main():
    H, W = map(int, input().split())
    Cy, Cx = map(lambda i : int(i) - 1, input().split())
    Dy, Dx = map(lambda i : int(i) - 1, input().split())
    G = []
    for _ in range(H):
        G.append(input())
    from collections import deque
    q = deque()
    q.append((Cy, Cx))
    INF = 10 ** 9
    dist = [[INF] * W for _ in range(H)]
    seen = [[False] * W for _ in range(H)]
    dist[Cy][Cx] = 0
    while len(q) != 0:
        nowy, nowx = q.popleft()
        if seen[nowy][nowx]:
            continue
        seen[nowy][nowx] = True
        # if (nowy, nowx) == (Dy, Dx):
        #     break
        for dy in range(-2, 3):
            for dx in range(-2, 3):
                if dx == dy == 0:
                    continue
                nexty = nowy + dy
                nextx = nowx + dx
                if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W or G[nexty][nextx] == "#" or seen[nexty][nextx]:
                    continue
                if abs(dx) + abs(dy) == 1:
                    if dist[nexty][nextx] > dist[nowy][nowx]:
                        dist[nexty][nextx] = dist[nowy][nowx]
                        q.appendleft((nexty, nextx))
                else:
                    if dist[nexty][nextx] > dist[nowy][nowx] + 1:
                        dist[nexty][nextx] = dist[nowy][nowx] + 1
                        q.append((nexty, nextx))

    # print(dist)
    print(dist[Dy][Dx] if dist[Dy][Dx] != INF else -1)
    return


if __name__ == '__main__':
    main()



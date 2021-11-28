#!/usr/bin/env python3


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    H, W = map(int, input().split())
    G = []
    for _ in range(H):
        G.append(input())
    from collections import deque
    q = deque()
    INF = 10 ** 16
    dist = [[INF] * W for _ in range(H)]
    seen = [[False] * W for _ in range(H)]
    dist[0][0] = 0
    q.appendleft((0, 0))
    while len(q) != 0:
        nowy, nowx = q.popleft()
        if seen[nowy][nowx]:
            continue
        seen[nowy][nowx] = True

        # move
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nexty = nowy + dy
            nextx = nowx + dx
            if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W or G[nexty][nextx] == "#" or seen[nexty][nextx]:
                continue
            if dist[nexty][nextx] > dist[nowy][nowx]:
                dist[nexty][nextx] = dist[nowy][nowx]
                q.appendleft((nexty, nextx))
        
        # break
        for dy in range(-2, 3):
            for dx in range(-2, 3):
                nexty = nowy + dy
                nextx = nowx + dx
                if abs(dy) + abs(dx) == 4:
                    continue
                if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W or seen[nexty][nextx]:
                    continue
                if dist[nexty][nextx] > dist[nowy][nowx] + 1:
                    dist[nexty][nextx] = dist[nowy][nowx] + 1
                    q.append((nexty, nextx))
        
    print(dist[-1][-1])
    # print(dist)  
    return

if __name__ == '__main__':
    main()

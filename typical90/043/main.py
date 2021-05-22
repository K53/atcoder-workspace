#!/usr/bin/env python3


def main():
    INF = 10 ** 18
    import queue
    INF = 10 ** 9
    def bfs(field: "List[Lsit[]]", H: int, W: int, y: int, x: int) -> list:
        q = queue.Queue()
        dist = []
        for _ in range(H):
            dist.append([(INF, 0, 0)] * W)
        q.put((x, y))
        dist[y][x] = (0, 0, 0)
        while not q.empty():
            now_x, now_y= q.get()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_x, next_y = now_x + dx, now_y + dy
                if next_y < 0 or next_y >= H or next_x < 0 or next_x >= W or field[next_y][next_x] == "#" or dist[next_y][next_x][0] != INF:
                    continue
                q.put((next_x, next_y))
                if dist[now_y][now_x][1] == dist[now_y][now_x][2] == 0 or dist[now_y][now_x][1] == dx and dist[now_y][now_x][2] == dy:
                    dist[next_y][next_x] = (dist[now_y][now_x][0], dx, dy)
                else:
                    dist[next_y][next_x] = (dist[now_y][now_x][0] + 1, dx, dy)
        return dist
    H, W = map(int, input().split())
    rs, cs = map(lambda i: int(i) - 1, input().split())
    rt, ct = map(lambda i: int(i) - 1, input().split())
    field = []
    for _ in range(H):
        field.append(input())
    print(bfs(field, H, W, rs, cs)[rt][ct][0])

if __name__ == '__main__':
    main()

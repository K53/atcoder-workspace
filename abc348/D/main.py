#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10 ** 9)

YES = "Yes"  # type: str
NO = "No"  # type: str

def main():
    from collections import deque, defaultdict

    H, W = map(int, input().split())    
    A = [input() for _ in range(H)]
    N = int(input())
    # R, C, E = [], [], []
    medicine = defaultdict(lambda : defaultdict(int))
    for _ in range(N):
        rr, cc, ee = map(int, input().split())
        medicine[rr - 1][cc - 1] = ee
        # R.append(rr)
        # C.append(cc)
        # E.append(ee)
    
    start_hh, start_ww, goal_hh, goal_ww = -1, -1, -1, -1
    for hh in range(H):
        for ww in range(W):
            if A[hh][ww] == "S":
                start_hh = hh
                start_ww = ww
            elif A[hh][ww] == "T":
                goal_hh = hh
                goal_ww = ww

    # used = 
    # dist = [[0] * W for _ in range(H)]
    stk = deque()
    stk.append((start_hh, start_ww, 0, deque(), [[0] * W for _ in range(H)]))
    count = 0
    while len(stk) > 0:
        count += 1
        if count > 50:
            exit()
        cur_hh, cur_ww, cur_life, used, is_used, dist = stk.pop()
        print("----")
        print(cur_hh + 1, cur_ww + 1, cur_life, "M:", medicine[cur_hh][cur_ww])
        for i in range(H):
            print(dist[i])
        print("----")
        if cur_hh == goal_hh and cur_ww == goal_ww:
            print(YES)
        is_used = False
        if (cur_hh, cur_ww) not in used and medicine[cur_hh][cur_ww] > cur_life:
            cur_life = medicine[cur_hh][cur_ww]
            print("get!!! ->", cur_life)
            used.append((cur_hh, cur_ww))
            is_used = True
        
        if cur_life == 0:
            continue
        go = False
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nexty = cur_hh + dy
            nextx = cur_ww + dx
            if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W or dist[nexty][nextx] > cur_life - 1 or A[nexty][nextx] == "#":
                continue
            # prev = dist[nexty][nextx]
            dist[nexty][nextx] = cur_life - 1
            go = True
            stk.append((nexty, nextx, cur_life - 1, used, is_used, prev_dist dist[nexty][nextx]))
            # dist[nexty][nextx] = prev
        if not go:
            if is_used:
                used.pop()
        dist[cur_hh][cur_ww] = prev_dist


    def dfs(cur_hh, cur_ww, cur_life):
        # print("----")
        # print(cur_hh + 1, cur_ww + 1, cur_life, "M:", medicine[cur_hh][cur_ww])
        # for i in range(H):
        #     print(dist[i])
        # print("----")
        is_used = False
        if cur_hh == goal_hh and cur_ww == goal_ww:
            print(YES)
            exit()
        if (cur_hh, cur_ww) not in used and medicine[cur_hh][cur_ww] > cur_life:
            cur_life = medicine[cur_hh][cur_ww]
            # print("get!!! ->", cur_life)
            used.append((cur_hh, cur_ww))
            is_used = True
        if cur_life == 0:
            return 0
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nexty = cur_hh + dy
            nextx = cur_ww + dx
            nextlife = cur_life - 1
            if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W or dist[nexty][nextx] > nextlife or A[nexty][nextx] == "#":
                nextlife = cur_life
                continue
            prev = dist[nexty][nextx]
            dist[nexty][nextx] = nextlife
            dfs(nexty, nextx, nextlife)
            dist[nexty][nextx] = prev
            nextlife = cur_life
        if is_used:
            used.pop()
        return

    # dfs(start_hh, start_ww, 0)
    print(NO)

if __name__ == '__main__':
    main()

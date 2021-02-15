#!/usr/bin/env python3
import queue

def main():    
    q = queue.Queue()
    n = int(input())
    d = [-1] * n
    ll = [0] * n
    for _ in range(n):
        inp = list(map(int, input().split()))
        u = inp.pop(0)
        k = inp.pop(0)
        ll[u - 1] = inp
    
    d[0] = 0
    q.put(0)
    while not q.empty():
        target = q.get()
        for i in ll[target]:
            if d[i - 1] != -1:
                continue
            d[i - 1] = d[target] + 1
            q.put(i - 1)
    for i, val in enumerate(d, 1):
        print(i, val)

if __name__ == '__main__':
    main()

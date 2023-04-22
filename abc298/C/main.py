#!/usr/bin/env python3
import heapq
from collections import defaultdict

# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    N = int(input())
    Q = int(input())
    d = defaultdict(list)
    # query = []
    ctod = defaultdict(set)
    for _ in range(Q):
        t, *args = map(int, input().split())
        if t == 1:
            heapq.heappush(d[args[1]], args[0])
            ctod[args[0]].add(args[1])
        elif t == 2:
            ans = []
            for _ in range(len(d[args[0]])):
                num = heapq.heappop(d[args[0]])
                ans.append(num)
            d[args[0]] = ans
            heapq.heapify(d[args[0]])
            print(*ans)
        else:
            # ans = set()
            print(*sorted(list(ctod[args[0]])))




if __name__ == '__main__':
    main()
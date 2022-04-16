#!/usr/bin/env python3


from collections import deque


def main():
    Q = int(input())
    d = deque()
    for i in range(Q):
        query = input().split()
        if query[0] == "1":
            d.append([query[1], int(query[-1])])
        else:
            rest = int(query[1])
            ans = [0] * 26
            while rest > 0:
                if len(d) == 0:
                    rest = 0
                    continue
                c, x = d.popleft()
                if rest >= x:
                    ans[ord(c) - ord("a")] += x
                    rest -= x
                else:
                    ans[ord(c) - ord("a")] += rest
                    d.appendleft([c, x - rest])
                    rest = 0
            res = 0
            # print(ans)
            for i in ans:
                res += i ** 2
            print(res)
    return

if __name__ == '__main__':
    main()

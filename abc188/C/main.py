#!/usr/bin/env python3


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    from collections import deque
    N = int(input())
    A = list(map(int, input().split()))
    q = deque(A)
    while len(q) > 2:
        aa = q.popleft()
        bb = q.popleft()
        q.append(max(aa, bb))
    aa = q.popleft()
    bb = q.popleft()
    print(A.index(min(aa, bb)) + 1)

    # Failed to predict input format
    pass

if __name__ == '__main__':
    main()

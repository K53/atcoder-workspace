#!/usr/bin/env python3
def main():
    N, S = map(int, input().split())
    ans = []
    for i in range(N, 0, -1):
        if S - i > 0:
            ans.append(i)
            S -= i
        elif S - i == 0:
            ans.append(i)
            S -= i
            break
    print(len(ans))
    print(*ans[::-1], sep=" ")
    return

if __name__ == '__main__':
    main()
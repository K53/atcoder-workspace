#!/usr/bin/env python3
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    even = [A[i] for i in range(N) if i % 2 == 1]
    idx = even[]
    print(sum(sorted(A[1:])[::-1][:K]))
    return

if __name__ == '__main__':
    main()
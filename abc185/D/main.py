#!/usr/bin/env python3
import math

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(1)
        return
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A + [N + 1]
    nums = []
    for i in range(M + 1):
        if A[i + 1] - A[i] - 1 != 0:
            nums.append(A[i + 1] - A[i] - 1)
    nums.sort()
    if len(nums) == 0:
        print(0)
        return
    k = nums[0]
    ans = 0
    for n in nums:
        ans += math.ceil(n / k)
    print(ans)

if __name__ == '__main__':
    main()

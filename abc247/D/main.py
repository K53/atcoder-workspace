#!/usr/bin/env python3
import bisect

def main():
    Q = int(input())
    smallcontent = []
    smallnum = []
    offsetsum = 0
    sums = [0]
    nums = [0]
    offsetnum = 0
    has = [0, 0]
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x, c = query[1], query[2]
            m = x * c
            smallcontent.append(x)
            smallnum.append(c)
            sums.append(sums[-1] + m)
            nums.append(nums[-1] + c)
        else:
            c = query[1]
            if has[-1] >= c:
                res = has[0] * c
                print(res)
                has[-1] -= c # あまりを減らす。
            else:
                res = has[-1] * has[0]  # あまりを全部取得
                need = c - has[-1] # あまり分を要求から減算
                idx = bisect.bisect_left(nums, c + offsetnum)
                print("idx", idx)
                target = smallcontent[idx - 1]
                print("target", target)
                print(smallnum[idx - 1]) # こしかない
                if need > smallnum[idx - 1]:
                    
                    pass
                res += target * need
                print(res)
                has = [target, nums[idx] - need] # あまりとして保持
                print(has)
            offsetnum += c

  

            print()      
            print(smallcontent)
            print(smallnum)
            print(sums)
            print(nums)
            print(offsetsum)
            print(offsetnum)
            print()

        
        
if __name__ == '__main__':
    main()

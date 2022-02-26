#!/usr/bin/env python3


class SegmentTree:
    def __init__(self, initVal: int, bottomLen: int, func: "function(int, int)"):
        self.initVal = initVal
        self.func = func
        self.bottomLen = bottomLen
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [initVal] * self.segLen

    """ 一点加算
    tree[index] += val
    """
    def pointAdd(self, index: int, val: int):
        segIndex = index + self.offset
        self.tree[segIndex] += val # Add
        while True:
            segIndex //= 2
            if segIndex == 0:
                break
            self.tree[segIndex] = self.func(self.tree[segIndex * 2], self.tree[segIndex * 2 + 1])
    
    """ 一点更新
    tree[index] = val
    """
    def pointUpdate(self, index: int, val: int):
        segIndex = index + self.offset
        self.tree[segIndex] = val # Update # 更新方法も変更が必要な場合は書き換えること。 eg.) XOR演算など |= val
        while True:
            segIndex //= 2
            if segIndex == 0:
                break
            self.tree[segIndex] = self.func(self.tree[segIndex * 2], self.tree[segIndex * 2 + 1])

    """ 区間最小値 (RMQ)
    """
    def rangeQuery(self, l: int, r: int):
        l += self.offset
        r += self.offset
        res = self.initVal
        while l < r:
            if l % 2 == 1:
                res = self.func(res, self.tree[l])
                l += 1
            l //= 2
            if r % 2 == 1:
                res = self.func(res, self.tree[r - 1])
                r -= 1
            r //= 2
        return res

    # def queryKthItem(self, K: int):
    #     index = 1
    #     restK = K
    #     while index < self.offset:
    #         if restK <= self.tree[2 * index]:
    #             index = 2 * index
    #         else:
    #             restK -= self.tree[2 * index] # 左に進む場合は右側の分を差し引く。
    #             index = 2 * index + 1
    #     return index - self.offset




# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    Q = int(input())
    query = []
    nums = []
    for _ in range(Q):
        ll = list(map(int, input().split()))
        query.append(ll)
        # if ll[0] == 1:
        nums.append(ll[1])
    compressed = {}
    compressed_to_raw = []
    for index, val in enumerate(sorted(list(set(nums)))):
        compressed[val] = index
        compressed_to_raw.append(val)
    # print(compressed)
    def add(x: int, y: int):
        return x + y
    
    seg = SegmentTree(0, len(compressed), add)
    for qq in query:
        if qq[0] == 1:
            seg.pointAdd(compressed[qq[1]], 1)
            # print(seg.tree[seg.offset:])
        elif qq[0] == 2:
            ok = 0
            ng = compressed[qq[1]] + 1
            if seg.rangeQuery(ok, ng) < qq[2]:
                print(-1)
                continue
            while abs(ok - ng) > 1:     # 終了条件（差が1となり境界を見つけた時)
                mid = (ok + ng) // 2
                # print("target > ", mid)
                result = seg.rangeQuery(mid, compressed[qq[1]] + 1)
                # print(result)
                if result >= qq[2]:
                    ok = mid            # midが条件を満たすならmidまではokなのでokの方を真ん中まで持っていく
                else:
                    ng = mid            # midが条件を満たさないならmidまではngなのでngの方を真ん中まで持っていく
                # print(ok, ng)          # 半分に切り分ける毎の2値の状態
            print(compressed_to_raw[ok])
        else:
            ok = seg.bottomLen
            ng = compressed[qq[1]]
            if seg.rangeQuery(ng, ok) < qq[2]:
                print(-1)
                continue
            while abs(ok - ng) > 1:     # 終了条件（差が1となり境界を見つけた時)
                mid = (ok + ng) // 2
                # print("target > ", mid)
                result = seg.rangeQuery(compressed[qq[1]], mid)
                # print(result)
                if result >= qq[2]:
                    ok = mid            # midが条件を満たすならmidまではokなのでokの方を真ん中まで持っていく
                else:
                    ng = mid            # midが条件を満たさないならmidまではngなのでngの方を真ん中まで持っていく
                # print(ok, ng)          # 半分に切り分ける毎の2値の状態
            print(compressed_to_raw[ok - 1])

    return
if __name__ == '__main__':
    main()

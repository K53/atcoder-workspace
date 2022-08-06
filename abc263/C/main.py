#!/usr/bin/env python3
from copy import deepcopy
import sys
sys.setrecursionlimit(10 ** 9)

def solve(N: int, M: int):
    ans = []
    def dfs(acc: list):
        nonlocal ans
        # --- 探索終了条件 ----------------------------
        if len(acc) > N:
            # print("#", acc)
            ans.append(acc)
            return
        # --- 次の探索(分岐) --------------------------
        for mm in range(acc[-1] + 1, M + 1): # 0なしMまで
            # print(acc, mm)
            cpacc = deepcopy(acc)
            cpacc.append(mm)
            dfs(cpacc)
        return
    dfs([0])
    # print(ans)
    for aa in ans:
        print(*aa[1:], sep=" ")
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(N, M)

if __name__ == '__main__':
    main()

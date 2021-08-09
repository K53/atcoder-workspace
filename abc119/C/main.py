#!/usr/bin/env python3
import sys


def solve(N: int, A: int, B: int, C: int, l: "List[int]"):
    flg = [-1] * N
    ans = 10 ** 16
    def dfs(target: int):
        nonlocal ans
        a = b = c = 0
        count = 0
        # --- 探索終了条件 ----------------------------
        if target == N: # 全ての竹をアサインし終えたら
            for i in range(N):
                if flg[i] == 0:
                    a += l[i]
                    count += 1
                elif flg[i] == 1:
                    b += l[i]
                    count += 1
                elif flg[i] == 2:
                    c += l[i]
                    count += 1
            if a == 0 or b == 0 or c == 0:
                return
            # print(ans)
            ans = min(ans, abs(A - a) + abs(B - b) + abs(C - c) + count * 10 - 30) 
            return
        # --- カウントアップ条件 -----------------------
        # なし
        
        # --- 次の探索(分岐) --------------------------
        for i in range(4):
            flg[target] = i
            dfs(target + 1)
    dfs(0)
    print(ans)
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    l = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B, C, l)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import sys


def solve(N: int, K: int, s: "List[int]"):
    if 0 in s:
        print(N)
        return
    r = 0
    l = 0
    ans = 0
    mul = 1
    for _ in range(N):
        # 行けるだけrを進める。条件を満たさなくなったところで抜ける。※抜ける時sumは条件を満たしていない。
        while r < N and mul <= K:
            # print("#", l, r, mul)
            mul *= s[r]
            r += 1
        # → 条件を満たしていない状態をlを進めることで修正する。
        # ifの前でansに対する更新を試みてはいけない理由→この時点では条件を満たしていないから。
        # ifを構えるのはwhileを抜ける理由がrの上限だった場合。lを縮める必要がないから。
        if l == r:
            l += 1
            r += 1
            continue
        if mul > K:
            # print(">", l, r, mul) # rを含まないのでr=N+1までは来る。
            mul //= s[l]
            l += 1
            ans = max(ans, r - l)
    ans = max(ans, r - l) # 一度もlを縮めることがないケースではansに到達しないため最後にansの更新を入れる必要あり。 ansがlに依存する問題では入れること。
    print(ans)
    return
    
# Generated by 2.11.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    s = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, s)

if __name__ == '__main__':
    main()

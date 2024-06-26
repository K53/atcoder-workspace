#!/usr/bin/env python3
import sys

    

def solve(N: int, A: int, B: int, C: int, l: "List[int]"):
    abc = [A, B, C]
    ans = 10 ** 9
    def dfs(depth: int, group: list):
        nonlocal ans
        if depth == N:
            tmp = 0
            for i in range(3):
                if len(group[i]) == 0:
                    return
                tmp += (len(group[i]) - 1) * 10
                s = sum(group[i])
                tmp += abs(abc[i] - s)
            ans = min(ans, tmp)
            return 
        for i in range(4):
            group[i].append(l[depth])
            dfs(depth + 1, group)
            group[i].remove(l[depth])
        return

    dfs(0, [[] for _ in range(4)])
    print(ans)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
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

#!/usr/bin/env python3
import sys
import queue

YES = "Yes"  # type: str
NO = "No"

def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    nodes = [[] for _ in range(N + 1)]
    direction = [0, 0] + [-1] * (N - 1)
    q = queue.Queue()
    q.put(1)
    for i in range(M):
        nodes[A[i]].append(B[i])
        nodes[B[i]].append(A[i])
    while not q.empty():
        n = q.get()
        for i in nodes[n]:
            if direction[i] == -1:
                direction[i] = n
                q.put(i)
    if -1 in direction[2:]:
        print(NO)
    else:
        print(YES)
        print(*direction[2:], sep="\n")
    
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)

if __name__ == '__main__':
    main()
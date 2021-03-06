#!/usr/bin/env python3
import sys
import queue

def solve(K: int):
    q = queue.Queue()
    for i in range(1, 10):
        q.put(i)
    loop = 0
    next = 0
    while loop < K:
        next = q.get()
        loop += 1
        if str(next)[-1] == "0":
            q.put(next * 10)
            q.put(next * 10 + 1)
        elif str(next)[-1] == "9":
            q.put(next * 10 + 8)
            q.put(next * 10 + 9)
        else:
            l = int(str(next)[-1])
            q.put(next * 10 + l - 1)
            q.put(next * 10 + l)
            q.put(next * 10 + l + 1)
    print(next)
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    solve(K)

if __name__ == '__main__':
    main()

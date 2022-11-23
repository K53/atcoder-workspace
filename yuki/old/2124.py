#!/usr/bin/env python3
import string

def main():
    ans = []
    N = int(input())
    tot = (1 + N) * N // 2
    print(f"? 2 {N}", flush=True)
    res = int(input())
    ans.append(str(tot - res))
    acc = tot - res
    for i in range(1, N - 1):
        print(f"? {i} {i + 1}", flush=True)
        res = int(input())
        r = res - int(ans[-1])
        ans.append(str(r))
        acc += r
    ans.append(str(tot - acc))
    l = " ".join(ans)
    print(f"! {l}")
    return

if __name__ == '__main__':
    main()
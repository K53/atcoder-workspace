#!/usr/bin/env python3


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    N, M, Q = map(int, input().split())
    W, V = [], []
    for _ in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    X = list(map(int, input().split()))
    l = []
    for m in range(M):
        internal = []
        for n in range(N):
            if W[n] <= X[m]:
                internal.append(V[n])
            else:
                internal.append(0)
        l.append([X[m], internal])
    # print(l)

    for q in range(Q):
        L, R = map(lambda i: int(i) - 1, input().split())
        target = []
        if L == 0 and R == M - 1:
            print(0)
            continue
        elif L == 0:
            target = l[R + 1:]
        elif R == M - 1:
            target = l[:L]
        else:
            target = l[:L] + l[R + 1:]
        target.sort()
        # print(target)
        ans = 0
        for i in range(len(target)):
            # print(target[i])
            if len(target[i][1]) == 0:
                continue
            mx = max(target[i][1])
            # print("##")
            # print(mx)
            # print("##")
            ans += mx
            if mx != 0:
                for j in range(len(target)):
                    try:
                        # print(target[j])
                        target[j][1].remove(mx)
                    except ValueError:
                        pass
        print(ans)
             






if __name__ == '__main__':
    main()

#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    H1, W1 = map(int, input().split())
    A = []
    for _ in range(H1):
        A.append(list(map(int, input().split()))) 
    H2, W2 = map(int, input().split())
    B = []
    for _ in range(H2):
        B.append(list(map(int, input().split()))) 
    res = []
    nowA = 0
    for bb in B:
        for la in range(nowA, len(A)):
            aa = A[la]
            if set(bb) <= set(aa):
                tmp = []
                for bbb in bb:
                    tmp.append(aa.index(bbb))
                if tmp != sorted(tmp):
                    print(NO)
                    return
                res.append(tmp)
                nowA = la + 1
                break
            else:
                # print("kip", aa)
                pass

    if len(res) != len(B):
        print(NO)
        return
    for ss in res:
        for sss in res:
            if ss != sss:
                print(NO)
                return
    print(YES)
    return

if __name__ == '__main__':
    main()
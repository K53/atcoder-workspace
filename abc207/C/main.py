#!/usr/bin/env python3




# Generated by 2.5.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def endCheck(i, j):
        k1, s1, t1 = i
        k2, s2, t2 = j
        if s2 < t1:
            return True
        if s2 == t1 and (k1 == 1 or k1 == 3) and (k2 == 1 or k2 == 2):
            return True
        return False 

    def startCheck(i, j):
        k1, s1, t1 = i
        k2, s2, t2 = j
        if s1 < t2:
            return True
        if s1 == t2 and (k1 == 1 or k1 == 2) and (k2 == 1 or k2 == 3):
            return True
        return False 

    N = int(input())
    v = []
    for _ in range(N):
        t, i, j = map(int, input().split())
        v.append((t, i, j))
    # print(v)

    count = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if startCheck(v[i], v[j]) and endCheck(v[i], v[j]):
                count += 1
                # print(v[i], v[j])
    print(count)


            

    # Failed to predict input format
    pass

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
INF = 10 ** 10

# def g(A, queries):
#     l = [i for i in A]
#     for qq in queries:
#         if qq[0] == 1:
#             idx = l.index(qq[1])
#             l.insert(idx + 1, qq[2])
#         else:
#             l.remove(qq[1])
#     return l

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    nums = set(A)
    nums.add(-1)
    for _ in range(Q):
        l = list(map(int, input().split()))
        queries.append(l)
        if l[0] == 1:
            nums.add(l[2])

    raw_to_compressed = {}
    compressed_to_raw = []
    for index, val in enumerate(sorted(list(nums))):
        raw_to_compressed[val] = index
        compressed_to_raw.append(val)
    
    top = raw_to_compressed[A[0]]
    bivec = [[INF, INF] for _ in range(len(raw_to_compressed) + 1)]
    tmpA = [-1] + A + [-1]
    for i in range(1, N + 1):
        # print(raw_to_compressed[tmpA[i]])
        # print(raw_to_compressed[tmpA[i]], bivec[raw_to_compressed[tmpA[i]]])
        # print(raw_to_compressed[tmpA[i]], bivec[raw_to_compressed[tmpA[i]]], raw_to_compressed[tmpA[i - 1]])
        # print(raw_to_compressed[tmpA[i]], bivec[raw_to_compressed[tmpA[i]]], raw_to_compressed[tmpA[i - 1]], raw_to_compressed[tmpA[i + 1]])
        bivec[raw_to_compressed[tmpA[i]]] = [raw_to_compressed[tmpA[i - 1]], raw_to_compressed[tmpA[i + 1]]]

    # print(raw_to_compressed)
    # print(tmpA)
    # print(bivec)
    for qq in queries:
        if qq[0] == 1:
            x, y = raw_to_compressed[qq[1]], raw_to_compressed[qq[2]]
            _, back = bivec[x][0], bivec[x][1]
            bivec[x][1] = y
            if back != raw_to_compressed[-1]:
                bivec[back][0] = y
            bivec[y] = [x, back]
        else: 
            x = raw_to_compressed[qq[1]]
            front, back = bivec[x][0], bivec[x][1]
            if front != raw_to_compressed[-1]:
                bivec[front][1] = back
            if back != raw_to_compressed[-1]:
                bivec[back][0] = front
            bivec[x] = [INF, INF]
            if top == x:
                top = back
        # print(bivec)

    ans = [compressed_to_raw[top]]
    # print(top)
    while True:
        back = bivec[top][1]
        if back == raw_to_compressed[-1]:
            break
        ans.append(compressed_to_raw[back])
        top = back
    print(*ans)

    # gans = g(A, queries)
    # print(*gans)



if __name__ == '__main__':
    main()

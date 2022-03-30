#!/usr/bin/env python3

def greedy(lkjN, lkjQ, q):
    N, Q = lkjN, lkjQ
    ans=[[0]*(N+1) for i in range(N+1)]
    o=[0,0]
    ex=[[1],[0]]
    ey=[[0],[1]]

    #####################

    def mul(a,b):
        n=len(a)
        m=len(b[0])
        res=[[0]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                for k in range(len(a[0])):
                    res[i][j]+=a[i][k]*b[k][j]

        return res
    def mpow(a,n):
        N = len(a)
        if n == 0:
            res = [[0] * N for i in range(N)]
            for i in range(N):
                res[i][i] = 1
            return res
        if n==1:return a
        res=mpow(a,n//2)
        res=mul(res,res)
        if n%2==1:
            res=mul(res,a)
        return res

    #######################



    mir=0
    mir2=0
    for i in range(Q):
        que=q[i]
        if que[0]=="1":
            x,y=int(que[1]),int(que[2])
            X=x*ex[0][0]+o[0]+y*ey[0][0]
            Y=x*ex[1][0]+o[1]+y*ey[1][0]
            ans[X][Y]^=1
        elif que[0]=="2":
            if mir:
                if que[1]=="A":que[1]="B"
                else:que[1]="A"
            if que[1]=="A":
                ex=mul([[0,-1],[1,0]],ex)
                ey=mul([[0,-1],[1,0]],ey)
                if o[0]==0 and o[1]==0:
                    o=[N+1,0]
                elif o[0]==N+1 and o[1]==0:
                    o=[N+1,N+1]
                elif o[0]==o[1]==N+1:
                    o=[0,N+1]
                else:
                    o=[0,0]
            else:

                ex=mul([[0,1],[-1,0]],ex)
                ey=mul([[0,1],[-1,0]],ey)
                if o[0]==0 and o[1]==0:
                    o=[0,N+1]
                elif o[0]==N+1 and o[1]==0:
                    o=[0,0]
                elif o[0]==o[1]==N+1:
                    o=[N+1,0]
                else:
                    o=[N+1,N+1]
        else:
            mir^=1
            if ex[0][0]==0:
                mir2=1
            else:
                mir2=0

            if mir2:
                if que[1]=="A":que[1]="B"
                else:que[1]="A"

            if que[1]=="A":
                ex[0][0]*=-1
                ey[0][0]*=-1
                o[0]=N+1-o[0]
            else:
                ex[1][0]*=-1
                ey[1][0]*=-1
                o[1] = N + 1 - o[1]

    res=[[0]*(N+1) for i in range(N+1)]
    for x in range(1,N+1):
        for y in range(1,N+1):
            X = x * ex[0][0] + o[0] + y * ey[0][0]
            Y = x * ex[1][0] + o[1] + y * ey[1][0]
            res[x][y]=ans[X][Y]

    res=res[1:]
    ans = []
    for l in res:
        ans.append(l[1:])
    return ans

def main(lkjN, lkjQ, q):
    # N, Q = map(int, input().split())
    N, Q = lkjN, lkjQ
    field = [[0] * N for _ in range(N)]
    rotate = 0
    flipVertical = 0
    flipHorizontal = 0
    for lkj in range(Q):
        # query = list(input().split())
        query = q[lkj]
        if query[0] == "1":
            x, y = int(query[1]) - 1, int(query[2]) - 1
            # プロットする場所を帰る。
            if flipVertical:
                x = N - x - 1
            if flipHorizontal:
                y = N - y - 1
            if rotate == 90:
                y, x = x, N - y - 1
            elif rotate == 180:
                y, x = N - y - 1, N - x - 1
            elif rotate == 270:
                y, x = N - x - 1, y
            field[x][y] ^= 1
            # print("--------")

        elif query[0] == "2":
            if query[1] == "A":
                rotate += 90
            else:
                rotate -= 90
            rotate %= 360
            flipHorizontal, flipVertical = flipVertical, flipHorizontal
        else:
            if query[1] == "A":
                if rotate == 90 or rotate == 270:
                    flipHorizontal ^= 1
                else:
                    flipVertical ^= 1
            else:
                if rotate == 90 or rotate == 270:
                    flipVertical ^= 1
                else:
                    flipHorizontal ^= 1
        print("---")
        print(rotate)
        print("v", flipVertical)
        print("h", flipHorizontal)
        print("---")
        for i in range(N):
            print(field[i])
    print("--------")
    if flipVertical:
        # field = [o for o in field][::-1] # #####
        field = [o for o in field][::-1]
        ff = []
        for f in field:
            ff.append(list(f))
        field = ff
    if flipHorizontal:
        print(field)
        # field = [o[::-1] for o in field] # #####
        field = [o[::-1] for o in field]
        ff = []
        for f in field:
            ff.append(list(f))
        field = ff
        print(field)
    if rotate == 90:
        field = list(zip(*field[::-1])) # +90する
        ff = []
        for f in field:
            ff.append(list(f))
        field = ff
    elif rotate == 180:
        field = [o[::-1] for o in field][::-1]
        ff = []
        for f in field:
            ff.append(list(f))
        field = ff
    elif rotate == 270:
        field = list(zip(*[o[::-1] for o in field])) # -90する
        ff = []
        for f in field:
            ff.append(list(f))
        field = ff
    # for i in range(N):
    #     print(*field[i], sep="")
    return field

if __name__ == '__main__':
    checkTimes = 10 # テスト試行回数
    for i in range(checkTimes):
        import random
        N = 4
        Q = 3
        # q = [['2', 'B'], ['1', '4', '2'], ['3', 'A'], ['1', '4', '3']]
        # q = [['3', 'A'], ['2', 'B'], ['1', '1', '3'], ['2', 'B']]
        q = [['1', '2', '1'], ['2', 'A'], ['3', 'A']]
        # q = [['1', '2', '1'], ['3', 'A'], ['2', 'A']]
        # q = []
        # for i in range(Q):
        #     c = random.randint(1, 3) # 発生させる乱数範囲 (末尾を含む)
        #     if c == 1:
        #         x = random.randint(1, N) 
        #         y = random.randint(1, N) 
        #         q.append([str(c), str(x), str(y)])
        #     else:
        #         ab = "A" if random.randint(1, 2) == 1 else "B"
        #         q.append([str(c), ab])
        ac = greedy(N, Q, q)
        checkee = main(N, Q, q)
        if ac != checkee:
            print(N, Q)
            print(q)
            print(ac, "!=", checkee)
            print("----------------")
            break
    # main()
    # greedy(1,1,1)

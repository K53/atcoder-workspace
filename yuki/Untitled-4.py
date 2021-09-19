#!/usr/bin/env python3
def main():
    class Union_Find():
        __slots__=["n","parents","rank"]
        def __init__(self,N):
            """0,1,...,N-1を要素として初期化する.

            N:要素数
            """
            self.n=N
            self.parents=[-1]*N
            self.rank=[0]*N

        def find(self, x):
            """要素xの属している族を調べる.

            x:要素
            """
            V=[]
            while self.parents[x]>=0:
                V.append(x)
                x=self.parents[x]

            for v in V:
                self.parents[v]=x
            return x

        def union(self, x, y):
            """要素x,yを同一視する.

            x,y:要素
            """
            x=self.find(x)
            y=self.find(y)

            if x==y:
                return

            if self.rank[x]<self.rank[y]:
                x,y=y,x

            self.parents[x]+=self.parents[y]
            self.parents[y]=x

            if self.rank[x]==self.rank[y]:
                self.rank[x]+=1

        def size(self, x):
            """要素xの属している要素の数.

            x:要素
            """
            return -self.parents[self.find(x)]

        def same(self, x, y):
            """要素x,yは同一視されているか?

            x,y:要素
            """
            return self.find(x) == self.find(y)

        def members(self, x):
            """要素xが属している族の要素.
            ※族の要素の個数が欲しいときはsizeを使うこと!!

            x:要素
            """
            root = self.find(x)
            return [i for i in range(self.n) if self.find(i) == root]

        def roots(self):
            """族の名前のリスト
            """
            return [i for i, x in enumerate(self.parents) if x < 0]

        def group_count(self):
            """族の個数
            """
            return len(self.roots())

        def all_group_members(self):
            """全ての族の出力
            """
            X={r:[] for r in self.roots()}
            for k in range(self.n):
                X[self.find(k)].append(k)
            return X

        def refresh(self):
            for i in range(self.n):
                _=self.find(i)

        def __str__(self):
            return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

        def __repr__(self):
            return self.__str__()
    #==================================================
    from collections import defaultdict
    from collections import deque
    import sys

    input=sys.stdin.readline
    write=sys.stdout.write

    N=int(input())
    E=[[] for _ in range(N+1)]
    for k in range(N):
        A,B=map(int,input().split())

        if A==B:
            E[A].append((B,k))
        else:
            E[A].append((B,k))
            E[B].append((A,k))

    #判定パート
    U=Union_Find(N+1)
    for linked in range(1,N+1):
        for b,_ in E[linked]:
            U.union(linked,b)

    Edge=defaultdict(int)
    T=[0]*N
    for linked in range(1,N+1):
        for b,k in E[linked]:
            if T[k]==0:
                T[k]+=1
                Edge[U.find(linked)]+=1
    

    G=U.all_group_members()
    for g in G:
        if g==0:
            continue
        if U.size(g) !=Edge[g]:
            exit(print("No"))

    #構築パート
    U=Union_Find(N+1)
    Ans=[-1]*N
    L=[0]*(N+1)
    T=[0]*N
    for root in G:
        print(root)
        if root==0: continue

        #サイクル辺を見つける
        flag=False
        for linked in G[root]:
            print(linked)
            for b,k in E[linked]:
                print(b,k)
                if T[k]==0:
                    T[k]=1
                    if U.same(linked,b):
                        alpha=linked
                        beta =b
                        flag=True
                        K=k
                        break
                    else:
                        U.union(linked,b)
            if flag:
                break

        Ans[K]=alpha
        Q=deque([alpha]); L[alpha]=1
        while Q:
            x=Q.popleft()
            for y,k in E[x]:
                if L[y]==0:
                    if k==K:
                        continue
                    L[y]=1
                    Q.append(y)
                    Ans[k]=y

    print("Yes")
    write("\n".join(map(str,Ans)))


if __name__ == '__main__':
    main()

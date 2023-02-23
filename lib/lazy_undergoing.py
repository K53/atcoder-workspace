class Lazy_Evaluation_Tree():
    def __init__(self,L,calc,unit,op,comp,id):
        """calcを演算,opを作用とするリストLのSegment Treeを作成

        calc:演算
        unit:モノイドcalcの単位元 (xe=ex=xを満たすe)
        op:作用素
        comp:作用素の合成
        id:恒等写像

        [条件] M:Monoid,F={f:F x M→ M:作用素}に対して,以下が成立する.
        Fは恒等写像 id を含む.つまり,任意の x in M に対して id(x)=x
        Fは写像の合成に閉じている.つまり,任意の f,g in F に対して, comp(f,g) in F
        任意の f in F, x,y in M に対して,f(xy)=f(x)f(y)である.

        [注記]
        作用素は左から掛ける.更新も左から.
        """

        self.calc=calc
        self.unit=unit
        self.op=op
        self.comp=comp
        self.id=id

        N=len(L)
        d=max(1,(N-1).bit_length())
        k=1<<d

        self.data=[unit]*k+L+[unit]*(k-len(L))
        self.lazy=[self.id]*(2*k)
        self.N=k
        self.depth=d

        for i in range(k-1,0,-1):
            self.data[i]=calc(self.data[i<<1],self.data[i<<1|1])

    def _eval_at(self,m):
        if self.lazy[m]==self.id:
            return self.data[m]
        return self.op(self.lazy[m],self.data[m])

    #配列の第m要素を下に伝搬
    def _propagate_at(self,m):
        self.data[m]=self._eval_at(m)

        if m<self.N and self.lazy[m]!=self.id:
            self.lazy[m<<1]=self.comp(
                self.lazy[m],
                self.lazy[m<<1]
                )

            self.lazy[m<<1|1]=self.comp(
                self.lazy[m],
                self.lazy[m<<1|1]
                )

        self.lazy[m]=self.id

    #配列の第m要素より上を全て伝搬
    def _propagate_above(self,m):
        H=m.bit_length()
        for h in range(H-1,0,-1):
            self._propagate_at(m>>h)

    #配列の第m要素より上を全て再計算
    def _recalc_above(self,m):
        while m>1:
            m>>=1
            self.data[m]=self.calc(
                self._eval_at(m<<1),
                self._eval_at(m<<1|1)
            )

    def get(self,k,index=1):
        m=k-index+self.N
        self._propagate_above(m)
        self.data[m]=self._eval_at(m)
        self.lazy[m]=self.id
        return self.data[m]

    #作用
    def operate(self,From,To,alpha,index=1,left_closed=True,right_closed=True):
        L=(From-index)+self.N+(not left_closed)
        R=(To-index)+self.N+(right_closed)

        L0=R0=-1
        X,Y=L,R-1
        while X<Y:
            if X&1:
                L0=max(L0,X)
                X+=1

            if Y&1==0:
                R0=max(R0,Y)
                Y-=1

            X>>=1
            Y>>=1

        L0=max(L0,X)
        R0=max(R0,Y)

        self._propagate_above(L0)
        self._propagate_above(R0)

        while L<R:
            if L&1:
                self.lazy[L]=self.op(alpha,self.lazy[L])
                L+=1

            if R&1:
                R-=1
                self.lazy[R]=self.op(alpha,self.lazy[R])

            L>>=1
            R>>=1

        self._recalc_above(L0)
        self._recalc_above(R0)

    def update(self,k,x,index=1):
        """ 第k要素をxに変更する.

        """
        m=k-index+self.N
        self._propagate_above(m)
        self.data[m]=x
        self.lazy[m]=self.id
        self._recalc_above(m)

    def product(self,From,To,index=1,left_closed=True,right_closed=True):
        L=(From-index)+self.N+(not left_closed)
        R=(To-index)+self.N+(right_closed)

        L0=R0=-1
        X,Y=L,R-1
        while X<Y:
            if X&1:
                L0=max(L0,X)
                X+=1

            if Y&1==0:
                R0=max(R0,Y)
                Y-=1

            X>>=1
            Y>>=1

        L0=max(L0,X)
        R0=max(R0,Y)

        self._propagate_above(L0)
        self._propagate_above(R0)

        vL=vR=self.unit

        while L<R:
            if L&1:
                vL=self.calc(vL,self._eval_at(L))
                L+=1

            if R&1:
                R-=1
                vR=self.calc(self._eval_at(R),vR)

            L>>=1
            R>>=1

        return self.calc(vL,vR)

    def all_product(self):
        return self.product(1,self.N,1)

    #リフレッシュ
    def refresh(self):
        for m in range(1,2*self.N):
            self.data[m]=self._eval_at(m)

            if m<self.N and self.lazy[m]!=self.id:
                self.lazy[m<<1]=self.comp(
                    self.lazy[m],
                    self.lazy[m<<1]
                    )

                self.lazy[m<<1|1]=self.comp(
                    self.lazy[m],
                    self.lazy[m<<1|1]
                    )

            self.lazy[m]=self.id
#================================================
from operator import add

N=int(input())
A=list(map(int,input().split()))
D={}

for i in range(N):
    if A[i] in D:
        D[A[i]][1]=i
    else:
        D[A[i]]=[i,i]

E=sorted(list(D.items()))

B=Lazy_Evaluation_Tree([0]*N,max,0,lambda a,x:a,lambda a,b:a,"*")
for (x,(l,r)) in E:
    B.operate(l,r,x,0)

B.refresh()
X=B.data[B.N:B.N+N]
print(*X)
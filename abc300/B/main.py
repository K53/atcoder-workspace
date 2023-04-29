#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


def main():
    H, W = map(int, input().split())
    G = []
    for _ in range(H):
        G.append(list(input()))
    ans = []
    for _ in range(H):
        ans.append(list(input()))
    for ss in range(H):
        Gs = G[ss:] + G[:ss]
        # print(Gs)
        for tt in range(W):
            Gans = []
            for i in range(H):
                newL = Gs[i][tt:] + Gs[i][:tt]
                Gans.append(newL)
            # for i in range(H):
            #     print(Gans[i])
            # print("---")
            if Gans == ans:
                print(YES)
                return
    print(NO)
    return

            


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

def main():
    l = [
        [[0], [1], [2]], 
        [[1, 2], [2, 0], [0, 1]]
    ]
    for t in range(60):
        next = []
        for ll in l[-1]: # [[1, 2], [2, 0], [0, 1]]
            chank = []
            for i in ll: # [1, 2]
                chank.extend(l[-1][i])
            next.append(chank)
        l.append(next)
        print(t, l)    




        


    # s = "ABC"
    # t = 6
    # while t > 0:
    #     a = ""
    #     for ss in s:
    #         if ss == "A":
    #             a += "BC"
    #         elif ss == "B":
    #             a += "CA"
    #         else:
    #             a += "AB"
    #     print(a)
    #     s = a
    #     t -= 1

if __name__ == '__main__':
    main()

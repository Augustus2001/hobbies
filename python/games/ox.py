#Kun Kerdthaisong
#07/15/2022
#ref Parinya Sanguansat from a book:Artificial Intelligence with mechine learning

import numpy as np
import random
o=[] #for a starter aka.human
x=[] #bot
win=[[1,2,3],[4,5,6],[7,8,9],[2,5,8],[1,4,7],[3,6,9],[1,5,9],[3,5,7]]
def check_win(player):
    for i in win:
        if all(x-1 in player for x in i):
            return  True
    return  False
def display_ox():
    ox=np.array([" "]*9)
    ox[o]=["o"]
    ox[x]=["x"]
    print(ox.reshape([3,3]))
def bot():
    validmove=list(set(range(9))-set(o+x))
    v=[-100]*9
    for m in validmove:
        tempx=x+[m]
        v[m],criticalmove=eval_ox(o,tempx)
        if len(criticalmove)>0:
            move=[i-1 for i in criticalmove if i-1 in validmove]
            return  random.choice(move)
    max_v=max(v)
    imax_v=[i for i,j in enumerate(v) if j==max_v]
    return  random.choice(imax_v)
def eval_ox(o,x):
    SO,SX,criticalmove=calSOX(o,x)
    return 1+SX-SO,criticalmove
def calSOX(o,x):
    SO=SX=0
    criticalmove=[]
    for w in win:
        o=[i-1 in o for i in w]
        x=[i-1 in x for i in w]
        if not any(x):
            nO=o.count(True)
            SO+=nO
            if nO==2:
                print("critical",w)
                criticalmove=w
        if not any(o):
            SX+=x.count(True)
        return SO,SX,criticalmove
def main():
    while True:
        move=int(input("enter position 1-9 to enter o"))-1
        while move in o+x or move>8 or move<0:
            move=int(input("wrong enter position 1-9 agian"))
        o.append(move)
        display_ox()
        if check_win(o):
            print("you won")
            break
        if len(o)+len(x)==9:
            print("draw")
            break
        x.append(bot())
        display_ox()
        if check_win(x):
            print("you loose")
            break
        if len(o)+len(x)==9:
            print("draw")
            break



if __name__=="__main__":
    main()

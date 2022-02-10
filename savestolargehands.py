import random
import time
#program deals bridge cards. calculates points (A=4, K=3, Q=2, J=1) and
#losers(cards that are not AKQ. accommodates exceptions of K/Qx, where
#K will be crushed by A/Qx by AK. they are counted as losers.

def deal(North, pack):#this deals 1 card. dealing multiple may result in
    while True:       #hands that are too unbalancely shaped         ^^^
        suit=random.randint(0,3)
        if pack[suit] != []:
            card= random.choice(pack[suit])
            pack[suit].remove(card)
            North[suit].append(card)
            break
    return North, pack

def arrange(north):#takes unsorted hand. arrages in order, converts honours
    points=0       #calculates pts & losers
    losers=0
    for row in range(0,4):
        north[row].sort(reverse=True)
        for i in range(0,3):
            if i+1 <= len(north[row]):
                if north[row][i]<12 or north[row][i]+len(north[row])<15:
                    losers+=1
        for item in range(0, len(north[row])):
            if north[row][item] == 11:
                north[row][item]= "J"
                points+=1
            elif north[row][item] == 12:
                points+=2
                north[row][item]= "Q"
            elif north[row][item] == 13:
                points+=3
                north[row][item]= "K"
            elif north[row][item] == 14:
                points+=4
                north[row][item]= "A"
            north[row][item]= str(north[row][item])
    for i in range (0, 4):
        if north[i]== []:
            north[i]=["-"]
    if points>25 or losers<3:
        with open("largehands.txt","a+") as f:#other way no work
            for row in north:
                for item in row:
                    f.write(str(item))
                f.write("\n")
            f.write("\n")
    return north, points, losers

pack=[[ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
North = [[],[],[],[]]
South = [[],[],[],[]]
East = [[],[],[],[]]
West = [[],[],[],[]]#setting hands to empty
lsers=[]
for i in range(0,13):#deals cards one eachto avoid unfair 
    North, pack = deal(North, pack)        #distributions
    East, pack = deal(East, pack)
    South, pack = deal(South, pack)
    West, pack = deal(West, pack)
print("       North")
North, p, l = arrange(North)
lsers.append(["North", l, p])
South, p, l = arrange(South)#same as north
lsers.append(["South", l, p])
East, p, l = arrange(East)
lsers.append(["East",l, p])
West, p, l= arrange(West)
lsers.append(["West",l, p])
for row in North:#prints norths cards row by row
    print("       "+"".join(row))#in the middle
print("\nWest            East")#w and e on same line
for i in range (0, 4):
    for item in range(0, (16-len(West[i]))):#formatting so E neat
            West[i].append(" ")
    if "10" in West[i]:
        West[i].pop()
    print("".join(West[i])+"".join(East[i]))
print("       South")
for row in South:
    print("       "+"".join(row))
print("\n")
for hand in lsers:
    print(hand[0]+": "+str(hand[1])+" losers, " +str(hand[2])+" points")

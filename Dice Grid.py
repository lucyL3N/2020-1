#Start with a score of 0,
#If all four corners are even numbers, add 20 pts to the score, ====1
#If all four corners are odd numbers, add 20 pts to the score, ====
#If all four dice on a diagonal are even numbers, add 20 pts to the score,2
#If all four dice on a diagonal are odd numbers, add 20 pts to the score,
#If all four dice on on any row are even numbers, add 20 pts to the score,3
#If all four dice on on any row are odd numbers, add 20 pts to the score,
#If all four dice on on any column are even numbers, add 20 pts to the score,4
#If all four dice on on any column are odd numbers, add 20 pts to the score,
#Add to the score the total value (sum) of all 16 dice.
import random
dice=[" . ", " : ", ":. ", ":: ", ":.:", ":::"]
grid=[[],[],[],[]]
score=0
for i in range(4):
    for x in range(4):
        grid[i].append(random.randint(1,6))
for i in range(4):
    line=[]
    print("____________________\n")
    for x in range(4):
        line.append("["+dice[grid[i][x]-1]+"]")
    print("".join(line))

def checker(a, b, c, d, e, f, g, h, placement):
    if grid[a][b]%2==0 and grid[c][d]%2==0 and grid[e][f]%2==0 and grid[g][h]%2==0:
        print(placement+" even, +20 points!")
        return 20
    elif grid[a][b]%2==1 and grid[c][d]%2==1 and grid[e][f]%2==1 and grid[g][h]%2==1:
        print(placement+" odd, +20 points!")
        return 20
    else:
        return 0


score+= checker(0, 0, 0, -1, -1, 0, -1, -1, "All corners are ")
score+= checker(0, 0, 1, 1, 2, 2, 3, 3, "Left to right diagonal is ")
score+= checker(0, 3, 1, 2, 2, 1, 3, 0, "Right to left diagonal is ")
for i in range(4):
    score+= checker(i, 0, i, 1, i, 2, i, 3, "Row "+str(i+1) +" is ")
for i in range(4):
    score+= checker(0, i, 1, i, 2, i, 3, i, "Column "+str(i+1) +" is ")
print("Your score: "+str(score))

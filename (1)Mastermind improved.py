import random
import shelve
#######
def highscore(mode,score):
    try:
        f= open(mode+".txt","r+")
        wwtw=(int(f))
        f.close
    except:
        wwtw=score+1
    f= open(mode+".txt","w+")
    if score<wwtw:
        f.write(str(score))
        print("Thats a new highscore")
    else:
        print("The current highscore is "+str(wwtw))
    f.close()
#######
while True:
    number = []
    guesses=0
    correct = 0
    mode=input("Pick mode (easy, normal, hard)\n")
    if mode=="easy":#easy
        for i in range (0, 4):
            number.append(str(random.randint(0,9)))
        while True:
            try:
                position=[]
                correct = 0
                unumber = ()
                unumber = input("Guess my number\n")
                unumber = list(unumber)
                guesses+=1
                if unumber == number:
                    break
                else:
                    for i in range(0, len(unumber)):
                        if unumber[i]== number[i]:
                            correct+= 1
                            position.append(str(i+1))
            except:
                ()
            if correct > 0:
                print("Numbers in positions "+(", ".join(position))+" are correct!")
            else:
                print("None correct")
        print("Congrats, you did it! You took "+str(guesses)+" tries")
#store score#####################################################
        highscore("easy", guesses)                              #
 ################################################################           
    elif mode=="hard":#hard
        for i in range (0, 5):
            number.append(str(random.randint(0,9)))
        while True:
            try:#try works for empty shelves
                correct = 0
                unumber = ()
                unumber = input("Guess my 5 digit number\n")
                unumber = list(unumber)
                guesses+=1
                if unumber == number:
                    break
                else:
                    for i in range(0, len(unumber)):
                        if unumber[i]== number[i]:
                            correct+= 1
            except:
                ()
                    
            print("You got "+str(correct)+" numbers right")
        print("Congrats, you did it! You took "+str(guesses)+" tries")
#storescoree#########################################################
        highscore("hard", guesses)                                  #
#####################################################################
    else:#normal
        for i in range (0, 4):
            number.append(str(random.randint(0,9)))
        while True:
            try:#try works for empty shelves
                correct = 0
                unumber = ()
                unumber = input("Guess my number\n")
                unumber = list(unumber)
                guesses+=1
                if unumber == number:
                    break
                else:
                    for i in range(0, len(unumber)):
                        if unumber[i]== number[i]:
                            correct+= 1
            except:
                ()
                    
            print("You got "+str(correct)+" numbers right")
        print("Congrats, you did it! You took "+str(guesses)+" tries")
##################################################################
        highscore("normal", guesses)                             #
##################################################################
    cont = input("type 'yes' or 'y' to play again")
    if cont.lower() != "yes" and cont.lower() != "y":
        break

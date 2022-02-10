import random
import time as t
r= open("hmwords.txt","r")
words=[]
for row in r:
    for item in str.split(row):
        words.append(item)
r.close
word = list(random.choice(words))
guessed= []
letters=[]
for letter in word:
    guessed.append(" __ ")
lives= 10

while lives != 0:
    print("".join(guessed))
    print(" ".join(letters))
    guess = input()
    if len(guess) == 1:
        if guess not in letters and guess in word:
            letters.append(guess)
            print("Well done!")
            for i in range (0, len(word)):
                if word[i]== guess:
                    guessed[i] = (guess+" ")
        elif guess in letters:
            print("you guessed that already")
        else:
            print("good try, that letter is not there though")
            letters.append(guess)
            lives=lives-1
    elif len(guess) == len(word):
        if list(guess) == word:
            guessed=word
        else:
            lives=lives-1
            print("bad luck, thats not the word")
    else:
        print("that guess is not the right length!")
    if [item.strip() for item in guessed]==word:
        print("You did it! The word was "+"".join(word)+
              " and you had "+str(lives-1)+" lives left")
        break
    if lives == 10:
        print:("\n"
               "\n"
               "\n"
               "\n"
               "\n"
               "\n")
    elif lives ==9 :
        print("\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "____")
    elif lives ==8:
        print("\n"
              "|\n"
              "|\n"
              "|\n"
              "|\n"
              "|____")
    elif lives ==7:
        print(" _______\n"
              "|\n"
              "|\n"
              "|\n"
              "|\n"
              "|____")
    elif lives ==6:
        print(" _______\n"
              "| /\n"
              "|/\n"
              "|\n"
              "|\n"
              "|____")
    elif lives ==5:
        print(" _______\n"
              "| /    O\n"
              "|/ \n"
              "|\n"
              "|\n"
              "|____")
    elif lives ==4:
        print(" _______\n"
              "| /    O\n"
              "|/     |\n"
              "|\n"
              "|\n"
              "|____")
    elif lives ==3:
         print(" _______\n"
              "| /    O\n"
              "|/     |\ \n"
              "|\n"
              "|\n"
              "|____")
    elif lives ==2:
        print(" _______\n"
              "| /    O\n"
              "|/    /|\ \n"
              "|\n"
              "|\n"
              "|____")
    elif lives ==1:
        print(" _______\n"
              "| /    O\n"
              "|/    /|\ \n"
              "|       \ \n"
              "|\n"
              "|____")
    else:
        print(" _______\n"
              "| /    O\n"
              "|/    /|\ \n"
              "|     / \ \n"
              "|\n"
              "|____")
    t.sleep(1)

    
if lives > 0:
    ()
else:
    print ("better luck next time! the word was "+"".join(word))
    

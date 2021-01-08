import random

def is_str(a):
    #checks each word in a
    for i in a:
        try:
            int(i)
            a=None
        except ValueError:
            continue
    return a   
        

while (True):

    print("Welcome to HANGMAN GAME!!!")

    chances=5
  
    file_name=open("wordlist.txt","r")
    lines=file_name.read()
    lst=lines.split()
    wrd=random.choice(lst)

    while chances>0:
        ans=input("Guess the word :")
        #checking if x is a complete string
        x=is_str(ans)
        if (x==None):
            print("Not a word.Please retry!")
        #guessing begins            
        elif not wrd==ans:
                print("Oops! Wrong Guess. Try Again!")
                if chances==4:
                    print("Hint : The word starts with -",wrd[0])
                if chances==3:
                    print("Hint : The word ends with -",wrd[-1])
                if chances==2:
                    print("Hint : The word has -",wrd[2],"in 3rd position.")
                if chances==5:
                    print("Hint! The length of the word is: ",len(wrd))
        elif wrd==ans:
                print("Congratulations, You WON!!!")
                break
        #decrementing and printing chances left
        chances=chances-1
        print("Tries left :",chances)
    #failed    
    if chances==0:
        print("Better luck next time!!")
        print("The word is :",wrd)
    #playing again   
    y=input("Play Again?(Y/N) : ")
    
    if (y=='n'or y=='N') :
        break
            
    

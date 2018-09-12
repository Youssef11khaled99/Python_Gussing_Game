R=0
while R!="no":
    import random
    tries=0
    WORDS=("lion","python","youssef")
    word = random.choice(WORDS) 
    length = len(word)
    length = str(length)
    print("The word is " + length + " letters long. Guess a letter! ")  
    if word==WORDS[0]:
        print("Hint:the word is animal name!! ")
        
    elif word==WORDS[1]:
        print("Hint:the word is programming language name!! ")
        
    elif word==WORDS[2]:
        print("Hint:the word is human name!! ")
        
    guess=str(input("Please enter your gusse again after this : "))
   
    while guess != word :
        p=0
        tries=tries+1
        guess=str(input("enter your new_guess : "))
        while len(guess) < len(word) :
            print("Please enter  "+ length +" Letters")
            guess=str(input("Enter your guess again : "))
        total1=0
        total2=0
        while p < len(word) : 
            if guess[p] in word :
                if guess[p]==word[p]:
                    total1=total1+1
                else :
                    total2=total2+1
            p=p+1
        if word==guess : 
            print("congratulations you guessed right","after",tries,"trials")
            break
        else:
            print(total1,total2)
            
    print("Thanks for playing!")
    R=str(input("Do you want to play again?(yes/no) "))
    print('''   ''')

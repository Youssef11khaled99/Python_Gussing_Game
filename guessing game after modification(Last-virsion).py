R=""
while (R!="no"):
    import random
    trials = 0
    WORDS = ("lion", "python", "youssef", "elephant", "ruby", "roshdy")
    hints = ("animal", "programming language", "human")
    word = random.choice(WORDS) 
    length = len(word)
    print("The word is " + str(len(word)) + " letters long. Guess a letter! ")
    for i in range(0, len(WORDS)):
        if word==WORDS[i]:
            print("Hint:the word is "+ hints[i%3] +" name!! ")
            
    
    indecator = 0
    guess = ""
    while guess != word :
        p=0
        trials=trials+1
            
        if indecator == 0:
            guess=str(input("Please enter your guess: "))
            indecator = 1
        else:
            guess=str(input("enter your new_guess : "))
            
        while len(guess) != len(word) :
            print("Please enter  "+ str(len(word)) +" Letters")
            guess=str(input("Enter your guess again : "))
        total1=0
        total2=0
        for i in range(0, len(word)):
            if guess[i] in word[i] :
                total1=total1+1
            else :
                total2=total2+1
        if word==guess : 
            print("congratulations you guessed right","after",trials,"trials")
            break
        else:
            print(total1,total2)
            
    print("Thanks for playing!")
    R=str(input("-> If you want to quit enter no:  \n-> If you want to play again press any key: "))
    print('''   ''')

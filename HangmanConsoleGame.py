def containsNumber(value):
    if True in [char.isdigit() for char in value]:
        return True
    return False

def output():
    print("")
    x = 0
    if remainingGuesses > 0:
        while x != length:
            if word[x] in guessed:
                print(word[x].upper(), end=" ")
                
            elif word[x] == " ":
                print(" ", end=" ")
                
            else:
                print("_", end=" ")
            x = x + 1
        print("\n")
        print("Guesses left: " + str(remainingGuesses))


        if len(guessed) == 2:
            print("\nYou have guessed:", ' and '.join([x.upper() for x in guessed]))
        elif len(guessed) >= 3:
            print("\nYou have guessed:", ', '.join(guessed).upper())

        print("\n"*10)

def hasAll():
    return all([char in guessed for char in word])

while True:
    guessed = []

    print("\n"*5)
    word = input("Please enter a word for the opponent to guess: ")
    length = len(word)

    print("\n"*2)
    guesses = int(input("Enter number of guesses for the opponent: "))
    remainingGuesses = guesses

    print("\n"*50)
    output()

    while remainingGuesses > 0 and hasAll() != True:
        guess = input("\nEnter a letter to guess: ")

        if containsNumber(guess) == True:
            print("You may not guess numbers.")
            output()

        elif len(guess) > 1:
            print("You may only guess a single letter.")
            output()

        elif len(guess) < 1:
            print("You must enter at least one character.")
            output()

        elif guess in guessed:
            print("You have already guessed this letter.")
            output()

        elif guess not in word:
            print("This letter is not in the word.")
            
            guessed.append(guess.lower())

            if remainingGuesses > 0:
                remainingGuesses = remainingGuesses-1
                output()
            if remainingGuesses == 0:
                print("\nYou have run out of guesses.\n")
                print("The word was " + word.upper() + ".")

        else:
            guessed.append(guess.lower())
            output()
        
    if hasAll():
        print("You guessed all the letters with " + str((guesses-remainingGuesses)) + " wrong guess(es).")
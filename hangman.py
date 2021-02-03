import random
tv_series = ['Game Of Thrones','Breaking Bad','Vikings','Sherlock','Spartacus','House Of Cards','Narcos','Westworld']
answer = random.choice(tv_series) # One of the tv-series will be selected as answer.
users_lives = int(input('How many lives do you want?')) # We ask the user how many lives he/she wants.
# We need to tell the user length of the answer. For that we are going to use len command. In order to calculate the length
# we need to combine words that have spaces between them. For that we are gonna use replace command.
print('This Tv-series includes {} letters.'.format(len(answer.replace(' ','')))) # Example: Game Of Thrones will be GameOfThrones.
# And this line tell the length of it. (len(GameOfThrones) = 13)

answer_uppercase = answer.replace(' ','').upper() # For convenience, all letters will be uppercased.
answer_empty = ('_' * len(answer_uppercase)) # This line will create a series of '_'. Example:'____________'

# After every right guess, '_' character will be changed with the right guess(Example:['_________'] will be ['G___B____'] after the right guess of 'G' and 'B').
# To apply this, we need to convert ['_______'] character to ['_','_','_','_'] characters. For this, we are going to use list command.
choice = list(answer_empty) # Now we have ['_','_','_','_','_'] series for choice value.
# Now we are getting in a loop. Loop will continue until finding the right answer or when the user's lives is finished.
while(users_lives > 0):
    users_guess = input('Guess a letter:')  # We want user to guess a letter.
    users_guess = users_guess.upper()  # In case the letter will lowercase.

    if users_guess in answer_uppercase: # If user's guess is in the answer_uppercase value;
        # We need to find where user_guess value in the answer_uppercase value. To do this we need to find indices;
        for i,x in enumerate(answer_uppercase): # i will be indices of answer_uppercase and x will be values of answer_uppercase.
            if x == users_guess: # If users_guess value is the same value of 2nd indice of answer_uppercase value. Then 'i' value will equal to '2' value.
                choice[i] = users_guess # index i of choice will be users_guess. (Example: ['_','_','_','_','_'] will be ['G','_','B','_','_'] etc.)
         # To print the results, we need to combine the choice value. For that we will use "''.join" command.
        result = ''.join(choice) # (Example:['G','_','B','_','_'] will be [G_B__] etc.)
        print(result) # After every right guess, results will be printed.
        if result == answer_uppercase: # If the user continue to guess the letter and complete the answer;
            print('Congratulations.') # The game is won.
            users_lives = 0 # We will make the users_lives value to '0'. When the users_lives equal to 0, while loop will be over.
            break # End for loop.
        # If not, after every right guess, we will ask the user if he/she wants to guess the answer or not.
        want_to_guess = input('Do you want to guess the answer? (Y/N)')
        if want_to_guess == 'Y': # If user wants to guess the answer;
            guess_answer = input('Please write your answer with words combined and with uppercase letters:') # We will ask the user to give his/her answer.
            if guess_answer == answer_uppercase: #If the guessed answer will equal to right answer. The game is won.
                print('Congratulations.')
                users_lives = 0 # We will make the users_lives value to '0'. When the users_lives equal to 0, while loop will be over.
            else: # If the guessed answer is wrong, the user's lives will decrease.
                print('Wrong answer.')
                users_lives -= 1
                print('{} lives left'.format(users_lives)) # This line will print how many lives user has left after the wrong answer.
        else: # If user does not want to guess the answer;
            users_guess = '' # Continue loop.

    # If the user guess the wrong letter user's lives will decrease.
    if users_guess not in answer_uppercase:
        print('This letter does not exist in the answer.')
        users_lives -= 1
        print('{} lives left'.format(users_lives)) # This line will print how many lives user has left after the wrong guess.
        # If user can't guess the letter and will have 0 lives remain;
        if users_lives == 0 :
            print("Your lives are over. You're lost. The answer was: {}".format(answer_uppercase)) # Game is over.






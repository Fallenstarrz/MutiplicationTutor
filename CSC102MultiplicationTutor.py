#############################################################################################################################
# In this assignment you will write a python program that will create and display simple multiplication problems            #
# for the user to solve.                                                                                                    #
#                                                                                                                           #
# User interaction with the program should look like this:                                                                  #
#                                                                                                                           #
# 1. Program Starts and asks the user how many problems they want to solve. If user enters any input other than             #
#       the valid range of one through 10, program interprets this as an error and re-asks for input.                       #
# 2. Program generates a random multiplication problem with two random factors between zero and 12                          #
#       (zero and 12 are valid factors).                                                                                    #
# 3. Program displays the problem for the user.                                                                             #
# 4. Program asks the user for the answer to the current problem. If the user's answer is not correct then the program      #
#       gives a hint by telling the user if their answer is too high or too low, and then returns to step 3.                #
#       If the user's answer is correct then the program displays a message telling the user that the answer is correct,    #
#       and then the program either returns to step 2 (if the user has not solved the requested number of problems) or      #
#       the program continues on to step 5.                                                                                 #
# 5. The program displays the average number of tries the user took to get the correct answer.                              #
# 6. Be sure to use comments for both structure of the program and documentation of the code.                               #
# 7. All code must completely be your own individual work product.                                                          #
# 8. You must create and use a function that takes two int factors as arguments and displays a multiplication problem       #
# with these factors for the user.                                                                                          #
# TRY. You should also look for other opportunities to effectively create and use user-defined functions in this program.   #
#############################################################################################################################

#modules
import random

def validInput(x):                                                                                                      # defines validInput                                                        
    while True:                                                                                                         # always run this loop
        if (str.isdigit(x)):                                                                                            # if passed variable's input is a number
            x = int(x)                                                                                                  # changed the string variable to an integer
            break                                                                                                       # then break the loop, ending the function
        else:                                                                                                           # if passed variables input is not a number
            x = input('Please select a valid integer\n')                                                                # prompt user to enter something else and restart the loop
    return x                                                                                                            # return the variable x

# main program
def main():                                                                                                             # defines main as a function
    totTries = 0                                                                                                        # totTries is assigned 0, so it can be used later.
    numProblems = input("How many problems would you like to solve?\n")                                                 # numProblems is an input
    numProblems = (validInput(numProblems))                                                                             # numProblems is passed into validInput function and the return value is assigned to numProblems
    if ((numProblems > 10) or (numProblems < 1)):                                                                       # check if numProblems is not between 1 and 10
        while ((numProblems > 10) or (numProblems < 1)):                                                                # while numproblems is not between 1 and 10
            print("Invalid input")                                                                                      # print invalid input
            numProblems = input("Please select a value between 1 and 10\n")                                             # prompt the user to select a value between 1 and 10
            numProblems = (validInput(numProblems))                                                                     # numProblems is passed into validInput function and the return value is assigned to numProblems
            print('We will be solving', numProblems, 'problems')                                                        # print the number of problems we will be solving
    else:                                                                                                               # if numProblems is between 1 and 10
        print('We will be solving', numProblems, 'problems')                                                            # print the number of problems we will be solving
    for totalProblems in range(1, numProblems +1, 1):                                                                   # create loop the repeats for the number of problems we will be solving and go up by 1 each time
        print("This is problem number", totalProblems)                                                                  # print the problem number we are on
        randNum1 = (random.randint (0,12))                                                                              # assign random number to randNum1 (from 0 to 12)
        randNum2 = (random.randint (0,12))                                                                              # assign random number to randNum2 (from 0 to 12)
        realAnswer = randNum1 * randNum2                                                                                # realAnswer is randNum1 times randNum2
        print(randNum1, "*", randNum2, "=")                                                                             # print the problem for the user to solve
        playerAnswer = input('')                                                                                        # playerAnswer is assigned input, this represents the players answer
        playerAnswer = (validInput(playerAnswer))                                                                       # pass playerAnswer into validInput function and assign playerAnswer to the return
        totTries += 1                                                                                                   # total number of tries goes up by 1 every new problem
        tryNumber = 1                                                                                                   # tryNumber is assigned 1 to reset it for every new problem
        while (playerAnswer != realAnswer):                                                                             # while playerAnswer does not equal realAnswer
            totTries += 1                                                                                               # increase total tries by 1
            tryNumber += 1                                                                                              # increate try number by 1
            if (playerAnswer > realAnswer):                                                                             # if playerAnswer is greater than realAnswer
                print("Too High")                                                                                       # let user know the answer they gave was too high
            elif(playerAnswer < realAnswer):                                                                            # if playerAnswer is less than realAnswer
                print("Too Low")                                                                                        # let user know the answer they gave was too low
            print("Guess Again\n",randNum1, " * ", randNum2, " = ", sep='')                                             # print the problem again, so the user knows the problem they are trying to answer
            playerAnswer = input('')                                                                                    # playerAnswer is assigned input, this represents the players answer
            playerAnswer = (validInput(playerAnswer))                                                                   # pass playerAnswer into validInput function and assign playerAnswer to the return
        if (tryNumber == 1):                                                                                            # if user got it on first try
            print("Correct\n", "This took you ", tryNumber, " try.", sep='')                                            # let user know they got it on first try
        else:                                                                                                           # if it took user more than 1 try
            print("Correct\n", "This took you ", tryNumber, " tries.", sep='')                                          # let user know how many tries it took them
    avTries = totTries / numProblems                                                                                    # average tries is equal to total tries divided by the number of problems
    if(totTries == 1):                                                                                                  # if total tries is 1
        print('You solved', numProblems, 'problem, and they took you', '{:,.2f}'.format(avTries), 'try on average')     # let user know how many problems they solved and the average number of tries to complete them all
    else:                                                                                                               #if total tries is not 1
        print('You solved', numProblems, 'problem, and they took you', '{:,.2f}'.format(avTries), 'tries on average')   # let user know how many problems they solved and the average number of tries to complete them all
    input('Press ENTER to close the program')                                                                           # Prompts the user to press ENTER to close the program

main()                                                                                                                  # call the main function to start the program

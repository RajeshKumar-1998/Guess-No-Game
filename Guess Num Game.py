#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Rajesh
#
# Created:     28-04-2020
# Copyright:   (c) Rajesh 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

 # import the modules to access their methods
import random
import time
import emoji

# Defined this user defined function
def ran():
    inp = int(input("Guess the number Between 1 and 10\n"))
    Guess = None
    Guess = random.randrange(1,10)

    if inp > 0 and inp < 11:

        if inp == Guess:
               # grinning face

               print("Are You Guessed The Correct Number ")
               time.sleep(3)
               print('Hurrah! You Guessed correct one \U0001f600')
        elif inp > Guess:
               print("Are You Guessed The Correct Number ")
               time.sleep(3)
               print("Alas! You Gone Wrong,Please Try Another Time ")
               print("You have guessed too high! \U0001F61C")

        elif inp < Guess:
               print("Are You Guessed The Correct Number ")
               time.sleep(3)
               print("Alas! You Gone Wrong,Please Try Another Time ")
               print("You have guessed too low! \U0001F61C")
    else:

         raise IOError("Please Enter the no between 1 and 10")

    return

def main():
            # grinning face
            print("\U0001f600")
            print("Welcome \U0001f600 to Guess No Game ")
            ran()

if __name__ == '__main__':
    main()

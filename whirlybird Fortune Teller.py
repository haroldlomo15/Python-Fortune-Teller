"""Howard SYCS100 Programming Assignment 3: Whirlybird

Now is the time for you to practice writing a program *from scratch*!!

You are going to implement a whirlybird game. Whirlybird is that fortune-
telling game where your fortune is determined using a number and a color.

This project is intended to have you practice a few things:
    - Using both while and for loops
    - Writing a program from scratch
    - Defining and calling functions
    - Using raw_input
    - Slightly more advanced string manipulation
  

Grading Rubric:
    - Functionality: 100 pts (graded automatically)
    - Style: 50 pts (graded manually)

Notes:
    - This is an individual project. You must complete all work on your own.
    - Copy the current contents of this file as your starting point.
    - Follow directions *carefully*. The autograder isn't very tolerant.
    - Be sure to follow the coding standards.
    - You may define helper functions in this file, but be sure that you 
      definitely have all of the required functions and they are in the format
      described in the comments.
    - Please use appropriate fortunes. Some should be hopeful, some should be
      devastating, but all should be G-rated (i.e. safe for children).
"""

"""Global Variables

Define four variables called BLUE, GREEN, RED, and YELLOW that contain string 
values you can use to compare against user input (e.g. later on in the 
program, the user is going to input a color, like 'red' and you need to match 
that to RED).

Also, define a variable called EXIT that contains the string 'exit' (which is 
what the user enters when he wants to quit the program.

You should use these variables throughout the program rather than hardcoding 
'red', 'blue', 'green', 'yellow', or 'exit' anywhere else in the code.
"""
# Define variables here
RED = "red"
BLUE = "blue"
GREEN = "green"
YELLOW = "yellow"
EXIT = "exit"

"""GetFortune Function

Define a function called GetFortune that takes one parameter named fortune_num. 
The parameter should be an integer between 1 and 8 (inclusive). For each valid 
value, the function should return a different fortune as a string. If the 
parameter's value is anything other than an integer between 1 and 8, the 
function should return the following string: 
  'Invalid fortune number.'
"""
# Define GetFortune herere
def GetFortune(fortune_num):
  if (fortune_num == 1):
    return "You will have a great day today!"
  elif(fortune_num == 2):
    return "You would become really successful"
  elif (fortune_num == 3):
    return "You would own a company"
  elif (fortune_num == 4):
    return "you would lose your job"
  elif (fortune_num == 5):
    return "You would go to the moon"
  elif (fortune_num == 6):
    return "you would go to war"
  elif(fortune_num == 7):
    return "you would lose your job"
  elif (fortune_num == 8):
    return "you would go to war"
  else:
    return "Enter an appropriate number"



"""GetColorSelection Function

Define a function called GetColorSelection that takes no parameters. The 
function should prompt the user to enter one of the colors defined at the 
beginning of the file. The user's input should not be case-sensitive. Only the 
four colors defined at the beginning of the program should be considered valid 
input and only valid values should be returned. If the user enters anything 
other than a valid color, you should notify the user that the input was invalid 
and prompt them to enter their color again. This process should continue until 
the user enters a valid color.

Note: see Python documentation to find a function that will convert strings 
      to lower case.

"""
# Define GetColorSelection here
def GetColorSelection():
  user_input = raw_input ("Enter a red, blue, yellow or green: ")
  while ((user_input.lower() != "red") and (user_input.lower() != "yellow") and (user_input.lower() != "blue") and (user_input.lower() != "green")):
    user_input = raw_input ("That input was invalid. Enter red, blue, yellow, or green: ") 
"""GetNumberSelection Function

Define a function called GetNumberSelection that takes one parameter named 
use_even_numbers. The parameter will be a boolean value. The function should 
prompt the user to enter an interger and return their selection as an 
integer. If use_even_numbers is True, the user should be prompted to enter 2, 
4, 6, or 8. If use_even_numbers is False, the user should be prompted to 
input 1, 3, 5, or 7. No other input values should be allowed and only valid 
values should be returned. If the user enters anything other than a valid 
integer, you should notify the user that the input was invalid and prompt 
them to enter their number again. This process should continue until the user 
enters a valid number.
"""
# Define GetNumberSelection here
def GetNumberSelection(use_even_numbers):
  if use_even_numbers == True:
    number = input ("Please enter an interger: ")
    if (number % 2 == 0):
      even_num = input("Please eneter 2, 4, 6, or 8: ")
      return even_num
  if use_even_numbers == False:
    number = input("Please enter an interger")
    if (number % 2 == 1):
      odd_num = input("please enter 1, 3, 5, 7: ")
      return odd_num
    else:
      while (number > 8):
        number = input ("please enter an appropriate interger: ")


"""IsPrime Function

Define a function called IsPrime that takes one parameter named x. The 
parameter will be an integer. The function should return a boolean value: True 
if the number is prime, False otherwise. If x is not an integer, then the 
function should return None.

Notes:
    - 0 and 1 are *not* prime numbers.
    - Negative numbers are never prime.
    - Even though we only use 1-8 in this program, this function should work 
      for any integer.
"""
# Define IsPrime
def IsPrime(x):
  if ((isinstance(x, int)) == False):
    return "None"
  elif (x % 2  == 0) and (x % 3 == 0 ) and (x % 5 == 0) and (x % 7 == 0) and (x % 11 == 0) and (x == 0) and (x == 1):
    return False
  else:
    return True


"""Play Function

Define a function called Play that takes no parameters. The function should 
use the other functions you have defined to handle the overall logic of the 
whirlybird.
    1) The user should be prompted to enter a question for the whirlybird.
    2) If the user entered 'exit' (not case-sensitive), the program should exit.
    3) The user should be prompted to choose a color.
    4) If there are an even number of letters in the selected color, the user 
       should be prompted to select an even number. If there are an odd number 
       of letters in the color, they should be prompted to choose an odd number.
    5) If the number the user selected is prime, the user should be prompted to 
       enter an even number. If the selected number is not prime, the user 
       should be prompted to enter an odd number.
    6) This second number the user has selected should be used to determine the 
       fortune the user should receive.
    7) The user's original question and then the fortune (on separate lines) 
       should be printed out.
    8) Go back to step 1.
"""
# Define Play
def Play():
  
  GetColorSelection()
  print GetFortune(GetNumberSelection(IsPrime(1)))
  

Play()  # DO NOT TOUCH THIS LINE!!

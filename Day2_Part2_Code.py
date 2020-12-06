#### ----- DAY 2: PASSWORD PHILOSOPHY PART 2 ----- ####

# The input is a list of passwords as well as a password policy - the task is to check how many passwords are geniune

# The Policy has change! It's on the same form as before though - x-y n: psswrd
# n : the letter featuring in the password
# x-y : they are indexes of the password, n must feature exactly once for it to be valid (either/or)

## THE CODE:

# Read the input file

with open("Input_Day2.txt") as f:
    content = f.readlines()

# Removing whitespace characters like `\n` at the end of each line

content = [x.strip() for x in content]

valid = 0
invalid = 0

for n in range(0,len(content)):

    test = content[n] # selecting the string to test

    split_test = test.split() # splitting it at the spaces

    # (a) Getting the bounds
    lowerupper = split_test[0] # grabbing the lower and upper bounds 
    bounds = lowerupper.split("-") # seperating at the dash
    firstpos = int(bounds[0]) - 1
    secondpos = int(bounds[1]) - 1

    # (b) Getting the letter to search for
    lettercol = split_test[1]
    lettercolsep = lettercol.split(":")
    letter = lettercolsep[0]

    # (c) The password
    password = split_test[2]

    # (2) Getting positions and their corresponding 
    letterfirst = password[firstpos]
    lettersecond = password[secondpos]

    if letterfirst == letter and lettersecond == letter:
        invalid += 1
    elif letterfirst == letter and lettersecond != letter:
        valid += 1
    elif letterfirst != letter and lettersecond == letter:
        valid += 1
    elif letterfirst != letter and lettersecond != letter:
        invalid += 1


    


print("Valid: " + str(valid))
print("Invalid: " + str(invalid))

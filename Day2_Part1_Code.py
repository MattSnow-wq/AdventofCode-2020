#### ----- DAY 2: PASSWORD PHILOSOPHY ----- ####

# The input is a list of passwords as well as a password policy - the task is to check how many passwords are geniune

# The Policy - x-y n: psswrd
# n : the letter featuring in the password
# x-y : the lower and upper number of times n features in the password

## THE CODE:

# Read the input file

with open("Input_Day2.txt") as f:
    content = f.readlines()

# Removing whitespace characters like `\n` at the end of each line

content = [x.strip() for x in content]

### WHILE LOOP OVER ALL PASSWORDS TO CHECK

valid = 0
invalid = 0

for n in range(0,len(content)):

    test = content[n] # selecting the string to test

    split_test = test.split() # splitting it at the spaces

    # (a) Getting the bounds
    lowerupper = split_test[0] # grabbing the lower and upper bounds 
    bounds = lowerupper.split("-") # seperating at the dash
    lowerbound = int(bounds[0])
    upperbound = int(bounds[1])

    # (b) Getting the letter to search for
    lettercol = split_test[1]
    lettercolsep = lettercol.split(":")
    letter = lettercolsep[0]

    # (c) The password
    password = split_test[2]


    ## (2) Checking the number of times the letter appears in the password


    appears = 0 

    for i in range(0,len(password)):
        if password[i] == letter:
            appears += 1
            
    if appears < lowerbound or appears > upperbound:
        invalid += 1
    else:
        valid += 1




print("Valid: " + str(valid))
print("Invalid: " + str(invalid))







##### ------ Day 1 : PART 2 ------ #####

# From the input list, find the pair of numbers that SUM to 2020 and find their product

# Read the input file

with open("Input_Day1.txt") as f:
    content = f.readlines()

# Removing whitespace characters like `\n` at the end of each line

content = [x.strip() for x in content] 

# Converting each into a number rather than a string

for i in range(0,len(content)):
   content[i] = int(content[i])


# Brute forcing the pair of numbers

result = False

first = 0
second = 0
third = 0

while result == False:
   
    sum_ans = 0

    for a in range(0,len(content)):
        for b in range(0,len(content)):
            for c in range(0,len(content)):
                sum_ans = content[a] + content[b] + content[c]
                if sum_ans == 2020:
                    first = content[a]
                    second = content[b]
                    third = content[c]
                    result = True
                else:
                    sum_ans = 0

# Print the pair of numbers

print(first)
print(second)
print(third)

# Print the summation

triple  = first*second*third
print(triple)



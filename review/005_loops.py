# Yes, I put loops after functions
# The main reason - operations and functions are very similar
# but realistically, loops are different than functions recursion

# the simplest thing 
for i in range(100):
    if i%19 == 0:
        print(i)

# the thing that everyone heard, and everyone forgot
for i in range(100):
    if i%15 == 0:
        print("fizzbuzz")
    elif i%5 == 0:
        print("buzz")
    elif i%3 == 0:
        print("fizz")
    else:
        print(i)

# of course, this can be extended, to a more general structure
for i in range(100):
    tmp_str = ("")
    if i % 3 == 0:
        tmp_str += "fizz"
    if i % 5 == 0:
        tmp_str += "buzz"
    if i % 7 == 0:
        tmp_str += "snap"
    if i % 11 == 0:
        tmp_str += "crackle"
    if i % 13 == 0:
        tmp_str += "pop"
    
    if len(tmp_str) == 0:
        print(i)
    else:
        print(tmp_str)

# and then, we start to see repetition in the code, and think,
# hey... could we use a loop for that?

# and yes, you could

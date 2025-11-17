# This is where things get really... fun. 
# Wait, that doesn't work in Python.

#hey check it out - you can compare existance of object
# semantically, this is the difference between
# "are these both apples"
# "are these the 'same' apple, "
def is_function(x, y):
    return x is y

def equal_function(x, y):
    return x == y

def recurse_function(counter):
    if counter != 0:
        print(counter)
        return recurse_function(counter - 1)

    elif counter <= 0:
        print("recursion terminated")
        return 0

# this function calls itself, but be careful
# notice this function grows when you aren't careful 
# and notice how it does so much redunant work! 

# if you see redundant work, your function probably needs
# to change some things! Storing prior calls in memory is usually a
# good idea.
def bad_forking_function(counter):
    if counter < 1:
        return
    
    print(counter)
    bad_forking_function(counter//2)
    bad_forking_function(counter//2)

# config functions are not recomended, since they make changes 
# that are not limited to the function scope. That is, they have
# side-effects, which is a cute way to say weight gain and balding
unscoped_variable = 5

def config_function(counter):
    global unscoped_variable # not idomatic, avoid if possible
    if counter**2 < 100:
        unscoped_variable = counter**2
    else:
        unscoped_variable = counter 
    

recurse_function(6)
bad_forking_function(16)

# This should not happen if it can be avoided
# if it cannot, state it explicitly
print(unscoped_variable)
config_function(12)
print(unscoped_variable)

unscoped_variable_2 = 0
def better_config(counter):
    return counter + 1

unscoped_variable_2 = better_config(3)
print(unscoped_variable_2)

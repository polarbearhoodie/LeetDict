# Oh yeah, the boolean are capitalized here.
my_boolean = True

if(my_boolean == True):
    print("Unnecessarily verbose")


if(my_boolean):
    print("This is simpler and does the same thing!")

# Try to name booleans so that they make sense!
# Although, is_ could be redundant and implies action
# You can do this... but I wouldn't

def is_data_valid():
    return True

data_validity = is_data_valid()
if(data_validity):
    print("repetitive!")

# We can inline some of this

if (is_data_valid()):
    print("you can call functions inside another!")
else:
    print("This won't show up!")

# the fun thing about strings is that you can do so many things with them
# slicing a string, indexing a string, iterating on a string...

def slice(my_str):
    if len(my_str) == 0:
        return my_str

    else:
        return my_str[1:]

local_str = "string of words with spaces"
print(local_str)
print(slice(local_str))
print(local_str.split())
print(local_str.split('o'))
print([c for c in local_str]) 

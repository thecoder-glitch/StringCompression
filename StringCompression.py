s = "aaaabbbddbaa"

def stringcompression(s):
    # set a new string variable to hold the new string
    new_str = ""
    # create a count variable to keep track of the occurence for each character
    counter = 0
    # create a for loop to loop through entire string
    for i in range(len(s)):
        # we need to create a variable to keep track of the second character to compare it to
        j = i
        j += 1
        try:
        # check if the 2 characters equal each other
            if s[i] == s[j]:
            # if they do incrament the counter
                counter += 1
        # otherwise get the character count and the character added to the new string
            else:
                new_str += s[i]
                new_str += str(counter)
            # reset the counter
                counter = 1
        # we cant reach the last index so we need to throw an exception
        except:
            new_str += s[i]
            j = i
            j -= 1
            if s[i] == s[j]:
                new_str += str(counter)
            else:
                new_str = "1"
    #return
    if len(new_str) > len(s):
        print(s)
    else:
        print(new_str)
stringcompression(s)
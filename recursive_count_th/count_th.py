'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loop.
'''
def count_th(word):

    # if 'word' is empty, return 0
    if word == '':
        return 0
    # slice through every 2 indexes in 'word'...
    if word[0:2] == 'th':
        # ...if slices == 'th', return 1 and recurse through again, moving up one index
        return 1 + count_th(word[1:])
    #if 'th' isn't found, continue searching the rest of the word incrementing by one 
    return count_th(word[1:])
     

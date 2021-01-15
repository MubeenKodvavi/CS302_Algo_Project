# Function to determine if can be segmented into a space-separated
# sequence of one or more dictionary words
def wordBreak(dict, str, lookup):
 
    # n stores length of current substring
    n = len(str)
 
    # return true if we have reached the end of the String
    if n == 0:
        return True
 
    # if sub-problem is seen for the first time
    if lookup[n] == -1:
 
        # mark sub-problem as seen (0 initially assuming String
        # can't be segmented)
        lookup[n] = 0
 
        for i in range(1, n + 1):
            # consider all prefixes of current String
            prefix = str[:i]
 
            # if prefix is found in dictionary, then recur for suffix
            if prefix in dict and wordBreak(dict, str[i:], lookup):
                # return true if the can be segmented
                lookup[n] = 1
                return True
 
    # return solution to current sub-problem
    return lookup[n] == 1

# List of Strings to represent dictionary
# we can also use trie or Set to store dictionary
dict = ["self", "th", "is", "famous", "Word",
        "break", "b", "r", "e", "a", "k", "br",
        "bre", "brea", "ak", "problem"]

# input String
str = "Wordbreakproblem"

# look-up table to store solutions to sub-problems
# lookup[i] stores if substr[n-i..n) can be segmented or not
lookup = [-1] * (len(str) + 1)

if wordBreak(dict, str, lookup):
    print("String can be segmented")
else:
    print("String can't be segmented")
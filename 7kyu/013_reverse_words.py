# Reverse_words

# ---
# ## CodeWars Description
# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

# ---
# ## Solution

def reverse_words(text):
    # Split the input string by space to get words and empty strings for multiple spaces.
    words = text.split(' ') 
    
    # Initialize a counter.
    n = 0
    # Initialize an empty string for the result.
    out = ''
    
    # Iterate through each item (word or empty string) in the list.
    for i in words:
        # Reverse the current item and append it to the result.
        out += i[::-1]
        
        # Add a space after the reversed item, unless it's the very last one.
        if n < len(words) - 1:
            out += ' '
        
        # Increment the counter.
        n += 1
    
    # Return the final string.
    return out

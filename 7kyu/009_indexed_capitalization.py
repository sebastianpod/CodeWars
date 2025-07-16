# Indexed capitalization

# ---
# ## CodeWars Description
# Given a string of lowercase letters and an array of integer indices, capitalize all letters at the given indices. If an index is beyond the string, it should be ignored.
# Examples:
# "abcdef", [1,2,5]     ==> "aBCdeF"
# "abcdef", [1,2,5,100] ==> "aBCdeF" // There is no index 100.

# ---
# ## Solution

def capitalize(s, ind):
    # Convert the input string 's' into a list of characters.
    # This allows individual characters to be modified (capitalized) by index.
    char_list = list(s)
    
    # Iterate through each index provided in the 'ind' array.
    for index in ind:
        # Check if the current 'index' is valid for the string.
        # An index is valid if it's non-negative and less than the length of the string.
        # Indices beyond the string's length should be ignored, as per the problem description.
        if 0 <= index < len(char_list):
            # If the index is valid, capitalize the character at that specific position.
            # .upper() is used to ensure the character becomes uppercase.
            char_list[index] = char_list[index].upper()
            
    # Join the modified list of characters back into a single string.
    # This creates the final string with specified characters capitalized.
    return "".join(char_list)

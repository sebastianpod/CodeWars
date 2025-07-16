# isograms

# ---
# ## CodeWars Description
# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
# Example: (Input --> Output)
# "Dermatoglyphics" --> true
# "aba" --> false
# "moOse" --> false (ignore letter case)

# ---
# ## Solution

def is_isogram(text):
    # Initialize an empty dictionary to keep track of character occurrences.
    occurence = {}
    # Iterate through each character in the input text, converting it to lowercase
    # to ignore letter case as per the problem description.
    for i in text.lower(): # Added .lower() to handle case-insensitivity
        # If the character is already in the dictionary, it means it's a repeat.
        if i in occurence:
            return False # Not an isogram
        # If the character is not in the dictionary, add it with a value (e.g., 1).
        # Note: 'wystapienia' appears to be a typo for 'occurence' in the original code.
        occurence[i] = 1 
    # If the loop completes without finding any repeating characters, it's an isogram.
    return True

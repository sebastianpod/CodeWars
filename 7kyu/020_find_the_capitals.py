# find the capitals

# ---
# ## CodeWars Description
# Write a function that takes a single non-empty string of only lowercase and uppercase ascii letters (word) as its argument, and returns an ordered list containing the indices of all capital (uppercase) letters in the string.
# Example (Input --> Output)
# "CodEWaRs" --> [0,3,4,6]

# ---
# ## Solution

def capitals(word):
    # Initialize an empty list to store the indices of capital letters.
    x = []
    # Initialize a counter for the current character's index.
    c = 0
    # Iterate through each character in the input 'word'.
    for i in word:
        # Check if the current character 'i' is an uppercase letter.
        # Comparing the character with its uppercase version (i.upper()) effectively checks this.
        if i.upper() == i:
            # If it's an uppercase letter, append its current index 'c' to the list.
            x.append(c)
        # Increment the index counter for the next character.
        c += 1
    # Return the list containing all found indices of capital letters.
    return x

# consonant_count

# ---
# ## CodeWars Description
# Complete the function that takes a string of English-language text and returns the number of consonants in the string.
# Consonants are all letters used to write English excluding the vowels a, e, i, o, u.

# ---
# ## Solution

def consonant_count(s):
    # Convert the input string to lowercase to handle both uppercase and lowercase letters uniformly.
    # Iterate through each character in the modified string.
    # Check if the character is not a vowel ('a', 'e', 'i', 'o', 'u') and is an alphabetic character.
    # Create a list of characters that meet these conditions (i.e., are consonants).
    # Return the length of this list, which represents the total count of consonants.
    return len([i for i in s.lower() if i not in 'aeiou ' and i.isalpha()])

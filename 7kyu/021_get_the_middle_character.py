# Get the Middle Character

# ---
# ## CodeWars Description
# You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.
# If the string's length is odd, return the middle character.
# If the string's length is even, return the middle 2 characters.
# Examples:
# "test" --> "es"
# "testing" --> "t"
# "middle" --> "dd"
# "A" --> "A"

# ---
# ## Solution

def get_middle(s):
    # Check if the length of the string is odd.
    if len(s) % 2 != 0:
        # If odd, return the single middle character.
        # Integer division (//) can be used to find the middle index directly: len(s) // 2.
        # For example, len=5, 5//2=2 (index of 's' in "testiNG").
        return s[len(s) // 2]
    else:
        # If even, return the two middle characters.
        # The first middle character's index is (length / 2) - 1.
        # The second middle character's index is (length / 2).
        # Using integer division for len(s) // 2 is more precise for indices.
        middle_start_index = (len(s) // 2) - 1
        middle_end_index = len(s) // 2
        return s[middle_start_index] + s[middle_end_index]

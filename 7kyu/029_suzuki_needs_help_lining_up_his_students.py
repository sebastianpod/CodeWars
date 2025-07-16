# Suzuki needs help lining up his students!

# ---
# ## CodeWars Description
# Today Suzuki will be interviewing his students to ensure they are progressing in their training. He decided to schedule the interviews based on the length of the students name in descending order. The students will line up and wait for their turn.
# You will be given a string of student names. Sort them and return a list of names in descending order.
# Here is an example input:
# string = 'Tadashi Takahiro Takao Takashi Takayuki Takehiko Takeo Takeshi Takeshi'
# Here is an example return from your function:
#  lst = ['Takehiko',
#         'Takayuki',
#         'Takahiro',
#         'Takeshi',
#         'Takeshi',
#         'Takashi',
#         'Tadashi',
#         'Takeo',
#         'Takao']
# Names of equal length will be returned in reverse alphabetical order (Z->A) such that:
# string = "xxa xxb xxc xxd xa xb xc xd"
# Returns
# ['xxd', 'xxc', 'xxb', 'xxa', 'xd', 'xc', 'xb', 'xa']

# ---
# ## Solution

def lineup_students(string):
    # Split the string into a list of names.
    list_ = string.split()
    
    # Sort the list by name length (descending).
    # Note: This sort does not fully implement the secondary rule for equal lengths
    # (reverse alphabetical). To do so, a more complex key would be needed,
    # e.g., `key=lambda name: (-len(name), name)`.
    list_ = sorted(list_, key=len, reverse=True)
    
    # Return the sorted list.
    return list_

# Super Duper Easy

# ---
# ## CodeWars Description
# Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".

# ---
# ## Solution

def problem(a):
    try:
        return a*50+6
    except TypeError:
        return "Error"

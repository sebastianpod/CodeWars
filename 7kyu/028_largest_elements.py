# Largest Elements

# ---
# ## CodeWars Description
# Write a program that outputs the top n elements from a list.
# Example:
# k = 2; list = [7, 6, 5, 4, 3, 2, 1]==> [6, 7]

# ---
# ## Solution

def largest(n, xs):
    # Initialize an empty list (not strictly needed as it's immediately reassigned).
    x = []
    # Sort the input list 'xs' in descending order.
    xs = sorted(xs, reverse=True)
    # Take the first 'n' elements from the sorted list, which are the largest.
    x = xs[:n]
    # Sort these 'n' largest elements in ascending order as required by the example output.
    x = sorted(x)
    # Return the list of top 'n' elements.
    return x

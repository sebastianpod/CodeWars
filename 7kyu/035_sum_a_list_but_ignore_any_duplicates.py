# Sum a list but ignore any duplicates

# ---
# ## CodeWars Description
# Please write a function that sums a list, but ignores any duplicated items in the list.
# For instance, for the list [3, 4, 3, 6] the function should return 10,
# and for the list [1, 10, 3, 10, 10] the function should return 4.

# ---
# ## Solution

def sum_no_duplicates(l):
    # Iterate through each item 'i' in the input list 'l'.
    # Include 'i' in the sum only if its count in the list is exactly 1 (i.e., it's not a duplicate).
    # Sum all such unique items.
    return sum(i for i in l if l.count(i) == 1)

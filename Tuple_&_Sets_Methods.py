# Tuples and Sets: Basic Usage

# 1. Tuples: Immutable collections of ordered elements
sample_tuple = (10, 20, 30, 40, 50)

# Accessing elements in a tuple
print("Original Tuple:", sample_tuple)
print("First element:", sample_tuple[0])      # Accessing by index
print("Last element:", sample_tuple[-1])     # Negative indexing

# Slicing a tuple
print("Slice (0-3):", sample_tuple[0:3])     # From index 0 to 2

# Tuples are immutable, so you cannot modify elements
# sample_tuple[0] = 15  # This will raise an error

# Tuple methods
print("Count of 20:", sample_tuple.count(20)) # Count occurrences of a value
print("Index of 30:", sample_tuple.index(30)) # Find the index of a value

# Packing and unpacking tuples
a, b, c, d, e = sample_tuple
print("Unpacked values:", a, b, c, d, e)

# Nested tuples
nested_tuple = (1, 2, (3, 4), 5)
print("Nested Tuple:", nested_tuple)
print("Access nested element (4):", nested_tuple[2][1])

# 2. Sets: Unordered collections of unique elements
sample_set = {10, 20, 30, 40, 50}

# Basic set operations
print("Original Set:", sample_set)

# Adding elements
sample_set.add(60)
print("After add(60):", sample_set)

# Removing elements
sample_set.remove(20) # Raises KeyError if the element doesn't exist
print("After remove(20):", sample_set)

sample_set.discard(70) # Does not raise an error if the element doesn't exist
print("After discard(70):", sample_set)

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union: Elements in either set
print("Union of A and B:", set_a | set_b)

# Intersection: Elements in both sets
print("Intersection of A and B:", set_a & set_b)

# Difference: Elements in A but not in B
print("Difference of A and B:", set_a - set_b)

# Symmetric Difference: Elements in either set, but not both
print("Symmetric Difference of A and B:", set_a ^ set_b)

# Checking membership
print("3 in set_a:", 3 in set_a)
print("5 not in set_a:", 5 not in set_a)

# Frozenset: Immutable version of a set
immutable_set = frozenset([1, 2, 3])
print("Frozenset:", immutable_set)

# Frozensets support set operations but are immutable
print("Union with frozenset:", immutable_set | {4, 5})

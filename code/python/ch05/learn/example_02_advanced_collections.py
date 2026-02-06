"""
Example 02: Advanced Collections
=================================
Chapter 5: Collections

Run with:
    python code/python/ch05/learn/example_02_advanced_collections.py
"""

# ============================================================
# PART 1: Sets
# ============================================================
# A set is an unordered collection of UNIQUE elements.
# Great for membership testing and removing duplicates.


def set_demo():
    """Demonstrate set operations."""
    # Creating sets
    colors = {"red", "green", "blue"}
    from_list = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3} — duplicates removed
    empty_set = set()  # NOT {} — that creates an empty dict!

    # Add and remove
    colors.add("yellow")
    colors.remove("red")   # raises KeyError if not found
    colors.discard("pink")  # does nothing if not found (safer)

    # Membership testing (very fast — O(1) on average)
    has_blue = "blue" in colors      # True
    has_red = "red" in colors        # False

    # Set operations
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    union = a | b            # {1, 2, 3, 4, 5, 6}
    intersection = a & b     # {3, 4}
    difference = a - b       # {1, 2}

    return colors, from_list, has_blue, union, intersection, difference


print("=== PART 1: Sets ===")
colors = {"red", "green", "blue"}
print(f"colors = {colors}")
colors.add("yellow")
print(f"After add('yellow'): {colors}")
colors.discard("red")
print(f"After discard('red'): {colors}")
print(f"'blue' in colors = {'blue' in colors}")
print()

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"a = {a}")
print(f"b = {b}")
print(f"a | b  (union)        = {a | b}")
print(f"a & b  (intersection) = {a & b}")
print(f"a - b  (difference)   = {a - b}")
print(f"Duplicates removed: set([1,2,2,3,3,3]) = {set([1, 2, 2, 3, 3, 3])}")
print()

# ============================================================
# PART 2: Dictionaries (maps)
# ============================================================
# A dictionary maps keys to values. Keys must be unique and
# immutable (strings, numbers, tuples). Values can be anything.


def dict_demo():
    """Demonstrate dictionary operations."""
    # Creating dictionaries
    scores = {"Alice": 95, "Bob": 87, "Charlie": 92}

    # Accessing values
    alice_score = scores["Alice"]        # 95
    # safe_get = scores["Dave"]          # KeyError! Dave doesn't exist
    safe_get = scores.get("Dave", 0)     # 0 (default if key not found)

    # Adding / updating
    scores["Diana"] = 88                 # add new key
    scores["Bob"] = 90                   # update existing key

    # Iteration
    keys = list(scores.keys())
    values = list(scores.values())
    items = list(scores.items())         # list of (key, value) tuples

    # Frequency counting pattern — super common!
    word = "abracadabra"
    freq = {}
    for ch in word:
        freq[ch] = freq.get(ch, 0) + 1
    # freq = {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

    return scores, alice_score, safe_get, freq


print("=== PART 2: Dictionaries ===")
scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
print(f"scores = {scores}")
print(f"scores['Alice'] = {scores['Alice']}")
print(f"scores.get('Dave', 0) = {scores.get('Dave', 0)}")
scores["Diana"] = 88
scores["Bob"] = 90
print(f"After updates: {scores}")
print()

print("Iterating over a dictionary:")
for name, score in scores.items():
    print(f"  {name}: {score}")
print()

# Frequency counting
word = "abracadabra"
freq = {}
for ch in word:
    freq[ch] = freq.get(ch, 0) + 1
print(f"Frequency of '{word}': {freq}")
print()

# ============================================================
# PART 3: Tuples
# ============================================================
# A tuple is like a list, but IMMUTABLE — once created, it can't
# be changed. Good for fixed collections and as dictionary keys.


def tuple_demo():
    """Demonstrate tuple operations."""
    # Creating tuples
    point = (3, 7)
    rgb = (255, 128, 0)
    single = (42,)    # Note the comma! Without it, (42) is just 42
    empty = ()

    # Unpacking — assign tuple elements to variables
    x, y = point      # x = 3, y = 7
    r, g, b = rgb     # r = 255, g = 128, b = 0

    # Tuples as dict keys (lists can't be keys because they're mutable)
    grid = {}
    grid[(0, 0)] = "start"
    grid[(1, 2)] = "treasure"

    # List of tuples — common pattern for paired data
    students = [("Alice", 95), ("Bob", 87), ("Charlie", 92)]
    for name, score in students:
        pass  # we'll print in the demo below

    return point, x, y, grid, students


print("=== PART 3: Tuples ===")
point = (3, 7)
print(f"point = {point}")
x, y = point
print(f"Unpacked: x = {x}, y = {y}")
print()

rgb = (255, 128, 0)
r, g, b = rgb
print(f"rgb = {rgb}")
print(f"Unpacked: r = {r}, g = {g}, b = {b}")
print()

grid = {}
grid[(0, 0)] = "start"
grid[(1, 2)] = "treasure"
print(f"grid = {grid}")
print(f"grid[(1, 2)] = '{grid[(1, 2)]}'")
print()

students = [("Alice", 95), ("Bob", 87), ("Charlie", 92)]
print("List of tuples:")
for name, score in students:
    print(f"  {name}: {score}")
print()

# ============================================================
# PART 4: Sorting
# ============================================================
# Python gives you two ways to sort:
# - list.sort()  — sorts in place, returns None
# - sorted(seq)  — returns a NEW sorted list, original unchanged


def sorting_demo():
    """Demonstrate sorting techniques."""
    nums = [5, 2, 8, 1, 9, 3]

    # sort() modifies the list in place
    nums.sort()                    # [1, 2, 3, 5, 8, 9]

    # sorted() returns a new list
    original = [5, 2, 8, 1, 9, 3]
    ascending = sorted(original)   # [1, 2, 3, 5, 8, 9]
    descending = sorted(original, reverse=True)  # [9, 8, 5, 3, 2, 1]
    # original is still [5, 2, 8, 1, 9, 3]

    # Sorting with key — sort by a custom rule
    words = ["banana", "apple", "cherry", "date"]
    by_length = sorted(words, key=len)
    # ["date", "apple", "banana", "cherry"]

    by_last_char = sorted(words, key=lambda w: w[-1])
    # sorted by last character

    # Multi-key sorting — sort by length, then alphabetically
    by_len_then_alpha = sorted(words, key=lambda w: (len(w), w))

    # Sorting a list of tuples
    students = [("Charlie", 92), ("Alice", 95), ("Bob", 87)]
    by_name = sorted(students, key=lambda s: s[0])
    by_score_desc = sorted(students, key=lambda s: -s[1])

    return ascending, descending, by_length, by_len_then_alpha, by_name, by_score_desc


print("=== PART 4: Sorting ===")
nums = [5, 2, 8, 1, 9, 3]
print(f"Original: {nums}")
print(f"sorted(nums) = {sorted(nums)}")
print(f"sorted(nums, reverse=True) = {sorted(nums, reverse=True)}")
print(f"Original unchanged: {nums}")
print()

words = ["banana", "apple", "cherry", "date"]
print(f"words = {words}")
print(f"sorted by length: {sorted(words, key=len)}")
print(f"sorted by last char: {sorted(words, key=lambda w: w[-1])}")
print(f"sorted by (len, alpha): {sorted(words, key=lambda w: (len(w), w))}")
print()

students = [("Charlie", 92), ("Alice", 95), ("Bob", 87)]
print(f"students = {students}")
print(f"by name:       {sorted(students, key=lambda s: s[0])}")
print(f"by score desc: {sorted(students, key=lambda s: -s[1])}")

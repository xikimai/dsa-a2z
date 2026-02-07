"""
Example 01: Digit Explorer
==============================
Chapter 7: Number Wizardry — Math for Programmers

Run with:
    python code/python/ch07/learn/example_01_digit_explorer.py

This demo shows how to extract, manipulate, and analyze individual
digits of a number using the mod-10 / div-10 pattern.
"""

# ============================================================
# PART 1: Extracting Digits (mod 10 / div 10)
# ============================================================
# The key insight: n % 10 gives the LAST digit, n // 10 removes it.
# This is like peeling digits off from right to left.

print("=== PART 1: Extracting Digits ===")
n = 54321
print(f"Number: {n}")
print(f"Step-by-step digit extraction:")
temp = n
step = 1
while temp > 0:
    digit = temp % 10
    temp = temp // 10
    print(f"  Step {step}: digit = {digit}, remaining = {temp}")
    step += 1
print()

# ============================================================
# PART 2: Count, Reverse, Sum Digits
# ============================================================
print("=== PART 2: Count, Reverse, Sum ===")
for num in [12345, 100, 7, 9876543210]:
    # Count digits
    count = 0
    temp = abs(num) if num != 0 else 0
    if num == 0:
        count = 1
    else:
        while temp > 0:
            count += 1
            temp //= 10

    # Reverse
    reversed_num = 0
    temp = abs(num)
    while temp > 0:
        reversed_num = reversed_num * 10 + temp % 10
        temp //= 10

    # Sum digits
    digit_sum = 0
    temp = abs(num)
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10

    print(f"  {num:>12} → digits: {count}, reversed: {reversed_num}, sum: {digit_sum}")
print()

# ============================================================
# PART 3: Palindrome Check
# ============================================================
print("=== PART 3: Palindrome Numbers ===")
for num in [121, 12321, 100, 1001, 7, 12345]:
    # Reverse and compare
    reversed_num = 0
    temp = num
    while temp > 0:
        reversed_num = reversed_num * 10 + temp % 10
        temp //= 10
    is_palindrome = (num == reversed_num)
    print(f"  {num:>6} → reversed: {reversed_num:>6} → palindrome: {is_palindrome}")
print()

# ============================================================
# PART 4: Armstrong Numbers
# ============================================================
print("=== PART 4: Armstrong Numbers ===")
print("An Armstrong number equals the sum of its digits raised to the power of digit count.")
for num in [153, 370, 9474, 100, 1, 0]:
    digits = len(str(num)) if num > 0 else 1
    temp = num
    total = 0
    while temp > 0:
        total += (temp % 10) ** digits
        temp //= 10
    is_armstrong = (total == num)
    print(f"  {num:>5}: sum of digits^{digits} = {total} → Armstrong: {is_armstrong}")
print()

print("The mod-10/div-10 pattern is your Swiss Army knife for digit problems!")

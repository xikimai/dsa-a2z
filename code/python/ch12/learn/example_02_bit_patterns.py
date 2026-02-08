"""
Example 02: Bit Manipulation Patterns in Action
================================================
Chapter 12: Bit Manipulation — The Language of Computers

This example demonstrates:
  - Part 1: XOR tricks (swap, single number, properties)
  - Part 2: Bitmask-as-set operations (add, remove, toggle, enumerate)
  - Part 3: Power set generation using bitmasks
  - Part 4: Two odd-occurring numbers with XOR partitioning
"""


# ── Part 1: XOR Tricks ───────────────────────────────────────────

def part1_xor_tricks():
    """Demonstrate XOR properties and classic tricks."""
    print("=" * 60)
    print("PART 1: XOR Tricks")
    print("=" * 60)

    # XOR properties
    print("\n  XOR Properties:")
    print(f"    5 ^ 5  = {5 ^ 5}   (a ^ a = 0)")
    print(f"    5 ^ 0  = {5 ^ 0}   (a ^ 0 = a)")
    print(f"    3 ^ 5  = {3 ^ 5}   (commutative: same as 5 ^ 3 = {5 ^ 3})")

    # XOR swap
    print("\n  XOR Swap (without temp variable):")
    a, b = 42, 99
    print(f"    Before: a = {a}, b = {b}")
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"    After:  a = {a}, b = {b}")

    # Single number
    print("\n  Find Single Number (XOR all):")
    nums = [4, 1, 2, 1, 2]
    result = 0
    for x in nums:
        result ^= x
        print(f"    XOR {x}: result = {result}")
    print(f"    Single number in {nums} is: {result}")


# ── Part 2: Bitmask as Set ───────────────────────────────────────

def part2_bitmask_set():
    """Demonstrate set operations using bitmasks."""
    print("\n" + "=" * 60)
    print("PART 2: Bitmask as Set")
    print("=" * 60)

    elements = ["A", "B", "C", "D"]
    n = len(elements)

    def mask_to_set(mask):
        return "{" + ", ".join(elements[i] for i in range(n) if (mask >> i) & 1) + "}"

    mask = 0b0000  # empty set
    print(f"\n  Elements: {elements}")
    print(f"  Start:  mask = {mask:04b} = {mask_to_set(mask)}")

    # Add A (bit 0)
    mask = mask | (1 << 0)
    print(f"  Add A:  mask = {mask:04b} = {mask_to_set(mask)}")

    # Add C (bit 2)
    mask = mask | (1 << 2)
    print(f"  Add C:  mask = {mask:04b} = {mask_to_set(mask)}")

    # Toggle B (bit 1)
    mask = mask ^ (1 << 1)
    print(f"  Tog B:  mask = {mask:04b} = {mask_to_set(mask)}")

    # Remove A (bit 0)
    mask = mask & ~(1 << 0)
    print(f"  Rem A:  mask = {mask:04b} = {mask_to_set(mask)}")

    # Check D (bit 3)
    has_d = (mask >> 3) & 1
    print(f"  Has D?  ({mask:04b} >> 3) & 1 = {has_d}  ({'Yes' if has_d else 'No'})")

    # Set operations
    set1 = 0b1010  # {B, D}
    set2 = 0b0110  # {B, C}
    print(f"\n  Set1 = {set1:04b} = {mask_to_set(set1)}")
    print(f"  Set2 = {set2:04b} = {mask_to_set(set2)}")
    print(f"  Union:        {set1 | set2:04b} = {mask_to_set(set1 | set2)}")
    print(f"  Intersection: {set1 & set2:04b} = {mask_to_set(set1 & set2)}")


# ── Part 3: Power Set Generation ─────────────────────────────────

def part3_power_set():
    """Generate all subsets using bitmask iteration."""
    print("\n" + "=" * 60)
    print("PART 3: Power Set Using Bitmasks")
    print("=" * 60)

    elements = [1, 2, 3]
    n = len(elements)
    print(f"\n  Elements: {elements}")
    print(f"  Total subsets: 2^{n} = {1 << n}\n")

    for mask in range(1 << n):
        subset = [elements[i] for i in range(n) if (mask >> i) & 1]
        print(f"    mask = {mask:03b} ({mask})  ->  {subset}")


# ── Part 4: Two Odd-Occurring Numbers ────────────────────────────

def part4_two_odd():
    """Find two numbers that appear an odd number of times."""
    print("\n" + "=" * 60)
    print("PART 4: Two Odd-Occurring Numbers")
    print("=" * 60)

    nums = [2, 4, 7, 9, 2, 4]
    print(f"\n  Input: {nums}")
    print(f"  Expected: 7 and 9 (each appears once; 2 and 4 appear twice)")

    # Step 1: XOR all
    xor_all = 0
    for x in nums:
        xor_all ^= x
    print(f"\n  Step 1: XOR all = {xor_all} = {xor_all:08b}")
    print(f"          This is 7 ^ 9 = {7 ^ 9}")

    # Step 2: Find lowest set bit
    diff_bit = xor_all & (-xor_all)
    print(f"  Step 2: Lowest set bit = {diff_bit} = {diff_bit:08b}")

    # Step 3: Partition and XOR
    a, b = 0, 0
    for x in nums:
        if x & diff_bit:
            a ^= x
            print(f"  Step 3: {x:>2} has bit {diff_bit} set   -> group A, running XOR = {a}")
        else:
            b ^= x
            print(f"  Step 3: {x:>2} has bit {diff_bit} unset -> group B, running XOR = {b}")

    result = sorted([a, b])
    print(f"\n  Answer: {result}")


# ── Main ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_xor_tricks()
    part2_bitmask_set()
    part3_power_set()
    part4_two_odd()

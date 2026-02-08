"""
Example 01: Bit Manipulation Basics — See Bits in Action
=========================================================
Chapter 12: Bit Manipulation — The Language of Computers

This example demonstrates:
  - Part 1: Binary conversion (decimal to binary, binary to decimal)
  - Part 2: Bitwise operators (AND, OR, XOR, NOT, shifts) with visual output
  - Part 3: Check i-th bit, power of 2, count set bits
  - Part 4: Brian Kernighan's algorithm step-by-step trace
"""


# ── Part 1: Binary Conversion ─────────────────────────────────────

def part1_binary_conversion():
    """Show decimal ↔ binary conversion."""
    print("=" * 60)
    print("PART 1: Binary Conversion")
    print("=" * 60)

    # Manual decimal to binary
    def to_binary(n):
        if n == 0:
            return "0"
        bits = []
        while n > 0:
            bits.append(str(n % 2))
            n //= 2
        return "".join(reversed(bits))

    print("\n  Decimal to Binary (manual):")
    for num in [0, 1, 5, 10, 42, 255, 1024]:
        manual = to_binary(num)
        builtin = bin(num)[2:]
        match = "OK" if manual == builtin else "MISMATCH"
        print(f"    {num:>5} = {manual:>12}  (bin() = {builtin})  [{match}]")

    # Binary to decimal
    print("\n  Binary to Decimal:")
    for bits in ["0", "1", "101", "1010", "101010", "11111111"]:
        dec = int(bits, 2)
        print(f"    {bits:>12} = {dec}")


# ── Part 2: Bitwise Operators ─────────────────────────────────────

def part2_bitwise_operators():
    """Demonstrate all six bitwise operators with visual output."""
    print("\n" + "=" * 60)
    print("PART 2: Bitwise Operators")
    print("=" * 60)

    a, b = 42, 15
    print(f"\n  a = {a} = {a:08b}")
    print(f"  b = {b} = {b:08b}")

    ops = [
        ("AND (a & b)", a & b),
        ("OR  (a | b)", a | b),
        ("XOR (a ^ b)", a ^ b),
        ("NOT (~a)", ~a),
        ("Left Shift  (a << 2)", a << 2),
        ("Right Shift (a >> 2)", a >> 2),
    ]

    print()
    for name, result in ops:
        if result >= 0:
            print(f"  {name:>25} = {result:08b}  ({result})")
        else:
            print(f"  {name:>25} = {result}  (negative due to two's complement)")


# ── Part 3: Bit Checks ───────────────────────────────────────────

def part3_bit_checks():
    """Check i-th bit, power of 2, count set bits."""
    print("\n" + "=" * 60)
    print("PART 3: Bit Checks")
    print("=" * 60)

    n = 42  # 101010
    print(f"\n  n = {n} = {n:08b}")
    print("  Checking each bit position:")
    for i in range(8):
        bit_val = (n >> i) & 1
        marker = " SET" if bit_val else ""
        print(f"    bit {i}: (n >> {i}) & 1 = {bit_val}{marker}")

    print("\n  Power of 2 checks:")
    for num in [0, 1, 2, 3, 4, 6, 8, 16, 24, 32, 64, 100, 128]:
        is_pow2 = num > 0 and (num & (num - 1)) == 0
        tag = "YES" if is_pow2 else "no "
        print(f"    {num:>4} = {num:08b}  -> {tag}")


# ── Part 4: Brian Kernighan's Algorithm ──────────────────────────

def part4_kernighan():
    """Step-by-step trace of Brian Kernighan's set-bit counting."""
    print("\n" + "=" * 60)
    print("PART 4: Brian Kernighan's Algorithm (Count Set Bits)")
    print("=" * 60)

    for n in [42, 255, 1023, 0]:
        original = n
        count = 0
        print(f"\n  n = {original} = {original:016b}")
        if n == 0:
            print(f"    n is 0, count = 0")
            continue
        while n > 0:
            old_n = n
            n &= (n - 1)
            count += 1
            print(f"    Step {count}: {old_n:016b} & {old_n - 1:016b} "
                  f"= {n:016b}  (cleared lowest bit)")
        print(f"    Result: {count} set bits")
        assert count == bin(original).count('1'), "Mismatch!"


# ── Main ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_binary_conversion()
    part2_bitwise_operators()
    part3_bit_checks()
    part4_kernighan()

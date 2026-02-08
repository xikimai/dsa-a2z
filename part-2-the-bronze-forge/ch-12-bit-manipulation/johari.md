# Johari Window: Chapter 12 — Bit Manipulation — The Language of Computers

Use this worksheet **before** and **after** studying the chapter. Be honest — there are no wrong answers! This is a tool for YOU to track your own growth.

---

## Before This Chapter

Think about what you already know (or think you know) about binary numbers and bit manipulation.

### Open (I know well)
> Things I'm confident I understand:
> - [ ] That computers store numbers in binary (0s and 1s)
> - [ ] What "binary" means (base 2 number system)
> - [ ] That `bin()` in Python converts a number to binary (from Ch 7)
> - [ ] That XOR can find a missing number (from Ch 11 AOPS showcase)
> - [ ] _________________________________

### Hidden (I think I know but I'm not sure)
> Things I've heard of but couldn't explain clearly:
> - [ ] How AND, OR, XOR, NOT actually work at the bit level
> - [ ] What left shift and right shift do
> - [ ] Why "n & (n-1)" checks for power of 2
> - [ ] How to check if a specific bit in a number is 1 or 0
> - [ ] _________________________________

### Blind Spot (I know I don't know)
> Things I know exist but haven't learned:
> - [ ] Brian Kernighan's algorithm for counting set bits
> - [ ] How to represent sets as bitmasks (single integers)
> - [ ] XOR trick to find the element that appears only once
> - [ ] How to enumerate all subsets of a set using bitmask iteration
> - [ ] _________________________________

### Unknown (I haven't even thought about)
> Things I don't know that I don't know — leave blank now, fill in after!
> - [ ] _________________________________
> - [ ] _________________________________
> - [ ] _________________________________

---

## After This Chapter

Come back here after finishing the chapter. Compare with your "Before" answers!

### Open — Expanded (Now I truly understand)
> - [ ] Binary representation: how to convert decimal to binary and back
> - [ ] All six bitwise operators (AND, OR, XOR, NOT, left shift, right shift)
> - [ ] Checking if the i-th bit is set using `(n >> i) & 1`
> - [ ] Power of 2 check using `n & (n - 1) == 0`
> - [ ] Brian Kernighan's algorithm: `n &= (n - 1)` removes the lowest set bit
> - [ ] XOR properties: `a ^ a = 0`, `a ^ 0 = a`, commutative, associative
> - [ ] Single number problem solved with XOR in O(n) time, O(1) space
> - [ ] Bitmasks represent subsets: iterate 0 to 2^n - 1 to enumerate all subsets
> - [ ] _________________________________

### Surprised Me! (was Unknown/Blind Spot, now Open)
> - [ ] That an integer IS a set — each bit represents whether an element is included!
> - [ ] That `n & (-n)` isolates the lowest set bit (two's complement trick)
> - [ ] That two odd-occurring numbers can be found by XOR + bit partitioning
> - [ ] That operator precedence makes `n & 1 == 1` different from `(n & 1) == 1`!
> - [ ] _________________________________

### Still Working On (honest self-assessment)
> - [ ] Recognizing when a problem benefits from bit manipulation
> - [ ] The two-odd-occurring-numbers technique (XOR + partition)
> - [ ] Understanding signed vs. unsigned shift behavior across languages
> - [ ] Using bitmasks fluently in practice problems
> - [ ] _________________________________

### Questions I Now Have (new curiosity!)
> - [ ] How do bitmask DP problems work? (Coming in Ch 31)
> - [ ] Can we handle elements appearing 3 times with a similar XOR trick?
> - [ ] What are "bitset" data structures and when are they useful?
> - [ ] How does two's complement representation actually work for negative numbers?
> - [ ] _________________________________

---

**Tip:** Revisit this page after completing Ch 13 (Bronze Battle Plan) — the bitmask subset technique from this chapter becomes your primary tool for complete search problems!

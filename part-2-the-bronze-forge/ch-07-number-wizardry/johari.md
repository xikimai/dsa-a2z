# Johari Window: Number Wizardry — Math for Programmers

Use this worksheet to track your understanding before and after studying Chapter 7.

---

## Before This Chapter

Fill this out BEFORE you read the chapter. Be completely honest — there's no wrong answer here, only honest ones.

### I Know Well (Open)
> Things I'm confident I understand and could explain to a friend.

- [ ] How to get the last digit of a number (using % 10)
- [ ] What "divisible by" means (no remainder)
- [ ] What a prime number is
- [ ] _____________________________________
- [ ] _____________________________________

### I Think I Know But I'm Not Sure (Hidden)
> Things I've heard of but couldn't confidently explain or code from scratch.

- [ ] How to reverse a number using code (not converting to a string)
- [ ] What GCD (greatest common divisor) means and how to find it
- [ ] What modular arithmetic is and why competitive programmers use it
- [ ] How to find all divisors of a number efficiently
- [ ] _____________________________________

### I Know I Don't Know (Blind Spot)
> Things I'm aware exist but haven't learned yet.

- [ ] The Euclidean algorithm for computing GCD
- [ ] What the Sieve of Eratosthenes is and how it works
- [ ] How to compute huge powers like 2^1000000 mod 10^9+7
- [ ] What prime factorization means and how to find it efficiently
- [ ] _____________________________________

### I Haven't Even Thought About (Unknown)
> Leave this blank for now. You'll fill it in after the chapter when you discover things you didn't even know existed!

- [ ] _____________________________________
- [ ] _____________________________________
- [ ] _____________________________________

---

## After This Chapter

Fill this out AFTER you complete the chapter. Compare with your "Before" answers!

### Now I Truly Understand (Open — Expanded)
> Things that moved from "Hidden" or "Blind Spot" to genuine understanding.

- [ ] The mod-10/div-10 pattern for extracting digits from any number
- [ ] Finding all divisors of n in O(sqrt(n)) by only checking up to the square root
- [ ] The Euclidean algorithm: GCD(a, b) = GCD(b, a % b), and why it's O(log(min(a,b)))
- [ ] Computing LCM safely using a/gcd*b (not a*b/gcd) to avoid overflow
- [ ] Modular arithmetic properties: (a+b)%m = ((a%m)+(b%m))%m
- [ ] Binary exponentiation: computing base^exp mod m in O(log exp) time
- [ ] The Sieve of Eratosthenes: finding ALL primes up to n in O(n log log n)
- [ ] Prime factorization by trial division up to sqrt(n)
- [ ] Proof by contradiction: "if d > sqrt(n) divides n, then n/d < sqrt(n)"
- [ ] _____________________________________

### Surprised Me! (Was Unknown/Blind, Now Open)
> Things you didn't expect to learn or that changed how you think about coding.

- _____________________________________
- _____________________________________
- _____________________________________

### Still Working On (Honest Self-Assessment)
> Things you understand in theory but need more practice with.

- _____________________________________
- _____________________________________
- _____________________________________

### Questions I Now Have (New Curiosity)
> New questions that popped up while studying. These are GREAT — they mean you're thinking deeply!

- _____________________________________
- _____________________________________
- _____________________________________

---

## Reflection

1. **The Euclidean algorithm finds GCD by ___. It's faster than subtraction because ___.**

   _____________________________________

2. **MOD 10^9+7 appears in competitive programming because ___.**

   _____________________________________

3. **The Sieve of Eratosthenes is faster than checking each number individually because ___.**

   _____________________________________

4. **The proof by contradiction for the sqrt optimization says: if both divisors were > sqrt(n), then ___.**

   _____________________________________

5. **One "trade space for time" example from this chapter is ___.**

   _____________________________________

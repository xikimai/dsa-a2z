/*
 * Example 01: Variables and Data Types
 * =====================================
 * Chapter 2: Your First Programs — Speaking Three Languages
 *
 * This file shows you the fundamental data types in C++ and how to declare
 * variables. Run this file and study the output to understand how each
 * type works.
 *
 * Build and run:
 *   g++ -std=c++17 -o example_01 example_01_variables_types.cpp && ./example_01
 */

#include <iostream>
#include <string>
#include <climits>   // INT_MAX, INT_MIN, etc.
#include <cfloat>    // DBL_MAX, FLT_MAX, etc.
using namespace std;

int main() {
    // ── 1. Integer types ─────────────────────────────────────────────────
    // int stores whole numbers (no decimal point).
    int age = 14;
    int temperature = -5;
    int score = 0;

    cout << "=== Integer (int) ===" << endl;
    cout << "age         = " << age << endl;
    cout << "temperature = " << temperature << endl;
    cout << "score       = " << score << endl;
    cout << "sizeof(int) = " << sizeof(int) << " bytes" << endl;
    cout << "Range: " << INT_MIN << " to " << INT_MAX << endl;
    cout << endl;

    // ── 2. Long long ─────────────────────────────────────────────────────
    // Use long long when numbers might exceed ~2 billion.
    long long worldPopulation = 8000000000LL;
    long long bigCalc = 1000000LL * 1000000LL;  // 10^12

    cout << "=== Long Long (long long) ===" << endl;
    cout << "worldPopulation = " << worldPopulation << endl;
    cout << "bigCalc         = " << bigCalc << endl;
    cout << "sizeof(long long) = " << sizeof(long long) << " bytes" << endl;
    cout << "Range: " << LLONG_MIN << " to " << LLONG_MAX << endl;
    cout << endl;

    // ── 3. Floating-point types ──────────────────────────────────────────
    // double stores decimal numbers. It's the default choice for decimals.
    // float uses less memory but is less precise — usually stick with double.
    double pi = 3.14159265358979;
    double price = 9.99;
    float piFloat = 3.14159265358979f;  // notice the 'f' suffix

    cout << "=== Double and Float ===" << endl;
    cout << "pi (double) = " << pi << endl;
    cout << "price       = " << price << endl;
    cout << "pi (float)  = " << piFloat << "  (less precise!)" << endl;
    cout << "sizeof(double) = " << sizeof(double) << " bytes" << endl;
    cout << "sizeof(float)  = " << sizeof(float) << " bytes" << endl;
    cout << endl;

    // ── 4. Character type ────────────────────────────────────────────────
    // char holds a single character, wrapped in single quotes.
    char grade = 'A';
    char newline = '\n';  // special "escape" character

    cout << "=== Character (char) ===" << endl;
    cout << "grade = " << grade << endl;
    cout << "grade as number = " << (int)grade << "  (ASCII value)" << endl;
    cout << "sizeof(char) = " << sizeof(char) << " byte" << endl;
    cout << endl;

    // ── 5. Boolean type ──────────────────────────────────────────────────
    // bool is either true or false. Useful for conditions.
    bool isStudent = true;
    bool hasLicense = false;

    cout << "=== Boolean (bool) ===" << endl;
    cout << "isStudent  = " << isStudent << "  (1 = true)" << endl;
    cout << "hasLicense = " << hasLicense << "  (0 = false)" << endl;
    cout << "sizeof(bool) = " << sizeof(bool) << " byte" << endl;
    cout << endl;

    // ── 6. String type ───────────────────────────────────────────────────
    // string holds text. It's from the <string> library.
    // Strings use double quotes; chars use single quotes.
    string name = "Maya";
    string greeting = "Hello, " + name + "!";

    cout << "=== String (string) ===" << endl;
    cout << "name     = " << name << endl;
    cout << "greeting = " << greeting << endl;
    cout << "name.length() = " << name.length() << endl;
    cout << endl;

    // ── 7. Type casting (converting between types) ───────────────────────
    // Sometimes you need to convert one type to another.

    // Integer division vs double division:
    int a = 7, b = 2;
    cout << "=== Type Casting ===" << endl;
    cout << "7 / 2 (int division)    = " << a / b << "  (truncates!)" << endl;
    cout << "7.0 / 2 (double division) = " << 7.0 / 2 << endl;

    // C++ style cast: static_cast<type>(value)
    double result = static_cast<double>(a) / b;
    cout << "static_cast<double>(7) / 2 = " << result << endl;

    // Casting double to int (truncates toward zero):
    double pi2 = 3.99;
    int truncated = static_cast<int>(pi2);
    cout << "static_cast<int>(3.99) = " << truncated << "  (truncates, not rounds!)" << endl;

    // char to int and back:
    char letter = 'A';
    int asciiVal = static_cast<int>(letter);
    char backToChar = static_cast<char>(asciiVal + 1);
    cout << "'A' as int = " << asciiVal << endl;
    cout << "ASCII " << asciiVal + 1 << " as char = " << backToChar << endl;
    cout << endl;

    // ── 8. Constants ─────────────────────────────────────────────────────
    // Use 'const' for values that should never change.
    const double SPEED_OF_LIGHT = 299792458.0;  // meters per second
    const int MAX_SCORE = 100;

    cout << "=== Constants ===" << endl;
    cout << "Speed of light = " << SPEED_OF_LIGHT << " m/s" << endl;
    cout << "Max score      = " << MAX_SCORE << endl;
    // SPEED_OF_LIGHT = 0;  // ERROR! Can't modify a const.
    cout << endl;

    // ── 9. auto keyword (C++11) ──────────────────────────────────────────
    // 'auto' lets the compiler figure out the type for you.
    auto x = 42;         // int
    auto y = 3.14;       // double
    auto z = "hello";    // const char* (not string!)
    auto w = string("hello");  // string

    cout << "=== auto keyword ===" << endl;
    cout << "auto x = 42      -> sizeof = " << sizeof(x) << endl;
    cout << "auto y = 3.14    -> sizeof = " << sizeof(y) << endl;
    cout << endl;

    cout << "Done! You've seen all the basic C++ types." << endl;
    return 0;
}

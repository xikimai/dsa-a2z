/*
 * Warmup 3: Simulate Robot Moves
 * ====================================
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * PROBLEM:
 *   A robot starts at (0, 0). Given a string of commands (U/D/L/R),
 *   simulate the moves and return the final {x, y} position.
 *
 * EXAMPLES:
 *   solve("UURRDDLL") -> {0, 0}
 *   solve("UUU")       -> {0, 3}
 *   solve("")           -> {0, 0}
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<int> solve(string commands) {
    // TODO: Replace this with your solution
    return {0, 0};
}

// -- Do not change anything below this line --------------------------
int main() {
    string commands;
    getline(cin, commands);
    vector<int> result = solve(commands);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}

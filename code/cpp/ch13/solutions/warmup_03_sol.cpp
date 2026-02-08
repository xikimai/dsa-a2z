/*
 * Solution for Warmup 3: Simulate Robot Moves
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * APPROACH: Walk through commands, update x/y.
 * TIME:  O(n)
 * SPACE: O(1)
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<int> solve(string commands) {
    int x = 0, y = 0;
    for (char cmd : commands) {
        if (cmd == 'U') y++;
        else if (cmd == 'D') y--;
        else if (cmd == 'L') x--;
        else if (cmd == 'R') x++;
    }
    return {x, y};
}

// -- Do not change anything below this line --------------------------
int main() {
    string commands;
    getline(cin, commands);
    vector<int> result = solve(commands);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}

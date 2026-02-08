#include <iostream>
#include <vector>
using namespace std;

bool solve(vector<int> bills) {
    int fives = 0, tens = 0;
    for (int bill : bills) {
        if (bill == 5) fives++;
        else if (bill == 10) { if (fives == 0) return false; fives--; tens++; }
        else {
            if (tens > 0 && fives > 0) { tens--; fives--; }
            else if (fives >= 3) fives -= 3;
            else return false;
        }
    }
    return true;
}

int main() {
    int n; cin >> n;
    vector<int> bills(n); for (int i = 0; i < n; i++) cin >> bills[i];
    cout << (solve(bills) ? "true" : "false") << endl;
    return 0;
}

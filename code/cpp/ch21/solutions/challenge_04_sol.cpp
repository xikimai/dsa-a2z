/* Solution: Challenge 4 — Flatten. TIME: O(n) SPACE: O(d) */
#include <iostream>
#include <vector>
using namespace std;

static const int BEGIN_LIST = -999999;
static const int END_LIST = -999998;

vector<int> solve(vector<int> encoded) {
    vector<int> result;
    for (int val : encoded) {
        if (val != BEGIN_LIST && val != END_LIST) {
            result.push_back(val);
        }
    }
    return result;
}

int main() { int n; cin>>n; vector<int> a(n); for(int i=0;i<n;i++) cin>>a[i];
    auto r=solve(a); for(int i=0;i<(int)r.size();i++) cout<<(i?" ":"")<<r[i]; cout<<endl; }

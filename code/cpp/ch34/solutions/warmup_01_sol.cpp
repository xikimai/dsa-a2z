/*
 * Solution for Warmup 1: Cross Product and Orientation
 * Chapter 34: Computational Geometry & Sweep Line
 */
#include <vector>
using namespace std;

vector<int> solve(vector<vector<vector<int>>>& queries) {
    vector<int> result;
    for (auto& q : queries) {
        auto& a = q[0]; auto& b = q[1]; auto& c = q[2];
        long long cp = (long long)(b[0] - a[0]) * (c[1] - a[1])
                     - (long long)(b[1] - a[1]) * (c[0] - a[0]);
        if (cp > 0) result.push_back(1);
        else if (cp < 0) result.push_back(-1);
        else result.push_back(0);
    }
    return result;
}

int main() { return 0; }

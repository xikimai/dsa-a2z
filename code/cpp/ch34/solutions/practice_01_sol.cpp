/*
 * Solution for Practice 1: Closest Pair of Points
 * Chapter 34: Computational Geometry & Sweep Line
 */
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;

double dist_p1(vector<int>& a, vector<int>& b) {
    return sqrt((double)(a[0]-b[0])*(a[0]-b[0])
              + (double)(a[1]-b[1])*(a[1]-b[1]));
}

double rec_p1(vector<vector<int>>& pts, int lo, int hi) {
    if (hi - lo < 3) {
        double best = 1e18;
        for (int i = lo; i <= hi; i++)
            for (int j = i + 1; j <= hi; j++)
                best = min(best, dist_p1(pts[i], pts[j]));
        return best;
    }
    int mid = (lo + hi) / 2;
    int midX = pts[mid][0];
    double d = min(rec_p1(pts, lo, mid), rec_p1(pts, mid + 1, hi));

    vector<vector<int>> strip;
    for (int i = lo; i <= hi; i++)
        if (abs(pts[i][0] - midX) < d) strip.push_back(pts[i]);
    sort(strip.begin(), strip.end(),
         [](auto& a, auto& b) { return a[1] < b[1]; });

    for (int i = 0; i < (int)strip.size(); i++)
        for (int j = i + 1; j < (int)strip.size()
             && strip[j][1] - strip[i][1] < d; j++)
            d = min(d, dist_p1(strip[i], strip[j]));
    return d;
}

double solve(vector<vector<int>>& points) {
    auto pts = points;
    sort(pts.begin(), pts.end());
    return rec_p1(pts, 0, pts.size() - 1);
}

int main() { return 0; }

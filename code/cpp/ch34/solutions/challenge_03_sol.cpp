/*
 * Solution for Challenge 3: Rectangle Union Area (Sweep Line)
 * Chapter 34: Computational Geometry & Sweep Line
 */
#include <algorithm>
#include <map>
#include <set>
#include <vector>
using namespace std;

int solve(vector<vector<int>>& rectangles) {
    if (rectangles.empty()) return 0;

    set<int> ySet;
    vector<tuple<int,int,int,int>> events; // x, type(0=open,1=close), y1, y2
    for (auto& r : rectangles) {
        ySet.insert(r[1]);
        ySet.insert(r[3]);
        events.push_back({r[0], 0, r[1], r[3]});
        events.push_back({r[2], 1, r[1], r[3]});
    }

    sort(events.begin(), events.end());

    vector<int> ys(ySet.begin(), ySet.end());
    map<int, int> yIndex;
    for (int i = 0; i < (int)ys.size(); i++) yIndex[ys[i]] = i;

    int m = ys.size() - 1;
    if (m <= 0) return 0;
    vector<int> count(m, 0);

    long long area = 0;
    int prevX = get<0>(events[0]);

    for (auto& [x, typ, y1, y2] : events) {
        long long activeY = 0;
        for (int i = 0; i < m; i++)
            if (count[i] > 0) activeY += ys[i + 1] - ys[i];
        area += (long long)(x - prevX) * activeY;
        prevX = x;

        int i1 = yIndex[y1], i2 = yIndex[y2];
        int delta = (typ == 0) ? 1 : -1;
        for (int i = i1; i < i2; i++)
            count[i] += delta;
    }

    return (int)area;
}

int main() { return 0; }

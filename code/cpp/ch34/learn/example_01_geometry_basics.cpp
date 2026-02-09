/*
 * Example 01: Geometry Basics — Cross Product, Distance, Orientation
 * ==================================================================
 * Chapter 34: Computational Geometry & Sweep Line
 *
 * Demonstrates fundamental 2D geometry operations.
 */

#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

long long cross(vector<int>& o, vector<int>& a, vector<int>& b) {
    return (long long)(a[0] - o[0]) * (b[1] - o[1])
         - (long long)(a[1] - o[1]) * (b[0] - o[0]);
}

long long dot(vector<int>& o, vector<int>& a, vector<int>& b) {
    return (long long)(a[0] - o[0]) * (b[0] - o[0])
         + (long long)(a[1] - o[1]) * (b[1] - o[1]);
}

double dist(vector<int>& a, vector<int>& b) {
    return sqrt((double)(a[0]-b[0])*(a[0]-b[0])
              + (double)(a[1]-b[1])*(a[1]-b[1]));
}

int orientation(vector<int>& a, vector<int>& b, vector<int>& c) {
    long long cp = cross(a, b, c);
    if (cp > 0) return 1;   // counter-clockwise
    if (cp < 0) return -1;  // clockwise
    return 0;               // collinear
}

int main() {
    cout << string(60, '=') << endl;
    cout << "GEOMETRY BASICS: Cross Product, Distance, Orientation" << endl;
    cout << string(60, '=') << endl;

    vector<int> o = {0, 0}, a = {4, 4};
    vector<int> b1 = {1, 2}, b2 = {1, 0}, b3 = {2, 2};

    cout << "\n--- Cross Product ---" << endl;
    cout << "  cross(O, A, (1,2)) = " << cross(o, a, b1) << endl;  // 4
    cout << "  cross(O, A, (1,0)) = " << cross(o, a, b2) << endl;  // -4
    cout << "  cross(O, A, (2,2)) = " << cross(o, a, b3) << endl;  // 0

    cout << "\n--- Orientation ---" << endl;
    cout << "  (0,0)-(4,4)-(1,2): " << orientation(o, a, b1) << " (1=CCW)" << endl;
    cout << "  (0,0)-(4,4)-(1,0): " << orientation(o, a, b2) << " (-1=CW)" << endl;
    cout << "  (0,0)-(4,4)-(2,2): " << orientation(o, a, b3) << " (0=collinear)" << endl;

    cout << "\n--- Distance ---" << endl;
    vector<int> p1 = {0, 0}, p2 = {3, 4};
    cout << "  distance((0,0), (3,4)) = " << dist(p1, p2) << endl;  // 5.0

    return 0;
}

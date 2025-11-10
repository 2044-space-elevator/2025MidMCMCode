#include <bits/stdc++.h>
using namespace std;

double posX[15], posY[15];
double floyd[15][15][15];
int permutation[15];
int ans_per[15];

double dis(double fx, double fy, double ex, double ey) {
    return sqrt((fx - ex) * (fx - ex) + (fy - ey) * (fy - ey));
}

int main() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> posX[i] >> posY[i];
        permutation[i] = i;
    }
    double ans = 1e9;
    do {
        double stx = 0, sty = 10;
        double edx = 10, edy = 0;
        double res = 0;
        res += dis(stx, sty, posX[permutation[1]], posY[permutation[1]]);
        // Path A 
        res += dis(edx, edy, posX[permutation[n]], posY[permutation[n]]);
        // Ring line 
        // res  += dis(stx, sty, posX[permutation[1]], posY[permutation[1]]);
        for (int i = 2; i <= n; i++) {
            res += dis(posX[permutation[i - 1]], posY[permutation[i - 1]], posX[permutation[i]], posY[permutation[i]]);
        }
        if (ans > res) {
            ans = res;
            for (int i = 1; i <= n; i++) {
                ans_per[i] = permutation[i];
            }
        }
    } while (next_permutation(permutation + 1, permutation + n + 1));
    cout << "(0.000, 10.000)\n";
    for (int i = 1; i <= n; i++) {
        printf("(%.3lf, %.3lf)\n", posX[ans_per[i]], posY[ans_per[i]]);
    }
    // Exit
    cout << "(10.000, 0.0000)\n";
    cout << ans;
    // Ring line
    // cout << "(0.000, 0.000)\n";
}
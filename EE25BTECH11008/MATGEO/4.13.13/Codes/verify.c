#include <stdio.h>

double verify_m(double m, int sign) {
    // sign = 1  => v = [1, 1]
    // sign = -1 => v = [1, -1]
    double v1 = 1.0;
    double v2 = (double)sign;

    // Matrix A
    double A[2][2];
    A[0][0] = -m;
    A[0][1] = (1 - m * m) / 2.0;
    A[1][0] = (1 - m * m) / 2.0;
    A[1][1] = m;

    // Compute v^T A v
    double res = v1 * (A[0][0] * v1 + A[0][1] * v2) +
                 v2 * (A[1][0] * v1 + A[1][1] * v2);

    return res;
}

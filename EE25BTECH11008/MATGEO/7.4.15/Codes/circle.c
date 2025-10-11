// circle_calc.c
#include <math.h>
#include <stdlib.h>

void calc_circle(double a1, double b1, double c1,
                 double a2, double b2, double c2,
                 double area,
                 double *ux, double *uy, double *f, double *cc, double *r)
{
    double det = a1*b2 - a2*b1;
    if (fabs(det) < 1e-12) {
        // parallel (degenerate) - return zeros
        *ux = *uy = *f = *cc = *r = 0.0;
        return;
    }

    // centre (h,k) is intersection of the two diameter lines
    double h = (b1*c2 - b2*c1) / det;
    double k = (c1*a2 - c2*a1) / det;

    *r = sqrt(area / 3.14);

    // From your excerpt: u = -c_center (vector), f = ||u||^2 - r^2
    *ux = -h;
    *uy = -k;
    *f  = h*h + k*k - (*r) * (*r);

    // circle constant term (same as f in this notation)
    *cc = *f;
}

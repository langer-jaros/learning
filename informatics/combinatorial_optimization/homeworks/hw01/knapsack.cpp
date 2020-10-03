#include <iostream>
using namespace std;

void showProblem(int n, int m, int b, int *wgts, int *vals)
{
    cout << "Number: " << n << ", Max weight: " << m << ", Boundary value: " << b << endl;
    int i = 0;
    for (i = 0; i < n; i++)
        cout << wgts[i] << ", " << vals[i] << endl;
}

void showDecision(bool decision, int n, int *wgts, int *vals, bool *solution)
{
    cout << "Decision: " << decision << " ";
    int value = 0;
    int i;
    for (i = 0; i < n; i++)
        value += vals[i] * solution[i];
    cout << value << " ";
    for (i = 0; i < n; i++)
        (i < n - 1)? cout << solution[i] << " ": cout << solution[i] << endl;
}

/**
 * Decide the knapsack problem.
 *
 * @param sol One particular solution of the problem.
 * @param n Number of items.
 * @param m Maximum weight.
 * @param b Boundary condition of minimal value for success.
 * @param wght Array of weights.
 * @param vals Array of values.
 * @return True if there is a solution that fits the boundary value.
 */
bool decide(bool *sol, int wgt, int val, int idx, int n, int m, int b, int *wgts, int *vals)
{
    if (wgt >= m) {
        return false;
    } else if (val >= b) {
        return true;
    } else if (idx > n - 1) {
        return false;
    }
    int i;
    bool put;
    for (i = 1; i >= 0; i--) {
        put = (bool)i;
        sol[idx] = put;
        if (decide(sol, wgt + wgts[idx] * put, val + vals[idx] * put, idx+1, n, m, b, wgts, vals)) {
            return true;
        }
    }
    return false;
}

int main () {
    // INPUT FORMAT: "ID n M B weight value weight value"
    int id, n, m, b;
    cin >> id >> n >> m >> b;
    int *weights = new int [n];
    int *values = new int [n];
    int i = 0;
    while (cin >> weights[i] >> values[i++])
        ; // just reading the input

    // showProblem(n, m, b, weights, values);
    
    bool *solution = new bool [n];
    bool decision;

    decision = decide(solution, 0, 0, 0, n, m, b, weights, values);
    
    showDecision(decision, n, weights, values, solution);
    
    return 0;
}
#include <iostream>
#include <fstream>
#include <chrono>
#include "knapsack.h"

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
    cout << decision << "\t";
    int value = 0;
    int i;
    for (i = 0; i < n; i++)
        value += vals[i] * solution[i];
    cout << value << "\t";
    for (i = 0; i < n; i++)
        (i < n - 1)? cout << solution[i] << " ": cout << solution[i] << endl;
}

void writeDecision(ofstream *f_out, int id, bool decision, int n, int *wgts, int *vals, bool *solution)
{
    int value = 0;
    int i;
    for (i = 0; i < n; i++)
        value += vals[i] * solution[i];
    
    *f_out << id << " " << decision << " " << value << " ";
    for (i = 0; i < n; i++)
        (i < n - 1)? *f_out << solution[i] << " ": *f_out << solution[i] << endl;
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
    if (wgt > m) {
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

double solve(const char *file_in, const char *file_out)
{
    auto start = std::chrono::steady_clock::now();

    int id, n, m, b;
    int *weights, *values;
    int i;
    bool *solution;
    bool decision;

    ifstream f_in;
    f_in.open(file_in);
    ofstream f_out;
    f_out.open(file_out);

    while (f_in >> id >> n >> m >> b) {
        weights = new int [n];
        values = new int [n];
        for (i = 0; i < n; i++) {
            f_in >> weights[i] >> values[i];
        }
        // showProblem(n, m, b, weights, values);
        solution = new bool[n]();
        decision = decide(solution, 0, 0, 0, n, m, b, weights, values);
        writeDecision(&f_out, id, decision, n, weights, values, solution);
        delete weights;
        delete values;
        delete solution;
    }
    f_in.close();
    f_out.close();
    auto end = std::chrono::steady_clock::now();
    std::chrono::duration<double> elapsed_seconds = end-start;
    return elapsed_seconds.count();
}

int main () {
    double time;
    // time = solve("./data/nr/NR4_inst.dat", "./data/jl/NR4.txt");
    time = solve("./data/in", "./data/jl/NR4.txt"); //_10_1_10.txt

    
    // INPUT FORMAT: "ID n M B weight value weight value"
    // int id, n, m, b;
    // int *weights, *values;
    // int i;
    // bool *solution;
    // bool decision;

    // while (cin >> id >> n >> m >> b) {
    //     weights = new int [n];
    //     values = new int [n];
    //     for (i = 0; i < n; i++) {
    //         cin >> weights[i] >> values[i];
    //     }
    //     // showProblem(n, m, b, weights, values);
    //     solution = new bool[n]();
    //     decision = decide(solution, 0, 0, 0, n, m, b, weights, values);
    //     showDecision(decision, n, weights, values, solution);
    //     delete weights;
    //     delete values;
    //     delete solution;
    // }
    return 0;
}
#include <iostream>
#include <fstream>
#include <chrono>
#include <cassert>
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

void writeDecision(ofstream *f_out, int id, int n, bool decision, int *wgts, int *vals, 
    bool *solution, int complexity, double seconds)
{
    int value = 0;
    int i;
    for (i = 0; i < n; i++)
        value += vals[i] * solution[i];
    
    *f_out << id << " " << n << " " << decision << " " << value << " ";
    for (i = 0; i < n; i++)
        *f_out << solution[i] << " ";
    *f_out << complexity << " " << seconds << endl;
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
bool decide(bool *sol, int &cmx, int wgt, int val, int idx, int n, int m, int b, int *wgts, int *vals)
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
        cmx++; // *cmx += 1; // &((*cmx)++)
        if (decide(sol, cmx, wgt + wgts[idx] * put, val + vals[idx] * put, idx+1, n, m, b, wgts, vals)) {
            return true;
        }
    }
    return false;
}

bool decide_naive(bool *sol, bool *tmp, unsigned long long int &cmx, int wgt, int val, int idx,
    int n, int m, int b, int *wgts, int *vals)
{
    if (idx > n - 1) {
        cmx++;
        return (wgt <= m && val >= b)? true: false;
    }
    bool keep;
    bool *ptr;
    keep = (decide_naive(sol, tmp, cmx, wgt + wgts[idx], val + vals[idx], idx+1, n, m, b, wgts, vals));
    ptr = (keep)? tmp: sol;

    if (decide_naive(ptr, tmp, cmx, wgt, val, idx+1, n, m, b, wgts, vals) || keep)
        return true;
    return false;
}


double solve(const char *file_in, const char *file_out)
{
    int id, n, m, b;
    int *weights, *values;
    int i;
    bool *solution, *temporary;
    unsigned long long int complexity;
    double seconds;
    bool decision;

    ifstream f_in;
    f_in.open(file_in);
    assert(("Input file was not possible to open", f_in.fail() == false));
    ofstream f_out;
    f_out.open(file_out);
    assert(("Output file was not possible to create", f_out.fail() == false));

    while (f_in >> id >> n >> m >> b) {
        auto start = std::chrono::steady_clock::now();
        weights = new int [n];
        values = new int [n];
        for (i = 0; i < n; i++) {
            f_in >> weights[i] >> values[i];
        }
        // showProblem(n, m, b, weights, values);
        solution = new bool[n]();
        temporary = new bool[n];
        complexity = 0;
        decision = decide_naive(solution, temporary, complexity, 0, 0, 0, n, m, b, weights, values);
        
        auto end = std::chrono::steady_clock::now();
        std::chrono::duration<double> elapsed_seconds = end-start;
        seconds = elapsed_seconds.count();
        writeDecision(&f_out, id, n, decision, weights, values, solution, complexity, seconds);
        delete weights;
        delete values;
        delete solution;
    }
    f_in.close();
    f_out.close();
    return 0;
}

int main () {
    double time;
    // time = solve("./data/nr/NR4_inst.dat", "./data/jl/NR4.txt");
    // time = solve("../data/nr/NR4_inst.dat", "../blbost"); //_10_1_10.txt
    time = solve("../data/nr/NR15_inst.dat", "./test_here.txt"); //_10_1_10.txt
    cout << time << " seconds" << endl;
    
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
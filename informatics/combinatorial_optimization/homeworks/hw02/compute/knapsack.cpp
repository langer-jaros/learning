#include <vector>
#include <string>
#include <iostream>
#include <chrono>
#include <algorithm>
#include <iterator>

using namespace std;

enum APPROACH {
    BF=1,       // Brute Force
    BAB=2,      // Branch and Bound
    DP=3,       // Dynamic Programming
    GH=4,       // Greedy Heuristic
    REDUX=5,    // REDUX
    FPTAS=6     // FPTAS
};

struct Item {
    int i; // original index
    int w; // weight
    int v; // value
};

struct Problem {
    int id;                 // ID of the problem
    int n;                  // Number of items
    int W;                  // Weight capacity
    // int V;               // Required total value
    vector<Item> items;     // vector of items
    vector<int> val_left;   // sums of values left
    void init_size(int s){
        items = vector<Item>(s);
        val_left = vector<int>(s+1);
        val_left[0] = 0;
    };
};

struct State {
    int i; // index of the state item
    int w; // total weight of the state
    int v; // total value of the state
    int p; // previous weight or value
};

struct Result {
    int max_value;
    vector<bool> solution;              // boolean choice of every item
    vector<bool> sol_tmp;               // temporary vector of boolean solution
    unsigned long long int complexity;  // number of called recursion tails
    double seconds;                     // number of computation seconds
};

// void brute_force(Problem &prob, Result &resu)
// {
//     vector<bool> solution;
// }

// void branch_and_bound(Problem &prob, Result &resu)
// {

// }

void trace_back(Problem &prob, Result &resu, vector<vector<State>> &dp)
{
    int w = prob.W;
    int i;
    for (i = 0; i < prob.n; i++) {
        if (dp[i][w].w == dp[i][w].p) {
            resu.solution[i] = false;
            // w = dp[i][w].w;
        } else {
            resu.solution[i] = true;
            w = dp[i][w].p; // dp[i][w].w - prob.items[i].w;
        }
    }
}

void dynamic_programming(Problem &prob, Result &resu)
{
    int i, j;
    vector<vector<State>> dp(prob.n+1, vector<State>(prob.W+1));
    vector<State> choices;
    for (i = prob.n; i >= 0; i--) {
        for (j = 0; j <= prob.W; j++) {
            if (i == prob.n) {
                dp[i][j] = State({i, 0, 0, 0}); // = 0;
            } else {
                choices = vector<State>();
                choices.push_back({i, dp[i+1][j].w, dp[i+1][j].v, dp[i+1][j].w}); // dp[i+1][j]
                if (j >= prob.items[i].w) {
                    choices.push_back({i, dp[i+1][j-prob.items[i].w].w+prob.items[i].w,
                        dp[i+1][j-prob.items[i].w].v+prob.items[i].v, dp[i+1][j-prob.items[i].w].w});
                }
                auto max_st = max_element(choices.begin(), choices.end(),
                    [] (const State &ls, const State &rs) {return ls.v < rs.v;});
                dp[i][j] = *max_st;
            }
        }
    }
    trace_back(prob, resu, dp);
    resu.max_value = dp[0][prob.W].v;
}

bool cmp_value_per_weight(Item i1, Item i2) 
{ 
    return ((float)i1.v/i1.w >= (float)i2.v/i2.w);
}

void greedy_heuristic(Problem &prob, Result &resu)
{
    sort(prob.items.begin(), prob.items.end(), cmp_value_per_weight);
    int i;
    State st = {0, 0, 0, 0};
    for (i = 0; i < prob.n; i++) {
        if (st.w + prob.items[i].w <= prob.W) {
            st.w += prob.items[i].w;
            st.v += prob.items[i].v;
            resu.solution[prob.items[i].i] = true;
        } else {
            resu.solution[prob.items[i].i] = false;
        }
    }
    resu.max_value = st.v;
    return;
}

void redux(Problem &prob, Result &resu)
{
    greedy_heuristic(prob, resu);
    
    Problem problem;
    copy_if(prob.items.begin(), prob.items.end(), back_inserter(problem.items),
        [prob] (Item i) { return i.w <= prob.W; });

    if (problem.items.empty()) return;

    auto max_item = max_element(problem.items.begin(), problem.items.end(),
         [] (const Item &i1, const Item &i2) {return i1.v < i2.v;});

    if (max_item[0].v <= resu.max_value) return;

    resu.max_value = max_item[0].v;
    resu.solution = vector<bool>(prob.n);
    resu.solution[max_item[0].i] = true;
    return;
}

// void fptas(Problem &prob, Result &resu)
// {

// }

bool read_problem(Problem &p)
{
    int i, w, v;
    if (! (cin >> p.id >> p.n >> p.W))
        return false;
    p.init_size(p.n);
    for (i = 0; i < p.n; i++) {
        cin >> w >> v;
        p.items[i] = Item({i, w, v});
        p.val_left[i+1] = p.val_left[i] + v;
    }
    return true;
}

void write_result(Problem &p, Result &r)
{
    cout << p.id << " " << p.n << " " << r.max_value << " ";
    for (int i : r.solution)
        cout << i << " ";
    cout << endl;
}

int main(int argc, char **argv)
{
    if (argc != 2) return 1; // Approach is expected as a number 1-6

    APPROACH approach = (APPROACH)stoi(argv[1]);
    Problem problem;
    Result result;

    while (read_problem(problem)) {
        result = Result({0, vector<bool>(problem.n), vector<bool>(problem.n), 0, 0});
        
        auto start = std::chrono::steady_clock::now();
        switch (approach) {
            case BF:
                // brute_force(problem, result);
                break;
            case BAB:
                // branch_and_bound(problem, result);
                break;
            case DP:    dynamic_programming(problem, result);   break;
            case GH:    greedy_heuristic(problem, result);      break;
            case REDUX: redux(problem, result);                 break;
            case FPTAS:
                // fptas(problem, result);
                break;
        }
        auto end = std::chrono::steady_clock::now();
        result.seconds = (end-start).count();

        write_result(problem, result);
    }
    return 0;
}

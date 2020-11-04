#include <vector>
#include <string>
#include <iostream>
#include <chrono>

using namespace std;

struct ITEM {
    int w; // weight
    int v; // value
};

struct PROBLEM {
    int id;                 // ID of the problem
    int n;                  // Number of items
    int W;                  // Weight capacity
    // int V;               // Required total value
    vector<ITEM> items;     // vector of items
    vector<int> val_left;   // sums of values left
    void init_size(int s){
        items = vector<ITEM>(s);
        val_left = vector<int>(s+1);
        val_left[0] = 0;
    };
};

struct STATE {
    int index;  // index of the state item
    int weight; // total weight of the state
    int value;  // total value of the state
};

struct RESULT {
    int max_value;
    vector<bool> solution;              // boolean choice of every item
    vector<bool> sol_tmp;               // temporary vector of boolean solution
    unsigned long long int complexity;  // number of called recursion tails
    double seconds;                     // number of computation seconds
};

// void dynamic_programming(PROBLEM &prob, STATE &stat, RESULT &resu)
void dynamic_programming(PROBLEM &prob, RESULT &resu)
{
    int i, j;
    vector<vector<int>> dp(prob.n+1, vector<int>(prob.W+1));
    vector<int> choices;
    for (i = prob.n; i >= 0; i--) {
        for (j = 0; j <= prob.W; j++) {
            if (i == prob.n) {
                dp[i][j] = 0;
            } else {
                choices = vector<int>();
                choices.push_back(dp[i+1][j]);
                if (j >= prob.items[i].w) {
                    choices.push_back(dp[i+1][j-prob.items[i].w]+prob.items[i].v);
                }
                dp[i][j] = (choices.size() == 2)? max(choices[0], choices[1]): choices[0];
            }
        }
    }
    resu.max_value = dp[0][prob.W];
}

bool read_problem(PROBLEM &p)
{
    int i, w, v;
    if (! (cin >> p.id >> p.n >> p.W))
        return false;
    p.init_size(p.n);
    for (i = 0; i < p.n; i++) {
        cin >> w >> v;
        p.items[i] = ITEM({w, v});
        p.val_left[i+1] = p.val_left[i] + v;
    }
    return true;
}

void write_result(PROBLEM &p, RESULT &r)
{
    cout << p.id << " " << p.n << " " << r.max_value;
    for (int i : r.solution)
        cout << " " << i;
    cout << endl;
}

int main()
{
    PROBLEM problem;
    STATE state;
    RESULT result;

    while (read_problem(problem)) {
        state = STATE();
        result = RESULT();
        
        // auto start = std::chrono::steady_clock::now();
        // dynamic_programming(problem, state, result);
        dynamic_programming(problem, result);
        // auto end = std::chrono::steady_clock::now();
        // result.seconds = (end-start).count();

        write_result(problem, result);
    }
    return 0;
}

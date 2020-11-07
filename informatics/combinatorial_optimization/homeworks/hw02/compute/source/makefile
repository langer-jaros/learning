CC = g++

knapsack : ../knapsack.cpp build greedy_heuristic dynamic_programming read_problem knap_mock
	$(CC) -Wall -Wextra -pedantic ../knapsack.cpp -o build/knapsack

greedy_heuristic : greedy_heuristic.cpp build
	$(CC) -Wall -pedantic -Wextra -Werror greedy_heuristic.cpp -o build/greedy_heuristic
	g++ -g greedy_heuristic.cpp

dynamic_programming : dynamic_programming.cpp build
	$(CC) -Wall -Wextra -Werror dynamic_programming.cpp -o build/dynamic_programming

read_problem : read_problem.cpp build
	$(CC) -Wall -Wextra -Werror read_problem.cpp -o build/read_problem

knap_mock : knap_mock.cpp build
	$(CC) knap_mock.cpp -o build/knap_mock

clean:
	rm a.out
	rm build/*

CC = g++

knapsack : knapsack.cpp build knap_mock read_problem
	$(CC) knapsack.cpp -o build/knapsack

read_problem : read_problem.cpp build
	$(CC) -Wall -Wextra -Werror read_problem.cpp -o build/read_problem

knap_mock : knap_mock.cpp build
	$(CC) knap_mock.cpp -o build/knap_mock

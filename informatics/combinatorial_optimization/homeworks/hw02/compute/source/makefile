CC = g++

knapsack : ../knapsack.cpp build knap_mock read_problem dynamic_programming
	$(CC) ../knapsack.cpp -o build/knapsack

dynamic_programming : dynamic_programming.cpp build
	$(CC) -Wall -Wextra -Werror dynamic_programming.cpp -o build/dynamic_programming

read_problem : read_problem.cpp build
	$(CC) -Wall -Wextra -Werror read_problem.cpp -o build/read_problem

knap_mock : knap_mock.cpp build
	$(CC) knap_mock.cpp -o build/knap_mock

knapsack.so : knapsack.o
	g++ -shared -Wl,-soname,knapsack.so -o knapsack.so knapsack.o

knapsack.o : knapsack.cpp
	g++ -c -fPIC knapsack.cpp -o knapsack.o

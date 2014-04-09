#include <stdio.h>
#include <stdlib.h>

int fib(int);

int main(){
	printf("%d\n", fib(10));
}

int fib(int x){
	if(x == 0 || x == 1) return x; //Base case
	else return fib(x - 1) + fib(x - 2);
}

#include <stdio.h>

#define MAX 10000

unsigned long long memo[MAX];

unsigned long long fibonacci(int n) {
    if (n <= 1) {
        return n;
    } else if (memo[n] != 0) {
        return memo[n];
    } else {
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2);
        return memo[n];
    };
};

int main() {
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    if (num < 0) {
        printf("The Fibonacci sequence is not defined for negative numbers.\n");
    } else {
        printf("The Fibonacci number of %d is %llu\n", num, fibonacci(num));
    }

    return 0;
};
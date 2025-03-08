#include <stdio.h>

unsigned long long fibonacci(int n) {
    if (n <= 1) {
        return n;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
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
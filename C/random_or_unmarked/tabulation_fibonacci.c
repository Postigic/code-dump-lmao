#include <stdio.h>
#include <stdlib.h>

#define MAX 1000

unsigned long long fibonacci(int n) {
    unsigned long long* table = malloc((n + 1) * sizeof(unsigned long long));

    table[0] = 0;
    table[1] = 1;

    for (int i = 2; i <= n; i++) {
        table[i] = table[i - 1] + table[i - 2];
    };

    return table[n];
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
#include <stdio.h>

unsigned long long factorial(int n) {
    if (n <= 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

int main() {
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);
    
    if (num < 0) {
        printf("Factorials are not defined for negative numbers.\n");
    } else {
        printf("The factorial of %d is %llu\n", num, factorial(num));
    }
    
    return 0;
}
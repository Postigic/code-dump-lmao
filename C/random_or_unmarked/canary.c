#include <stdio.h>
#include <stdlib.h>

int main() {
    char buffer[8];
    int canary = 0xDEADBEEF;

    gets(buffer);

    if (canary != 0xDEADBEEF) {
        printf("You have been pwned! Canary: %d\n", canary);
        exit(1);
    }

    printf("You have not been pwned! Canary: %d\n", canary);
    return 0;
}
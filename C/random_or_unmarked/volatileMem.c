#include <stdio.h>

int main() {
    volatile int x = 0;
    int counter = 0;
    while (x == 0) {
        printf("%d\n", counter);
        counter++;
    }
    return 0;
}
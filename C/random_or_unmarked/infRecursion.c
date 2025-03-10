#include <stdio.h>

void recursive(int counter) {
    printf("%d\n", counter);
    recursive(counter + 1);
}

int main() {
    int counter = 0;
    recursive(counter);
    return 0;
}
#include <stdio.h>

int steps(int start) {
    if (start <= 0) {
        return -1;
    } else if (start == 1) {
        return 0;
    } else if (start % 2 == 0) {
        return 1 + steps(start / 2);
    } else {
        return 1 + steps(3 * start + 1);
    }
}

int main() {
    int start;
    printf("Enter a number: ");
    scanf("%d", &start);

    printf("Number of steps: %d\n", steps(start));
    return 0;
}
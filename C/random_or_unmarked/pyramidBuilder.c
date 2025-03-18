#include <stdio.h>

int main() {
    int max_width = 200;
    int i, j;

    for (i = 1; i <= max_width; i += 2) {
        int spaces = (max_width - i) / 2;

        for (j = 0; j < spaces; j++) {
            printf(" ");
        }

        for (j = 0; j < i; j++) {
            printf("*");
        }

        printf("\n");
    }

    return 0;
}
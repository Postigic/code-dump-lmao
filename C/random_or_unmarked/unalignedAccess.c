#include <stdio.h>

int main() {
    char data[5] = {1, 2, 3, 4, 5};
    int *ptr = (int *)(data + 1);
    printf("%d\n", *ptr);
    return 0;
}
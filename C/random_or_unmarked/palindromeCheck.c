#include <stdio.h>
#include <string.h>

void reverseStr(char str[]) {
    int left = 0;
    int right = strlen(str) - 1;
    char temp;

    while (left < right) {
        temp = str[left];
        str[left] = str[right];
        str[right] = temp;

        left++;
        right--;
    }
}

int main() {
    char str[100], rev[100];

    printf("Enter a string: ");
    scanf("%s", str);

    strcpy(rev, str);
    reverseStr(rev);  // strrev(rev);

    printf("The string %s is %s\n", str, (strcmp(str, rev) == 0) ? "a palindrome." : "not a palindrome.");

    return 0;
}
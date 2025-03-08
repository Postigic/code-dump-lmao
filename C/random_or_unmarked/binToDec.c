#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

int binaryToDecimal(const char *binaryStr) {
    int decimalValue = 0;
    int length = strlen(binaryStr);

    for (int i = 0; i < length; i++) {
        if (binaryStr[length - i - 1] == '1') {
            decimalValue += pow(2, i);
        }
    }

    if (binaryStr[0] == '1' && length > 1) {
        decimalValue -= pow(2, length);
    }

    return decimalValue;
}

int main() {
    char binaryStr[100];

    while (1) {
        printf("Enter a binary number: ");
        scanf("%s", binaryStr);
        
        int isValid = 1;
        for (int i = 0; i < strlen(binaryStr); i++) {
            if (binaryStr[i] != '0' && binaryStr[i] != '1') {
                isValid = 0;
                break;
            }
        }

        if (isValid) {
            break;
        } else {
            printf("Invalid input. Only '0' and '1' are allowed.\n");
        }
    }

    int decimalValue = binaryToDecimal(binaryStr);
    printf("Decimal value: %d\n", decimalValue);

    return 0;
}
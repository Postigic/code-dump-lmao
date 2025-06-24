#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

void clear_input_buffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

double get_valid_number(const char *prompt) {
    double num;
    char input[100];
    while (true) {
        printf("%s", prompt);
        if (fgets(input, sizeof(input), stdin) != NULL) {
            if (sscanf(input, "%lf", &num) == 1) {
                return num;
            } else {
                printf("Invalid input. Please enter a valid number.\n");
            }
        } else {
            printf("Error reading input. Please try again.\n");
        }
    }
}

char get_valid_operator(const char *prompt) {
    char op;

    while (true) {
        printf("%s", prompt);
        op = getchar();
        clear_input_buffer();
        if (op == '+' || op == '-' || op == '*' || op == '/') {
            return op;
        } else {
            printf("Invalid operator. Please enter one of (+, -, *, /).\n");
        }
    }
}

int main() {
    double num1, num2;
    char operation;

    while (true) {
        num1 = get_valid_number("Enter first number: ");
        num2 = get_valid_number("Enter second number: ");
        operation = get_valid_operator("Enter operator (+, -, *, /): ");

        switch (operation) {
            case '+':
                printf("Result: %lf\n", num1 + num2);
                break;
            case '-':
                printf("Result: %lf\n", num1 - num2);
                break;
            case '*':
                printf("Result: %lf\n", num1 * num2);
                break;
            case '/':
                if (num2 != 0) {
                    printf("Result: %lf\n", num1 / num2);
                } else {
                    printf("Error: Division by zero is not allowed.\n");
                }
                break;
        }

        char choice;
        printf("Do you want to perform another calculation? (Y/N): ");
        choice = getchar();
        clear_input_buffer();
        if (toupper(choice) != 'Y') {
            printf("Goodbye!\n");
            break;
        }
    }

    return 0;
}

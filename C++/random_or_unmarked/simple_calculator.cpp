#include <iostream>

using namespace std;

int main() {
    double num1, num2;
    char operation;
    while (true) {
        cout << "Enter first number: ";
        cin >> num1;
        cout << "Enter second number: ";
        cin >> num2;
        cout << "Enter operator (+, -, *, /): ";
        cin >> operation;

        if (operation == '+') {
            cout << num1 + num2 << "\n";
        } 
        else if (operation == '-') {
            cout << num1 - num2 << "\n";
        } 
        else if (operation == '*') {
            cout << num1 * num2 << "\n";
        } 
        else if (operation == '/') {
            if (num2 != 0) {
                cout << num1 / num2 << "\n";
            } else {
                cout << "Error. Division by zero is not allowed." << "\n";
            }
        } 
        else {
            cout << "Invalid operator." << "\n";
        }
    }
}
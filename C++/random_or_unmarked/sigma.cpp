#include <iostream>
#include <string>
using namespace std;

int main() {
    int mark = 70;
    char grade = (mark >= 70) ? 'M' : (mark >= 50) ? 'P' : 'F';

    cout << grade << "\n";

    unsigned long long num = 1234567890123456789;
    cout << num << "\n";

    string name;
    int age;
    
    cout << "Enter your name: ";
    cin >> name;
    cout << "Enter your age: ";
    cin >> age;

    cout << "Hello, my name is " << name << " and I am " << age << " years old!" << "\n";
    return 0;
}
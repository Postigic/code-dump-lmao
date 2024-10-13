#include <iostream>
#include <ctime>
#include <limits>

int main() {
    int num;
    int guess;
    int tries;

    srand(time(0));
    num = rand() % 100 + 1;
    tries = 0;

    std::cout << "Number Guessing Game!\n";
    std::cout << "*********************\n";

    do {
        std::cout << "Enter a guess between 1 to 100: ";

        while (!(std::cin >> guess) || std::cin.peek() != '\n' || guess < 1 || guess > 100) {
            std::cout << "Invalid input. Please enter a number between 1 and 100: ";
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        }

        tries++;

        if (guess > num) {
            std::cout << "Too high!\n";
        }
        else if (guess < num) {
            std::cout << "Too low!\n";
        }
        else {
            std::cout << "Correct! Number of tries: " << tries << "\n";
        }
    } while (guess != num);

    return '\0';
}

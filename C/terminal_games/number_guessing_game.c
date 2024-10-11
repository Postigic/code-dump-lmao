#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    const int MIN = 1;
    const int MAX = 100;
    int num;
    int guess;
    int tries;
    
    srand(time(0));
    num = rand() % (MAX - MIN + 1) + MIN;
    tries = 0;

    printf("Number Guessing Game!\n");
    printf("*********************\n");

    do
    {
        printf("Enter a guess between %d and %d: ", MIN, MAX);
        
        while (scanf("%d", &guess) != 1 || guess < MIN || guess > MAX) {
            printf("Invalid input. Please enter a guess between %d and %d: ", MIN, MAX);
            while (getchar() != '\n');
        }

        while (getchar() != '\n') {
            continue;
        }

        tries++;

        if (guess > num) {
            printf("Too high!\n");
        }
        else if (guess < num) {
            printf("Too low!\n");
        }
        else {
            printf("Correct! Number of tries: %d\n", tries);
        }
    } while (guess != num);
    
    return 0;
}
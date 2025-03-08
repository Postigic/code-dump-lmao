#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char getUserChoice();
char getComputerChoice();
void showChoice(char choice);
void chooseWinner(char player, char computer);

int main() {
    char player;
    char computer;

    player = getUserChoice();
    printf("Your choice: ");
    showChoice(player);

    computer = getComputerChoice();
    printf("Computer's choice: ");
    showChoice(computer);

    chooseWinner(player, computer);

    return 0;
}

char getUserChoice() {
    char player;
    printf("Rock-Paper-Scissors Game!\n");

    do {
        printf("*************************\n");
        printf("Choose one of the following:\n");
        printf("'r' for rock\n");
        printf("'p' for paper\n");
        printf("'s' for scissors\n");
        scanf("%c", &player);
    } while (player != 'r' && player != 'p' && player != 's');

    return player;
}

char getComputerChoice() {
    srand(time(0));
    int num = rand() % 3 + 1;

    switch (num) {
        case 1: return 'r';

        case 2: return 'p';

        case 3: return 's';
    }

    return '\0';
}

void showChoice(char choice) {
    switch (choice) {
        case 'r': printf("Rock\n"); break;

        case 'p': printf("Paper\n"); break;

        case 's': printf("Scissors\n"); break;
    }
}

void chooseWinner(char player, char computer) {
    switch (player) {
        case 'r':   if (computer == 'r') {
                        printf("Draw!\n");
                    }
                    else if (computer == 'p') {
                        printf("You lose!\n");
                    }
                    else {
                        printf("You win!\n");
                    }
                    break;

        case 'p':   if (computer == 'r') {
                        printf("You win!\n");
                    }
                    else if (computer == 'p') {
                        printf("Draw!\n");
                    }
                    else {
                        printf("You lose!\n");
                    }
                    break;

        case 's':   if (computer == 'r') {
                        printf("You lose!\n");
                    }
                    else if (computer == 'p') {
                        printf("You win!\n");
                    }
                    else {
                        printf("Draw!\n");
                    }
                    break;
    }
}
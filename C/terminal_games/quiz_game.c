#include <stdio.h>
#include <ctype.h>

int main() {
    char questions[][100] = {
        "1. What year did the C language debut?",
        "2. Who is credited with creating C?",
        "3. What is the predecessor of C?"
    };

    char options[][100] = {
        "A. 1970\nB. 1972\nC. 1978\nD. 1980",
        "A. Dennis Ritchie\nB. Ken Thompson\nC. Bjarne Stroustrup\nD. Linus Torvalds",
        "A. B\nB. BCPL\nC. Assembly\nD. Objective C"
    };

    char answers[] = {'B', 'A', 'A'};
    int numberOfQuestions = sizeof(questions) / sizeof(questions[0]);

    char guess;
    int score;

    printf("Quiz Game!\n");
    printf("**********\n");

    for (int i = 0; i < numberOfQuestions; i++) {
        printf("%s\n", questions[i]);
        printf("%s\n", options[i]);

        printf("Enter your answer: ");
        scanf("%c", &guess);
        guess = toupper(guess);

        while (getchar() != '\n');

        if (guess == answers[i]) {
            printf("\nCorrect!\n\n");
            score++;
        } else {
            printf("\nIncorrect!\n\n");
        }
    }

    printf("Score: %d/%d\n", score, numberOfQuestions);

    return 0;
}
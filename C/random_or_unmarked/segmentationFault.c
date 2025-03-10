#include <stdio.h>
#include <signal.h>
#include <stdlib.h>

void signal_handler(int signum) {
    printf("Caught signal %d (Segmentation Fault)!\n", signum);
    exit(1);
}

int main() {
    signal(SIGSEGV, signal_handler);

    int *p = NULL;

    *p = 10;

    return 0;
}

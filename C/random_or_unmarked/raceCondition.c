#include <windows.h>
#include <stdio.h>

int shared = 0;

DWORD WINAPI thread_func(LPVOID arg) {
    for (int i = 0; i < 1000000; i++) {
        shared++;
    }
    return 0;
}

int main() {
    HANDLE t1 = CreateThread(NULL, 0, thread_func, NULL, 0, NULL);
    HANDLE t2 = CreateThread(NULL, 0, thread_func, NULL, 0, NULL);

    WaitForSingleObject(t1, INFINITE);
    WaitForSingleObject(t2, INFINITE);

    printf("%d\n", shared);

    return 0;
}

// #include <windows.h>
// #include <stdio.h>

// int shared = 0;
// CRITICAL_SECTION criticalSection;

// DWORD WINAPI thread_func(LPVOID arg) {
//     for (int i = 0; i < 1000000; i++) {
//         EnterCriticalSection(&criticalSection);
//         shared++;
//         LeaveCriticalSection(&criticalSection);
//     }
//     return 0;
// }

// int main() {
//     InitializeCriticalSection(&criticalSection);

//     HANDLE t1 = CreateThread(NULL, 0, thread_func, NULL, 0, NULL);
//     HANDLE t2 = CreateThread(NULL, 0, thread_func, NULL, 0, NULL);

//     WaitForSingleObject(t1, INFINITE);
//     WaitForSingleObject(t2, INFINITE);

//     DeleteCriticalSection(&criticalSection);

//     printf("%d\n", shared);

//     return 0;
// }

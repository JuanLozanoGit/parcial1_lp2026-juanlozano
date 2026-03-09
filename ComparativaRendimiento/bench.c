#include <stdio.h>
#include <time.h>

long long fibo(int n) {
    if (n <= 1) return n;
    return fibo(n-1) + fibo(n-2);
}

int main() {
    clock_t start = clock();
    long long res = fibo(40);
    double time = (double)(clock() - start) / CLOCKS_PER_SEC;
    printf("C Result: %lld | Time: %.4f s\n", res, time);
    return 0;
}

#include <stdio.h>

int main() {
    int sayi = 10;
    int *ptr;      
    ptr = &sayi;    
    *ptr = 20;

    printf("Yeni değer: %d\n", sayi);

    return 0;
}
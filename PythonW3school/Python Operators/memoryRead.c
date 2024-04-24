#include <stdio.h>

int main() {
    int value = 42; /
    int *ptr = &value; 

    printf("Değer: %d\n", value); 
    printf("Değerin Bellek Adresi: %p\n", (void*)&value);
    printf("İşaretçinin İşaret Ettiği Değer: %d\n", *ptr); 
    
    return 0;
}
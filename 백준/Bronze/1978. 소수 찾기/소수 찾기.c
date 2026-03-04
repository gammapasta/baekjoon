#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    int num = 0;
    int total = 0;
    scanf("%d", &num);

    for(int i = 0; i < num; i++) {
        int prime = 0;

        scanf("%d", &prime);
        int sum = 0;
        if(prime == 1) {
            continue;
        }

        for(int j = 1; j < (prime/2+1); j++) {
            if(prime % j == 0) {
                sum += j;
            }
        }

        if(sum <= 1) {
            total++;
        }
    }

    printf("%d", total);
    return 0;
}
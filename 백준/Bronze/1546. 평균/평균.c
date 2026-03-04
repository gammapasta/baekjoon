#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void swap(int *arr, int num) {

    for(int i = 0; i < (num - 1); i++) {
        for(int j = 0; j < num - i - 1; j++) {
            if(arr[j + 1] < arr[j]) {
                int temp = arr[j + 1];
                arr[j + 1] = arr[j];
                arr[j] = temp;
            }
        }
    }
}
int main(void) {
    int num = 0;
    scanf("%d", &num);
    int arr[1001] = {0};

    for(int i = 0; i < num; i++) {
        int temp = 0;
        scanf("%d", &temp);
        arr[i] = temp;
    }

    swap(arr, num);

    int top = arr[num - 1];
    double arr2[1001] = {0};

    double newSum = 0;
    for(int i = 0; i < num; i++) {
        arr2[i] = ((double)arr[i] / (double)top * 100.0);
        newSum += arr2[i];
    }

    printf("%lf\n", newSum / num);
    return 0;
}
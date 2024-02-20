#include <stdio.h>

int main(){
    int num[1002] = {0};
    int start, end;
    int index = 1;
    int count = 1;
    int sum = 0;

    for (int i = 1; i < 1001; i++){
        num[i] = count;
        index--;
        if (index == 0){
            index = ++count;
        }
    }
    scanf("%d %d", &start, &end);

    for(int i=start; i<=end; i++){
        sum += num[i];
    }
    printf("%d", sum);

    return 0;
}
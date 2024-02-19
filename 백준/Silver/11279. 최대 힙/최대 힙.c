#include <stdio.h>
#include <stdlib.h>

// 자식에서 부모 나누기 2
// 부모에서 왼쪽 자식 *2 +1
//         오른쪽 자식 *2 +2

void max_heap_insert(int *array, int *size, int insert)
{
    int i = ++(*size);

    while((i != 1) && (insert > *(array+(i/2)))){
        *(array + i) = *(array + (i/2));
        i /= 2;
    }
    *(array + i) = insert;
    //printf("insert %d / size %d\n", insert, *size);
}

int max_heap_del(int *array, int *size)
{
    int parent, child; //index
    int delete, temp;  //item

    delete = *(array + 1);
    temp = *(array + (*size)--);
    //printf("del %d / size-- %d\n", delete, *size);
    parent = 1; child = 2;

    while (child <= *size){
        if((child < *size) && (*(array + child) < *(array + child + 1)))
            child++;

        if (temp >= *(array + child))
            break;

        *(array + parent) = *(array + child);
        parent = child;
        child *= 2;
    }
    *(array + parent) = temp;

    return delete;
}

int main(){
    int *array;
    int size = 0;
    int N = 0;
    int insert;
    
    scanf("%d", &N);
    array = (int *)malloc((N+1) * sizeof(int));

    for (int i=0; i<N; i++){
        scanf("%d", &insert);

        if(insert == 0){
            if (size == 0){
                printf("0\n");
                continue;
            }
            int a = max_heap_del(array, &size);
            printf("%d\n", a);
        }
        else{
            max_heap_insert(array, &size, insert);
        }
        //print_heap(array, size);
    }

    return 0;
}
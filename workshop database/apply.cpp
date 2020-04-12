#include<stdio.h>
#include<stdlib.h>


int main(){
    FILE *f;
    f = fopen("apply.csv", "w");
    for (int i = 0; i < 52800; i++)
    {
        fprintf(f, "%d\n", rand() % (20 - 1 + 1) + 1);
    }
    fclose(f);
    return 0;
}
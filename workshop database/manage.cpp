#include<stdlib.h>
#include<stdio.h>
int main(){
    FILE *f;
    f=fopen("manage.csv","w");
    for(int i=0;i<10;i++){
        fprintf(f,"10000,JEwcI\n");
    }
    fclose(f);
    return 0;
}
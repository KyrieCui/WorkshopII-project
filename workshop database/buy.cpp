#include<stdio.h>
#include<stdlib.h>

int main(){
    FILE *f;
    f=fopen("buy.csv","w");
    for(int i=0;i<10000;i++){
        for(int j=10001;j<=10010;j++){
            fprintf(f,"%d,%d\n",j,rand()%(25-1+1)+1);
        }
    }
    fclose(f);
    return 0;
}
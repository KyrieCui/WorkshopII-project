#include <stdio.h>
#include <stdlib.h>
#include<time.h>


int main(){
    FILE *f;
    f = fopen("account.csv", "w");
    int passwd;
    for(int i=10000;i<=100000;i++){
        passwd = rand()%(654321 - 123456 + 1) + 123456;
        
        
        fprintf(f, "%d,%d\n", i,passwd);
       
    }

    fclose(f);
    return 0;

}
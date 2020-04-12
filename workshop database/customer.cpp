#include<stdlib.h>
#include<stdio.h>
#include<time.h>
int main(){
    FILE *f;
    f=fopen("customer.csv","w");
    for(int i=0;i<60000;i++){
        for(int j=1;j<=4;j++){
            int age = rand() % (22 - 18 + 1) + 18;
            if(age-j+1==18)
                fprintf(f, "%d,M,V%d,%d\n", j, rand() % (28 - 15 + 1) + 15,age );
        }
    }
    for (int i = 0; i < 65000; i++)
    {
        for (int j = 1; j <= 4; j++)
        {
            int age = rand() % (22 - 18 + 1) + 18;
            if (age - j + 1 == 18)
                fprintf(f, "%d,F,V%d,%d\n", j, rand() % (28 - 15 + 1) + 15, age);
        }
    }
    fclose(f);
    return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    FILE *f;
    int profit;
    f = fopen("checkout.csv", "w");
    for (int i = 0; i < 100; i++)
    {
        for (int i = 1; i <= 31; i++)
        {
            for (int j = 1; j <= 12; j++)
            {
                profit = rand() % 2000;
                fprintf(f, "10000,JEwcI,2017-%d-%d,%d\n", j, i, profit);
            }
        }
    }
    fclose(f);
    return 0;
}
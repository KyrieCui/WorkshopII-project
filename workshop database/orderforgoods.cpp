#include <stdlib.h>
#include <stdio.h>
int main()
{
    FILE *f;
    f = fopen("orderforgoods.csv", "w");
    for (int i = 0; i < 30; i++)
    {
        for (int i = 1; i <= 31; i++)
        {
            for (int j = 1; j <= 12; j++)
            {
            
                fprintf(f, "2017-%d-%d,%d\n", j, i,rand()%(100000-10011+1)+10011);
            }
        }
    }
    fclose(f);
    return 0;
}   
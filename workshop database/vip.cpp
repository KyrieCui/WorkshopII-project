#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    FILE *f;
    f = fopen("vip.csv", "w");
    int vipPoint;
    for (int i = 10000; i <= 100000; i++)
    {
        vipPoint = rand() % (100 - 0 + 1) + 0;

        fprintf(f, "%d,%d\n", i, vipPoint);
    }

    fclose(f);
    return 0;
}
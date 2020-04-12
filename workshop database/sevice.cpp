#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *f;
    f = fopen("service.csv", "w");
    for (int i = 0; i < 100000; i++)
    {
        fprintf(f, "JEwcI\n");
    }
    fclose(f);
    return 0;
}
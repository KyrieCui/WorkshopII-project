#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 5 //固定长度为10
int main()
{
    FILE *f;
    f = fopen("login.csv", "w");
    int flag, charLengt;
    int i, j, k = 0;
    char ch[N + 1] = {NULL};
    srand((unsigned)time(NULL));
    for (i = 0; i < 90000; i++) //生成10个String吧
    {
        for (j = 0; j < N; j++)
        {
            flag = rand() % 2;
            if (flag)
                ch[k++] = 'A' + rand() % 26;
            else
                ch[k++] = 'a' + rand() % 26;
        }
        ch[k] = '\0';
        k = 0;
        fprintf(f, "%s\n",ch);
    }
    fclose(f);
    return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main()
{
    FILE *f;
    f = fopen("goods.csv", "w");
    for(int i=1;i<=1100;i++){
        fprintf(f, "%d,drink,Ceston,1,1100,0\n", i);
    }
    for(int i=1101;i<=2200;i++){
        fprintf(f, "%d,drink,Coca Cola,3,1100,0\n", i);
    }
    for(int i=2201;i<=3300;i++){
        fprintf(f, "%d,drink,Pepsi Cola,3,1100,0\n", i);
    }
    for(int i=3301;i<=4400;i++){
        fprintf(f, "%d,drink,Watson,2,1100,0\n",i);
    }
    for(int i=4401;i<=5500;i++){
        fprintf(f, "%d,drink,Kang Shifu black tea,3,1100,0\n", i);
    }
    for(int i=5501;i<=6600;i++){
        fprintf(f, "%d,drink,Kang Shifu green tea,2,1100,0\n", i);
    }
    for(int i=6601;i<=7700;i++){
        fprintf(f, "%d,drink,Sprite,3,1100,0\n", i);
    }
    for(int i=7701;i<=8800;i++){
        fprintf(f, "%d,drink,Sarsae,5,1100,0\n",i);
    }
    for(int i=8801;i<=9900;i++){
        fprintf(f, "%d,fruit,banana,4,1100,0\n", i);
    }
    for(int i=9901;i<=11000;i++){
        fprintf(f, "%d,fruit,apple,3,1100,0\n", i);
    }
    for(int i=11001;i<=12100;i++){
        fprintf(f, "%d,fruit,Pitaya,6,1100,0\n", i);
    }
    for(int i=12101;i<=13200;i++){
        fprintf(f, "%d,fruit,Durian,15,1100,0\n", i);
    }
    for(int i=13201;i<=14300;i++){
        fprintf(f, "%d,fruit,Grape,7,1100,0\n", i);
    }
    for(int i=14301;i<=15400;i++){
        fprintf(f, "%d,fruit,Honeydew melon,25,1100,0\n",i);
    }
    for(int i=15401;i<=16500;i++){
        fprintf(f, "%d,fruit,Litchi,15,1100,0\n", i);
    }
    for(int i=16501;i<=17600;i++){
        fprintf(f, "%d,fruit,pineapple,30,1100,0\n", i);
    }
    for(int i=17601;i<=18700;i++){
        fprintf(f, "%d,snack,Lays,5,1100,0\n", i);
    }
    for(int i=18701;i<=19800;i++){
        fprintf(f, "%d,snack,melon seed,7,1100,0\n", i);
    }
    for (int i = 19801; i <= 20900; i++)
    {
        fprintf(f, "%d,snack,Spicy strips,2,1100,0\n", i);
    }
    for (int i = 20901; i <= 22000; i++)
    {
        fprintf(f, "%d,snack,Cup Noodle,5,1100,0\n", i);
    }
    for (int i = 22001; i <= 23100; i++)
    {
        fprintf(f, "%d,snack,Kang Shifu Noodle,4,1100,0\n", i);
    }
    for (int i = 23101; i <= 24200; i++)
    {
        fprintf(f, "%d,snack,Tongyi Noodle,5,1100,0\n", i);
    }
    for (int i = 24201; i <= 25300; i++)
    {
        fprintf(f, "%d,snack,Chicken Feet with Pickled Peppers,6,1100,0\n", i);
    }
    for (int i = 25301; i <= 26400; i++)
    {
        fprintf(f, "%d,snack,Laver,4,1100,0\n", i);
    }
    for (int i = 26401; i <= 27500; i++)
    {
        fprintf(f, "%d,daily,Broom,9,1100,0\n", i);
    }
    for (int i = 27501; i <= 28600; i++)
    {
        fprintf(f, "%d,daily,Mop,15,1100,0\n", i);
    }
    for (int i = 28601; i <= 29700; i++)
    {
        fprintf(f, "%d,daily,Towel,6,1100,0\n", i);
    }
    for (int i = 29701; i <= 30800; i++)
    {
        fprintf(f, "%d,daily,toothbrush,8,1100,0\n", i);
    }
    for (int i = 30801; i <= 31900; i++)
    {
        fprintf(f, "%d,daily,cup,10,1100,0\n", i);
    }
    for (int i = 31901; i <= 33000; i++)
    {
        fprintf(f, "%d,daily,Coat hanger,4,1100,0\n", i);
    }
    for (int i = 33001; i <= 34100; i++)
    {
        fprintf(f, "%d,daily,Liquid soap,20,1100,0\n", i);
    }
    for (int i = 34101; i <= 35200; i++)
    {
        fprintf(f, "%d,daily,toothpaste,5,1100,0\n", i);
    }
    for (int i = 35201; i <= 36300; i++)
    {
        fprintf(f, "%d,sports,badminton,5,1100,0\n", i);
    }
    for (int i = 36301; i <= 37400; i++)
    {
        fprintf(f, "%d,sports,badminton racket,50,1100,0\n", i);
    }
    for (int i = 37401; i <= 38500; i++)
    {
        fprintf(f, "%d,sports,table tennis,3,1100,0\n", i);
    }
    for (int i = 38501; i <= 39600; i++)
    {
        fprintf(f, "%d,sports,table tennis racket,40,1100,0\n", i);
    }
    for (int i = 39601; i <= 40700; i++)
    {
        fprintf(f, "%d,sports,tennis,10,1100,0\n", i);
    }
    for (int i = 40701; i <= 41800; i++)
    {
        fprintf(f, "%d,sports,tennis racket,200,1100,0\n", i);
    }
    for (int i = 41801; i <= 42900; i++)
    {
        fprintf(f, "%d,sports,basketball,200,1100,0\n", i);
    }
    for (int i = 42901; i <= 44000; i++)
    {
        fprintf(f, "%d,sports,rootball,150,1100,0\n", i);
    }
    for (int i = 44001; i <= 45100; i++)
    {
        fprintf(f, "%d,Stationery,pencil,6,1100,0\n", i);
    }
    for (int i = 45101; i <= 46200; i++)
    {
        fprintf(f, "%d,Stationery,rubber,5,1100,0\n", i);
    }
    for (int i = 46201; i <= 47300; i++)
    {
        fprintf(f, "%d,Stationery,ruler,8,1100,0\n", i);
    }
    for (int i = 47301; i <= 48400; i++)
    {
        fprintf(f, "%d,Stationery,pen,15,1100,0\n", i);
    }
    for (int i = 48401; i <= 49500; i++)
    {
        fprintf(f, "%d,Stationery,Signature pen,5,1100,0\n", i);
    }
    for (int i = 49501; i <= 50600; i++)
    {
        fprintf(f, "%d,Stationery,Pencil case,25,1100,0\n", i);
    }
    for (int i = 50601; i <= 51700; i++)
    {
        fprintf(f, "%d,Stationery,ear phone,70,1100,0\n", i);
    }
    for (int i = 51701; i <= 52800; i++)
    {
        fprintf(f, "%d,Stationery,Battery,30,1100,0\n", i);
    }
    fclose(f);

    return 0;
}


#include <cs50.h>
#include <stdio.h>
#include <math.h>

float get_positive_float(void);
int get_remain(int num);

int main(void)
{
    float dollars = get_positive_float();
    // int change_in_cents = round(dollars * 100);
    int remain = round(dollars * 100);

    int coins = 0;
    while (remain > 0)
    {
        remain = get_remain(remain);
        coins++;
    }
    printf("coins = %i \n", coins);
}

float get_positive_float(void)
{
    float n;
    do
    {
        n = get_float("Change owed: ");
    }
    while (n <= 0);
    return n;
}

int get_remain(int num)
{

	int remain = num >= 25 ? num - 25
        : num >= 10 ? num - 10
        : num >= 5 ?  num - 5
        : num >= 1 ?  num - 1 
        :num ;

	return remain;
}


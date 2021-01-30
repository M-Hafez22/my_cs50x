#include <cs50.h>
#include <stdio.h>

int get_height_int(void);
void print_space(int n); 

int main(void)
{
    int height = get_height_int();
    print_space(height);
}

// get number between 1-8
int get_height_int(void)
{
    int n;
    do
    {
        n = get_int("height: ");
    }
    while (n < 1 || n > 8);
    return n;
}

void print_space(int n)
{
    for(int i=0; i < n; i++)
    {
        printf(".");
    }
}

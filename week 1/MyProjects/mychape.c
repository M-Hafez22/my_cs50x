#include <cs50.h>
#include <stdio.h>

int get_positive_int(string);

int main(void)
{
    int width = get_positive_int("width");
    int height = get_positive_int("height");
    
    for(int i = 0; i < height; i++){
        for (int j = 0; j < width; j++){
            printf(" #");
        }
        printf("\n");
    }
}

int get_positive_int(string demintion)
{
    int n;
    do
    {
        n = get_int("%s: ", demintion);
    }
    while (n < 1);
    return n;
}

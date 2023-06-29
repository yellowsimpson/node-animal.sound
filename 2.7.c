#include <stdio.h>

int main(void)
{
    int amount, $20, $10, $5, $1;

    printf("Enter a doolar amount:");
    scanf("%d", &amount);

    $20= amount/ 20;
    amount= amount - $20*20;

    $10= amount/ 10;
    amount= amount-$10;

    $5= amount/ 5;
    amount= amount-$5*5;

    $1 = amount;

    printf("$20 bills: %d\n", $20);
    printf("$10 bills: %d\n", $10);
    printf("$5 bills: %d\n", $5);
    printf("$1 bills: %d\n", $1);
    
    return 0;
}
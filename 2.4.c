#include <stdio.h>

int main()
{
    double Enter_amount, amount_with_tax;

    Enter_amount=100;
    amount_with_tax=105;

    printf("Enter an amount:");
    scanf("%lf", &Enter_amount);

    amount_with_tax=Enter_amount*1.05;
    printf("With tax added: $%.21f\n", amount_with_tax);

    return 0;
}
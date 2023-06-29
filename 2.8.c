#include <stdio.h>

int main()
{
    double balance;
    double interest;
    double payment;

    printf("Enter amount of laon:");
    scanf_s("%lf", &balance);
    printf("Enter interest rate:");
    scanf_s("%lf", &interest);
    printf("Enter amount of loan:");
    scanf_s("%lf", &payment);

    char* a[]={ "first", "second","third"};

    for (int i = 0; i<3; i++) {
        balance *= (1+ interest * 0.01/12);
        balance -= payment;
        printf("Balance remaining after %s payment: $%,2f\n", a[i], balance);
    }
}

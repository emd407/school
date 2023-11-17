#include <stdio.h>
#include <stdlib.h>
/*
Assignment  M2PA
File        prog4.c

Student:    [Eric Dixon] [U90014290]
Date:       [10/28/22]

Features:   [This program calculates payoff based on rules of the game]
Bugs:       [Specify here remaining bugs at time of submission]
*/

int main()
{
int R1 =0;
int R2 = 0;
int R3 = 0;
int payoff = 0;

    // Prompt the user to enter values for R1, validating it's within range (1-6)
    do {
        printf("Enter values for R1 (1-6): ");
        scanf("%d", &R1);
    } while (R1 < 1 || R1 > 6);
   
   // Prompt the user to enter values for R2, validating it's within range (1-6)	
    do {
        printf("Enter values for R2 (1-6): ");
        scanf("%d", &R2);
    } while (R2 < 1 || R2 > 6);
   
   // Prompt the user to enter values for R3, validating it's within range (1-6)
    do {
        printf("Enter values for R3 (1-6): ");
        scanf("%d", &R3);
    } while (R3 < 1 || R3 > 6);

    // Compute the payoff based on the rules
    payoff = R1; //set payoff to R1 per instructions

    if (R2 < R1) {
        payoff += R2;

        if (R3 < R2) {
            payoff += 2 * R3;
        } else if (R3 < R1) {
            payoff += R3;
        }
    } else if (R3 < R1) {
        payoff += R3;
    }

    // Print the payoff
    printf("Payoff: %d\n", payoff);
    
    return EXIT_SUCCESS;
}

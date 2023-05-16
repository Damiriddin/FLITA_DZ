#include <stdio.h>
#include <stdlib.h>


int  main()
{
    int num;
    printf("Enter a number num = ");
    scanf("%d",&num);
    for (int i = 2; i <= num ;i++ ){
         int prime = 1;
        for(int j = 2;j<i;j++){
        if (i % j == 0){
            prime = 0;
            break;
            }
        }
        if (prime){
            printf("Number %d is prime.\n",i);
        }
    }

    return EXIT_SUCCESS;
}

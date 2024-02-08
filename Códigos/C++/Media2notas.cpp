#include <iostream>

int main(){

float nota1;
float nota2;
float media;

printf("Digite a Nota 1 \n");
scanf("%f", &nota1);

printf("Digite a Nota 2 \n");
scanf("%f", &nota2);

media = (nota1 + nota2) / 2;

printf("\n A média é:  %.2f", media);

printf("\n");
printf("\n");
 system("PAUSE");
return 0;

}
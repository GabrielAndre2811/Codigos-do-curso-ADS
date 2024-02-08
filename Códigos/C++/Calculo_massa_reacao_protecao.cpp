

/*  Situação Problema
Foi solicitado a voce para automatizar um calculo de uma reação chamada de proteção.
Nessa reação um composto A de massa = 321,43 g/mol será somado a um composto B de 
massa = 150,72 g/mol. Seu programa além de calcular o composto com base nas informações
do usuário, deverá também exibir uma tabela com os valores de referencia das combinações (pesos): 
(1,2 : 1,0), (1,4 : 1,0), (1,0 : 1,6).

//interpretando : Quer uma função que calcule (some) a massa de A e de B multiplicado por esses pesos

*/


#include <iostream>


int calcularMassa(float a, float b){

const float mA=321.43; 
const float mB= 150.72; //valores passados na questão

//calcular com pesos passados na questão
printf("\n 1,2 : 1,0 \t = %.3f", (1,2*mA+1*mB));
printf("\n 1,4 : 1,0 \t = %.3f", (1,4*mA+1*mB));
printf("\n 1,0 : 1,6 \t = %.3f \n", (1*mA+1,6*mB));


return (a* mA) + (b* mB);
}


int main(){

float a=0, b=0, resultado=0;

printf("\n Digite a massa do elemento A: ");
scanf("%f", &a);

printf("\n Digite a massa do elemento B: ");
scanf("%f", &b);

resultado = calcularMassa(a, b); //chamando a função - massas somadas totais

printf("\n\t Resultado: %.2f", resultado);
printf("\n\n");
printf("\n\n");
 system("PAUSE");
}


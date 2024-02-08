/*   

               2
        Xn = Xn - 1 + n
            ------------     formula raiz de newton
              2Xn - 1


*/
#include<iostream>
#include <stdio.h>
#include<math.h>

float calcularraiz(float n, float raizant){

float raiz = (pow(raizant, 2)+ n) / (2 * raizant);

if (fabs(raiz - raizant)<0.001)
return raiz;
return calcularraiz(n, raiz);

}

int main(int argc, char const *argv[])
{

    float numero, raiz;

    printf("\n Digite um numero para calcular a raiz: \n");
    scanf("%f", &numero);
    raiz = calcularraiz(numero, numero/2);

    printf("\n Raiz quadrada função: =\t %f\n", raiz);
    system("PAUSE");
    return 0;
}

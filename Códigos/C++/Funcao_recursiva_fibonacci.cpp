#include <iostream>
//Fibonnaci usando função recursiva
using namespace std;

int fibonacci(int valor){

if (valor == 0)

    return 0;

else {

if(valor == 1)
return 1;

else
return fibonacci(valor - 1) + fibonacci(valor - 2);

}

}

int main(){

int n;
printf("\n Digite um numero: \n");
scanf("%d", &n);

fibonacci(n);

printf("Resultado da Sequencia de Fibonacci: %d, para o numero: %d", fibonacci(n), n);

printf("\n\n");
 system("PAUSE");
return 0;
}


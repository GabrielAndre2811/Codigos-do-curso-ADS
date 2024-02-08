#include <iostream>
//Fatorial usando função recursiva
using namespace std;

int fatorial(int valor){

if (valor != 1){ 

return valor * fatorial(valor - 1);

} else {

return valor;

}

}

int main(){

int n;
printf("\n Digite um numero: \n");
scanf("%d", &n);

fatorial(n);

printf("Resultado Fatorial: %d, para o numero: %d", fatorial(n), n);

printf("\n\n");
 system("PAUSE");
return 0;
}


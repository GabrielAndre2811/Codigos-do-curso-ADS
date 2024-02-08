#include <stdio.h>
#include <cstdlib>

int* Numero_aleatorio(){

static int a[10];
int s;

printf(" \n Numeros Atealórios enumerados até 10: \n");

 for (s=0; s <= 10; s++) {

    a[s] = rand();
 
    printf("\t a[%d] = %d \n", s, a[s]);

 }

return a;
}

int main(){

   Numero_aleatorio();
 system("PAUSE");
}
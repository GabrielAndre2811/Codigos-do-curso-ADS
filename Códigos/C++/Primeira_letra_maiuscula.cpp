#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main() {

char nome [30];
int i;

printf("\n Digite o sobrenome do aluno ou aluna: \n");

scanf("%s", &nome);

for(i=0; nome[i]!=' '; i++) //enumera todos os caracteres do vetor de 0 a 30
{

nome[i] = toupper (nome[i]); //coloca o valor dentro do vetor em letra maiuscula, começando do 0 ao 30

printf("\n Sobrenome convertido: %s \n \n",nome );

break; //corta o for na primeira execução deixando somente a primeira letra maiuscula
}


 system("PAUSE");
return 0;
}
#include <iostream>
#include <stdio.h> //Para fun��o gets
#include <stdlib.h> //Para fun��o malloc

using namespace std;


int main (){

char *vnome; //mudou de vnome[50] para um ponteiro sem tamanho

vnome = (char *) malloc(sizeof(char));
/* tempquest para converter o retorno da funcao malloc porque ela normalmente retorna void
e precisamos que ela converta para o tipo char, entao (char *) nada mais e que a convers�o do retorno
do malloc para concordar com a variavel vnome, poderia usar 1 no malloc, mas usei sizeof para aceitar o
tamanho independente da variavel que vai alocar
*/
cout << "\n" << "Digite o nome e sobrenome: " << "\n";
gets (vnome); //utilizar gets porque cin n�o pega espa�os em variaveis tipo char parando a aloca��o

cout << "\n" << vnome;

cout << "\n" << "Ver tamanho guardado por cada tipo de variavel: " << "\n";

cout << "Char: "<< sizeof(char)<<" bytes.\n";
cout << "Int: "<< sizeof(int)<<" bytes.\n";
cout << "Float: "<< sizeof(float) <<" bytes.\n";
cout << "Boolean: "<< sizeof(bool) <<" bytes.\n";
cout << "Double: "<< sizeof(double) <<" bytes.\n";
cout << "Short: "<< sizeof(short) <<" bytes.\n";
cout << "Long: "<< sizeof(long) <<" bytes.\n";
cout << "String: "<< sizeof(string) <<" bytes.\n";
 system("PAUSE");
return 0;
}

#include <iostream>

using namespace std;

int main (){

string veiculo = "carro";
string *pv; //cria ponteiro

pv = &veiculo; //pv recebe o endere�o da variavel veiculo

printf(" \n \t Mostrar Endereco: \n");

cout << "\n" << pv << "\t" << &veiculo << "\n";


/* At� o momento foi criado um ponteiro e foi apontado para um ENDERE�O de variavel */

*pv = "Moto"; // No endere�o que o ponteiro pv aponta adiciona o valor "Moto"

/* Agora atribuimos um valor diretamente a aquele endere�o
mudando o valor da variavel que era Carro para Moto */


printf("\n \t Mostrar valores: \n" );
cout << "\n" << veiculo << "\t" << *pv << "\n";
 system("PAUSE");
}

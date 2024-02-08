#include <iostream>

using namespace std;

int main (){

int *pn; // criado um ponteiro

int vetor[10];

pn = vetor; // atribui ao ponteiro o valor do primeiro array do vetor

/* Outra forma de fazer isso e at� mais "bonita" � utilizar ---> p = &vetor[0]; */

*(pn+=2); //incrementando 2 posi��es de memoria do meu ponteiro (repare que � a mesma que a posi��o 3 da lista abaixo) vetor[3]
*pn = 10; //vetor[3] = 10


cout << "\n" << "Endereco incrementado: " << pn << "\n";

cout << "\n" << "Valor adicionado no endereco incrementado: "  << vetor[2] << "\n";

*(pn+=1);// vetor[4]
*pn = 30; //atribui um valor para esse array novo vetor[4]=30

cout << "\n" << "Endereco incrementado novamente: " << pn << "\n";

cout << "\n" << "Valor adicionado no endereco incrementado novamente: "  << vetor[3] << "\n";


cout << "\n Mostrar todos os campos de vetores abaixo: \n";

for (int i =0; i <= 10; i++){

 pn = &vetor[i];

cout << "\n" << pn << "\t" << vetor[i] << "\n";

}
 system("PAUSE");
/*  Quando o array n�o tem valor definido ele pode ter 0 ou valores de lixos residuais alocados na memoria */
return 0;
}



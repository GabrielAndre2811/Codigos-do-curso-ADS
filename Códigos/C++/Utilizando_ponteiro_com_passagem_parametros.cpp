#include <iostream>

using namespace std;

void soma(float *var, float valor); //prototipar a fun��o (opcional)
void iniVetor(float *v); //tem que prototipar caso a fun��o fique embaixo do main

int main (){
float vetor[5];
float num = 2;

soma(&num, 15); // utilizando a fun��o somar com a variavel num dando o valor para 15
iniVetor(vetor); //atribuindo a variavel vetor ao ponteiro *v, em vetores nao precisa do & comercial
cout << "\n" << num << "\n"; // apresentando o valor atual contido na variavel num

for(int i; i <=5; i++){

   cout << vetor[i] << "\n";
}


/* Passagem de parametro n�o da certo se o valor de num que era para receber da fun��o soma
o valor de var, porem var tem que ser um ponteiro, fa�a o teste tire os * asteriscos
e & o "E comercial", e depois teste, a variavel num n�o vai receber o valor 15 mas sim o valor anterior = 0
*/
 system("PAUSE");
return 0;
}


void soma(float *var, float valor) { //criado estrutura para passagem de parametros
*var+=valor; //fun��o a ser atribuida
}

void iniVetor(float *v){ //necessidade de ponteiro com vetores

v[0]=0; //zero s� pra ver se deu certo
v[1]=0;
v[2]=0;
v[3]=0;
v[4]=0;

}

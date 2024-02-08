#include <iostream>
#include <stdio.h>

/*  Fazer programa que pergunta o valor
em metro e imprime o valor em centimetros e milimetros*/

using namespace std;


int main(){

int metro;

cout << "Digite o valor em metros: ";
cin >> metro;

int cm = (metro * 100);
int dm = (metro * 10);

cout << "Valor em metros: "  << metro << "\n";
cout << "Valor em decametros: "  << dm << "\n";
cout << "Valor em centimetros: "  << cm << "\n";


system("PAUSE");

return 0;
}



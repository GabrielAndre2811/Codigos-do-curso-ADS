#include <iostream>
#include <stack>
#include<list>

using namespace std;

int main(){

   stack <string> cartas;//criado uma lista(pilha) do tipo string

  cartas.push("Reforcos");
  cartas.push("Yami");
  cartas.push("Kuriboh");
  cartas.push("Buraco Armadilha");
  cartas.push("Monstro Renascido");
  cartas.push("Pote da Ganancia"); //ultimo na pilha
  cartas.push("Mago Negro"); //ultimo na pilha
  cartas.push("Dragao Guardiao da Fortaleza"); //terceiro na pilha
  cartas.push("Elfa Mistica"); //segundo na lista
  cartas.push("Mago do Tempo"); //primeiro na lista

    cout <<"Deck total: " << cartas.size() << "\n";

    int puxe;

    cout <<"Digite 1 para puxar suas cartas iniciais: " << "\n";
    cin >> puxe;

    if(puxe == 1){

        for(int i = 0; i < 5; i++){

             cout <<"Carta: " << i << "\t" << cartas.top() << "\n";
             cartas.pop();

        }

            }

  if(cartas.empty()){ //ou pode se utilizar (cartas.size () == 0) para comparar
        printf("\n Deck Vazio \t %c", cartas.size());
            } else {
            cout <<"Deck Atual: " << cartas.size() << "\n";
            } 


 system("PAUSE");
return 0;
}

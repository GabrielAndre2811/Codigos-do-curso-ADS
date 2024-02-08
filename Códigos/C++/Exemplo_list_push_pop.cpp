#include <iostream>
#include <list>

using namespace std;

int main(){
int tam = 10;
list < int > aula; //declara��o b�sica de lista, para usar com com 5 posi��es de valor 50 basta colocar aula(5, 50)
list < int >::iterator it; //iterator cria uma fun��o para nomear as posi��es


//declarando valores da lista
for(int i = 0; i< 10; i++){
aula.push_front(i);//insere no primeiro elemento da lista, usano push_back, ele come�a pelo ultimo numero
}


//it=aula.begin(); //inicializa a fun��o iterator relacionando com a lista
//advance(it, 5); // cria um ponto de intera��o na posi��o 5 da lista
//aula.insert(it, 999); //valor inserido 999 na posi��o do it da lista

cout <<"\n" << "Tamanho da lista: " << aula.size() << "\n\n";

tam = aula.size();// atribui a variavel tam o tamanho da lista aula

//aula.sort(); //organiza os elementos da lista caso estivessem bagun�ada
aula.reverse(); //organiza de forma reversa a lista

//aula.erase(--it);// se colocar somente o it ele exclui o da posi��o da frente coloca decremento para selecionar a posi��o correta
//aula.clear(); // apaga todos os elementos da fila



//imprimindo valores da lista
for(int i = 0; i< 10; i++){
cout <<"\n" << aula.front()<< "\n"; //retorna o primeiro elemento da lista
aula.pop_front(); //retira o elemento que esta na frente
}

 system("PAUSE");
/* para deletar usamos ou clear, ou empty, ou erase*/
return 0;
}

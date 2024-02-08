#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;


struct Node{

int dado;
struct Node *next; //criado um ponteiro chamado next do tipo struct Node

};

void insere_inicio(struct Node** inicio_ref, int new_dado){

struct Node* new_node = (struct Node*) malloc(sizeof(struct Node)); //
new_node->dado = new_dado;
new_node->next = (*inicio_ref);
(*inicio_ref)= new_node;

}
 void insere_fim(struct Node** inicio_ref, int new_dado){//cria uma fun��o inserefim e 2 parametros uma variavel inteiro new_dado e uma estrutura inicio_ref que recebe o valor que NOde aponta
struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));//cria uma strutura newnode que aloca dinamicamente valores que o Node aponta
struct Node *ultimo = *inicio_ref;
new_node->dado = new_dado;
new_node->next = NULL;

if(*inicio_ref == NULL){

    *inicio_ref =  new_node;
    return;
}
while(ultimo->next != NULL){

    ultimo=ultimo->next;
    ultimo->next = new_node;

    return;



}
 }

 void insertAfter(struct Node* prev_node, int new_dado)
{

}

void printlist(struct Node *node){

while(node != NULL){
    printf("%d", node->dado);
    node= node->next;
}


}


int main(){

struct Node* inicio = NULL;

  insere_fim(&inicio, 6);
  insere_inicio(&inicio, 7);
  insere_inicio(&inicio, 1);
 // insere_fim(&inicio, 4);

printf("\nLista Criada: ");
printlist(inicio);
 system("PAUSE");
return 0;
}

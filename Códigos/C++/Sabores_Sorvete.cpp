#include <iostream>

int main(){

 int s;
 do {
      printf("\n Digite o valor para escolher o sabor do sorvete \n");

      printf("\t (1)   ....COCO \n");
      printf("\t (2)   ....MORANGO \n");
      printf("\t (3)   ....LEITE CONDENSADO \n");

      scanf("%d", &s);
      
 }while ((s<1) || (s>3));
 

 switch (s)
 {
 case 1:
    printf("\t\t Voce escolheu Coco\n");
    printf("\t Valor Nutricional do Coco: 100g = 423kcal\n");
    break;
 
case 2:
    printf("\t\t Voce escolheu Morango \n");
    printf("\t Valor Nutricional do Morango: 100g = 30kcal\n");
    break;

case 3:
    printf("\t\t Voce escolheu Leite Condensado \n");
    printf("\t Valor Nutricional do Leite Condensado: 100g = 328kcal\n");
    break;

 default:
    break;
 }
 
 printf("\n");
 printf("\n");

 system("PAUSE");


}
#include <iostream>
#include <stdio.h>

using namespace std;

struct Carro
{
    string modelo;
    string cor;
    int ano;
    int pot; 
    int velMax;
    int vel;

  void insere(string stmodelo, string stcor, int stano, int stpot, int stvelMax, int stvel) {
    modelo = stmodelo;
    cor = stcor;
    ano = stano;
    pot = stpot;
    velMax = stvelMax;
    vel = 0;
  }

  void mostra(){
   
   cout << "\nNome do modelo: " << modelo << "\n";
   cout << "Cor: " << cor << "\n";
   cout << "Ano: " << ano << "\n";
   cout << "Potencia: " << pot << "\n";
   cout << "VelocidadeMax: " << velMax << "\n";
   cout << "Velocidade Atual: " << vel << "\n";
   
  }

  
  void movvel(int movimento){
    
  vel = movimento;

  if(vel > velMax) {
    vel = velMax;
  }

  if(vel < 0){
    vel = 0;
  }

 }

 void mostravel(){
 cout << "\n\t Velocidade Atual: " << vel << "\n";
 }

};

void escolha(){


   printf("\n Digite 1......Civic: \n");
   printf("\n Digite 2......Golf: \n");
   printf("\n Digite 3......Corolla: \t");

}

void escolhavel(){
    printf("\n \t Escolha a velocidade: ");
}

int main(int argc, char const *argv[])
{

    Carro car1, car2, car3;
    //modelo, cor, ano, potencia, velmax, vel
    car1.insere ("Civic", "Prata", 2013, 500, 213, 0);
    car2.insere ("Golf", "Branco", 2010, 300, 213, 0);
    car3.insere ("Corolla", "Cinza", 2018, 280, 213, 0);
    

    escolha();

     int a;
    scanf("\t %d", &a);

    if(a == 1){
    car1.mostra();
   }
   

    if(a == 2){
   car2.mostra();
   }

    if(a == 3){
   car3.mostra();
   }


  escolhavel(); //escolher velocidade nova
  
  int v; //recebe valor de velocidade atual
  scanf("\t %d", &v);

  if (v != 0 && a==1){
   car1.movvel(v);
   car1.mostravel();
  }
   if (v != 0 && a==2){
   car2.movvel(v);
   car2.mostravel();
  }
  if (v != 0 && a==3){
   car3.movvel(v);
   car3.mostravel();
  }




printf("\n\n");
 system("PAUSE");
    return 0;
}

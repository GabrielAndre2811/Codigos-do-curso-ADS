#include<stdio.h>
#include<iostream>
int somar(int valor) {
    if(valor == 1) {
        //critério de parada
        return valor;
    } else {
        //chamada recursiva
        return valor * somar(valor - 1); 
    }
}
int main() {
    int n, resultado;
    printf("\nDigite um numero inteiro positivo: ");
    scanf("%d", &n);
    resultado = somar(n); // primeira chamada da função
    printf("\n Resultado = %d\n",resultado);
    system("PAUSE");
    return 0;
}

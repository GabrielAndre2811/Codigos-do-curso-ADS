#include<stdio.h>

void inserir(int a[]) { //a variavel que recebe o valor numeros[] poderia ser igual seu nome
    int i = 0;
    for(i = 0; i < 3; i++){
        printf("\nDigite o valor %d: ", i);
        scanf("%d", &a[i]); // é capturado 3 valores e jogados nos indices a[1], a[2], a[3] (atenção ao endereço no caso de vetor a passagem de parametro tem que ter o &, se não nao captura)
    }
}

void imprimir(int b[]) {
    int i = 0;
    for(i = 0; i < 3; i++){
        printf("\nNumero[%d] = %d", i, 2 * b[i]);//imprime o indice do vetor e o valor armazenado multiplica por 2
    }
}
int main(){
    int numeros[3];//cria um vetor de tamanho maximo de 3 indices
    printf("\nPreenchendo o vetor... \n ");
    inserir(numeros); //numeros[3] = int a[] e chama a função inserir rodando seu comando primeiro
    printf("\n\nDobro dos valores informados:");
    imprimir(numeros);
    return 0;
}

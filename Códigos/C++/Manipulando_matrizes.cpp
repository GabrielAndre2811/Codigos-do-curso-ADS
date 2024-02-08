#include <iostream>

#include <cstdio>

int main() {
    int linhas, colunas;

    printf("Digite o número de linhas da matriz: ");
    scanf("%d", &linhas); //formando a matriz captura do numero de linhas

    printf("Digite o número de colunas da matriz: ");
    scanf("%d", &colunas); //formando a matriz captura do numero de colunas

    int matriz[linhas][colunas];

    printf("Digite os elementos da matriz:\n");

    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < colunas; j++) {
            printf("\n Digite o elemento da linha %d e coluna %d: ", i + 1, j + 1); //capturar os elementos enumerando em linhas e colunas
            scanf("%d", &matriz[i][j]); //captura da matriz
        }
    }

    // Exibir a matriz
    printf("\n A matriz digitada é:\n");

    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < colunas; j++) {
            printf("\t %d ", matriz[i][j]);
        }
        printf("\n\n");
    }
   system("PAUSE");
    return 0;
}

#include <stdlib.h>
#include <stdio.h>

int main(void){
	int *ptr; //criando ponteiro
	int i, quant_elementos; //criando contador
	
	//recebendo elementos
	printf("Digite a quantidade de elementos do vetor: ");
	scanf("%d", &quant_elementos);
	
	//alocando memoria para o vetor com a quantidade de elementos
	ptr = (int *)(malloc(quant_elementos * sizeof(int)));
	
	//caso nao seja possivel alocar memoria exibir erro e sair do programa com exit(1);
	if (ptr == NULL){
		printf("\nErro de alocacao de memoria");
		system("pause");
		exit(1);
	}
	printf("\n");
	
	//recebendo dados para o vetor
	for( i = 0; i < quant_elementos; i++){
		printf("Digite o numero para indice [%d] : ", i);
		scanf("%d", &ptr[i]);
	}
	printf("\n");
	
    //realloc sendo feito e printado
     ptr = (realloc (ptr, quant_elementos * sizeof (int)));{
	 	printf("Realocamento de memoria feito com sucesso!!!");
	 };
	 printf("\n");
	 printf("\n");
	
	//percorre o vetor mostrando os valores
	for ( i = 0; i < quant_elementos; i++){
		printf("Valor armazenado no elemento de indice [%d] = %d\n", i, ptr[i]);
	}
	printf("\n");
	
	//liberando memoria
	free(ptr);
	system("pause");
	return 0;
}

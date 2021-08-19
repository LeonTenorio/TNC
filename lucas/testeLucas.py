import sys
import numpy as np
import os

arquivo_primos = "primos.npy"


class DescobridorDePrimos:
    def __init__(self):
        self.primos = []
        if(os.path.isfile(arquivo_primos)):
            self.primos = np.load(arquivo_primos).tolist()

    def descobrirFatores(self, n):
        # Esse objeto tem que ser explorado de 1, 2, 3, .... sucessivamente
        # obrigatoriamente, para quando, depois de n-1 achar n que nao é dividido
        # pelos primos já encontrados, n é primo
        fatores = [1]
        metade = int(n/2) + 1
        for primo in self.primos:
            while(n % primo == 0):  # Pode ser divisivel por um primo mais de uma vez
                n = int(n/primo)
                fatores.append(primo)
            if(primo > metade):
                break
        if(len(fatores) > 1 and n > 1):
            raise Exception("Algoritmo errado")
        if(n > 1):  # Ainda nao descobri esse primo
            fatores.append(n)
            self.primos.append(n)
        return fatores

    def salvar(self):
        np.save(arquivo_primos, np.array(self.primos))


def fatorar(n):
    descobridor = DescobridorDePrimos()
    inicio = 2
    # Otimizacao para comecar a construcao da listagem de primos necessaria
    # depois do ultimo primo ja descoberto que pode estar carregado no objeto
    # ja que ele pode ter sido recuperado de um arquivo
    if(len(descobridor.primos) > 0):
        if(descobridor.primos[len(descobridor.primos) - 1] > inicio):
            inicio = descobridor.primos[len(descobridor.primos) - 1] + 1
    for i in range(inicio, n):
        descobridor.descobrirFatores(i)
    fatores = descobridor.descobrirFatores(n)
    descobridor.salvar()
    return fatores


def raizes_primitivas(n):
    raizes = [1]
    for a in range(2, n):
        calculo = int(a**(n-1))
        if(calculo % n == 1):
            raizes.append(a)
    return raizes


def teste_lucas(n):
    fatores = fatorar(n-1)
    fatores.pop(0)  # Remoção do termo 1
    raizes = raizes_primitivas(n)
    for a in raizes:
        # Descobrindo se existe a tal que, para todo q em fatores primos de n-1
        # a**((n-1)/q) !== 1 (mod n)
        valido = True
        for q in fatores:
            # Solucao de problema de execução python
            calculo = int(a**(int((n-1)/q)))
            # Números com vírgula estavam aparecendo e calsando overflow com números grandes
            if(calculo % n == 1):
                valido = False
                break
        if(valido):
            return True
    return False


entrada = int(sys.argv[1])
print('De acordo com o teste de lucas, o número '+str(entrada), end=' ')
if(teste_lucas(entrada)):
    print('é primo')
else:
    print('não é primo')

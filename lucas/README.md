## Exercício Teste de Lucas

Nesse exercício foi implementado o teste de lucas para verificar se um número n é primo, essa implementação se encontra em [`testeLucas.py`](testeLucas.py) e é possível a sua execução por linha comando passando como argumento o número o número a ser testado, como foi feito no exercício proposto utilizando o seguinte comando:

```
python testeLucas.py 127
```

Essa execução tem como saída (como pode ser observado no arquivo [`resposta.txt`](resposta.txt)):

```
De acordo com o teste de lucas, o número 127 é primo
```

Em uma breve explicação da implementação feita posso dizer que a classe `DescobridorDePrimos` realiza o descobrimento de números primos e é utilizada para armazenar todos os primos já descobertos a partir de 2 até n, testando para cada novo número se ele é fatorável pelos primos já descobertos e se não, como estamos seguindo ordenalmente de 2 até n, o número que está sendo explorado é primo.

Além disso, são descobertas todas as raízes primitivas módulo n e para todos os fatores primos de n-1 é testada a condição do teste de lucas, resultando na resposta que podemos obter ao executar o teste.

Por fim, foi feita uma melhoria mantendo salvo permanentemente os primos que já foram encontrados pelo algoritmo no teste, para serem recarregados na próxima execução o que aceleraria o programa, o arquivo utilizado é o arquivo `primos.npy`. Foi observado também que essa otimização não acarreta em ganhos efetivos na velocidade de execução, sendo observado no teste de 20023, número primo, corretamente identificado pelo algoritmo, 1 minuto e 18 segundos sem o arquivo `primos.npy` e 1 min e 16 segundos com o arquivo `primos.npy`.

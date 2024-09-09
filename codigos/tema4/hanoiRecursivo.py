'''
# Torres de Hanói

O problema envolve uma base de pinos verticais, em que os discos estão
inicialmente empilhados em ordem crescente de tamanho em um dos pinos,
com o disco menor no topo e o disco maior na base. 

O objetivo do problema é mover todos os discos da torre de origem para
a torre de destino, usando a torre auxiliar, de forma que os discos 
permaneçam empilhados em ordem crescente de tamanho em todos os momentos
e que apenas um disco seja movido por vez. Além disso,em nenhum momento
um disco maior pode ser colocado sobre um disco menor.

Agora, para realizar o exercício proposto, execute os passos a seguir.

1. Crie um arquivo de código fonte de Python Hanói recursivo.
2. Crie uma função para processar as torres chamando outra função para
   movimentar os discos.
3. Crie uma função para exibir o conteúdo das torres a cada passo.
4. Chame a função de forma recursiva.
5. Para iniciar o processamento, defina a quantidade de discos, crie as
   torres e chame para execução a função principal.
'''

def mover_disco(origem, destino):
    disco = origem.pop()
    destino.append(disco)

def imprimir_torres(torre_A, torre_B, torre_C):
    print("A:", torre_A)
    print("B:", torre_B)
    print("C:", torre_C)
    print()

def torres_de_hanoi_recursivo(num_discos, origem, destino, auxiliar):
   if num_discos == 1:
        mover_disco(origem, destino)
        imprimir_torres(torre_A, torre_B, torre_C)
   else:
        torres_de_hanoi_recursivo(num_discos - 1, origem, auxiliar, destino)
        mover_disco(origem, destino)
        imprimir_torres(torre_A, torre_B, torre_C)
        torres_de_hanoi_recursivo(num_discos - 1, auxiliar, destino, origem)

# Resolvendo o problema recursivamente
num_disco = 7
# Inicializando as torres e os discos
torre_A = list(range(num_disco, 0, -1))
torre_B = []
torre_C = []
# Mostrando o estado inicial
imprimir_torres(torre_A, torre_B, torre_C)
torres_de_hanoi_recursivo( num_disco, torre_A, torre_C, torre_B)

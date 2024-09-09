def func1(x):
    x = 10
    print(f'Função func1 - x = {x}')


def func2(x):
    x = 20
    print(f'Função func2 - x = {x}')


x = 0
func1(x)
func2(x)
print(f'Programa principal - x = {x}')

''' Saidas:
Função func1 - x = 10
Função func2 - x = 20
Programa principal - x = 0
'''
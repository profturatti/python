# Contagem regressiva de 10 a 0

# Uma função recursiva é aquela que chama a si mesma.
def regressiva(x):
  print(x)
  if x > 0:
    regressiva(x - 1)
  else:
    print('acabou')

regressiva(10)

# não recursiva
for y in range(10, -1, -1):
  print(y)
print('acabou')

# Exemplo de 'fatorial de n' ou 'n!'
''' 
O resultado será 1 se n for zero ou um; 
senão teremos n! = n.[n-1!] se n >=2
Que seria n! = n.(n-1).(n-2)...3.2.1 para n>=2
'''

# funcao recursiva fatorial
def fatorial(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fatorial(n-1)
vfat = fatorial(5)
print(f'resultado recursiva: {vfat}')

# funcao fatorial nao recursiva
def fatorial(n):
  fat = 1
  if n==0 or n==1:
    return fat
  else:
    for x in range(2, n + 1):
      fat = fat * x
    return fat

vfat = fatorial(5)
print(f'resultado iterativa: {vfat}')

# docString - mostra os comentários do código fonte
# Determine o n-ésimo termo da sequência de Fibonacci
# q para finalizar o helpq
def fibo(n):
  if n==1 or n==2:
    return 1
  else:
    return fibo(n-1) + fibo(n -2)

vfibo=fibo(6)
print(vfibo)
# docString
print(help(fibo))
      
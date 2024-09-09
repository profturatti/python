''' O Cadastro de Pessoas Físicas (CPF) é um número único atribuido a 
    cada residente no Brasil. Esse número é uma sequência composta por
    11 dígitos numéricos, onde 9 dígitos são únicos e os dois últimos 
    são dígitos verificadores. Os dígitos verificadores são usados para
    garantir a integridade do identificador e são calculados com base 
    nos 9 primeiros dígitos do CPF.

Os dígitos verificadores são calculados usando o algoritmo de módulo 11.
- O primeiro dígito verificador é calculado a partir dos 9 primeiros 
  dígitos do CPF.
- O segundo dígito verificador é calculado a partir dos 9 primeiros 
  dígitos do CPF, incluindo o primeiro dígito verificador.

Verificação
- Uma vez informados os 11 digitos, o cálculo dos digitos verificadores
  é realizado
- Compara-se o resultado com os dígitos verificadores informados
- Se forem iguais o CPF é válido. Caso contrário, é considerado inválido.

Erros e Exceções
- CPFs com todos os dígitos iguais (ex.: 111.111.111-11) ou CPFs com 
padrões específicos que foram anulados pela Receita Federal (baixa do
número de CPF em caso de óbito, por exemplo)

Nesta atividade, serão considerados somentes os tratamentos de números 
para verificar se uma sequência é válida ou não.


Para realizar o exercício proposto, siga o passo a passo.

1. Crie um arquivo fonte chamado validacpf.
2. Crie uma função que:
2.1. Remova os caracteres não numéricos.
2.2. Valide a quantidade de dígitos do CPF.
2.3. Valide se todos os dígitos não são iguais.
2.4. Calcule o primeiro dígito verificador e o valide.
2.5. Calcule o segundo dígito verificador e o valide.
3. Teste a função passando um CPF como parâmetro.
'''

def valida(numeros):
  # 2.1. Obtém os números do CPF e ignora outros caracteres
  cpf = [int(char) for char in numeros if char.isdigit()]
  # 2.2. Verifica se o CPF tem 11 dígitos
  if len(cpf) != 11:
    return False
  # 2.3. Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
  if cpf == cpf[::-1]:
    return False
  # Valida os dois dígitos verificadores
  for i in range(9, 11):
    value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
    digit = ((value * 10) % 11) % 10
    if digit != cpf[i]:
      return False
  return True

cpf = input('Digite o CPF: ')
if valida(cpf):
  print('CPF válido.')
else:
  print('CPF inválido.')
def validar_cpf(cpf):
    # Removendo caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificando se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False

    # Verificando se todos os dígitos são iguais (caso raro, mas inválido)
    if cpf == cpf[0] * 11:
        return False

    # Calculando o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto

    # Verificando o primeiro dígito verificador
    if int(cpf[9]) != digito_verificador_1:
        return False

    # Calculando o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto

    # Verificando o segundo dígito verificador
    if int(cpf[10]) != digito_verificador_2:
        return False

    # CPF válido
    return True
 
# Testando a função
#cpf = "123.456.789-09"
cpf = input("Digite o CPF: ")
if validar_cpf(cpf):
    print(f"O CPF {cpf} é válido.")
else:
    print(f"O CPF {cpf} é inválido.")
''' Nesta funcao, o parâmetro multiplicador da função taximetro tem um 
    valor padrão igual a 1. Isso significa que, se não passarmos um valor
    para multiplicador ao chamar a função, ele usará 1 como padrão.
'''
def taximetro(distancia, multiplicador=1):
    largada = 3
    km_rodado = 2
    valor = (largada + distancia * 
    km_rodado) * multiplicador
    return valor # retorna uma valor

pagamento = taximetro(3.5)
print(pagamento) # saida: 10.0

''' Atividade:
    Qual mudança você faria neste código para cobrar uma taxa mínima no
    aplicativo (distancia=1) quando o usuário cancelasse a chamada do
    após 5 minutos do pedido aceito pelo motorista

    Dica: Pesquise sobre o uso das bibliotecas datetime e pytz
'''
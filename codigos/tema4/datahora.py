from datetime import date
from datetime import datetime, timedelta, timezone

data_atual = date.today()
print(data_atual) # Saida padrao

data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)
print(data_em_texto) # Substituição do traço por / e ordem dos elementos dd mm AAAA

data_em_texto = data_atual.strftime('%d/%m/%Y')
print(data_em_texto) # Saida formatada com dois digitos para dia e mes

data_e_hora_atuais = datetime.now() # Usando datetime no lugar de date
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
print(data_e_hora_em_texto)

data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
print(data_e_hora_em_texto) # Saida com data e hora

diferenca = timedelta(hours=-3) # Como indicar o timezone?
print(diferenca)
fuso_horario = timezone(diferenca)
print(fuso_horario) # UTC -3 horas
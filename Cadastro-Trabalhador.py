from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de trabalho (0 caso não tenha): '))
if dados ['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['Aposetadoria'] = dados['idade'] + ((['Contratação'] + 35 - datetime.now().year))
print('==') *30
print(dados)
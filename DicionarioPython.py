# ex090_dicionario_pytho



'''

Faça um programa que leia nome e média de um aluno,

guardando também a situação em um dicionário.

No final, mostre o conteúdo da estrutura na tela.

'''

ficha = dict()

nome = str(input('Nome: '))

media = float(input('Média: '))

ficha['nome'] = nome

ficha['media'] = media

if media >= 7:

    ficha['resultado'] = 'Aprovado'

elif 5<= media:
    ficha['resultado'] = 'Recuperação'
else:

    ficha['resultado'] = 'Reprovado'



for key, values in ficha.items():

        print(f'{key} é igual a  {values}')

print()



# if ficha['media'] >= 7:

#     print(f"O aluno {ficha['nome']} teve a média de {ficha['media']} e está {ficha['resultado'][0]}")

# else:

#     print(f"O aluno {ficha['nome']} teve a média de {ficha['media']} e está {ficha['resultado'][1]}")



print(ficha) 
'''
   Curso básico de Python
   ----------------------
    www.cursoemvideo.com
   -----------------------------
   Professor: Gustavo Guanabara
   Aluno: Bruno Nascimento
   ----------------------------------------------------------------------------
   Desafio 003 = Crie um script python que leia dois números e tente mostrar a
   soma entre eles.
   ----------------------------------------------------------------------------
'''

#   INICIO DO PROGRAMA - DESAFIO 003  #

print('---------------------------------')
print('Programa para somar dois números')
print('---------------------------------')
n1 = float(input('Digite o primeiro Número: '))
n2 = float(input('Digite o segunto Número para somar com o primeiro: '))
s = n1 + n2
print ('A soma entre {} e {} é : {}'.format(n1, n2, s))  # 1ª forma de apresentar o resultado ( usando mascara {})
print ('A soma entre',n1,'e',n2,'é :',s)                 # 2ª Forma de apresentar o resultado metodo utilizado no python 2 assim com % , mas ainda funciona no python3


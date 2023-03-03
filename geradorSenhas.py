import random

print('Bem-Vindo ao Gerador de Senhas')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUWXYZ!@$%^&*().,?0123456789'

number = int(input('Quantas senhas você dejesa gerar: '))
length = int(input('Qual o tamanho de caracteres você que senha tenha: '))

print('\n Essas são as suas senha(s): ')

for pwd in range(number):
    passwords = ''

    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)


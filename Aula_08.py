# numero_verificacao = int(input(('digite:')))

# if numero_verificacao >= 0:
#     print('O numero é positvo')
    
# else:
#     print('O número é negativo')

# # Pode ou não votar?
    
# idade = int(input('Qual sua idade?'))
# if idade > 18:
#     print('Pode votar')
# else:
#     print('Não pode Votar')

# # Inpar ou par
# numero = 25
# if numero % 2 == 0:
#     print('O numero é par.')
# else:
#     print('O número é impar.')

# triangulo equilatero, isósceles ou escaleno

numero_1 = int(input('digite um número:'))
numero_2 = int(input('digite um número:'))
numero_3 = int(input('digite um número:'))

if numero_1 == numero_2 and numero_1 == numero_3:
    print('Triangulo equilatero')
elif numero_1 == numero_2 or numero_1 == numero_3 or numero_3 == numero_2:
    print('Triangulo Isósceles')
else:
    print('Triangulo escaleno')

 # Determine se um número é multiplo de 5 e 7



# verifique se um número é postivo maior que 10

comparacao = int(input('digite um numero'))
if comparacao >=10:
    print('numero positvio maoir que 10')
else:
    print('Número não é maior que 10')
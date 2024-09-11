def comparar():
    numero = 25
    if numero % 2 == 0:
        print('O numero é par')
    else:
        print('O numero é impar')

comparar()       
        
def multiplicar_tres_numeros(a, b, c):
    produto = a * b * c
    print(produto)

multiplicar_tres_numeros(10,5,30)

def elevar_numero(base, exponent):
    resultado = base ** exponent
    print(resultado)

elevar_numero(2,5)

def mensagem_idade(idade):
    if idade == 18:
       print("Você tem 18 anos! Bem-vindo à maioridade.")
    else:
        print("Você não tem 18 anos.")
      

mensagem_idade(27)        

def descobrir_idade(ano_atual, ano_nascimento):
   idade = ano_nascimento - ano_atual
   print(idade)

descobrir_idade(1996,2024)

def brasil_ganhou_copa_1999():
    print("Sim, o Brasil ganhou a Copa do América de 1999.")

brasil_ganhou_copa_1999()

def escolher_prato():
   pratos = ('''
       1: "Salada",
       2: "Macarronada",
       3: "Sanduíche",
       4: "Sorvete"
   ''')
   opcao = input('>>')
   if opcao == '1':
        print('Uma salada no capricho')
   elif opcao == '2':
        print('Macarronada a moda da casa')
   elif opcao == '3':
        print('Boa apetit com o sanduíche')
   elif opcao == '4':
        print('Boa pedida de sorvete')
   else:
            print('Opção invalida')


escolher_prato()
       

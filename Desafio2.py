# Cadastro de Clientes
clientes = [None] * 3
idades = [None] * 3

# Cadastro dos clientes
nome_cliente1 = input("Digite o nome do Cliente 1: ")
idade_cliente1 = int(input("Digite a idade do Cliente 1: "))
clientes[0] = nome_cliente1
idades[0] = idade_cliente1

nome_cliente2 = input("Digite o nome do Cliente 2: ")
idade_cliente2 = int(input("Digite a idade do Cliente 2: "))
clientes[1] = nome_cliente2
idades[1] = idade_cliente2

nome_cliente3 = input("Digite o nome do Cliente 3: ")
idade_cliente3 = int(input("Digite a idade do Cliente 3: "))
clientes[2] = nome_cliente3
idades[2] = idade_cliente3

# Preços dos quartos
preco_simples = 100
preco_duplo = 150
preco_luxo = 250

# Reservas e cálculo da estadia
# Entrada dos tipos de quarto e quantidade de dias
tipo_quarto_cliente1 = input(f"Digite o tipo de quarto para {clientes[0]} (Simples, Duplo, Luxo): ").strip().lower()
dias_cliente1 = int(input(f"Quantos dias {clientes[0]} ficará? "))

tipo_quarto_cliente2 = input(f"Digite o tipo de quarto para {clientes[1]} (Simples, Duplo, Luxo): ").strip().lower()
dias_cliente2 = int(input(f"Quantos dias {clientes[1]} ficará? "))

tipo_quarto_cliente3 = input(f"Digite o tipo de quarto para {clientes[2]} (Simples, Duplo, Luxo): ").strip().lower()
dias_cliente3 = int(input(f"Quantos dias {clientes[2]} ficará? "))

# Cálculo dos valores totais
if tipo_quarto_cliente1 == "simples":
    valor_cliente1 = preco_simples * dias_cliente1
elif tipo_quarto_cliente1 == "duplo":
    valor_cliente1 = preco_duplo * dias_cliente1
elif tipo_quarto_cliente1 == "luxo":
    valor_cliente1 = preco_luxo * dias_cliente1
else:
    valor_cliente1 = 0  # Caso o tipo de quarto seja inválido

if tipo_quarto_cliente2 == "simples":
    valor_cliente2 = preco_simples * dias_cliente2
elif tipo_quarto_cliente2 == "duplo":
    valor_cliente2 = preco_duplo * dias_cliente2
elif tipo_quarto_cliente2 == "luxo":
    valor_cliente2 = preco_luxo * dias_cliente2
else:
    valor_cliente2 = 0  # Caso o tipo de quarto seja inválido

if tipo_quarto_cliente3 == "simples":
    valor_cliente3 = preco_simples * dias_cliente3
elif tipo_quarto_cliente3 == "duplo":
    valor_cliente3 = preco_duplo * dias_cliente3
elif tipo_quarto_cliente3 == "luxo":
    valor_cliente3 = preco_luxo * dias_cliente3
else:
    valor_cliente3 = 0  # Caso o tipo de quarto seja inválido

# Exibindo o valor total a ser pago por cada cliente
print(f"O valor total a ser pago por {clientes[0]} é: R$ {valor_cliente1:.2f}")
print(f"O valor total a ser pago por {clientes[1]} é: R$ {valor_cliente2:.2f}")
print(f"O valor total a ser pago por {clientes[2]} é: R$ {valor_cliente3:.2f}")

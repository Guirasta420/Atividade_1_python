import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Função para calcular o valor da estadia
def calcular_valor(tipo_quarto, dias):
    precos = {
        "Simples": 100,
        "Duplo": 150,
        "Luxo": 250
    }
    preco = precos.get(tipo_quarto, 0)
    return preco * dias

# Função para processar as reservas
def processar_reservas():
    clientes = [nome_cliente1.get(), nome_cliente2.get(), nome_cliente3.get()]
    tipos_quarto = [tipo_quarto1.get(), tipo_quarto2.get(), tipo_quarto3.get()]
    dias = [int(dias_cliente1.get()), int(dias_cliente2.get()), int(dias_cliente3.get())]
    
    valores = []
    
    for tipo_quarto, dia in zip(tipos_quarto, dias):
        valores.append(calcular_valor(tipo_quarto, dia))
    
    resultado = ""
    for i, cliente in enumerate(clientes):
        resultado += f"O valor total a ser pago por {cliente} é: R$ {valores[i]:.2f}\n"
    
    messagebox.showinfo("Resultados", resultado)

# Configuração da janela principal
root = tk.Tk()
root.title("Cadastro de Clientes")
root.geometry("400x450")
root.configure(bg="#f0f0f0")

# Função para criar e configurar labels e entries
def criar_widget_label_entry(root, text_label, row, col, entry_var):
    tk.Label(root, text=text_label, bg="#f0f0f0", font=("Arial", 12)).grid(row=row, column=col, sticky="w", padx=10, pady=5)
    entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 12))
    entry.grid(row=row, column=col+1, padx=10, pady=5, sticky="ew")
    return entry

# Variáveis
nome_cliente1 = tk.StringVar()
idade_cliente1 = tk.StringVar()
nome_cliente2 = tk.StringVar()
idade_cliente2 = tk.StringVar()
nome_cliente3 = tk.StringVar()
idade_cliente3 = tk.StringVar()

tipo_quarto1 = tk.StringVar()
tipo_quarto2 = tk.StringVar()
tipo_quarto3 = tk.StringVar()
dias_cliente1 = tk.StringVar()
dias_cliente2 = tk.StringVar()
dias_cliente3 = tk.StringVar()

# Labels e Entrys para os clientes
tk.Label(root, text="Cliente 1", bg="#f0f0f0", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
criar_widget_label_entry(root, "Nome:", 1, 0, nome_cliente1)
criar_widget_label_entry(root, "Idade:", 2, 0, idade_cliente1)

tk.Label(root, text="Cliente 2", bg="#f0f0f0", font=("Arial", 14, "bold")).grid(row=3, column=0, columnspan=2, pady=10)
criar_widget_label_entry(root, "Nome:", 4, 0, nome_cliente2)
criar_widget_label_entry(root, "Idade:", 5, 0, idade_cliente2)

tk.Label(root, text="Cliente 3", bg="#f0f0f0", font=("Arial", 14, "bold")).grid(row=6, column=0, columnspan=2, pady=10)
criar_widget_label_entry(root, "Nome:", 7, 0, nome_cliente3)
criar_widget_label_entry(root, "Idade:", 8, 0, idade_cliente3)

# Labels e Combobox para tipos de quarto e dias
tk.Label(root, text="Tipo de Quarto e Dias para Cliente 1", bg="#f0f0f0", font=("Arial", 12, "bold")).grid(row=9, column=0, columnspan=2, pady=10)
tk.Label(root, text="Tipo de Quarto:", bg="#f0f0f0", font=("Arial", 12)).grid(row=10, column=0, padx=10, pady=5)
tk.Label(root, text="Dias:", bg="#f0f0f0", font=("Arial", 12)).grid(row=11, column=0, padx=10, pady=5)

opcoes_quarto = ["Simples", "Duplo", "Luxo"]
combobox_tipo_quarto1 = ttk.Combobox(root, values=opcoes_quarto, textvariable=tipo_quarto1, font=("Arial", 12))
combobox_tipo_quarto1.grid(row=10, column=1, padx=10, pady=5)
combobox_tipo_quarto1.set("Simples")

criar_widget_label_entry(root, "Dias:", 11, 1, dias_cliente1)

tk.Label(root, text="Tipo de Quarto e Dias para Cliente 2", bg="#f0f0f0", font=("Arial", 12, "bold")).grid(row=12, column=0, columnspan=2, pady=10)
tk.Label(root, text="Tipo de Quarto:", bg="#f0f0f0", font=("Arial", 12)).grid(row=13, column=0, padx=10, pady=5)
tk.Label(root, text="Dias:", bg="#f0f0f0", font=("Arial", 12)).grid(row=14, column=0, padx=10, pady=5)

combobox_tipo_quarto2 = ttk.Combobox(root, values=opcoes_quarto, textvariable=tipo_quarto2, font=("Arial", 12))
combobox_tipo_quarto2.grid(row=13, column=1, padx=10, pady=5)
combobox_tipo_quarto2.set("Simples")

criar_widget_label_entry(root, "Dias:", 14, 1, dias_cliente2)

tk.Label(root, text="Tipo de Quarto e Dias para Cliente 3", bg="#f0f0f0", font=("Arial", 12, "bold")).grid(row=15, column=0, columnspan=2, pady=10)
tk.Label(root, text="Tipo de Quarto:", bg="#f0f0f0", font=("Arial", 12)).grid(row=16, column=0, padx=10, pady=5)
tk.Label(root, text="Dias:", bg="#f0f0f0", font=("Arial", 12)).grid(row=17, column=0, padx=10, pady=5)

combobox_tipo_quarto3 = ttk.Combobox(root, values=opcoes_quarto, textvariable=tipo_quarto3, font=("Arial", 12))
combobox_tipo_quarto3.grid(row=16, column=1, padx=10, pady=5)
combobox_tipo_quarto3.set("Simples")

criar_widget_label_entry(root, "Dias:", 17, 1, dias_cliente3)

# Botão para processar reservas
tk.Button(root, text="Calcular Valores", command=processar_reservas, font=("Arial", 14), bg="#4CAF50", fg="white", padx=10, pady=5, relief="raised").grid(row=18, column=0, columnspan=2, pady=20)

# Iniciar a interface gráfica
root.mainloop()

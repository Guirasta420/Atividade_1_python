import tkinter as tk 

def mostrar_soma():
    n1 = float(input_entry.get())
    n2 = float(input_entry2.get())
    calculo = n1 + n2
    text2.config(text = f'RRESULTADO: {calculo}')

def mostrar_sub():
    n1 = float(input_entry.get())
    n2 = float(input_entry2.get())
    calculo = n1 - n2
    text2.config(text = f'RRESULTADO: {calculo}')

def mostrar_div():
    n1 = float(input_entry.get())
    n2 = float(input_entry2.get())
    calculo = n1 / n2
    text2.config(text = f'RRESULTADO: {calculo}')

def mostrar_mult():
    n1 = float(input_entry.get())
    n2 = float(input_entry2.get())
    calculo = n1 * n2
    text2.config(text = f'RRESULTADO: {calculo}')



janela = tk.Tk()
janela.title('Python GUI')
janela.geometry('400x500')


#TITULO
texto = tk.Label(janela, text = 'CALCULADORA', fg='black', fonte = 'arial',  )
texto.grid(row = 1, column=2, padx = 15, pady = 10)

input_entry = tk.Entry(janela)
input_entry.grid(row = 2, column = 2)

input_entry2 = tk.Entry(janela)
input_entry2.grid(row = 2, column = 3)

#SOMA
botao_SOMA = tk.Button(janela, text = '+', command = mostrar_soma)
botao_SOMA.grid(row = 3, column = 2)

#SUB
botao_SUB = tk.Button(janela, text = '-', command = mostrar_sub)
botao_SUB.grid(row = 4, column = 2)

#DIV
botao_DIV = tk.Button(janela, text = '/', command = mostrar_div)
botao_DIV.grid(row = 3, column = 3)

#MULT
botao_MULT = tk.Button(janela, text = 'x', command = mostrar_mult)
botao_MULT.grid(row = 4, column = 3)


text2 = tk.Label(janela, text ='RESULTADO = ')
text2.grid(row = 5, column = 0, padx = 10, pady = 10)

janela.mainloop()


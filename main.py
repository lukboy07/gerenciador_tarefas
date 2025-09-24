import tkinter as tk
import banco
import funcoes

# Inicializa banco
banco.criar_tabela()

# Cria janela
janela = tk.Tk()
janela.title('Gerenciador de Tarefas')
janela.geometry('480x420')

# Campo de entrada
entrada = tk.Entry(janela, width=40)
entrada.pack(pady=8)

# Botões
btn_add = tk.Button(janela, text='Adicionar', command=lambda: funcoes.adicionar_tarefa(entrada, lista))
btn_add.pack(pady=4)

btn_concluir = tk.Button(janela, text='Concluir', command=lambda: funcoes.concluir_tarefa(lista))
btn_concluir.pack(pady=2)

btn_remover = tk.Button(janela, text='Remover', command=lambda: funcoes.remover_tarefa(lista))
btn_remover.pack(pady=2)

# Lista de tarefas
lista = tk.Listbox(janela, width=60, height=15)
lista.pack(pady=10)

# Atualiza a lista ao iniciar
funcoes.atualizar_lista(lista)

# Mantém a janela aberta
janela.mainloop()

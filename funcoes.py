import banco
from tkinter import messagebox

tarefas_cache = []  # guarda as tarefas para a interface

def atualizar_lista(lista_widget):
    """Atualiza o Listbox com as tarefas do banco"""
    global tarefas_cache
    lista_widget.delete(0, 'end')
    tarefas_cache = banco.listar_tarefas()
    for t in tarefas_cache:
        status = "✅" if t[2] else "❌"
        lista_widget.insert('end', f'{t[0]} - {t[1]} {status}')

def get_id_selecionado(lista_widget):
    """Retorna o ID da tarefa selecionada"""
    sel = lista_widget.curselection()
    if not sel:
        return None
    idx = sel[0]
    return tarefas_cache[idx][0]

def adicionar_tarefa(entry_widget, lista_widget):
    titulo = entry_widget.get().strip()
    if not titulo:
        messagebox.showwarning('Aviso', 'Digite uma Tarefa!')
        return
    banco.adicionar_tarefa(titulo)
    entry_widget.delete(0, 'end')
    atualizar_lista(lista_widget)

def concluir_tarefa(lista_widget):
    tarefa_id = get_id_selecionado(lista_widget)
    if tarefa_id is None:
        messagebox.showwarning('Aviso', 'Selecione uma tarefa')
        return
    banco.concluir_tarefa(tarefa_id)
    atualizar_lista(lista_widget)

def remover_tarefa(lista_widget):
    tarefa_id = get_id_selecionado(lista_widget)
    if tarefa_id is None:
        messagebox.showwarning('Aviso', 'Selecione uma tarefa')
        return
    banco.remover_tarefa(tarefa_id)
    atualizar_lista(lista_widget)

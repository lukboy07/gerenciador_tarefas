#banco.py
import sqlite3
import os

#Variaveis utilizadas para garantir que o DB criado va para o diretorio correto
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, 'tarefas.db')


#FUNCOES:


#Funcao para criar a tabela
def criar_tabela():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tarefas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    concluida INT NOT NULL DEFAULT 0
            )
        ''')


#Funcao para adicionar tarefa
def adicionar_tarefa(titulo):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tarefas (titulo, concluida) VALUES (?, ?)', (titulo, 0))


#funcao para listar tarefas
def listar_tarefas():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, titulo, concluida FROM tarefas ORDER BY id')
        return cursor.fetchall()
    

#Funcao para concluir tarefas
def concluir_tarefa(tarefa_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE tarefas SET concluida = 1 WHERE id = ?',(tarefa_id,))


#Funcao para remover tarefas
def remover_tarefa(tarefa_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tarefas WHERE id =?', (tarefa_id,))


#rode para testar o arquivo
if __name__ == '__main__':
    criar_tabela()
    adicionar_tarefa('Testar banco')
    print(listar_tarefas())
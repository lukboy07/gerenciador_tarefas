# Gerenciador de Tarefas em Python

Projeto simples de um gerenciador de tarefas usando **Tkinter** para a interface gráfica e **SQLite** para armazenamento dos dados.
O objetivo é criar, listar, concluir e remover tarefas de forma prática.

## Funcionalidades

* Adicionar tarefas
* Listar tarefas com status (concluída ou não)
* Concluir tarefas
* Remover tarefas
* Armazenamento persistente usando SQLite

## Estrutura do Projeto

```
gerenciador_tarefas/
│
├── banco.py          # Funções de acesso ao SQLite
├── funcoes.py        # Funções de manipulação de tarefas para a interface
├── main.py           # Interface gráfica Tkinter
├── README.md         # Este arquivo
└── tarefas.db        # Banco de dados (gerado automaticamente)
```

## Como Rodar

1. Clone o repositório:

```bash
git clone https://github.com/lukboy07/gerenciador_tarefas
```

2. Entre na pasta do projeto:

```bash
cd gerenciador_tarefas
```

3. (Opcional) Crie um ambiente virtual:

```bash
python -m venv .venv
# Ative o ambiente:
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate
```

4. Execute o programa:

```bash
python main.py
```

## Observações

* O banco de dados `tarefas.db` é criado automaticamente na primeira execução.
* O projeto está modularizado, com funções separadas da interface gráfica.
* Ideal para aprendizado de Python, Tkinter e SQLite.

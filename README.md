# Gerenciador de Tarefas CLI (Python)

Um gerenciador de tarefas simples desenvolvido em Python, executado via linha de comando (CLI).
O projeto permite criar, listar, editar, concluir e remover tarefas, além de visualizar estatísticas e organizar tarefas por prioridade.

Este projeto foi desenvolvido com foco em boas práticas de programação, arquitetura modular e testes automatizados.


# Funcionalidades

- Adicionar tarefas
- Listar tarefas
- Remover tarefas
- Marcar tarefas como concluídas
- Editar tarefas
- Definir prioridade (Alta, Média, Baixa)
- Ordenação automática por prioridade
- Estatísticas do sistema
- Persistência de dados em arquivo JSON
- Testes automatizados com unittest


# Estrutura do Projeto

projeto_02_gerenciador_tarefas
│
├── main.py
├── manager.py
├── models.py
├── storage.py
├── tasks.json
│
├── tests
│   └── test_manager.py
│
└── README.md


### Descrição dos arquivos

| Arquivo     | Função 
| main.py     | Interface CLI do sistema 
| manager.py  | Lógica principal do gerenciador de tarefas 
| models.py   | Modelo da classe - Task
| storage.py  | Responsável por salvar e carregar tarefas do JSON 
| tasks.json  | Banco de dados simples do sistema 
| tests/      | Testes automatizados 


# Como executar o projeto

Clone o repositório ou navegue até a pasta do projeto:
cd projeto_02_gerenciador_tarefas

Execute o programa:
python main.py


# Exemplo de uso

GERENCIADOR DE TAREFAS

1 - Adicionar tarefa
2 - Listar tarefas
3 - Remover tarefa
4 - Marcar tarefa como concluída
5 - Editar tarefa
6 - Estatísticas
0 - Sair


# Estatísticas disponíveis

O sistema mostra:
- Total de tarefas
- Quantidade de tarefas concluídas
- Quantidade de tarefas pendentes
- Distribuição por prioridade

Exemplo:

ESTATÍSTICAS

Total de tarefas: 3
Concluídas: 1
Pendentes: 2

Por prioridade:
Alta: 1
Média: 2
Baixa: 0


# Executar testes

Para rodar os testes automatizados:
python -m unittest discover

Saída esperada:
Ran 6 tests in 0.02s
OK


# Tecnologias utilizadas

- Python 3
- unittest
- JSON


# Objetivo do projeto

Esse projeto foi desenvolvido como parte do aprendizado em Python, com foco em:

- Organização de código
- Separação de responsabilidades
- Testes automatizados
- Persistência de dados
- Estrutura de projetos


# Autor
João Marcelo 
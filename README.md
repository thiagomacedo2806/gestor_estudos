# Gestor de Estudos

Este é um projeto funcional e minimalista construído em Django para gerenciar tópicos de estudos de programação de forma ágil e sem complicações de configuração.

## Funcionalidades

- Listar tópicos de estudo cadastrados.
- Criar novos tópicos de estudo via requisição JSON.

## Como Executar

1. Instale o Django:
```bash
pip install django
```

2. Inicialize as tabelas do banco de dados (SQLite embutido):
```bash
python manage.py migrate
```

3. Inicie o servidor:
```bash
python manage.py runserver
```

## Como Testar

Para executar os testes automatizados da aplicação:
```bash
python manage.py test tests
```
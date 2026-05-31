# Sistema de Controle de Estoque Web 📦

Projeto desenvolvido como avaliação para a disciplina de Desenvolvimento Web.

## 👥 Nome
- Murillo Aparecido

## 🚀 Descrição do Sistema
Uma aplicação web simples e funcional voltada para o gerenciamento de produtos em estoque. O sistema permite listar mercadorias cadastradas, adicionar novos itens, atualizar informações de preço ou quantidade, e remover produtos do sistema, cobrindo assim todas as operações de um CRUD.

## 🛠️ Tecnologias Utilizadas
- **Back-end:** Python 3 e Flask
- **Front-end:** HTML5, Jinja2 (Templates) e Bootstrap 5 (CSS)
- **Banco de Dados:** SQLite3

## 🗄️ Estrutura do Banco de Dados
O sistema utiliza uma tabela chamada `produtos` com a seguinte estrutura:
- `id`: INTEGER (Chave Primária, Auto-incremento)
- `nome`: TEXT (Não Nulo)
- `quantidade`: INTEGER (Não Nulo)
- `preco`: REAL (Não Nulo)


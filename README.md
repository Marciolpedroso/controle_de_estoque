# Controle de Estoque - Sistema Básico em Python

## Descrição

Projeto de controle de estoque simples feito em Python, utilizando:

- **SQLite** para banco de dados local.
- **Tkinter** para interface gráfica (GUI).
- Funcionalidades de cadastro, consulta, atualização e remoção parcial de itens no estoque.

Ideal para quem está aprendendo a integrar banco de dados com interface gráfica, ou quer uma solução básica para gerenciamento de estoque.

---

## Funcionalidades

- Cadastro de novos itens com nome, tipo, valor e quantidade.
- Visualização de todos os itens cadastrados e suas informações.
- Remoção parcial de quantidade de um item (não remove o item do banco se quantidade chegar a zero).
- Adição de quantidade a um item já existente.
- Validações básicas para garantir entrada de dados correta.
- Interface gráfica simples e funcional usando Tkinter.

---

## Como usar

1. Clone o projeto ou baixe os arquivos `estoque_backend.py` e `estoque_frontend.py`.
2. Certifique-se de ter Python instalado (versão 3.7+ recomendada).
3. No terminal, execute:
   ```bash
   python estoque_frontend.py
   ```
4. A janela do sistema abrirá:
   - Cadastre itens preenchendo os campos e clicando em **Cadastrar Item**.
   - Visualize os itens cadastrados no painel lateral.
   - Para remover ou adicionar quantidade, informe o ID do item e a quantidade desejada, depois clique em **Remover do Estoque** ou **Adicionar ao Estoque**.
5. Feche o programa para salvar automaticamente.

---

## Estrutura do projeto

```
controle_estoque/
│
├── estoque_backend.py    # Código de acesso e manipulação do banco de dados SQLite
├── estoque_frontend.py   # Código da interface gráfica com Tkinter
└── estoque.db            # Arquivo do banco SQLite (gerado após o uso)
```

---

## Requisitos

- Python 3.7 ou superior
- Biblioteca padrão (sqlite3, tkinter) - já inclusas no Python padrão

---

## Possíveis melhorias futuras

- Implementar busca e filtro por nome, tipo, ou valor.
- Melhorar a interface gráfica com mais feedback e estética.
- Exportar relatório em CSV ou PDF.
- Criar autenticação de usuário.
- Usar uma arquitetura MVC para melhor organização.
- Implementar testes unitários para o backend.

---

## Autor

Seu nome aqui — [Seu contato ou link, se quiser]

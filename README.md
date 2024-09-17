# Roulotte Alex

## Descrição do Projeto

Este sistema foi desenvolvido para gerenciar os pedidos em um trailer de vendas de kebabs, chamado **Roulotte Alex**. O sistema permite que o proprietário registre pratos e bebidas, processe novos pedidos e marque pedidos como entregues. A interface gráfica foi desenvolvida com **Tkinter**, e a persistência dos dados é feita com **PostgreSQL** via **SQLAlchemy**.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
├── Makefile              # Automação de tarefas
├── README.md             # Instruções do projeto
├── app                   # Diretório da aplicação
│   ├── database.py       # Configuração e inicialização do banco de dados
│   ├── functions.py      # Funções de manipulação da lógica da aplicação
│   ├── main.py           # Ponto de entrada da aplicação (interface gráfica)
│   ├── models.py         # Definição dos modelos de dados (SQLAlchemy)
├── requirements.txt      # Dependências do projeto
```

## Dependências

- **Python 3.8+**
- **Tkinter**: Para a interface gráfica.
- **SQLAlchemy**: Mapeamento objeto-relacional (ORM) para interagir com o banco de dados.
- **psycopg2**: Driver para conectar ao PostgreSQL.
- **PostgreSQL**: Base de dados utilizada para armazenar pedidos, pratos e bebidas.
- **Docker**: Para gerenciar o container do PostgreSQL.

## Configuração e Instalação

### 1. Clonar o repositório:

```bash
git clone git@github.com:carvalhovitor2/des-rap-app-py.git
cd des-rap-app-py
```

### 2. Criar o ambiente virtual, instalar dependências e configurar o banco de dados:

```bash
make install
```

### 3. Ativar o ambiente virtual:

```bash
source venv/bin/activate   # Para Windows: venv\Scripts\activate
```

### 4. Executar a aplicação:

```bash
python -m app.main
```

## Estrutura do Banco de Dados

O banco de dados **PostgreSQL** utilizado no projeto é chamado `estacio_python` e é gerido via **Docker**. O Makefile já contém os comandos necessários para criar, rodar e remover o container PostgreSQL:

- **DB Name**: `estacio_python`
- **DB User**: `postgres`
- **DB Password**: `postgres`
- **Porta**: `5432`

### Comandos de Gerenciamento do Banco de Dados:

- **Criar/Iniciar o Banco de Dados**:
  ```bash
  make install
  ```

- **Remover o Banco de Dados e volumes**:
  ```bash
  make clean
  ```

## Limpeza e Remoção

Para remover o ambiente virtual e o banco de dados:

1. Desativar o ambiente virtual:
   ```bash
   deactivate
   ```

2. Limpar a instalação e remover o container e volumes do banco de dados:
   ```bash
   make clean
   ```

## Uso da Aplicação

- **Gestão**: Registra novos pratos e bebidas com nome, descrição e preço.
- **Pedidos**: Registra novos pedidos, permitindo ao usuário selecionar pratos e bebidas, adicionar quantidades, e confirmar o pedido.
- **Pedidos Entregues**: Permite marcar pedidos como entregues e visualizar o histórico de pedidos processados.


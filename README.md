# 🦇 Projeto Wayne Enterprises

Sistema desenvolvido em **Django** para gerenciamento de recursos e usuários, com autenticação e painel administrativo (dashboard).

---

## 📌 Funcionalidades

- 🔐 **Autenticação de usuários**
  - Login e logout seguros
  - Controle de permissões por papel (`admin`, `gerente`)

- 📦 **Gestão de Recursos**
  - Criar, listar, editar e deletar recursos
  - Registro de data/hora de criação

- 👥 **Gestão de Usuários**
  - Cadastro, listagem, edição e exclusão de usuários
  - Apenas administradores podem gerenciar usuários

- 📊 **Dashboard**
  - Total de usuários cadastrados
  - Total de recursos cadastrados
  - Gráfico de recursos por tipo
  - Últimos usuários e recursos criados

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.13](https://www.python.org/)
- [Django 5.2](https://www.djangoproject.com/)
- SQLite (banco de dados padrão do Django)
- Bootstrap 5 (frontend)
- Chart.js (gráficos no dashboard)

---

## ⚙️ Como Rodar o Projeto

1. **Clonar o repositório**
   ```bash
   git clone https://github.com/AtruDev/Projeto_Wayne.git
   cd Projeto_Wayne


### 2. Criar e ativar o ambiente virtual
- python -m venv venv 
- ./venv/Scripts/activate.ps1    # Windows(powershell)
- source venv/bin/activate # Linux/macOS

### 3. Instalar dependências
- pip install -r requirements.txt

### 4. ir para pasta principal
- cd wayne

### 4. Rodar migrações

- python manage.py migrate

### 5. Criar superusuário
- python manage.py createsuperuser

### 6. Subir o servidor
- python manage.py runserver

### Acesse:
http://127.0.0.1:8000/admin

### 7. mude o cargo 
 
mude o cargo do seu superuser para admin assim tendo acesso total

### Acesse:

http://127.0.0.1:8000

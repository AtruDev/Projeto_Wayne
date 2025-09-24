#  Sistema de Gestão Wayne Enterprises

Projeto desenvolvido em Django para gerenciamento de **recursos internos** das Indústrias Wayne.  
Inclui autenticação de usuários com papéis (funcionário, gerente e admin), dashboard com estatísticas e CRUD de recursos.

---

##  Tecnologias usadas
- Python 3.13
- Django 5.2
- SQLite (banco de dados padrão)
- Chart.js (para gráficos no dashboard)

---

##  Como rodar o projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/projeto-wayne.git
cd projeto-wayne
```

### 2. Criar e ativar o ambiente virtual
```bash
- python -m venv venv
- venv\Scripts\activate    # Windows
- source venv/bin/activate # Linux/macOS
```

### 3. Instalar dependências
```bash
- pip install -r requirements.txt
```

### 4. Rodar migrações
```bash
- python manage.py migrate
```

### 5. Criar superusuário
```bash
- python manage.py createsuperuser
```

### 6. Subir o servidor
```bash
- python manage.py runserver
```
### Acesse:
```
http://127.0.0.1:8000/
```
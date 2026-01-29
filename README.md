# Projeto FJU - Back-end 

Esse projeto tem como objetivo ser uma maneira simples de criar relátorios sobre jovens que participam do grupo FJU.

## Tecnologias usadas

- Linguagem Python
- Biblioteca FastAPI 
- Firebase Realtime Database
- Firebase Authentication

## Utilização

Para rodar o back-end é recomendavel criar um ambiente virtual do Python. Para fazer isso utilize os seguintes comandos:

```PYTHON
# --------------
# Criar ambiente

# No Windows
python -m venv venv

# no Linux ou MacOS
python3 -m venv venv

# --------------

# --------------
# Ativar ambiente

# no terminal bash (Windos, Linux, MacOS)
source venv/bin/activate

# No Windows (comand prompt)
venv\Scripts\activate

# No windows (PowerShell)
venv\Scripts\Activate.ps1

# --------------
```

Antes de rodar a aplicação é necessário baixar algumas depedências. Para baixar rode os seguintes comandos no terminal:

```PYTHON
# Baixar biblioteca FastAPI
pip install "fastapi[standard]"

# Baixar SDK do Firebase
pip install firebase-admin

```

Por fim basta apenas iniciar a aplicação com o seguinte comando:

```PYTHON
fastapi dev main.py
```

## Colaboradores do projeto

- [Daniela Medeiros](https://github.com/medeirosdani)
- [Isaque Camargo](https://github.com/MrZaza10)
- [Kayo Victor](https://github.com/kayoGc)
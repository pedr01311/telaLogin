# Tela de Login com Flask e MySQL

## Sobre o projeto
Sistema de login e cadastro de usuários desenvolvido com Python, Flask e MySQL.

## Funcionalidades
- Cadastro de usuários com confirmação de senha
- Login com validação no banco de dados
- Mensagens de feedback na tela

## Tecnologias utilizadas
- Python
- Flask
- MySQL
- HTML
- CSS

## Como rodar o projeto

### Pré-requisitos
- Python instalado
- MySQL instalado

### Instalação
1. Clone o repositório
   git clone https://github.com/pedr01311/telaLogin.git

2. Instale as dependências
   pip install -r requirements.txt

3. Configure o arquivo .env com suas credenciais
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=sua_senha
   DB_NAME=tela_login
   DB_PORT=3306
   SECRET_KEY=sua_chave_secreta

4. Crie o banco de dados no MySQL
   CREATE DATABASE tela_login;
   USE tela_login;
   CREATE TABLE usuarios (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(50) NOT NULL,
       password VARCHAR(50) NOT NULL
   );

5. Rode o servidor
   python app.py

6. Acesse no navegador
   http://127.0.0.1:5000

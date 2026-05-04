from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, flash, redirect, url_for
import pymysql

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

try:
    db = pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        port=int(os.getenv('DB_PORT'))
)
    print("MySQL conectado!")
except Exception as e:
    print(f"Erro ao conectar: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('As senhas não coincidem!', 'erro')
            return redirect(url_for('cadastro'))
        
        cursor = db.cursor()
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (%s, %s)", (username, password))
        db.commit()

        flash('Cadastro realizado com sucesso!', 'sucesso')
        return redirect(url_for('cadastro'))

    return render_template('cadastro.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username = %s AND password = %s", (username, password))
    usuario = cursor.fetchone()

    if usuario:
        flash('Login efetuado com sucesso!', 'sucesso')
        return redirect(url_for('index'))
    else:
        flash('Usuário ou senha incorretos!', 'erro')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
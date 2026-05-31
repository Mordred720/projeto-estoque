from flask import Flask, render_template, request, redirect, url_for, flash
import os
import sqlite3

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_alertas_flash'

# Garante que a pasta database exista
DB_DIR = os.path.join(os.path.dirname(__file__), 'database')
if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)

DB_PATH = os.path.join(DB_DIR, 'estoque.db')

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Permite acessar colunas pelo nome
    return conn

# Criação da tabela caso não exista
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# ---- ROTAS (CRUD) ----

# 1. READ (Listar)
@app.route('/')
def index():
    conn = get_db_connection()
    produtos = conn.execute('SELECT * FROM produtos').fetchall()
    conn.close()
    return render_template('index.html', produtos=produtos)

# 2. CREATE (Adicionar)
@app.route('/criar', methods=('GET', 'POST'))
def criar():
    if request.method == 'POST':
        nome = request.form['nome']
        quantidade = request.form['quantidade']
        preco = request.form['preco']

        # Validação básica
        if not nome or not quantidade or not preco:
            flash('Todos os campos são obrigatórios!', 'danger')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)',
                         (nome, int(quantidade), float(preco)))
            conn.commit()
            conn.close()
            flash('Produto adicionado com sucesso!', 'success')
            return redirect(url_for('index'))

    return render_template('criar.html')

# 3. UPDATE (Editar)
@app.route('/<int:id>/editar', methods=('GET', 'POST'))
def editar(id):
    conn = get_db_connection()
    produto = conn.execute('SELECT * FROM produtos WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        nome = request.form['nome']
        quantidade = request.form['quantidade']
        preco = request.form['preco']

        if not nome or not quantidade or not preco:
            flash('Todos os campos são obrigatórios!', 'danger')
        else:
            conn.execute('UPDATE produtos SET nome = ?, quantidade = ?, preco = ? WHERE id = ?',
                         (nome, int(quantidade), float(preco), id))
            conn.commit()
            conn.close()
            flash('Produto atualizado com sucesso!', 'success')
            return redirect(url_for('index'))

    conn.close()
    return render_template('editar.html', produto=produto)

# 4. DELETE (Excluir)
@app.route('/<int:id>/deletar', methods=('POST',))
def deletar(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM produtos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Produto excluído com sucesso!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
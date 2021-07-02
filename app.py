from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

DB_NAME = 'empresa'
DB_USER = 'root'
DB_PORT = 3307


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}@localhost:{}/{}'.format(DB_USER, DB_PORT, DB_NAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecurekey'

db = SQLAlchemy(app)


class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    idade = db.Column(db.String(120), unique=True, nullable=False)
    salario = db.Column(db.Integer, nullable=False)
    telefone = db.Column(db.Integer, nullable=True, default=0)
    cod = db.Column(db.String(80), nullable=True, default=9999)

    def format(self):
        return {
            'nome': self.nome,
            'idade': self.idade,
            'salario': self.salario,
            'telefone': self.telefone,
            'cod': self.cod
        }


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/pessoas', methods=['GET'])
def pessoas():
    pessoas = Pessoa.query.all()
    return render_template('pessoas.html', pessoas=pessoas)


@app.route('/inserir', methods=['GET', 'POST'])
def inserir():
    if request.method == 'POST':
        form = request.form.to_dict()

        pessoa = Pessoa(
            nome=form['nome'],
            idade=form['idade'],
            salario=form['salario'],
            telefone=form['telefone']
        )

        db.session.add(pessoa)
        db.session.commit()

        return redirect(url_for('pessoas'))
    return render_template('inserir.html')


@app.route('/apagar', methods=['GET'])
def apagar():
    pessoas = Pessoa.query.all()
    return render_template('apagar.html', pessoas=pessoas)


@app.route('/apagar/<int:pessoa_id>', methods=['POST'])
def apagar_pessoa(pessoa_id):
    pessoa = Pessoa.query.filter_by(id=pessoa_id).first()

    db.session.delete(pessoa)
    db.session.commit()

    return redirect(url_for('apagar'))


@app.route('/editar', methods=['GET'])
def editar():
    pessoas = Pessoa.query.all()
    return render_template('editar.html', pessoas=pessoas)


@app.route('/editar/<int:pessoa_id>', methods=['GET'])
def editar_pessoa(pessoa_id):
    pessoa = Pessoa.query.filter_by(id=pessoa_id).first()
    return render_template('editar_pessoa.html', pessoa=pessoa)


@app.route('/editar/<int:pessoa_id>', methods=['POST'])
def actualizar_pessoa(pessoa_id):
    form = request.form.to_dict()
    pessoa = Pessoa.query.filter_by(id=pessoa_id).first()

    pessoa.nome = form['nome']
    pessoa.idade = form['idade']
    pessoa.salario = form['salario']
    pessoa.telefone = form['telefone']

    db.session.commit()

    return redirect(url_for('editar'))


@app.route('/pesquisar', methods=['GET', 'POST'])
def pesquisar():
    if request.method == 'POST':
        pesquisa = request.form.get('pesquisar')
        current_pessoas = Pessoa.query.filter(
            Pessoa.nome.ilike('%' + pesquisa + '%'),
        ).all()

        return render_template('pesquisar.html', pessoas=current_pessoas)

    pessoas = Pessoa.query.all()
    return render_template('pesquisar.html', pessoas=pessoas)


if __name__ == '__main__':
    app.run(debug=True)

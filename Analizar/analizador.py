from flask import Flask, render_template, request
import ply.lex as lex

app = Flask(__name__)

# Lista de palabras reservadas y sus descripciones
reservadas = {
    'for': 'Reservada for',
    'if': 'Reservada if',
    'do': 'Reservada do',
    'while': 'Reservada while',
    'else': 'Reservada else',
    '(': 'Paréntesis izquierdo',
    ')': 'Paréntesis derecho'
}

tokens = [
    'FOR',
    'IF',
    'DO',
    'WHILE',
    'ELSE',
    'LPAREN',
    'RPAREN'
]

# Expresiones regulares para los tokens
t_ignore = ' \n'

def t_FOR(t):
    r'\bfor\b'
    t.type = 'FOR'
    t.description = reservadas['for']
    return t

def t_IF(t):
    r'\bif\b'
    t.type = 'IF'
    t.description = reservadas['if']
    return t

def t_DO(t):
    r'\bdo\b'
    t.type = 'DO'
    t.description = reservadas['do']
    return t

def t_WHILE(t):
    r'\bwhile\b'
    t.type = 'WHILE'
    t.description = reservadas['while']
    return t

def t_ELSE(t):
    r'\belse\b'
    t.type = 'ELSE'
    t.description = reservadas['else']
    return t

def t_LPAREN(t):
    r'\('
    t.type = 'LPAREN'
    t.description = reservadas['(']
    return t

def t_RPAREN(t):
    r'\)'
    t.type = 'RPAREN'
    t.description = reservadas[')']
    return t

def t_error(t):
    print(f"Caracter no reconocido: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

@app.route('/', methods=['GET', 'POST'])
def index():
    tokens = None
    if request.method == 'POST':
        codigo = request.form['codigo']
        lexer.input(codigo)
        tokens = [(tok.type, tok.description) for tok in lexer]
    return render_template('index.html', tokens=tokens)

if __name__ == '__main__':
    app.run(debug=True)

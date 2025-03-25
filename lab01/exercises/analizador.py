import ply.lex as lex

#  Definir tokens
tokens = (
    'ID', 'NUMBER', 'DECIMAL', 'STRING',
    'ASSIGN', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQ', 'NEQ', 'GT', 'LT', 'AND', 'OR', 'NOT',
    'COMMA', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
)

# Palabras clave
reserved = {
    'si': 'SI',
    'sino': 'SINO',
    'mientras': 'MIENTRAS',
    'para': 'PARA',
    'definir': 'DEFINIR',
    'retornar': 'RETORNAR',
    'verdadero': 'VERDADERO',
    'falso': 'FALSO',
    'imprimir': 'IMPRIMIR'
}

tokens = tokens + tuple(reserved.values())

# Expresiones regulares para tokens simples
t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQ = r'=='
t_NEQ = r'!='
t_GT = r'>'
t_LT = r'<'
t_AND = r'y'
t_OR = r'o'
t_NOT = r'no'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

#  Tokens más complejos con funciones

# Identificadores (variables y funciones)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Si es palabra clave, cambia el tipo
    return t

# Números enteros
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Números decimales
def t_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Cadenas de texto
def t_STRING(t):
    r'"([^"\\]*(\\.[^"\\]*)*)"'
    t.value = t.value[1:-1]  # Quita comillas
    return t

# Comentarios de una línea
def t_COMMENT(t):
    r'//.*'
    pass  # Se ignoran

# Comentarios multilínea
def t_COMMENT_MULTI(t):
    r'/\*[\s\S]*?\*/'
    pass  # Se ignoran

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Contar saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en línea {t.lineno}")
    t.lexer.skip(1)

#  Construcción del lexer
lexer = lex.lex()

#Leer archivo y analizarlo
with open("codigo_fuente.txt", "r", encoding="utf-8") as f:
    data = f.read()

lexer.input(data)

# Guardar tokens en una lista de diccionarios
tokens_list = []
while True:
    tok = lexer.token()
    if not tok:
        break
    tokens_list.append({"type": tok.type, "value": tok.value, "line": tok.lineno})

# Imprimir tokens generados
for token in tokens_list:
    print(token)

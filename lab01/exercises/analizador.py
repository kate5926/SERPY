import ply.lex as lex

# Definir los tokens del lenguaje
tokens = (
    'NUMBER', 'CADENA', 'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVIDIR', 'LPAREN', 'RPAREN',
    'ASIGNACION', 'IGUALDAD', 'DESIGUALDAD','MAYOR','MENOR','NUMBER_DECIMAL', 'IDENTIFICADOR',
    'LLAVE_IZQ','LLAVE_DER','CORCHETE_IZQ', 'CORCHETE_DER','COMENTARIO', 'COMENTARIOS', 'COMA', 'PUNTO_Y_COMA'
    )

palabras_reservadas = {
    'retornar': 'RETORNAR',
    'para': 'PARA',
    'mientras': 'MIENTRAS',
    'si': 'SI',
    'sino': 'SINO',
    'imprimir': 'IMPRIMIR',
    'no': 'NO',
    'o': 'O',
    'yy': 'Y',
    'Verdadero': 'VERDADERO',
    'Falso': 'FALSO',
    'definir': 'FUNCION'
}

tokens = tokens + tuple(palabras_reservadas.values())

# Expresiones regulares para cada token
t_PUNTO_Y_COMA = ';'
t_COMA = r','
t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_RETORNAR = r'retornar'
t_PARA = r'para'
t_MIENTRAS = r'mientras'
t_SI = r'si'
t_SINO = r'sino'
t_VERDADERO = r'Verdadero'
t_FALSO = r'Falso'
t_NO = r'no'
t_O = r'o'
t_Y = r'yy'
t_MAYOR = r'>'
t_MENOR = r'<'
t_DESIGUALDAD = r'!='
t_IGUALDAD = r'=='
t_ASIGNACION = r'='
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVIDIR = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_CADENA = r'\".*?\"'
t_IMPRIMIR = r'imprimir'
t_FUNCION = r'definir'

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = palabras_reservadas.get(t.value, 'IDENTIFICADOR')
    return t

def t_NUMBER_DECIMAL(t):
    r'\d+\.(\d+)?'
    t.value = float(t.value)
    return t

# Definir cómo reconocer un número
def t_NUMBER(t):
    r'\d+' # d+ captura los numeros como cadena de texto
    t.value = int(t.value) # nosotros queremos trabajar con numeros enteros entonces una ves reconocido lo convertimos a entero.
    return t

def t_COMENTARIO(t):
    r'//.*'  
    print("Comentario de una línea encontrado")
    pass
def t_COMENTARIOMULTILINEA(t):
    r'/\*[\s\S]*?\*/'  
    print("Comentario de una multilínea encontrado")
    pass  

# Manejo de saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorar espacios y tabs
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Crear el analizador léxico
lexer = lex.lex()

# Leer el archivo de código fuente y procesarlo
with open("codigo_fuente.txt", "r") as archivo:
    codigo = archivo.read()

# Alimentar el código al lexer
lexer.input(codigo)

# Almacenar los tokens en una lista de objetos
tokens_list = []
while True:
    tok = lexer.token()
    if not tok:
        break
    tokens_list.append({
        'type': tok.type,
        'lexeme': tok.value,
        'line': tok.lineno,
        'column': tok.lexpos
    })

# Imprimir los tokens
for token in tokens_list:
    print(token)

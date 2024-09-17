import ply.lex as lex

# Lista de tokens: Define los tipos de tokens que el analizador léxico debe reconocer.
tokens = (
    'principal',
    'id',
    'retorna',
    'numero',
    'entero',
    'suma',
    'resta',
    'multiplicar',
    'dividir',
    'mayor_igual',
    'menor_igual',
    'mayor',
    'menor',
    'par_ini',
    'par_fin',
    'imprimir',
    'mientras',
    'bool',
    'llave_ini',
    'llave_fin',
    'cadena',
    'si',
    'sino',
    'decimales',
    'punto_coma',
    'igual_asignaccion',
    'igual_comparacion',
    'deshigualdad',
    'y',
    'o',
    'TRUE',
    'FALSE',
    'comillas',
    'texto',
)

# Diccionario de palabras reservadas: Mapea palabras reservadas a sus correspondientes nombres de tokens.
palabras_reservadas = {
    'principal': 'principal',
    'entero': 'entero',
    'bool': 'bool',
    'mientras': 'mientras',
    'sino': 'sino',
    'decimales': 'decimales',
    'cadena': 'cadena',
    'imprimir': 'imprimir',
    'si': 'si',
    'y': 'y',
    'o': 'o',
    'retorna': 'retorna',
    'texto': 'texto'
}

# Expresiones regulares para los tokens: Define patrones para identificar los distintos tokens en el texto.
t_suma = r'\+'
t_multiplicar = r'\*'
t_resta = r'-'
t_dividir = r'/'
t_par_ini = r'\('
t_par_fin = r'\)'
t_mayor_igual = r'>='
t_menor_igual = r'<='
t_mayor = r'>'
t_menor = r'<'
t_llave_ini = r'\{'
t_llave_fin = r'\}'
t_igual_asignaccion = r'='
t_igual_comparacion = r'=='
t_deshigualdad = r'!='
t_punto_coma = r';'
t_comillas = r'\"'

# Token para cadenas de texto: Se define una expresión regular para reconocer cadenas de texto entre comillas.
def t_cadena(t):
    r'"[a-zA-Z0-9 !@#$%^&()-+=/\|_.,;:<>?{}\[\]`~]+"'
    return t

# Token para identificadores: Reconoce palabras que comienzan con una letra seguida de letras y números.
def t_id(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = palabras_reservadas.get(t.value, 'id')
    return t

# Token para números: Reconoce números enteros y decimales.
def t_numero(t):
    r'[0-9]+(\.[0-9]+)?'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

# Token para comentarios: Ignora comentarios que comienzan y terminan con '/*' (esta expresión regular no es típica).
def t_COMENTARIO(t):
    r'![a-zA-Z0-9 !@#$%^&()-+=/\|_.,;:<>?{}\[\]`~ ]+!'
    pass

# Token para espacios en blanco: Ignora los espacios en blanco.
def t_espacio(t):
    r'\s+'
    pass

# Token para nueva línea: Actualiza el número de línea en el analizador léxico.
def t_nueva_linea(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

# Token para caracteres ilegales: Imprime un mensaje de error cuando se encuentra un carácter no reconocido.
def t_error(t):
    print("ilegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Crear el analizador léxico.
lexer = lex.lex()

# Leer el archivo de entrada.
with open("prueba.txt", "r") as file:
    data = file.read()

print("\nAnalizador lexico\n")
lexer.input(data)

# Clase para representar los tokens con tipo, lexema y línea.
class TodosTokens:
    def __init__(self, type, lexeme, line):
        self.type = type
        print(f"Token creado: {type} con lexema: {lexeme} en línea: {line}")  # Depuración
        self.lexeme = lexeme
        self.line = line

TK = []

# Extraer tokens del analizador léxico y guardarlos en una lista.
while True:
    tok = lexer.token()
    if not tok:
        break
    t = TodosTokens(tok.type, tok.value, tok.lineno)
    TK.append(t)

print("\nPALABRAS CLAVE: ")
# Imprimir los tokens extraídos.
for token in TK:
    print(f"{token.type} | {token.lexeme} | {token.line}")

# Agregar un token especial '$' al final de la lista de tokens.
dolar = TodosTokens("$", '', 0)
TK.append(dolar)

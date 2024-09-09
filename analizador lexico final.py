import ply.lex as lex # type: ignore

# Lista de nombres de tokens
tokens = (
    'CUANDO', 'MIENTRAS', 'SI', 'SI_NO', 'IMPRIMIR', 'ASIGNAR', 'O_SI', 'TAMBIEN', 'RETORNAR', 'FINL',
    'ENTERO', 'FLOTANTE', 'DOBLE', 'BOOLEANO', 'CADENA_CARACTER', 'CARACTER',
    'SUMA', 'MENOS', 'MULTIPLICACION', 'DIVISION',
    'MAYOR', 'MENOR', 'MENOR_O_IGUAL', 'MAYOR_O_IGUAL',
    'IGUAL_COMPARACION', 'DESIGUALDAD',
    'COMENTARIO_DE_BLOQUE', 'PARENTESIS_INICIO', 'PARENTESIS_FIN', 'SALTO_LINEA'
)

# Reglas de expresión regular para tokens simples
t_SUMA = r'\+'
t_MENOS = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_MAYOR = r'>'
t_MENOR = r'<'
t_MENOR_O_IGUAL = r'<='
t_MAYOR_O_IGUAL = r'>='
t_IGUAL_COMPARACION = r'=='
t_DESIGUALDAD = r'!='

# Reglas para comentarios de bloque
def t_COMENTARIO_DE_BLOQUE(t):
    r'/\*.*?\*/'
    pass  # Los comentarios de bloque se ignoran

# Reglas para paréntesis
t_PARENTESIS_INICIO = r'\('
t_PARENTESIS_FIN = r'\)'

# Reglas para palabras clave
def t_CUANDO(t):
    r'cuando'
    return t

def t_MIENTRAS(t):
    r'mientras'
    return t

def t_SI(t):
    r'si'
    return t

def t_SI_NO(t):
    r'si_no'
    return t

def t_IMPRIMIR(t):
    r'imprimir'
    return t

def t_ASIGNAR(t):
    r'asignar'
    return t

def t_O_SI(t):
    r'o_si'
    return t

def t_TAMBIEN(t):
    r'tambien'
    return t

def t_RETORNAR(t):
    r'retorno'
    return t

def t_FINL(t):
    r'finL'
    return t

# Reglas para tipos de datos
def t_ENTERO(t):
    r'\b\d+\b'
    t.value = int(t.value)  # Convertir el valor a entero
    return t

def t_FLOTANTE(t):
    r'\b\d*\.\d+\b'
    t.value = float(t.value)  # Convertir el valor a flotante
    return t

def t_DOBLE(t):
    r'\b\d*\.\d+([eE][-+]?\d+)?\b'  # Número en notación científica
    t.value = float(t.value)  # Convertir el valor a doble precisión
    return t

def t_BOOLEANO(t):
    r'\bverdadero\b|\bfalso\b'
    t.value = (t.value == 'verdadero')  # Convertir a booleano
    return t

def t_CADENA_CARACTER(t):
    r'\".*?\"'
    t.value = t.value.strip('"')  # Eliminar comillas alrededor
    return t

def t_CARACTER(t):
    r'\'.\''
    t.value = t.value.strip('\'')  # Eliminar comillas alrededor
    return t

# Regla para SALTO_LINEA
def t_SALTO_LINEA(t):
    r'finL'
    t.lexer.lineno += 1  # Incrementa el número de línea en 1
    return t

# Caracteres ignorados (espacios y tabuladores)
t_ignore = ' \t'

# Regla de manejo de errores
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Prueba del lexer
if __name__ == "__main__":
    data = '''
    cuando a < 10
    mientras a > 5
    si a == 10
    imprimir "El valor de a es 10"
    si_no
    asignar a 20
    o_si a < 10
    tambien
    retorno 3.14
    finL
    /* Este es un comentario de bloque */
    (a + b) * c
    '''

    # Proporcionar datos de entrada al lexer
    lexer.input(data)

    # Tokenizar
    while True:
        tok = lexer.token()
        if not tok:
            break  # No más entrada
        print(f'Type: {tok.type}, Value: {tok.value}, Line: {tok.lineno}, Position: {tok.lexpos}')

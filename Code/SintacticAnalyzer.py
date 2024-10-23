import ply.yacc as yacc
from LexicoAnalyzer import crear_lexer  # Asegúrate de que el nombre del archivo sea correcto
from LexicoAnalyzer import tokens
import codecs

# Crear el lexer
lexer = crear_lexer()

# Definición de la gramática
def p_program(p):
    'program : me instructions corro'
    print("Programa analizado correctamente")

def p_instructions_multiple(p):
    '''instructions : instructions instruction'''
    print(f"Instrucción procesada: {p[2]}")

def p_instructions_single(p):
    '''instructions : instruction'''
    print(f"Instrucción procesada: {p[1]}")

def p_instruction(p):
    '''instruction : loreI
                   | eteI
                   | muchotextoI
    '''

def p_lore(p):
    '''loreI : var lore arg1
             | var lore arg1 extralore
    '''
    value = p[3]
    print(f"Lore: {p[1],p[2],value}")

def p_lorexpr(p):
    '''arg1 : num
            | var
    '''
    print(f"ARG1:{p[1]}")
    p[0] = p[1]

def p_extralore(p):
    '''extralore : operator arg1
                 | operator arg1 extralore
    '''

    print(f"extralore:{p[1],p[2]}")

def p_operator(p):
    '''operator : plus
                | minus
                | times
                | divide
    '''
    print(f"operator:{p[1]}")
    p[0] = p[1]

def p_ete(p):
    '''eteI : ete lparen conditional rparen lcolon instructions rcolon
            | ete lparen conditional rparen lcolon instructions rcolon setchI
    '''
    print(f"Ete: {p[1],p[2],p[3],p[4],p[5],p[6]}")

def p_conditional(p):
    '''conditional : arg1 condition arg1
                   | arg1 condition arg1 logical conditional
    '''
    print(f"conditional: {p[1],p[2],p[3]}")

def p_condition(p):
    '''condition : greater
                 | equal
                 | less
                 | greater_equal
                 | less_equal
                 | not_equal
    '''
    print(f"condition: {p[1]}")
    p[0] = p[1]

def p_logical(p):
    '''logical : and
                 | or
    '''
    print(f"LOGICAL: {p[1]}")
    p[0] = p[1]

def p_setch(p):
    '''setchI : setch lcolon instructions rcolon
    '''
    print(f"Setch: {p[1],p[2],p[3],p[4]}")


def p_muchotexto(p):
    '''muchotextoI : muchotexto lparen arg1 rparen
                   | muchotexto lparen arg1 coma arg1 rparen
    '''
    print(f"muchotexto: {p[1],p[2],p[3],p[4],p[5]}")

def p_chambea(p):
    '''chambeaI : chambea lparen lore coma conditional coma additive rparen lcolon instructions rcolon
    '''
    print(f"chambea: {p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10],p[11]}")

def p_Additive(p):
    '''additive : plusplus
                | minusminus
    '''
    print(p[1])

    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Error de sintaxis en el token '{p.value}'")
    else:
        print("Error de sintaxis: fin de entrada inesperado")

# Leer el archivo de entrada
with codecs.open("entry.txt", "r", "utf-8") as fp:
    cadena = fp.read()

# Crear el analizador sintáctico
parser = yacc.yacc()

# Analizar la cadena
parser.parse(cadena, lexer=lexer)


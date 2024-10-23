import ply.lex as lex
import codecs

# Reservadas
reservadas = {
    'muchotexto': 'PR01',  # mostrar texto
    'elpepe': 'PR02',      # ciclo
    'lore': 'PR03',        # var asign
    'ete': 'PR04',         # If
    'setch': 'PR05',       # Else
    'chambea': 'PR06',     # For
    'me': 'PR07',          # inicio
    'corro': 'PR08',       # fin
}

# Tokens más reservadas
tokens = ['var', 'num', 'plus', 'minus', 'times', 'divide', 'lparen', 'rparen','rcolon','lcolon','greater','less',
          'equal','greater_equal','less_equal',"not_equal",'and','or','coma','plusplus','minusminus'] + list(reservadas.keys())
t_ignore = ' \t\r'

# Definición de los tokens
t_plus = r'\+'
t_minus = r'\-'
t_times = r'\*'
t_divide = r'\/'
t_lparen = r'\('
t_rparen = r'\)'
t_lcolon = r'\{'
t_rcolon = r'\}'
t_greater = r'\>'
t_less = r'\<'
t_equal = r'\=\='
t_greater_equal = r'\>\='
t_less_equal = r'\<\='
t_not_equal = r'\!\='
t_and = r'\&\&'
t_or = r'\|\|'
t_coma = r'\,'
t_plusplus =r'\+\+'
t_minusminus = r'\-\-'

t_muchotexto = r'muchotexto'
t_elpepe = r'elpepe'
t_lore = r'lore'
t_ete = r'ete'
t_setch = r'setch'
t_chambea = r'chambea'
t_me = r'me'
t_corro = r'corro'


def t_var(t):
    r'[A-Z][a-z0-9]*'
    t.type = reservadas.get(t.value, 'var')
    return t

def t_num(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("CARACTER ILEGAL '%s'" % t.value[0])
    t.lexer.skip(1)




def crear_lexer():
    lexer = lex.lex()
    return lexer


'''
fp = codecs.open("entry.txt","r","utf-8")
cadena=fp.read()
fp.close()
analizador = lex.lex()
analizador.input(cadena)
'''

'''
while True:
    tok = analizador.token()
    if not tok:break
    print (tok)
'''
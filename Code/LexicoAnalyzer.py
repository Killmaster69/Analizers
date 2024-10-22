import ply.lex as lex
import re
import codecs

#reservadas
reservadas={
    'PR01' : 'muchotexto', #mostrar texto
    'PR02' : 'elpepe'  , #ciclo
    'PR03' : 'lore'  ,
    'PR04' : 'doxeado'  ,
    'PR05' : 'ete'  ,
    'PR06' : 'setch'  ,
    'PR07' : 'chambea'  ,  
    'PR08' : 'me'  , #inicio
    'PR09' : 'corro'  , #fin
}
#tokens mas reservadas

tokens = ['var','num','sum'] + list(reservadas.values())
t_ignore = ' \t\r'
#t_me = r'me'
#t_corro = r'corro'
t_muchotexto = r'muchotexto'
t_elpepe = r'elpepe'
t_lore = r'lore'
t_doxeado = r'doxeado'
t_ete = r'ete'
t_setch = r'setch'
t_chambea = r'chambea'
t_me = r'me'
t_corro = r'corro'
t_sum = r'\+'

def t_var(t):
    r'[A-Z][a-z0-9]*'
    t.type = reservadas.get(t.value,'var')
    return t
def t_num(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("CARACTER ILEGAL '%s'" % t.value[0])
    t.lexer.skip(1)
fp = codecs.open("C:\\Users\\ferna\\Desktop\\me.txt","r","utf-8")
cadena=fp.read()
fp.close()
analizador = lex.lex()
analizador.input(cadena)

while True:
    tok= analizador.token()
    if not tok:break
    print (tok)
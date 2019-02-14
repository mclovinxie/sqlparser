# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: mclovinxie <mclovin.xxh@gmail.com>
# Note: don't change the doc of each function
# unless you really know what you are doing

from ply import lex

sum_value = 0

# List of token names.   This is always required
tokens = (
   'SUM',
   'NUMBER',
   # 'ZS',
   # 'FS',
   'LPAREN',
   'RPAREN',
   'COM'
)

# Regular expression rules for simple tokens
t_COM = r'\,'
t_LPAREN = r'\('
t_RPAREN = r'\)'


def t_NUMBER(t):
    r'(\-|\+)?\d+(\.\d+)?'
    t.value = float(t.value)
    global sum_value
    sum_value += t.value
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_SUM(t):
    r'SUM'
    t.value = sum_value
    return t


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


calculator_lexer = lex.lex()


if __name__ == '__main__':
    expression = '''
        SUM(2, SUM(1, -7), 3, 9, SUM(-1.5))
    '''
    calculator_lexer.input(expression)
    while True:
        tk = calculator_lexer.token()
        if not tk:
            break
        print(tk)
    print(sum_value)

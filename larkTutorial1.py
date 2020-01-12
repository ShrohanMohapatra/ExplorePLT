from lark import Lark
import logging
logging.basicConfig(level=logging.DEBUG)
collision_grammar = '''
start: as as
as: a*
a: "a"
'''
p = Lark(collision_grammar, parser='lalr', debug=True)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 12:47:18 2021

@author: shrohanmohapatra
"""

fileWriter = open('lambdaCalculusTools.txt','w')
fileWriter.write('0 := lambda f. lambda x. x\n')
fileWriter.write('1 := lambda f. lambda x. f x\n')
fileWriter.write('2 := lambda f. lambda x. f f x\n')
fileWriter.write('3 := lambda f. lambda x. f f f x\n')
fileWriter.write('4 := lambda f. lambda x. f f f f x\n')
fileWriter.write('5 := lambda f. lambda x. f f f f f x\n')
fileWriter.write('### .... Similarly ->\n')
fileWriter.write('m := lambda f. lambda x. f^m x\n')
fileWriter.write('SUCC := lambda m. lambda f. lambda x. f (m f x)\n')
fileWriter.write('PLUS := lambda m, n, f, x. m f n f x\n')
fileWriter.write('MULT := lambda m, n, f, x. m n f x\n')
fileWriter.write('TRUE := lambda x, y. x\n')
fileWriter.write('FALSE := lambda x, y. y\n')
fileWriter.write('EXP := lambda m, n. m (MULT n) 1\n')
fileWriter.write('AND := lambda p, q. p q p\n')
fileWriter.write('OR := lambda p, q. p p q\n')
fileWriter.write('NOT := lambda p, q. p FALSE TRUE\n')
fileWriter.write('ISZERO := lambda n. n (lambda x. FALSE) TRUE \n')
fileWriter.write('PRED := lambda n. n (lambda g. lambda k. ISZERO(g 1) k(PLUS(g k) 1)) (lambda v. 0) 0\n')
fileWriter.write('IFTHENELSE := lambda p, a, b. p a b\n')
fileWriter.write('NEGCHECK := lambda m, n. IFTHENELSE ISZERO PLUS m n m FALSE\n')
fileWriter.write('SUB := lambda m, n. PLUS m NEGCHECK -n n\n')
fileWriter.write('PRED1 := lambda m. SUB m 1\n')
fileWriter.write('Y := lambda g. (lambda x.g(x x))(lambda x. g(x x))\n')
fileWriter.close()

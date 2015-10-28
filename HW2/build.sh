#!/bin/bash
flex lexer.l
g++ lex.yy.c -o lexer
./lexer < "sample.txt"

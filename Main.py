from funcoes import *

a = selecionaArquivos()
print(a)
print(a[0])
print(a[1])
# a retorna uma tupla e nao uma string. tem que converter para b funcionar
b = tamanhoPagina(a)
print(b)
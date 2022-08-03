from funcoes import selecionaArquivos
from funcoes import tamanhoPagina

a = selecionaArquivos()
print(a[0])
# a retorna uma tupla e nao uma string. tem que converter para b funcionar
b = tamanhoPagina(a[0])
print(b)
from struct import pack
from tkinter import *
from tkinter import filedialog
from PyPDF2 import PdfFileReader

def selecionaArquivos():
    caminhoArquivo = filedialog.askopenfilenames()
    print(caminhoArquivo)
    return(caminhoArquivo)
    
def tamanhoPagina(arquivo):
    input1 = PdfFileReader(open(arquivo, 'rb'))
    return(input1.getPage(0).mediaBox)


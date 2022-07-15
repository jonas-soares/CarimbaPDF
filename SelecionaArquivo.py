from struct import pack
from tkinter import *
from tkinter import filedialog

def selecionaArquivos():
    caminhoArquivo = filedialog.askopenfilenames()
    print(caminhoArquivo)
    return(caminhoArquivo)
    

window = Tk()
botao = Button(text="Selecionar Arquivos", command=selecionaArquivos)
botao.pack()
window.mainloop()

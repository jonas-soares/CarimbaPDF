# pdf_watermarker.py

from struct import pack
from tkinter import *
from tkinter import filedialog

from PyPDF2 import PdfFileWriter, PdfFileReader

def selecionaArquivos():
    caminhoArquivos = filedialog.askopenfilename()
    pdfEntrada = str(caminhoArquivos)
    print(pdfEntrada)

def create_watermark(input_pdf, output, watermark):
    watermark_obj = PdfFileReader(watermark)
    watermark_page = watermark_obj.getPage(0)

    pdf_reader = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()

    # Watermark all the pages
    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)

"""if __name__ == '__main__':
    create_watermark(
        input_pdf='ArquivoTeste.pdf', 
        output='watermarked_notebook.pdf',
        watermark='CarimboTeste.pdf')
"""

pdfCarimbo = "C:\\Users\Viana e Moura\\Dropbox\\PROJETOS (INC_ENG)\\TEMP\\03 JONAS\\GIT\\Python\\CarimboPDF\\CarimboTeste.pdf"
#pdfEntrada = "C:\\Users\\Viana e Moura\\Dropbox\\PROJETOS (INC_ENG)\\TEMP\\03 JONAS\\GIT\\Python\\CarimboPDF\\ArquivoTeste.pdf"
pdfEntrada = ""
pdfSaida = "finalizado.pdf"

window = Tk()

botaoSelecionaArquivos = Button(text="Selecionar Arquivos", command=selecionaArquivos)
botaoSelecionaArquivos.pack()
botaoCriaMarca = Button(text="Gerar marca dágua", command=lambda: create_watermark(pdfEntrada, pdfSaida, pdfCarimbo))
botaoCriaMarca.pack()
botao_exit = Button(text="Sair",command= window.quit)
botao_exit.pack()

window.mainloop()
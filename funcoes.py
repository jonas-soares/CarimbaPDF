from struct import pack
from tkinter import *
from tkinter import filedialog
from fpdf import *
from PyPDF2 import PdfFileWriter, PdfFileReader


def selecionaArquivos():
    caminhoArquivo = filedialog.askopenfilenames()
    print(caminhoArquivo)
    return(caminhoArquivo)
    
def tamanhoPagina(arquivo):
    input1 = PdfFileReader(open(arquivo, 'rb'))
    return(input1.getPage(0).mediaBox)

def criaPDF(orientacao, formato, texto):
    largura = formato[0]
    altura = formato[1]
    pdf = FPDF(orientation=orientacao, unit="mm", format=formato)
    pdf.set_text_color(r=255,g=0,b=0)
    pdf.add_page(orientation=orientacao, format=formato)
    pdf.set_font(family="helvetica", size=12)
    pdf.text(10, altura-8, texto)
    pdf.output("teste.pdf")

def criaCarimbo(input_pdf, output, watermark):
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



criaPDF("P", (297,210), "CÓPIA SEM VALIDADE QUANDO IMPRESSA")


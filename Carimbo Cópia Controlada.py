
pdfCarimbo = ""
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
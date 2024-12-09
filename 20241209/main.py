#coding: utf-8

from ClassePasta import *
from ClasseArquivoPastaSuspensa import *
import time as t

def CriarPasta(QdeArquivos=5): 	
	Pasta1 = Pasta() #Crio a pasta
	Pasta1.CriarPastaVazia()	
	for _ in range(QdeArquivos):		
		Pasta1.Receber_arquivo()
	Pasta1.get_chaves_arquivos_pasta()
	return Pasta1				
		 	
def CriarArquivo(): 
	Arq1 = ArquivoPastaSuspensa("amarelo", "Pesquisa",NumMaxPastas=20)		
	return Arq1
def Mostrar_Pasta(Pastas):
	for i, j in range(Pastas):
		print(f'Pasta {i} com conteudo {j.conteudo} ')
		for c, k in j.documento.itens():
			print(f'\t chave {c} e valor {k} ')
			

if __name__ == "__main__": 
	
    Arq_de_Pastas = []
	NumPastasCriadas = 2
	for _ in range(NumPastasCriadas):
        PastaSuspensa = CriarPasta()
	    Arq_de_Pastas.append(PastaSuspensa)
		t.sleep(1.2) #0 programa vai parar por 1.2 segundos para mudar o momente onix
		print("Mudanca de Pasta")
		print()
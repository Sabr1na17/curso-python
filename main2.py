#coding utf-8
import os, shutil
import requests

def Selecao_Arquivos():
    '''
    url = 'https://docente.ifsc.edu.br/louis.augusto/Textos.zip'
    r = requests.get(url, allow_redirects=True)
    with open("Textos.zip", mode="wb") as file:
        file.write(r.content)
        shutil.unpack_archive("Textos.zip")	#Extrai os arquivos
    '''
    CaminhoPasta = os.getcwd()
    CaminhoPastaTxto = CaminhoPasta+os.sep+"Textos"
    Pasta_atual = os.chdir("Textos")
    ArquivosPastaTextos = os.listdir()
    print(ArquivosPastaTextos)
    ArquivosIndesejados = ["1"]
    for i in range(len(ArquivosIndesejados)):
        if ArquivosIndesejados[i] in ArquivosPastaTextos:
            ArquivosPastaTextos.remove(ArquivosIndesejados[i])
    print("Arquivos selecionados: ")
    for i, j in enumerate(ArquivosPastaTextos):
        print(f"Livro {i+j}: {j} ")
    print()
    return

if __name__=="__main__":
    Selecao_Arquivos()

   
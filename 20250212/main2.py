#coding: utf-8
import tkinter as tk



def main():
    JanelaPrincipal = tk.Tk()
    JanelaPrincipal.title("Banco Python")
    #Criacao de janela com 70% do tamanho da tela.
    TamHorJanela = int(JanelaPrincipal.winfo_screenwidth()*0.7)
    TamVerJanela = int(JanelaPrincipal.winfo_screenheigth()*0.7)
    print(TamHorJanela, TamVerJanela)
    TamTela = str(TamHorJanela)+"x"+str(TamVerJanela)
    JanelaPrincipal.geometry(TamTela)

    Pagina0 = Controlador(JanelaPrincipal)
    Pagina0.pack(fill=tk.BOTH)
    JanelaPrincipal.mainloop()



if __name__=="__main__":
    main()
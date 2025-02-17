#coding: utf -8

import tkinter as tk
import sqlite3 as sq #Importacao do banco de dados. 

def CriacaoBancoDados(): 
	NomeBD = "Usuario_senha.db"
	tabelaBD = '''
		CREATE TABLE IF NOT EXISTS Usuario_senha(
			nome TEXT NOT NULL,
			senha TEXT NOT NULL);
			'''
	conexao = sq.connect(NomeBD)
	cursor = conexao.cursor()
	cursor.execute(tabelaBD)
	conexao.commit()
	nome = input("Digite seu nome: ")
	senha = input("Digite sua senha: ")
	conexao.execute("INSERT INTO Usuario_senha VALUES (?,?)", (nome, senha))
	conexao.commit()

class Controlador(tk.Frame):
	def __init__(self, JanPr): 
		tk.Frame.__init__(self,JanPr)
		#Chama uma outra classe para construir a pagina sobre a pagina pai.
		#self.BotoesPrincipais()#Funcao para criar botoes
		self.PagLogin = PaginaLogin(self)
		self.PagLogin.grid(row=0, column = 0, sticky = "nswe")
		
		#Criacao do menu de tela. 
		self.menu = TrocadorTela(self)
		self.menu.grid(row = 0, column = 0, sticky = "nswe")
	

class PaginaLogin(tk.Frame): 
	def __init__(self, JanPr): 
		tk.Frame.__init__(self,JanPr)
		self.Label_login1 = tk.Label(self, text = "Pagina de Login", height = 5, width = 40, bg = 'Blue', fg = "White")
		self.Label_login1.grid()
		#Colocacao de nome de usuario e senha: 
		self.Label_Nome_usuario = tk.Label(self, text = "Nome do usuario: ", 
			height= 3, width = 15)
		self.Label_Nome_usuario.grid(row=1, column = 0)
		self.Entry_Nome_usuario=tk.Entry(self)
		self.Entry_Nome_usuario.grid(row=1, column = 1)
		self.Label_Senha_usuario = tk.Label(self, text = "Senha do usuario: ", 
			height= 3, width = 15)
		self.Label_Senha_usuario.grid(row=2, column = 0)
		self.Entry_Senha_usuario=tk.Entry(self, show = "*")
		self.Entry_Senha_usuario.grid(row=2, column = 1)
		#colocaco do botao
		self.VerLogin = tk.Button(self, text = "Entrar", bg = "White", height = 2, 
			width = 15, command = self.VerificaLogin)
		self.VerLogin.grid(row = 3, column=0)	
	
	def VerificaLogin(self): 			
		conexao = sq.connect('Usuario_senha.db')
		cursor=conexao.cursor()
		Selecao = '''
			SELECT * FROM Usuario_senha
			'''
		cursor.execute(Selecao)	
		Dados = cursor.fetchall()
		print(Dados)
		Nome_usuario = self.Entry_Nome_usuario.get()
		Senha_usuario = self.Entry_Senha_usuario.get()
		flagNome = False
		flagSenha = False
		if Nome_usuario ==Dados[0][0]: 
			print("Nome Validado")
			flagNome = True
		else: 
			print("Usuario nao encontrado")	
		if flagNome and Senha_usuario ==Dados[0][1]: 
			print("Senha Validada")
			flagSenha = True
		else: 
			print("Senha não validada")	
		if flagNome and flagSenha: 
			print("Usuario ok. ")	
			
			
			
		
	

class TrocadorTela(tk.Frame): 
	def __init__(self, JanPr): 
		tk.Frame.__init__(self,JanPr)
		self.BotoesPrincipais()
		self.LabelCentral=tk.Label(self, text = "Banco Python", height = 5, width = 52, background = "Red")
		self.LabelCentral.grid(row = 0, column = 2, columnspan=1)
		
		#Cuidado com o comando
		#self.PagLogin = tk.Button(self, text = "Login", height = 2, width = 16, command = self.master.PagLogin.tkraise)			
		#self.PagLogin.grid(row = 0, column = 0)

	def BotoesPrincipais(self): 
		self.BotaoLogin=tk.Button(self, text= "Tela de Login", height = 2, width = 16, bg = "WHITE", command = self.master.PagLogin.tkraise) 
		self.BotaoLogin.grid(row = 1, column = 2, columnspan = 1)	

def main(): 	
	JanelaPrincipal = tk.Tk()
	JanelaPrincipal.title("Banco Python")
	#Criacao de janela com 70% do tamanho da tela. 
	TamHorJanela = int(JanelaPrincipal.winfo_screenwidth()*0.3)
	TamVertJanela = int(JanelaPrincipal.winfo_screenheight()*0.6)	
	TamTela = str(TamHorJanela)+"x"+str(TamVertJanela)
	JanelaPrincipal.geometry(TamTela)
	Pagina0 = Controlador(JanelaPrincipal)
	Pagina0.pack(expand = True, fill=tk.BOTH)
	JanelaPrincipal.mainloop()


if __name__=="__main__": 
	#CriacaoBancoDados()
	main()
	


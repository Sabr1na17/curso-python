#coding:utf-8

#Cria uma janela com dimen




import tkinter as tk 
import PaletasDeCores as PC
janela = tk.Tk()
janela.title("Calc parte 1")
janela.geometry("240x320")#Comprimento e altura em pixels da janela
frame_visor=tk.Frame(janela, width =240, height =50, bg=PC.CorCinzaEscuro)#Criei o widget
                #bg = background - cor de fundo 
frame_visor.grid(row=0, column=0)#Ingere o frame usando grid
valor_visor = tk.StringVar() #Bariavel para entrar no visor
valor_visor.set("Calculadora ligada")
visor_label = tk.Label(frame_visor, textvariable= valor_visor, width = 16, height = 2)
visor_label.place(x=0, y=0)


#Criancao do frame botoes
frame_botoes = tk.Frame(janela, width =500, height =270, bg=PC.CorCinzaClaro)
frame_botoes.grid(row=1, column=0)

#Inclusao dos botoes 
#Linha 1
Botao_11 = tk.Button(frame_botoes, text = "Limpar", width = 11, height = 2)
Botao_11.place(x=0, y=0) #Posicao do botao 11 em pixels

Botao_12 = tk.Button(frame_botoes, text = "mod", width = 4, height = 2)
Botao_12.place(x=116, y=0) #Posicao do botao 11 em pixels

Botao_13 = tk.Button(frame_botoes, text = "div", width = 4, height = 2)
Botao_13.place(x=176, y=0) #Posicao do botao 11 em pixels

#Linha 2
Botao_21 = tk.Button(frame_botoes, text = '7', width = 4, height = 2)
Botao_21.place(x=0, y=52)

Botao_22 = tk.Button(frame_botoes, text = '8', width = 4, height = 2)
Botao_22.place(x=60, y=52)

Botao_23 = tk.Button(frame_botoes, text = '9', width = 4, height = 2)
Botao_23.place(x=120, y=52)

Botao_24 = tk.Button(frame_botoes, text = '*', width = 4, height = 2)
Botao_24.place(x=180, y=52)

#Linha 3
Botao_31 = tk.Button(frame_botoes, text = '4', width = 4, height = 2)
Botao_31.place(x=0, y=52*2)

Botao_32 = tk.Button(frame_botoes, text = '5', width = 4, height = 2)
Botao_32.place(x=60, y=52*2)

Botao_33 = tk.Button(frame_botoes, text = '6', width = 4, height = 2)
Botao_33.place(x=120, y=52*2)

Botao_34 = tk.Button(frame_botoes, text = '-', width = 4, height = 2)
Botao_34.place(x=180, y=52*2)

#Linha 4
Botao_41 = tk.Button(frame_botoes, text = '3', width = 4, height = 2)
Botao_41.place(x=0, y=52*3)

Botao_42 = tk.Button(frame_botoes, text = '2', width = 4, height = 2)
Botao_42.place(x=60, y=52*3)

Botao_43 = tk.Button(frame_botoes, text = '1', width = 4, height = 2)
Botao_43.place(x=120, y=52*3)

Botao_44 = tk.Button(frame_botoes, text = '+', width = 4, height = 2)
Botao_44.place(x=180, y=52*3)

#Linha 5
Botao_51 = tk.Button(frame_botoes, text = '0', width = 4, height = 2)
Botao_51.place(x=0, y=52*4)

Botao_52 = tk.Button(frame_botoes, text = '00', width = 4, height = 2)
Botao_52.place(x=60, y=52*4)

Botao_53 = tk.Button(frame_botoes, text = '.', width = 4, height = 2)
Botao_53.place(x=120, y=52*4)

Botao_54 = tk.Button(frame_botoes, text = '^', width = 4, height = 2)
Botao_54.place(x=180, y=52*4)

#Linha 6
Botao_61 = tk.Button(frame_botoes, text = '=', width = 25, height = 1)
Botao_61.place(x=5, y=52*5)

janela.mainloop()           
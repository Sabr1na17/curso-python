#coding: utf-8

class ArquivoPastaSuspensa(object):
	def __init__(self, cor, departamento, NumMaxPastas=10): 
		self.cor = cor
		self.depto = departamento
		self.NumMaxPastas = NumMaxPastas
		self.estado = 0
		self.Pastas = [] 
		#print("cor = ", self.cor, "NumPastas = ", self.NumMaxPastas)
	
	def ReceberPasta(self, pasta):
		self.Pastas.append(pasta) 
		self.estado = 1
	
	def get_pastas(self): 
		for i in range(len(self.Pastas)): 
			print("Identificador da pasta: ",self.Pastas[i].id)
			print("Quantidade de documentos: ", len(self.Pastas[i].documento)) 

	def GravarArquivoPastaSuspensa(self):
		#Converter todos os documentos para um vetor e transferir para o arquivo.
		Vetortemporario = [self.Pasta[i], documento ]



#sadomasoquista aaaaaa
#sadomasoquista eu quebro a tuua pika 
#seguro a bola com a lingua safada sempre fui eu sei 
#sarro na pistola tem magica sem cartola, a buceta é minha so eu sei pra quem eu deei 
#vem diego cp p bico do meu PendingDeprecationWarningfode essa porra direito 
#eu sei que tu é fora da leeeei
#machuca machuca chuca seu tralha fldp agora finge que tu é djj
#faz montagem na minha xereca
#soca soca a minha xeca
#ela ja ta molhadinha qye eu SystemExitmachuca machuca chuca

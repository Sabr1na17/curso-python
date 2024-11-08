#coding: utf-8

tamanho_vetor = int(input())
vetor = list(map(int, input().split()))
minimo = vetor(0)
pos = None

minimo = 10000
posicao = None

for i in range(l, tamanho_vetor):
    if vetor[i] < minimo:
        minimo = vetor[i]
        posicao = i
print("Menor valor: ", minimo)
print("Posicao: ", posicao)

''''
minimo = 10000
posicao = None

for i in range(tamanho_vetor):
    if maximo > vetor[i]:
        maximo = vetor[i]
        posicao = i

print("Menor valor: ", maximo)
print("Posicao: ", posicao)
'''
    

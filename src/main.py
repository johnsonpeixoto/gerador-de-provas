#!/usr/bin/env python
# coding=UTF-8

import csv, sys
import random
from random import randint

num_linhas = 0
junto = []
ab = 0
fe = 0

def carregarQuestoes(arquivo):
	global num_linhas
	with open(arquivo) as csvfile:
		arquivo = csv.reader(csvfile, delimiter=';')
		for row in arquivo:
			junto.append(row)
			num_linhas += 1

def escolherQuestoes(fechadas, abertas):
	qst = []
	total = fechadas+abertas
	fe = fechadas
	ab = abertas
	while(len(qst) < total):
		temp = randint(1, num_linhas)
		if qst.count(temp) == 0:
#			print('Nao e duplicada')
			if(junto[temp-1][0] == str(0) and fe > 0):
				fim = int(len(qst)-1)
				qst.append(temp)
				fe -= 1
			elif(junto[temp-1][0] == str(1) and ab > 0):
				qst.append(temp)
				ab -= 1
	return qst

def escreverQuestoes(questoes,arqNome):
	arquivo=open(arqNome+".txt", "a")
	rand_arr = [2,3,4,5,6]
	arquivo.write('================== PROVA ==================\n')
	for x in questoes:
		random.shuffle(rand_arr) # randomiza a cada laço os indices das respostas
		if(junto[x-1][0] == str(1)):
#			print('Q%s) %s\n' % ((questoes.index(x)+1),junto[x-1][1]))
			arquivo.write('Q%s) %s\n' % ((questoes.index(x)+1),junto[x-1][1]))
		else:
			arquivo.write('Q%s) %s\na)%s\nb)%s\nc)%s\nd)%s\ne)%s\n' % ((questoes.index(x)+1),junto[x-1][1],junto[x-1][rand_arr[0]],junto[x-1][rand_arr[1]],junto[x-1][rand_arr[2]],junto[x-1][rand_arr[3]],junto[x-1][rand_arr[4]]))
	arquivo.close()
def main(argv):
	if(len(argv) != 0):
		carregarQuestoes(str(argv[0]))
		escreverQuestoes(escolherQuestoes(int(argv[1]), int(argv[2])), argv[3])
	else:
		print ('Use: main.py <banco.csv> <fechadas> <abertas> <nome arquivo de saida>')

if __name__ == '__main__':
	main(sys.argv[1:])

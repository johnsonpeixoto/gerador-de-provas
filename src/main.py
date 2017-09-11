#!/usr/bin/env python
# coding=UTF-8

import csv, sys
from random import randint

num_linhas = 0
junto = []
ab = 0
fe = 0

def carregarQuestoes(arquivo):
	with open(arquivo) as csvfile:
		arquivo = csv.reader(csvfile, delimiter=';')
		for row in arquivo:
			junto.append(row)
			num_linhas+=1
			
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
				qst.append(temp)
				fe -= 1
			elif(junto[temp-1][0] == str(1) and ab > 0):
				qst.append(temp)
				ab -= 1
	return qst

def escreverQuestoes(questoes):
	for x in questoes:
		if(junto[x-1][0] == str(1)):
			print('Q%s) %s\n' % ((questoes.index(x)+1),junto[x-1][1]))
		else:
			print('Q%s) %s\na)%s\nb)%s\nc)%s\nd)%s\n' % ((questoes.index(x)+1),junto[x-1][1],junto[x-1][2],junto[x-1][3],junto[x-1][4],junto[x-1][5]))

def main(argv):
	if(len(argv) != 0):
		carregarQuestoes(str(argv[0]))
		escreverQuestoes(escolherQuestoes(int(argv[1]), int(argv[2])))
	else:
		print ('Use: main.py [banco.csv] [fechadas] [abertas]')

if __name__ == '__main__':
	main(sys.argv[1:])

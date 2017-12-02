################
# Background.py#
# S.Guillier.  #
# 18/10/2017   #
# S2A TFTRG    #
################
# coding: utf8
#!/usr/bin/python
import sys
import os
def create(b):
	bg = dict()
	
	for i in range(1,4):
	
		myfile = open(b+str(i)+".txt","r")
	
		chaine = myfile.read()
	
		listeLigne = chaine.splitlines()
		bg[b+str(i)] = dict()
		bg[b+str(i)]["map"] = []
	
		for line in listeLigne:
			listeChar = list(line)
			bg[b+str(i)]["map"].append(listeChar)
		
		myfile.close()
	
	return bg
	
def getChar(bg,x,y):
	return bg["map"][y][x]
	
def setChar(bg,x,y,c):
	bg["map"][y][x] = c


	
	
def show(bg,dpBG,pa):
	#Verifie si etat Pre-Active
		if pa == True:
			a = 0
		else:
			a = dpBG
		for y in range(len(bg["map"])):
			for x in range(a,len(bg["map"][y])):
				if getChar(bg, x, y) != " ":
					if pa == True:
						s ="\033["+str(y)+";"+str(x+99-dpBG)+"H";
					else:
						s ="\033["+str(y)+";"+str(x-dpBG)+"H";
					sys.stdout.write(s)
					if getChar(bg, x, y) == "*":
						sys.stdout.write("\033[33m")
					elif getChar(bg, x, y) == "/":
						sys.stdout.write("\033[97;42m")
					elif getChar(bg, x, y) == "|" or "_":
						sys.stdout.write("\033[37;40m")
			#Affichage du decor
				sys.stdout.write(bg["map"][y][x])
				
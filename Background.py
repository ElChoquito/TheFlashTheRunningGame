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
def create(filename,Intro):
	bg = dict()
	
	myfile = open(filename,"r")
	
	chaine = myfile.read()
	
	listeLigne = chaine.splitlines()
	
	bg["map"] = []
	
	for line in listeLigne:
		listeChar = list(line)
		bg["map"].append(listeChar)
		
	myfile.close()
	
	bg["PreActive"] = False
	bg["name"] = filename
	bg["intro"] = Intro
	
	return bg
	
def getChar(bg,x,y):
	return bg["map"][y][x]
	
def setChar(bg,x,y,c):
	bg["map"][y][x] = c

def getIntro(bg):
	return bg["intro"]
	

def getPreActiveState(bg):
	return bg["PreActive"]
def setPreActiveState(bg):
	bg["PreActive"] = True
def resetPreActiveState(bg):
	bg["PreActive"] = False
	
def getFilename(b):
	return b["name"]
	
def show(bg,dpBG):
	if getPreActiveState(bg) == True:
		a = 0
	else:
		a = dpBG
	for y in range(len(bg["map"])):
		for x in range(a,len(bg["map"][y])):
				
			if getChar(bg, x, y) != " ":
				if getPreActiveState(bg) == True:
					s ="\033["+str(y)+";"+str(x+99-dpBG)+"H";
				else:
					s ="\033["+str(y)+";"+str(x-dpBG)+"H";
					
				sys.stdout.write(s)
#				sys.stdout.write("\033[37m")
				if getIntro(bg) != True:
					if getChar(bg, x, y) == "*":
						sys.stdout.write("\033[33m")
					elif getChar(bg, x, y) == "/":
						sys.stdout.write("\033[97;42m")
					elif getChar(bg, x, y) == "|" or "_":
						sys.stdout.write("\033[37;40m")
				else:
					if getChar(bg, x, y) == "*":
						sys.stdout.write("\033[33m")
					if getChar(bg, x, y) == "#":
						sys.stdout.write("\033[31m")
					if getChar(bg, x, y) == "%":
						sys.stdout.write("\033[37m")
			#Affichage du decor
			sys.stdout.write(bg["map"][y][x])
				
				
				
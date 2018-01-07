################
# Menu.py	   #
# S.Guillier.  #
# 18/10/2017   #
# S2A TFTRG    #
################
# coding: utf8
#!/usr/bin/python
import sys
import os

def create(filename,set):
	menu = dict()
	
	myfile = open(filename,"r")
	if filename == "score.txt":
		menu["score"]=["P1",500,"P2",300,"P3",100]
		texte = myfile.read()
		a = texte.split(":")
		for i in range(6):
			menu["score"][i] = a[i]
			
	else:	
		menu["screen"] = []
	
		chaine = myfile.read()
		menu["screen"].append(chaine)
	menu["set"] = set
	menu["name"] = filename
		
	
	return menu
	
def getSet(menu):
	return menu["set"]
def setSet(menu):
	menu["set"] = True
def resetSet(menu):
	menu["set"] = False
def getScore(a,i):
	return a["score"][i]
def setScore(a,i,b):
	a["score"][i] = b
def show(menu):
	if menu["name"] == "score.txt":
			s ="\033["+str(20)+";"+str(20)+"H";
			sys.stdout.write("Top3: ")
			for i in range (6):
				sys.stdout.write(str(menu["score"][i])+" ")
	else:
		for x in range(len(menu["screen"])):
			s ="\033["+str(x)+";"+str(x)+"H";
			sys.stdout.write(s)
		sys.stdout.write(menu["screen"][x])
			

def score(a,b,score):
	a = int(a)
	if a > int(getScore(score, 1)):
		setScore(score, 4, getScore(score, 2))
		setScore(score, 5, getScore(score, 3))
		setScore(score, 2, getScore(score, 0))
		setScore(score, 3, getScore(score, 1))
		setScore(score, 0, b)
		setScore(score, 1, a)
	elif a > int(getScore(score, 3)):
		setScore(score, 4, getScore(score, 2))
		setScore(score, 5, getScore(score, 3))
		setScore(score, 2, b)
		setScore(score, 3, a)
	elif a > int(getScore(score, 5)):
		setScore(score, 4, b)
		setScore(score, 5, a)
	myfile=open("score.txt","w")
	for i in range(6):
		c = str(getScore(score, i)) +":"
		myfile.write(c)
	myfile.close()


		
		


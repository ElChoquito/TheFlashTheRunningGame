################
# Animat.py	   #
# S.Guillier.  #
# 18/10/2017   #
# S2A TFTRG    #
################
# coding: utf8
#!/usr/bin/python
import sys
import os


def create(x,y,filename,vitesse,genre):
	animat = dict()
	animat["x"] = x
	animat["y"] = y
	animat["look"] = []
	animat["animation"] = 2
	animat["flying"] = False
	animat["onUpperPlatform"] = False
	animat["flyingMax"] = False
	animat["falling"]= False
	animat["genre"] = genre
	animat["attack"] = False
	animat["set"] = True
	animat["score"] = 0
	
	myfile = open(filename,"r")
	chaine = myfile.read()
	listeLignes = chaine.splitlines()
	for line in listeLignes:
		listeChar = list(line)
		animat["look"].append(listeChar)
	myfile.close()
	return animat

def getScore(a):
	return a["score"]
def setScore(a,b):
	a["score"] = getScore(a) + b
def getSet(a):
	return a["set"]
def setSet(a):
	a["set"] = True
def resetSet(a):
	a["set"] = False
def getGenre (a):
	return a["genre"]
def setGenre(a,b):
	a["genre"]=b
def getChar(a,x,y):
	return (a["look"][y][x])
	
def getAttack(a):
	return a["attack"]
def setAttack(a):
	a["attack"] = True
def resetAttack(a):
	a["attack"] = False

def getY(a):
	return a["y"]
def setY(a,b):
	a["y"] = b

def increaseY(a):
	a["y"] = getY(a) + 2
def decreaseY(a):
	a["y"] = getY(a) - 1

def getFlying(a):
	return a["flying"]
def setFlying(a):
	a["flying"] = True
def resetFlying(a):
	a["flying"] = False

def getOnUpperPlatform(a):
	return a["onUpperPlatform"]
def setOnUpperPlatform(a):
	a["onUpperPlatform"] = True
def resetOnUpperPlatform(a):
	a["onUpperPlatform"] = False

def setFalling(a): 
	a["falling"] = True
def getFalling(a):
	return a["falling"]
def resetFalling(a):
	a["falling"] = False

def getFlyingMax(a):
	return a["flyingMax"]
def setFlyingMax(a):
	a["flyingMax"] = True
def resetFlyingMax(a):
	a["flyingMax"] = False
	
def getAnimation(a):
	return a["animation"]
def setAnimation(a,b):
	a["animation"] = b
		
def show(a,dpen,dpat):
	if getAnimation(a) == 1:
		d = 0
		f = 13
		h=0
		setAnimation(a, 2)
	else :
		d=20
		f=34
		h=20
		setAnimation(a, 1)
	for y in range(d,f):
		for x in range(len(a["look"][y])):
			if getChar(a,x,y) != " ":
				if getSet(a) == False:
					pass
				else:
					if getGenre(a) == "player" and getSet(a) == True:
						s = "\033["+str(y+23-getY(a)-h)+";"+str(x+2)+"H";
					if getGenre(a) == "ennemy" and getSet(a) == True:
						s = "\033["+str(y+23-getY(a)-h)+";"+str(x+200-dpen)+"H";
					sys.stdout.write(s)
					if getChar(a, x, y) == "#":
						sys.stdout.write("\033[41;31m")
					elif getChar(a, x, y) == "@":
						sys.stdout.write("\033[43;33m")
					elif getChar(a, x, y) == "^":
						sys.stdout.write("\033[41;30m")
					elif getChar(a, x, y) == "*":
						sys.stdout.write("\033[31;40m")
					elif getChar(a, x, y) == "=":
						sys.stdout.write("\033[47;30m")
					sys.stdout.write(a["look"][y][x])
	
		if getAttack(a) == True:
			s = "\033["+str(28)+";"+str(dpat)+"H";
			sys.stdout.write(s)
			sys.stdout.write("\033[46;30m")
			sys.stdout.write("FL")
		if getGenre(a) == "player":
			s = "\033["+str(2)+";"+str(2)+"H";
			sys.stdout.write(s)
			sys.stdout.write("\033[41;30m")
			sys.stdout.write("Score:"+str(getScore(a)))

#
def jump(a):
	if getFlying(a) == True and getOnUpperPlatform(a)==True:
				resetFlyingMax(a)
				resetOnUpperPlatform(a)
	if getFlying(a) == True and getFlyingMax(a) == False and getY(a) !=18 and getOnUpperPlatform(a)==False:
		setY(a, getY(a)+2)
	if getY(a) == 18:
		setFlyingMax(a)
	if getFlying(a) == True and getFlyingMax(a) == True and getY(a) !=0 :
		setY(a, getY(a)-1)
	if getY(a) == 0:
		resetFlying(a)
		resetFlyingMax(a)

def fall(a):
	setY(a, -5)
	#FIN DU JEU


def onUpperPlatform(a):
	if getOnUpperPlatform(a) == True:
		setY(a, 12)

#a = create(0, 0, "player.txt", 0)
#show(a)

		
				
				
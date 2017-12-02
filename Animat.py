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


def create(x,y,filename,genre):
	animat = dict()
	animat["x"] = [x,x+15]
	animat["y"] = [y,y+13]
	animat["look"] = []
	animat["animation"] = 2
	animat["flying"] = False
	animat["onUpperPlatform"] = False
	animat["flyingMax"] = False
	animat["falling"]= False
	animat["genre"] = genre
	animat["attack"] = False
	animat["attY"] = 0
	animat["attX"] = 0
	animat["set"] = True
	animat["score"] = 0
	animat["character"] = ["#","@","^","*","="]
	animat["color"] = ["\033[41;31m","\033[43;33m","\033[41;30m","\033[31;40m","\033[47;30m"]
	
	myfile = open(filename,"r")
	chaine = myfile.read()
	listeLignes = chaine.splitlines()
	for line in listeLignes:
		listeChar = list(line)
		animat["look"].append(listeChar)
	myfile.close()
	return animat

def getX1(a):
	return a["x"][0]
def getX2(a):
	return a["x"][1]
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
#def setGenre(a,b):
#	a["genre"]=b
def getChar(a,x,y):
	return (a["look"][y][x])
	
def getAttack(a):
	return a["attack"]
def setAttack(a):
	a["attack"] = True
def resetAttack(a):
	a["attack"] = False

def getY1(a):
	return a["y"][0]
def getY2(a):
	return a["y"][1]
def setY1(a,b):
	a["y"][0] = b
	a["y"][1] = b +13

def setAttY(a):
	a["attY"] =getY2(a)-5
def getAttY(a):
	return a["attY"]
def setAttX(a,b):
	a["attX"] = b
def getAttX(a):
	return a["attX"]
	
	
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
	
def getLenCharacter(a):
	return len(a["character"])
def getShowCharacter(a,i):
	return a["character"][i]
def getShowColor(a,i):
	return a["color"][i]
		
def show(a,dpen):
	ah = 23		#Hauteur animat
	#Gere l'affichage de l'animation
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
	if getSet(a) == False:
		pass
	else:
	#Affichage de l'animat
		for y in range(d,f):
			for x in range(len(a["look"][y])):
				if getChar(a,x,y) != " ":
				
				#Affichage animat en fonction du genre
					if getGenre(a) == "player" and getSet(a) == True:
						s = "\033["+str(y+ah-getY1(a)-h)+";"+str(x+getX1(a))+"H";
					if getGenre(a) == "ennemy" and getSet(a) == True:
						s = "\033["+str(y+ah-getY1(a)-h)+";"+str(x+getX1(a)-dpen)+"H";
					sys.stdout.write(s)
					for i in range(getLenCharacter(a)):
						if getChar(a, x, y) == getShowCharacter(a, i):			#Affiche la couleur associe au charactere
							sys.stdout.write(getShowColor(a, i))
					sys.stdout.write(a["look"][y][x])
	#Affichage de l'attaque
		if getAttack(a) == True:
			s = "\033["+str(36-getAttY(a))+";"+str(getAttX(a))+"H";
			sys.stdout.write(s)
			sys.stdout.write("\033[46;36m")
			sys.stdout.write("FL")
		#Affichage du score
		if getGenre(a) == "player":
			s = "\033["+str(2)+";"+str(2)+"H";
			sys.stdout.write(s)
			sys.stdout.write("\033[41;30m")
			sys.stdout.write("Score:"+str(getScore(a)))

#Gere le saut de l'animat
def jump(a):
	if getFlying(a) == True and getOnUpperPlatform(a)==True:
				resetFlyingMax(a)
				resetOnUpperPlatform(a)
	if getFlying(a) == True and getFlyingMax(a) == False and getY1(a) !=18 and getOnUpperPlatform(a)==False:
		setY1(a, getY1(a)+2)
	if getY1(a) == 18:
		setFlyingMax(a)
	if getFlying(a) == True and getFlyingMax(a) == True and getY1(a) !=0 :
		setY1(a, getY1(a)-1)
	if getY1(a) == 0:
		resetFlying(a)
		resetFlyingMax(a)

#Chute
def fall(a):
	setY1(a, -5)
	#FIN DU JEU

#Maintien sur plateforme haute
def onUpperPlatform(a):
	if getOnUpperPlatform(a) == True:
		setY1(a, 12)


					
				
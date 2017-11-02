################
# main.py      #
# S.Guillier.  #
# 18/10/2017   #
# S2A TFTRG    #
################
# coding: utf8
#!/usr/bin/python

#modules externes
import sys
import os
import time
import select
import tty 
import termios
import random
#Mes modules
import Background
import Animat


old_settings = termios.tcgetattr(sys.stdin)
#donne du jeu
animat=None
background=None
timeStep=None

def init():
	global timeStep, dpBG, animat, building, level,level2,building2,rdbg,rdlv,menu,ennemy,dpEn,dpAt,value,score,intro
	timeStep = 0.05
	dpBG = 0
	dpEn=0
	dpAt = 0
	score = 0
	rdbg = str(random.randint(1,3))
	rdlv =str(random.randint(1,3))
	animat= Animat.create(0,0, "player.txt", 0,"player")
	ennemy = Animat.create(0, 0, "ennemy.txt", 0, "ennemy")
	value = 2
	
	building = Background.create("building1.txt",False)
	building2 = Background.create("building"+rdbg+".txt",False)
	
	level = Background.create("level1.txt",False)
	level2 = Background.create("level"+rdlv+".txt",False)
	
	Background.setPreActiveState(building2)
	Background.setPreActiveState(level2)
	
	menu = Background.create("Menu.txt",True)
	intro = Background.create("Menu2.txt", True)
	
	#interaction clavier
	tty.setcbreak(sys.stdin.fileno())
	
	sys.stdout.write("\033[1;1H")
	sys.stdout.write("\033[2J")
	sys.stdout.write("\033[40;31m")
	
def move():
	global dpBG,building,building2,rdbg,rdlv,level, level2,dpEn,dpAt,value,score
	value = random.randint(1,2)
	#Affichage ou non d'ennemy
	if dpEn == 0 or dpEn == 99 and dpBG == 32:
		if value == 2:
			Animat.setSet(ennemy)
		else:
			Animat.resetSet(ennemy)
	
	if dpAt >= 199-dpEn and Animat.getAttack(animat) == True and Animat.getSet(ennemy)==True:
			Animat.resetSet(ennemy)
			Animat.resetAttack(animat)
			Animat.setScore(animat, 2)
			dpAt=0
	if Animat.getScore(animat) >=50 and Animat.getScore(animat)<150:
		dpBG = dpBG+3
		dpEn = dpEn +3
	elif Animat.getScore(animat) >=150:
		dpEn = dpEn +4
		dpBG = dpBG +4
	else:
		dpBG = dpBG +2
		dpEn = dpEn +2
	
	if Animat.getAttack(animat) == True:
		if dpAt == 0:
			dpAt=17
		else:
			dpAt = dpAt +8
	if dpEn >= 200 :
		dpEn = 0

	if Animat.getAttack(animat)==True and dpAt >183 :
		Animat.resetAttack(animat)
		dpAt = 0
		
	if dpBG >= 100:
		dpBG = 0
		Animat.setScore(animat, 10)
		
		building = Background.create("building"+rdbg+".txt",False)
		rdbg = str(random.randint(1,3))
		building2 = Background.create("building"+rdbg+".txt",False)
		Background.setPreActiveState(building2)
		
		level = Background.create("level"+rdlv+".txt",False)
		rdlv = str(random.randint(1,2))
		level2 = Background.create("level"+rdlv+".txt",False)
		Background.setPreActiveState(level2)

	Animat.jump(animat)
	ay = Animat.getY(animat)
	if ay == 0:
		if dpBG >= 82:
			if dpBG-82 == 199-13-dpEn and Animat.getSet(ennemy)==True:
				Animat.fall(animat)
			if Background.getChar(level2, dpBG-82, 36) == " ":			# Gere la chute de la platforme basse
				Animat.setFalling(animat)
				Animat.fall(animat)
		elif Background.getChar(level, 17+dpBG,36) == " ":
			Animat.setFalling(animat)
			Animat.fall(animat)
		if Background.getChar(level2, dpBG-82, 36) == "_":			#Gere maintien sur platforme basse
			Animat.resetOnUpperPlatform(animat)
		elif Background.getChar(level, 17+dpBG, 36) == "_":
			Animat.resetOnUpperPlatform(animat)
		
		if 17+dpBG == 199-13-dpEn and Animat.getSet(ennemy)==True:
			Animat.fall(animat)

	if ay == 12:
		if dpBG >=82:
			if Background.getChar(level2, dpBG-82, 24) == "_" and Animat.getFlyingMax(animat) == True:			# Gere maintien sur la platforme haute
				Animat.setOnUpperPlatform(animat)
				Animat.resetFlying(animat)
				Animat.onUpperPlatform(animat)
		elif Background.getChar(level, 17+dpBG, 24)== "_" and Animat.getFlyingMax(animat) == True :
			Animat.setOnUpperPlatform(animat)
			Animat.resetFlying(animat)
			Animat.onUpperPlatform(animat)
			
	
	if ay == 12:
		if dpBG >=82:
			if Background.getChar(level2, dpBG-82,24) == " " and Animat.getFlyingMax(animat) == True:
				Animat.resetOnUpperPlatform(animat)
				Animat.setFlying(animat)
				Animat.setFlyingMax(animat)
				Animat.jump(animat)								#Gere chute plateforme
		elif Background.getChar(level, 17+dpBG, 24) == " " and Animat.getFlyingMax(animat)==True:
			Animat.resetOnUpperPlatform(animat)
			Animat.setFlying(animat)
			Animat.setFlyingMax(animat)
			Animat.jump(animat)	
		
	
	
	

	
def isData():
	return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])
	
def interact():
	if isData():
			touche = sys.stdin.read(1)
			if touche == '\x1B':
				quitGame()
			if touche == ' ':
				Animat.setFlying(animat)
			if touche == 'd':
				if Animat.getY(animat) == 0:
					Animat.setAttack(animat)
	
def show():
	sys.stdout.write("\033[2J")
	sys.stdout.write("\033[40m")
	Background.show(building, dpBG)
	Background.show(building2, dpBG)
	Background.show(level, dpBG)
	Background.show(level2, dpBG)
	Animat.show(animat,dpEn,dpAt)
	Animat.show(ennemy,dpEn,dpAt)
	sys.stdout.write("\033[40m")
	sys.stdout.write("\033[1;1H\n")
	
def run():
	while 1:
		interact()
		move()
		show()
		time.sleep(timeStep)
		
def quitGame():
	sys.stdout.write("\033[2J")
	sys.exit()
		
##########################################################
init()
Background.show(menu, 0)
time.sleep(3)
Background.show(intro, 0)
time.sleep(6)
run()
quitGame()

#Affichage Animat: x:17 y:13
#Affichage Platforme y:24

#Affichage sans refresh?
#Decouper en sous batiment?

#Collision
#Menu
#Ecran accueil	

# Monter jusqu'a 18 avec etat S Actif MS I C I
#Arriver 18 etat Inactif MS = Actif C Actif
# Si le charactere est OK et que Chute:
	
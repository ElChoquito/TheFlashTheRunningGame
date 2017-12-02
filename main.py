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
import Menu


old_settings = termios.tcgetattr(sys.stdin)
#donne du jeu
animat=None
background=None
timeStep=None

def init():
	global timeStep, dpBG, animat,building,level,rdbg,rdlv,homeScreen,intro,ennemy,dpEn,dpAt,value,intro,gameOver,ll,bl,score
	timeStep = 0.05
	dpBG = 0
	dpEn=0
	dpAt = 0
	animat= Animat.create(2,0, "player.txt","player")
	ennemy = Animat.create(200, 0, "ennemy.txt","ennemy")
	value = 2
	
	building = Background.create("building")
	
	level = Background.create("level")
	
	
	bl = [1,2]
	ll = [1,2]
	
	
	homeScreen = Menu.create("Menu.txt",True)
	intro = Menu.create("Menu2.txt",False)
	gameOver = Menu.create("GameOver.txt", False)
	score = Menu.create("score.txt", False)
	#interaction clavier
	tty.setcbreak(sys.stdin.fileno())
	
	sys.stdout.write("\033[m")
	sys.stdout.write("\033[1;1H")
	sys.stdout.write("\033[2J")
	sys.stdout.write("\033[40;31m")
	
def move():
	global dpBG,dpEn,dpAt,value,score
	
	ul=24		#Niveau haut
	dl=36		#Niveau bas
	if Menu.getSet(homeScreen)==False and Menu.getSet(intro) == False and Menu.getSet(gameOver) == False and Menu.getSet(score) == False:	
		
		value = random.randint(1,2)
	
	#Affichage ou non d'ennemie
		if dpEn == 0 or dpEn == 99 and dpBG == 30:
			if value == 2:
				Animat.setSet(ennemy)
			else:
				Animat.resetSet(ennemy)
		#Gestion de l'attaque
		if Animat.getSet(ennemy) == True:
			if Animat.getAttack(animat) == True:
				if Animat.getAttX(animat) >= Animat.getX1(ennemy)-dpEn and Animat.getAttY(animat) <=Animat.getY2(ennemy) and Animat.getAttY(animat) >= Animat.getY2(ennemy) -4:
					Animat.resetSet(ennemy)
					Animat.resetAttack(animat)
					Animat.setScore(animat, 20)
					Animat.setAttX(animat, 0)
				elif Animat.getAttX(animat) >= Animat.getX1(ennemy)-dpEn and Animat.getAttY(animat) <= Animat.getY2(ennemy):
					Animat.resetSet(ennemy)
					Animat.resetAttack(animat)
					Animat.setScore(animat, 2)
					Animat.setAttX(animat, 0)
			if Animat.getX2(animat) >= Animat.getX1(ennemy)-dpEn and Animat.getY1(animat) <= Animat.getY2(ennemy):
				Animat.setFalling(animat)
				Animat.fall(animat)



	#Augmentation de la vitesse du jeu
		if Animat.getScore(animat) >=50 and Animat.getScore(animat)<150:
			dpBG = dpBG+3
			dpEn = dpEn +3
		elif Animat.getScore(animat) >=150:
			dpEn = dpEn +4
			dpBG = dpBG +4
		else:
			dpBG = dpBG +2
			dpEn = dpEn +2
	
	#Parametrage de l'attaque
		if Animat.getAttack(animat) == True:
			if Animat.getAttX(animat) == 0:
				Animat.setAttX(animat, Animat.getX2(animat)-2)
			else:
				Animat.setAttX(animat, Animat.getAttX(animat)+8)
		if dpEn >= 200 :
			dpEn = 0
		if Animat.getAttX(animat) >= 183 :
			Animat.setAttX(animat, 0)
			Animat.resetAttack(animat)


		
	#Augmentation du score
		if dpBG >= 100:
			dpBG = 0
			Animat.setScore(animat, 10)
			rdbg = random.randint(1,3)
			rdlv = random.randint(1,3)
	
	#Changement des niveaux a affiche
			bl[0] = bl[1]
			bl[1] = rdbg
			ll[0] = ll[1]
			ll[1] = rdlv
			
			
		Animat.jump(animat)
		ay = Animat.getY1(animat)
		if ay == 0:
			if dpBG >= 82:
				if Background.getChar(level["level"+str(ll[1])], dpBG-82, dl) == " ":			# Gere la chute de la platforme basse
					Animat.setFalling(animat)
					Animat.fall(animat)
			elif Background.getChar(level["level"+str(ll[0])], 17+dpBG,dl) == " ":
				Animat.setFalling(animat)
				Animat.fall(animat)
			if Background.getChar(level["level"+str(ll[1])], dpBG-82, dl) == "_":			#Gere maintien sur platforme basse
				Animat.resetOnUpperPlatform(animat)
			elif Background.getChar(level["level"+str(ll[0])], 17+dpBG, dl) == "_":
				Animat.resetOnUpperPlatform(animat)


		if ay == 12:
			if dpBG >=82:
				if Background.getChar(level["level"+str(ll[1])], dpBG-82, ul) == "_" and Animat.getFlyingMax(animat) == True: #Gere maintien sur la platforme haute
					Animat.setOnUpperPlatform(animat)
					Animat.resetFlying(animat)
					Animat.onUpperPlatform(animat)
				if Background.getChar(level["level"+str(ll[1])], dpBG-82,ul) == " " and Animat.getFlyingMax(animat) == True: #Gere chute sur la plateforme haute
					Animat.resetOnUpperPlatform(animat)
					Animat.setFlying(animat)
					Animat.setFlyingMax(animat)
					Animat.jump(animat)	
			
			#2eme Niveau en cours d'affichage
			
			elif Background.getChar(level["level"+str(ll[0])], 17+dpBG, ul)== "_" and Animat.getFlyingMax(animat) == True :# Gere maintien sur la platforme haute
				Animat.setOnUpperPlatform(animat)
				Animat.resetFlying(animat)
				Animat.onUpperPlatform(animat)
			elif Background.getChar(level["level"+str(ll[0])], 17+dpBG, ul) == " " and Animat.getFlyingMax(animat)==True: #Gere chute plateforme haute
				Animat.resetOnUpperPlatform(animat)
				Animat.setFlying(animat)
				Animat.setFlyingMax(animat)
				Animat.jump(animat)	
		if ay < 0 :																	#Chute = Fin du jeu
			if Menu.getSet(gameOver) == False and Menu.getSet(score) == False:
				a = raw_input("Nom du joueur: ")
				if not a :
					a = "Unknown"
				Menu.score(Animat.getScore(animat),a,score)
				Menu.setSet(gameOver)
	
	
	

	
def isData():
	return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])
	
def interact():
	if isData():
			touche = sys.stdin.read(1)
			if touche == '\x1B':				#Quitter le jeu
				quitGame()
			if touche == ' ':					#Saut
				Animat.setFlying(animat)
			if touche == 'd':					#Attaque
				if Animat.getAttack(animat) == False:
					Animat.setAttY(animat)
					Animat.setAttack(animat)
			else:
				if Menu.getSet(intro) == False and Menu.getSet(homeScreen) == True:
					Menu.setSet(intro)
					Menu.resetSet(homeScreen)
				elif Menu.getSet(intro) == True and Menu.getSet(homeScreen) == False:
					Menu.resetSet(intro)	
				elif Menu.getSet(intro) == False and Menu.getSet(homeScreen) == False and Menu.getSet(gameOver) == True and Menu.getSet(score) == False:
					Menu.setSet(score)
					Menu.resetSet(gameOver)
				elif Menu.getSet(gameOver) == False and Menu.getSet(score) == True:
					init()
					run()
def show():
	sys.stdout.write("\033[2J")
	sys.stdout.write("\033[40m")
	if Menu.getSet(score) == False and Menu.getSet(gameOver) == False:
		if Menu.getSet(homeScreen) == True and Menu.getSet(intro) == False:
			Menu.show(homeScreen)
		if Menu.getSet(homeScreen) == False and Menu.getSet(intro) == True:
			Menu.show(intro)
		if Menu.getSet(homeScreen)==False and Menu.getSet(intro) == False :		
			sys.stdout.write("\033[2J")
			sys.stdout.write("\033[40m")
			Background.show(building["building"+str(bl[0])], dpBG,False)
			Background.show(building["building"+str(bl[1])], dpBG,True)
			Background.show(level["level"+str(ll[0])], dpBG,False)
			Background.show(level["level"+str(ll[1])], dpBG,True)
			Animat.show(animat,dpEn)
			Animat.show(ennemy,dpEn)
			sys.stdout.write("\033[40;31m")
			sys.stdout.write("\033[1;1H\n")
	if Menu.getSet(gameOver) == True:
		sys.stdout.write("\033[2J")
		sys.stdout.write("\033[40;33m")
		Menu.show(gameOver)
		Menu.show(score)
		while not isData():
			time.sleep(0.05)

		
	
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
run()
quitGame()
	
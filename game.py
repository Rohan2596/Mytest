import pygame,sys
from pygame.locals import *
import time
##Adding the libraries 
pygame.init()#initialize the pygame
gameDisplay =pygame.display.set_mode((800,600))#setting the size of display screen
pygame.display.set_caption('A bit Racey')#adding title to  display screen
black =(0,0,0)#definig the RBG colors using 
white=(255,255,255)
clock =pygame.time.Clock()#to track the time in game
crashed =False
carImg =pygame.image.load('racecar.png') #loading the car image into the display screen

def car(x,y):#defining car image and size
	gameDisplay.blit(carImg,(x,y))
x=(800*0.45)
y=(600*0.8)
#
x_change=0
car_speed=0
while not crashed:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			crashed =True
		 if event.type == pygame.KEYDOWN:
		 	if event.key == pygame.K_LEFT:
		 		x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
        	if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

	x +=x_change		#print(event)
	gameDisplay.fill(white)
	car(x,y)		
	pygame.display.update()
	clock.tick(60)
pygame.quit()#closing the pygame library
quit()# closing whole

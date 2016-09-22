import sys #we will need the sys so the user can be able to quit
import pygame #the game
from hero import Hero #bring in the hero class with all its methods


#set up the main core function
def run_game():
	pygame.init() #initialize all the pygame modules
	screen = pygame.display.set_mode((1000,800)) # set the screen size with set_mode
	pygame.display.set_caption("Monster Attack") #set the message on the status bar

	bg_color = (82,111,53) #green grass color

	hero = Hero(screen) #set a variable equal to the class and pass it the screen

	while 1: #runt this loop forever
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		#fill the background with our green
		screen.fill(bg_color)
		hero.draw_me() #call the draw method and put the hero on the screen
		pygame.display.flip()
	

run_game() #start the game

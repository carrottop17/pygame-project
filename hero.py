import pygame

class Hero(object):
	def __init__(self, screen):
		self.screen = screen #give the hero the ability to control the screen

		# Load the hero image, get its rect
		self.image = pygame.image.load('images/robot.png')
		self.rect = self.image.get_rect() #pygame makes gives us get_rect on any object so we can get
		self.screen_rect = screen.get_rect() # assign a var so the hero class knows how big

		self.rect.centerx = self.screen_rect.centerx #this will put the middle of the hero at the middle of the screen
		self.rect.bottom = self.screen_rect.bottom #this will put our hero "bottom" at the bottom of the screen
		#not self.rect.center because we want the bottom on bottom, not the center

		self.moving_right = False #setup movement booleans
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

		# Add update to the hero class to keep all the hero updates in the hero class
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += 10 #Move the hero to the right
		elif self.moving_left and self.rect.left > self.screen_rect.left:
			self.rect.centerx -= 10 #Move the hero to the right
		# elif self.moving_up and self.rect.up > self.screen_rect.up:
		# 	self.rect.centerx += 10 #Move the hero to the right
		# elif self.moving_down and self.rect.down > self.screen_rect.down:
		# 	self.rect.centerx -= 10 #Move the hero to the right	

	def draw_me(self):
		self.screen.blit(self.image, self.rect)#draw the surface, the image, the where
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from AsteroidField import AsteroidField
from shot import Shot

def main():
    #initialize pygame, create the screen and clock
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #create groups for the game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #add group names as a static variable for Player class and initialize the player object 
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #add groups to Asteroid and Asteroid Field classes and create Asteroid Field
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    #create the game loop and allow the player to quit via the X button on the window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #fill the screen with black. update objects in updatable group, draw objects in the drawable group
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.checkCollision(bullet):
                    asteroid.split()
                    bullet.kill()
            if asteroid.checkCollision(player):
                sys.exit("Game over!")
        for object in drawable:
            object.draw(screen)
        
        #take all the changes from the previous block and update the screen to reflect these changes
        pygame.display.flip()

        #limit framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

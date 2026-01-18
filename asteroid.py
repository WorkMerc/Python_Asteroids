import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        
        new_angles = random.uniform(20, 50)

        new_asteroid_vector1 = self.velocity.rotate(new_angles)
        new_asteroid_vector2 = self.velocity.rotate(-new_angles)
        
        new_asteroid_radii = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid = Asteroid(self.position.x, self.position.y, new_asteroid_radii)
        asteroid.velocity = new_asteroid_vector1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_asteroid_radii)
        asteroid.velocity = new_asteroid_vector2* 1.2
        


            

         
        
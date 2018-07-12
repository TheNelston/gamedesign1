import pygame
import time
pygame.init()
pygame.display.set_mode((1,1))
pygame.mixer.music.load("thisissosad.mp3")
pygame.mixer.music.play()
time.sleep(3.0)
pygame.mixer.music.load("okay.mp3")
pygame.mixer.music.play()
time.sleep(1.5)
pygame.mixer.music.load("despacito.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()
clock = pygame.time.Clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
    pygame.event.poll()
    clock.tick(10)
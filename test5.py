import copy
import pygame
import time
class unit(object):
	hp = 50
	mark = "x"
	cost = 25
	dmg = 25
class Unithpdmg:	
	hpdmg = [unit.hp,unit.dmg]
properties = [100]
l = []
m = []
n = int(input("How many units?"))
for i in range(1,n+1):
	l.append("Unit {}".format(i))
for units in l:
	m.append(copy.copy(Unithpdmg.hpdmg))
print(m)
w = (int(input("Which unit would you like to attack?"))-1)
((m[w])[0]) -= 50
print("ATTACK!!!")
time.sleep(0.1)
pygame.init()
pygame.display.set_mode((1,1))
pygame.mixer.music.load("leroy.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()
clock = pygame.time.Clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
    pygame.event.poll()
    clock.tick(10)
for units in m:
	if units[0] <= unit.hp/2:
		units[1]= unit.dmg//2
for units in m:
	if units[0] <= 0:
		print("A unit died!")
		m.remove(units)
		time.sleep(0.1)
		pygame.display.set_mode((1,1))
		pygame.mixer.music.load("oof.mp3")
		pygame.mixer.music.play()
		clock = pygame.time.Clock()
		clock.tick(10)
		while pygame.mixer.music.get_busy():
		    pygame.event.poll()
		    clock.tick(10)
print(m)
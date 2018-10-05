import pygame as pg
from random import randint,random
import time
import math


anim_done = False ## set True to skip animation
pg.init()

screen_width = 500
screen_height = 300
line_thickness = 50
separation = 50
rate =60

bg_color = (126,126,126)

screen = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption("phi_mot_sim")

clock = pg.time.Clock()
# -------- Main Program Loop -----------
previousmillis = time.time()
colors = [ (255,255,255), (0,0,0)]
print(f'delay: {rate}')

while not anim_done: 
# --- Main event loop
    running = False
    for event in pg.event.get(): # User did something 
        if pg.event.EventType == pg.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if (pg.key.get_pressed()[pg.K_UP] != 0 ):
            rate += 1
            print(f'delay: {rate}')
        if (pg.key.get_pressed()[pg.K_DOWN] != 0  and rate > 0):
            rate -= 1
            print(f'delay: {rate}')
        if (pg.key.get_pressed()[pg.K_RETURN ] != 0 ):
            running = True
        if (pg.key.get_pressed()[pg.K_LEFT] != 0 and separation > 0):
            separation -= 1
            print(f'bar separation: {separation}')
        if (pg.key.get_pressed()[pg.K_RIGHT] != 0 ):
            separation += 1
            print(f'bar separation: {separation}')
            
    
    screen.fill(bg_color)
    pg.draw.line(screen, colors[1], ((int(screen_width/2 - line_thickness/2-separation)), 0), ((int(screen_width/2 - line_thickness/2-separation)), screen_height)  , line_thickness)
    pg.draw.line(screen, colors[1], (int(screen_width/2 + line_thickness/2+ separation), 0), (int(screen_width/2 + line_thickness/2+ separation), screen_height), line_thickness)
    pg.display.flip()
    
    if running:
        screen.fill(bg_color)
        pg.draw.line(screen, colors[0], ((int(screen_width/2 - line_thickness/2-separation)), 0), ((int(screen_width/2 - line_thickness/2-separation)), screen_height)  , line_thickness)
        pg.draw.line(screen, colors[1], (int(screen_width/2 + line_thickness/2+ separation), 0), (int(screen_width/2 + line_thickness/2+ separation), screen_height), line_thickness)
        pg.display.flip()

        pg.time.delay(rate)
        colors = colors[::-1]

        screen.fill(bg_color)
        pg.draw.line(screen, colors[0], ((int(screen_width/2 - line_thickness/2-separation)), 0), ((int(screen_width/2 - line_thickness/2-separation)), screen_height)  , line_thickness)
        pg.draw.line(screen, colors[1], (int(screen_width/2 + line_thickness/2+ separation), 0), (int(screen_width/2 + line_thickness/2+ separation), screen_height), line_thickness)
        pg.display.flip()
        pg.time.delay(rate)
       
        colors = colors[::-1]
        
    clock.tick()
     
pg.quit()


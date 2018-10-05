import pygame as pg
from random import randint,random
import time
import math
from pymunk.vec2d import Vec2d


anim_done = False ## set True to skip animation
pg.init()

screen_width = 500
screen_height = 300
line_thickness = 10
separation = 30
rate = 10
bg_color = (255,255,255)

screen = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption("phi_mot_sim")

clock = pg.time.Clock()
# -------- Main Program Loop -----------
previousmillis = time.time()
colors = [(0,0,0), (255,255,255)]

while not anim_done: 
# --- Main event loop
    print(rate)
    for event in pg.event.get(): # User did something 
        if pg.event.EventType == pg.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if (pg.key.get_pressed()[pg.K_UP] != 0 ):
            rate += 1
        if (pg.key.get_pressed()[pg.K_DOWN] != 0 ):
            rate -= 1
            
# --- Game logic should go here
    prev_t=time.time()
    
 # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command
    
    screen.fill(bg_color)

    pg.draw.line(screen, colors[0], ((int(screen_width/2 - line_thickness/2-separation)), 0), ((int(screen_width/2 - line_thickness/2-separation)), screen_height)  , line_thickness)
    pg.draw.line(screen, colors[1], (int(screen_width/2 + line_thickness/2+ separation), 0), (int(screen_width/2 + line_thickness/2+ separation), screen_height), line_thickness)
    
    pg.display.flip()

    colors = colors[::-1]        
    clock.tick(rate)
    
pg.quit()


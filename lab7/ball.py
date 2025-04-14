import pygame 

pygame.init()

width , height = 500 , 500
screen = pygame.display.set_mode((width , height))
pygame.display.set_caption('gumball')

red = (255 , 0 , 0)
white = (255 , 255 ,255)
running = True

x_axis = 250 
y_axis = 250 
r = 25 
spd = 20



while running:
    screen.fill(white)
    pygame.draw.circle(screen , red  , (x_axis , y_axis) , r )

    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y_axis - spd >= r:
                    y_axis -= spd
            elif event.key == pygame.K_DOWN:
                if y_axis + spd <= height - r:
                    y_axis += spd 
            elif event.key == pygame.K_LEFT:
                if x_axis - spd >= r:
                    x_axis -= spd
            elif event.key == pygame.K_RIGHT:
                if x_axis + spd <= width - r:
                    x_axis += spd
   



pygame.quit()

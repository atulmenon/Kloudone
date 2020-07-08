import pygame
height = 400
width = 400
win = pygame.display.set_mode((height,width))
pygame.display.set_caption("Chess Board by Atul Menon")
x = 50
y = 50
black = (0,0,0)
white = (255,255,255)
for i in range(0,400,50):
    for j in range(0,400,50):
        #pygame.time.delay(100)
        if i%20==0:
            pygame.draw.rect(win,white,(i,j*2,x,y))
            pygame.draw.rect(win,black,((i),(j+25)*2,x,y))
            pygame.display.update()
        else:
            pygame.draw.rect(win, black, (i, j * 2, x, y))
            pygame.draw.rect(win, white, ((i), (j + 25) * 2, x, y))
            pygame.display.update()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
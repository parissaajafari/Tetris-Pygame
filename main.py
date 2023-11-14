from numpy import block
import pygame
import sys
pygame.init()

block_size = 30

window_size = (800, 650)
pygame.display.set_caption("TetrisProject")
window = pygame.display.set_mode(window_size)
#ba tabe set mode ma mitunim panjare besaim


#for i in range(20):
#    print("this is y",i*block_size)
#    for j in range(10):
#        pygame.draw.rect(window, (186, 85, 211), ((j * block_size, i * block_size), (block_size, block_size)), 1)
#        print("this is x:", j*block_size)
#    print()
x=0
y=0

isGameRunning = True
while isGameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRunning = False
            pygame.quit()
            sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    X += 30




#jadvale tetris
    for i in range(20):
        for j in range(10):
            pygame.draw.rect(window, (186, 85, 211), ((j*block_size, i*block_size), (block_size, block_size)), 1)

    pygame.draw.rect(window,(0, 250, 154),((x,y),(block_size,block_size)),0)

    pygame.display.update()
    # pygame.display.flip() inam hast vali update behtare
    #display ro bezarim akhare halghe while ke harchi neveshtim akharesh display kone

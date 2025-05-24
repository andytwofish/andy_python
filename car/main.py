# 先用這個命令安裝
# python -m pip install --upgrade pip
# pip install pygame
import pygame

class game:
    def __init__(self):
        pass
        
    def start(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    print("quit")
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        print( "Left Key")
                    elif event.key == pygame.K_RIGHT:
                        print( "Right Key")
                    elif event.key == pygame.K_SPACE:
                        print("Space Key")
                    
            screen.fill((255, 255, 255))  
            
            self.mainLoop()
            
            pygame.display.flip()       # 更新畫面
            clock.tick(30)  

    def mainLoop(self):
        pygame.draw.rect(screen, (0, 0, 255), (100, 100, 150, 80))

pygame.init()
pygame.display.set_caption("移動方塊") 
screen = pygame.display.set_mode((600, 800))  
game().start()
# 先用這個命令安裝
# python -m pip install --upgrade pip
# pip install pygame
import pygame
pygame.init()
import math
from class2D import Class2D, Image2D
from draw_tool import gameContext, DrawTool

class Game:
    def __init__(self):
        self.BookStartX = 10 
        self.BookStartY = 200  
        self.BookTimeX = 300 
        self.BookTimeY = 40
        self.BookBoxX = 100 
        self.BookBoxY = 150    
        self.GameStartX = 410 
        self.GameStartY = 200  
        self.GameTimeX = 700 
        self.GameTimeY = 40
        self.GameBoxX = 500 
        self.GameBoxY = 150      
    def start(self) -> None : #開始執行
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    print(f"{x}, {y}")
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
                    
            gameContext.screen.fill((255, 255, 255))  
            
            self.mainLoop()
            
            pygame.display.flip()       # 更新畫面
            clock.tick(15)  

    def mainLoop(self):
        font = pygame.font.SysFont("Microsoft JhengHei", 25)
        #直線
        
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.BookStartX, self.BookStartY), (self.BookStartX+60, self.BookStartY), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.BookStartX+60, self.BookStartY), (self.BookStartX+60, self.BookStartY+100), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.BookStartX+60, self.BookStartY+100), (self.BookStartX, self.BookStartY+100), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.BookStartX, self.BookStartY+100), (self.BookStartX, self.BookStartY), 2)
        text_surface = font.render("Start", True, (0, 0, 0)) 
        gameContext.screen.blit(text_surface, (self.BookStartX+5, self.BookStartY))  
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.BookTimeX, self.BookTimeY), (self.BookTimeX+80, self.BookTimeY), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.BookTimeX+80, self.BookTimeY), (self.BookTimeX+80, self.BookTimeY+40), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.BookTimeX+80, self.BookTimeY+40), (self.BookTimeX, self.BookTimeY+40), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.BookTimeX, self.BookTimeY+40), (self.BookTimeX, self.BookTimeY), 2)
        text_surface = font.render("Time", True, (0, 0, 0)) 
        gameContext.screen.blit(text_surface, (self.BookTimeX+5, self.BookTimeY))  
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.BookBoxX, self.BookBoxY), (self.BookBoxX+250, self.BookBoxY), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.BookBoxX+250, self.BookBoxY), (self.BookBoxX+250, self.BookBoxY+300), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.BookBoxX+250, self.BookBoxY+300), (self.BookBoxX, self.BookBoxY+300), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.BookBoxX, self.BookBoxY+300), (self.BookBoxX, self.BookBoxY), 2)
        text_surface = font.render("Time", True, (0, 0, 0)) 
        gameContext.screen.blit(text_surface, (self.BookBoxX+5, self.BookBoxY))  
        
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.GameStartX, self.GameStartY), (self.GameStartX+60, self.GameStartY), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.GameStartX+60, self.GameStartY), (self.GameStartX+60, self.GameStartY+100), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.GameStartX+60, self.GameStartY+100), (self.GameStartX, self.GameStartY+100), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.GameStartX, self.GameStartY+100), (self.GameStartX, self.GameStartY), 2)
        text_surface = font.render("Start", True, (0, 0, 0)) 
        gameContext.screen.blit(text_surface, (self.GameStartX+5, self.GameStartY))  
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.GameTimeX, self.GameTimeY), (self.GameTimeX+80, self.GameTimeY), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.GameTimeX+80, self.GameTimeY), (self.GameTimeX+80, self.GameTimeY+40), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.GameTimeX+80, self.GameTimeY+40), (self.GameTimeX, self.GameTimeY+40), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.GameTimeX, self.GameTimeY+40), (self.GameTimeX, self.GameTimeY), 2)
        text_surface = font.render("Time", True, (0, 0, 0)) 
        gameContext.screen.blit(text_surface, (self.GameTimeX+5, self.GameTimeY))  
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.GameBoxX, self.GameBoxY), (self.GameBoxX+250, self.GameBoxY), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.GameBoxX+250, self.GameBoxY), (self.GameBoxX+250, self.GameBoxY+300), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.GameBoxX+250, self.GameBoxY+300), (self.GameBoxX, self.GameBoxY+300), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.GameBoxX, self.GameBoxY+300), (self.GameBoxX, self.GameBoxY), 2)
        text_surface = font.render("Time", True, (0, 0, 0)) 
        gameContext.screen.blit(text_surface, (self.GameBoxX+5, self.GameBoxY)) 
        
        text_surface = font.render("已累積時間", True, (0, 0, 0)) 
        gameContext.screen.blit(text_surface, (140, 40))  
       


gameContext.create( 800, 600, "測試視窗" )
Game().start()
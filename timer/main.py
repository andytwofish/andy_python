# 先用這個命令安裝
# python -m pip install --upgrade pip
# pip install pygame
import pygame
pygame.init()
import math
from class2D import Class2D, Image2D
from draw_tool import gameContext, DrawTool
from time_list import TimeList

class Game:
    def __init__(self):
        self.timeList1 = TimeList(0,0)  
        self.timeList2 = TimeList(400,0) 
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
        self.timeList1.mainLoop()
        self.timeList2.mainLoop()


gameContext.create( 800, 600, "測試視窗" )
Game().start()
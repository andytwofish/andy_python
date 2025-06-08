# 先用這個命令安裝
# python -m pip install --upgrade pip
# pip install pygame
import pygame
import math
from class2D import Class2D
from draw_tool import gameContext, DrawTool

class Game:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.myCar = MyCar(300, 300, 50, 50, 30)
        
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
                        self.x-=1
                        print( "Left Key")
                    elif event.key == pygame.K_RIGHT:
                        self.x+=1
                        print( "Right Key")
                    elif event.key == pygame.K_SPACE:
                        print("Space Key")
                    
            gameContext.screen.fill((255, 255, 255))  
            
            self.mainLoop()
            
            pygame.display.flip()       # 更新畫面
            clock.tick(15)  

    def mainLoop(self):
        #距形
        pygame.draw.rect(gameContext.screen, (0, 0, 255), (self.x, self.y, 150, 80))
        #直線
        pygame.draw.line(gameContext.screen, (0, 255, 0), (300, 100), (300, 500), 5)
        pygame.draw.line(gameContext.screen, (0, 255, 0), (100, 300), (500, 300), 5)
        
        #車子
        self.myCar.forward(1)
        self.myCar.draw()
        
class MyCar(Class2D):
    def __init__(self, x:int=0, y:int=0, width:int=10, height:int=10, rotation:int=0 ):
        super().__init__(x, y, width, height, rotation)
        self.img = pygame.transform.scale(pygame.image.load("car/images/transport.png") , (self.width,self.height))
        
    def draw(self):
        DrawTool.drawImg( self.img, self.x, self.y, self.rotation )


gameContext.create( 800, 600, "測試視窗" )
Game().start()
# 先用這個命令安裝
# python -m pip install --upgrade pip
# pip install pygame
import pygame
import math
from class2D import Class2D
from draw_tool import gameContext, DrawTool

class Game:
    def __init__(self):
        self.myCar = MyCar( 50, 50 )
        self.myCar.update_pose( 20, 20, 135 )
        
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
        #距形
        pygame.draw.rect(gameContext.screen, (0, 0, 255), (50, 50, 150, 80))
        #直線
        pygame.draw.line(gameContext.screen, (0, 255, 0), (300, 100), (300, 500), 5)
        pygame.draw.line(gameContext.screen, (0, 255, 0), (100, 300), (500, 300), 5)
        
        #車子
        self.myCar.forward(1)
        self.myCar.draw()
        
class MyCar(Class2D):
    def __init__(self, width:int=10, height:int=10 ):
        super().__init__( width, height )
        self.img = pygame.transform.scale(pygame.image.load("car/images/transport.png") , (self.width,self.height))
        
    def draw(self):
        DrawTool.drawImg( self.img, self.x, self.y, self.rotation )


gameContext.create( 800, 600, "測試視窗" )
Game().start()
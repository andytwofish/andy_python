import math 
import pygame
from draw_tool import gameContext


class Class2D:
    def __init__(self, width:int=10, height:int=10 ):
        self.width:int = width
        self.height:int = height
        
    def update_pose( self, x:int, y:int, rotation:int ):
        self.x = x
        self.y = y
        self.rotation = rotation
        # 1. 建立一個透明 Surface 當作臨時矩形
        temp_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        temp_surface.fill((255,0,0))

        # 2. 旋轉
        self.rotated_surface = pygame.transform.rotate(temp_surface, -rotation)  # 注意是負角度

        # 3. 把旋轉後的中心點對齊到你指定的中心 (x, y)
        self.rotated_rect = self.rotated_surface.get_rect(center=(x, y))

    def draw(self):
        gameContext.screen.blit(self.rotated_surface, self.rotated_rect.topleft)        

    def forward(self, distance=1):
        rad = math.radians(self.rotation)
        x = self.x + distance * math.sin(rad)
        y = self.y - distance * math.cos(rad)
        self.update_pose(x, y, self.rotation )
        
    def colliderect( self, otherClass2D):
        return self.rotated_rect.colliderect(otherClass2D.rotated_rect)
        
class Image2D(Class2D):
    def __init__(self, img_file_name:str, width:int=10, height:int=10 ):
        super().__init__( width, height )
        loadImg = pygame.image.load(img_file_name) 
        self.img = pygame.transform.scale(loadImg, (self.width,self.height) )
        
    def update_pose( self, x:int, y:int, rotation:int ):
        self.x = x
        self.y = y
        self.rotation = rotation
        self.original_rect = self.img.get_rect(center=(self.x, self.y))
        self.rotated_image = pygame.transform.rotate(self.img, -rotation)
        self.rotated_rect = self.rotated_image.get_rect(center=self.original_rect.center)
        
    def draw(self):
        gameContext.screen.blit(self.rotated_image, self.rotated_rect.topleft)
        

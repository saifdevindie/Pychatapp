import random, pygame


class biney:

    def __init__(self):
        
        self.x = random.randint(0,640)
        self.y = random.randint(0,600)
        self.bin = random.choice(["0","1"])
        self.font = pygame.font.SysFont("Arial",14,True)
        #self.font_size = self.font.size(str(random.randint(10,25),random.randint(10,25)))
        self.speed = random.randint(4,10)


class Label:
    def __init__(self):

        self.font = pygame.font.SysFont("Arial",15,True)
        self.field = ""
        self.active = False
        self.rect = pygame.Rect(0,560,640,40)
        self.colors = [(69,69,69),(255,255,0)]
        self.color = 0
        
    def update(self,surf):

        pygame.draw.rect(surf,self.colors[0],self.rect)
        pygame.draw.rect(surf,self.colors[self.color],self.rect,4)
        self.text_render(self.field,surf)
                       
    def text_render(self,text,surf):
        
        text = self.font.render(str(text),10,(255,255,255))
        tr = text.get_rect(midright=self.rect.midright)
       
        surf.blit(text,(tr[0]-20,tr[1]))
                       
class MassegeBox:
    def __init__(self,y,text):
    
        self.y = y
        self.text = text
        self.rect = pygame.Rect(0,self.y,0,20)
        self.colors = [(105,105,100),(125,125,25)]
        self.user = 0
        self.font = pygame.font.SysFont("Arial",12,True)
        self.text_rect = 0
        
    def adjust(self):
        
        self.rect.width = self.text_rect.width + 2
        
    def text_render(self,surf):
        
        text = self.font.render(str(self.text),1,(255,255,255))
        tr = text.get_rect(center=self.rect.center)
        self.text_rect = tr
        #tr.center = self.rect.midleft
        surf.blit(text,tr)
        self.adjust()
    def rendering(self,surf):
        if self.rect.y > 20:
            pygame.draw.rect(surf,self.colors[self.user],self.rect)
            self.text_render(surf)
             # but main massg box on the right
            if self.user:
                self.rect.x = 20
                 
            else:
                self.rect.x = 600 - self.rect.width
                
            

import pygame
from network import Network
import random
from binery import biney,Label,MassegeBox
import select

def Massege_Manger(massegs,masg):
    for masg in massegs:
        masg.rect.y -= 25
    

def text_render(text,pos,color=(155,220,200)):
    global font,win
    text = font.render(str(text),1,color)
    tr = text.get_rect()
    tr.topright = pos
    win.blit(text,tr.center)

# Initalize The Game
pygame.init()
# Font Opject
font = pygame.font.SysFont("Arial",20,True)
# Screen Set Up
clock = pygame.time.Clock()
win = pygame.display.set_mode((640,600))
pygame.display.set_caption("Micro Chat")
n = Network()
logo = pygame.image.load("Logo/logo.png").convert_alpha()
Label = Label()
frame = 0
animation_data = []
chat_session_history = []

x = 0
chatActive = False
for i in range(5):
    animation_data.append((x,0))
    x += 32
ad = []
for f in animation_data:
    for i in range(5):
        ad.append(f)

run = True
sec_screen = False
biners = [biney() for b in range(30)]
massege_refresh = 0
new_massege_add = "watting"
while run:
    clock.tick(30)
    
    win.fill((42,42,42))
    #r = select.select([n.client],[],[],0.01)
    other_user = n.send(new_massege_add)
    
    if other_user == "watting" or other_user == "1" or other_user == "client_out":
        pass
    else:
        mb = MassegeBox(520,other_user)
        mb.user = 1
        if mb.text not in chat_session_history:
            chat_session_history.append(mb)
            Massege_Manger(chat_session_history,mb)
            
            new_massege_add = n.send("watting")
            print(new_massege_add)
      
        
##    if len(chat_session_history):
##        other_user = n.send(chat_session_history[-1].text)
##        mb = MassegeBox(520,other_user)
##        mb.user = 1
##        
##        if other_user != new_massege_add:
##            chat_session_history.append(mb)
##            Massege_Manger(chat_session_history,mb)
##            new_massege_add = mb.text
##            
##            print("i recived:",other_user, "sending:",chat_session_history[-1].text)
##        
    
    if chatActive:
        Label.update(win)
        Label.active = True
##    write = input("type somthing: ")
##    p2 = ""
##    if write:
##        print("Sending :", write)
##        
##        p2 = n.send(write)
##    if p2 != "":
##        print(n.masgs, ": ",p2)
   
    
    chatActive = True
    if 8 - pygame.time.get_ticks()%60000//1000> 0 and sec_screen and Label.active == False:
        text_render("WELLCOME MICRO ",[640/2,600 -360],color=(235,235,235))
        chatActive = False
        for b in biners:
            b.y += b.speed
            text_render(b.bin,[b.x,b.y],color=(155,255,220))
            if b.y > 600:
                b.y = 0
        
    if 6 - pygame.time.get_ticks()%60000//1000> 0 and Label.active == False:
        chatActive = False
        for b in biners:
            b.y += b.speed
            text_render(b.bin,[b.x,b.y],color=(155,255,220))
            if b.y > 600:
                b.y = 0
        text_render("Micro Server is Runing",[640/2,600 -260])
        if frame < len(ad) - 1:
            win.blit(logo,(300,300),(ad[frame][0],ad[frame][1],32,32))
        else:
            frame = 0
        frame += 1
    else:
        sec_screen = True
    # Chack The Events
    mouse_rect = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],4,6)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            n.send("client_out")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_rect.colliderect(Label.rect):
                if Label.color:
                    Label.color = 0
                else:
                    Label.color = 1
        
            else:
                Label.color = 0
        
            
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_RETURN:
                
                if Label.field != "":
                    mb = MassegeBox(520,Label.field)
                    mb.user = 0
                    Massege_Manger(chat_session_history,mb)
                    chat_session_history.append(mb)
                    new_massege_add = Label.field
                    Label.field = ""
                
                Label.field = Label.field[:-1]
                
                    
            if event.key == pygame.K_LSHIFT:
                pass
        if event.type == pygame.KEYDOWN:
        
            if Label.color:
                if event.key == pygame.K_BACKSPACE:
                    Label.field = Label.field[:-1]
                elif event.key != 13: # 13 is enter in keybord 
                    Label.field += event.unicode
    # just a wait few fps befor sending new massege
   
    
    
    for masge in chat_session_history:
        masge.rendering(win)
        
    pygame.display.update()
  

pygame.quit()



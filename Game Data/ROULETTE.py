import pygame
import random

width = 1125  
height = 750  
FPS = 300
    
b = [5,15,25,34,43,52,61,71,81,91,100,110,120,130,140,150,160,170,180,190,200,210,219,230,239,248,258,268,278,287,298,306,315,325,335,345,355]
a = [32,15,19,4,21,2,25,17,34,6,27,13,36,11,30,8,23,10,5,24,16,33,1,20,14,31,9,22,18,29,7,28,12,35,3,26,0]
pygame.init()
fpsclock = pygame.time.Clock()  
screen = pygame.display.set_mode((width, height))

image_intro = pygame.image.load(r'data\intro.jpg')
image_roulette = pygame.image.load(r'data\name.png')
image_arrow = pygame.image.load(r'data\arrow.png')
image_data = pygame.image.load(r'data\data.jpg')
image_wback = pygame.image.load(r'data\backwheel.jpg')
image_wheel = pygame.image.load(r'data\wheel.png')   
image_pointer = pygame.image.load(r'data\pointer.png')
image_win = pygame.image.load(r'data\win.jpg')
image_loose = pygame.image.load(r'data\loose.jpg')

font_navigate = pygame.font.SysFont('Cambria',20)
font_TYL = pygame.font.SysFont('Cambria',100)
font_roulette = pygame.font.SysFont('Cambria',115)
font_data = pygame.font.SysFont('Cambria',34)

def intro(naam,iamt,amt,lamt,wamt,bno,bamt,pamt):
  loop = True
  while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): 
            loop = False
            return False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            loop = data(naam,iamt,amt,lamt,wamt,bno,bamt,pamt) 
        
        else:
            screen.blit(image_intro,(0,0))   
            screen.blit(image_roulette,(250,320))
            text2 = font_navigate.render("Press ENTER to next page",True,(205,133,63))
            screen.blit(text2,(880,720))  
            pygame.display.update()  
            fpsclock.tick(FPS)         

def data(naam,iamt,amt,lamt,wamt,bno,bamt,pamt):
    n = True
    loop = True
    while loop:
     for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): 
            loop = False 
            return False         

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                n = False

            elif event.key == pygame.K_UP:
                n = True

            elif event.key == pygame.K_RETURN:
                loop = wheel(naam,iamt,amt,lamt,wamt,bno,bamt,pamt)

            elif event.key == pygame.K_SPACE:
              naam = naam + ' '

            elif event.key == pygame.K_BACKSPACE:
              if n:
                l = len(naam)
                naam = naam[:l-1]
              else:
                l2 = len(amt)
                amt = amt[:l2-1]  

            else:
              if n:
                naam = naam + pygame.key.name(event.key)    
                naam = naam.upper()
              else:
                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9 or event.key == pygame.K_0:
                   amt = amt + pygame.key.name(event.key)  
                   iamt = amt

        else:
            screen.blit(image_data,(0,0))
            text1 = font_TYL.render("ENTER",True,(139,54,38))
            text2 = font_TYL.render("DETAILS",True,(139,54,38))
            screen.blit(text1,(50,70))
            screen.blit(text2,(10,200))
            
            if n:
               screen.blit(image_arrow,(0,525))
            else:
               screen.blit(image_arrow,(0,605))

            text3 = font_navigate.render("Press ENTER to next page and Use arrow keys to switch fields",True,(205,133,63))
            screen.blit(text3,(550,720))
            text = font_data.render("NAME:- " + naam ,True,(126,192,238))
            screen.blit(text,(60,530))
            text2 = font_data.render("AMOUNT:- " + amt ,True,(126,192,238))
            screen.blit(text2,(60,610))
            pygame.display.update()
            fpsclock.tick(FPS)    
        
def wheel(naam,iamt,amt,lamt,wamt,bno,bamt,pamt):
   screen.fill((255,255,255))
   loop = True
   loop1 = True
   n = True
   if amt == "":
      while loop:   
        for event in pygame.event.get():
          if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): 
            loop = False
            return False

          elif event.type == pygame.KEYDOWN:
           if event.key == pygame.K_RETURN: 
              loop = data(naam,iamt,amt,lamt,wamt,bno,bamt,pamt)
              return False
           
          else:
              screen.blit(image_data, (0,0)) 
              text1 = font_TYL.render("ENTER",True,(139,54,38))
              text2 = font_TYL.render("DETAILS",True,(139,54,38))
              screen.blit(text1,(50,70))
              screen.blit(text2,(10,200))
              text = font_navigate.render("Amount could not be 0 so enter some amount again...(Enter to continue)",True,(220,133,63))
              screen.blit(text , (30 , 720))
              pygame.display.update()
   while loop1:
       for event1 in pygame.event.get():
          if event1.type == pygame.QUIT or (event1.type == pygame.KEYDOWN and event1.key == pygame.K_ESCAPE): 
            loop1 = False
            return False
     
          elif event1.type == pygame.KEYDOWN:
            if event1.key == pygame.K_DOWN:
                n = False

            elif event1.key == pygame.K_UP:
                n = True

            elif event1.key == pygame.K_RETURN:
                loop1 = wheelspin(naam,iamt,amt,lamt,wamt,bno,bamt,pamt)
                return False  

            elif event1.key == pygame.K_BACKSPACE:
              if n:
                l = len(bno)
                bno = bno[:l-1]
              else:
                l2 = len(bamt)
                bamt = bamt[:l2-1]  

            else:
              if n:
                if event1.key == pygame.K_1 or event1.key == pygame.K_2 or event1.key == pygame.K_3 or event1.key == pygame.K_4 or event1.key == pygame.K_5 or event1.key == pygame.K_6 or event1.key == pygame.K_7 or event1.key == pygame.K_8 or event1.key == pygame.K_9 or event1.key == pygame.K_0:
                  bno = bno + pygame.key.name(event1.key)    
              else:
                if event1.key == pygame.K_1 or event1.key == pygame.K_2 or event1.key == pygame.K_3 or event1.key == pygame.K_4 or event1.key == pygame.K_5 or event1.key == pygame.K_6 or event1.key == pygame.K_7 or event1.key == pygame.K_8 or event1.key == pygame.K_9 or event1.key == pygame.K_0:
                  bamt = bamt + pygame.key.name(event1.key)  
             
          else:
            screen.blit(image_wback,(0,0))
            screen.blit(image_pointer,(775,50))   

            if n:
               screen.blit(image_arrow,(0,515))
            else:
               screen.blit(image_arrow,(0,595))
            
            screen.blit(image_wheel, (533,103))
            text2 = font_TYL.render("TRY YOUR" ,True,(121, 3, 1))
            text3 = font_TYL.render("LUCK!" ,True,(121, 3, 1))
            screen.blit(text2,(60,80))
            screen.blit(text3,(60,180))
            text4 = font_navigate.render("(Get your amount 10 times or loose it)",True,(10,10,255))
            screen.blit(text4,(60,285))
            text = font_data.render("NAME:- " + naam ,True,(0, 100, 0))
            screen.blit(text,(60,360))
            text2 = font_data.render("TOTAL AMOUNT:- " + amt ,True,(0, 100, 0))
            screen.blit(text2,(60,440))
            text2 = font_data.render("BETTING NUMBER:- " + bno ,True,(0, 100, 0))
            screen.blit(text2,(60,520))
            text2 = font_data.render("BETTING AMOUNT:- " + bamt ,True,(0, 100, 0))
            screen.blit(text2,(60,600))
            text = font_navigate.render("Press ENTER to next page and Use arrow keys to switch fields",True,(205,133,63))
            screen.blit(text , (550,720))
            pygame.display.update()  
            fpsclock.tick(FPS)

def wheelspin(naam,iamt,amt,lamt,wamt,bno,bamt,pamt):           
    loop2 = True
    loop3 = True
    n = True
    pamt = amt
    angle = 1
    count = 2.5
    rangle = 123
    #choice = 7 
    choice = random.randint(0,36)

    for i in range (0,37):
     if a[i] == choice:
       rangle = b[i]
   
    if bamt=="" or int(bamt)>int(pamt) or int(bno)>36 or int(bno)<0:
      while loop3:   
        for event3 in pygame.event.get():
          if event3.type == pygame.QUIT or (event3.type == pygame.KEYDOWN and event3.key == pygame.K_ESCAPE): 
            loop3 = False
            return False

          elif event3.type == pygame.KEYDOWN:
           if event3.key == pygame.K_RETURN: 
              loop3 = wheel(naam,iamt,amt,lamt,wamt,bno,bamt,pamt)
              return False

          elif bamt=="":
            text = font_navigate.render("Invalid Betting Amount...(Enter to continue)",True,(205,133,63))
            screen.blit(text , (30 , height-30))
            pygame.display.update()

          else:
            if (int(bno)>36 or int(bno)<0):
              text = font_navigate.render("Invalid Betting Number...(Enter to continue)",True,(220,133,63))
              screen.blit(text , (30 , height-30))
              pygame.display.update()
            elif (int(bamt)>int(pamt)):
              text = font_navigate.render("Invalid Betting Amount...(Enter to continue)",True,(205,133,63))
              screen.blit(text , (30 , height-30))
              pygame.display.update() 

    while loop2:
     for event2 in pygame.event.get():
        if event2.type == pygame.QUIT or (event2.type == pygame.KEYDOWN and event2.key == pygame.K_ESCAPE): 
                loop2 = False 
                return False

        elif event2.type == pygame.KEYDOWN:
            if event2.key == pygame.K_RETURN:
              result(naam,iamt,amt,lamt,wamt,bno,bamt,pamt,choice)
              return False

        else:  
            screen.blit(image_wback,(0,0))
            screen.blit(image_pointer,(775,50))   

            if n:
               screen.blit(image_arrow,(0,515))
            else:
               screen.blit(image_arrow,(0,595))
               
            screen.blit(image_wheel , (533,103))
            text2 = font_TYL.render("TRY YOUR" ,True,(121, 3, 1))
            text3 = font_TYL.render("LUCK!" ,True,(121, 3, 1))
            screen.blit(text2,(60,80))
            screen.blit(text3,(60,180))
            text4 = font_navigate.render("(Get your amount 10 times or loose it)",True,(10,10,255))
            screen.blit(text4,(60,285))
            text = font_data.render("NAME:- " + naam ,True,(0, 100, 0))
            screen.blit(text,(60,360))
            text2 = font_data.render("TOTAL AMOUNT:- " + pamt ,True,(0, 100, 0))
            screen.blit(text2,(60,440))
            text2 = font_data.render("BETTING NUMBER:- " + bno ,True,(0, 100, 0))
            screen.blit(text2,(60,520))
            text2 = font_data.render("BETTING AMOUNT:- " + bamt ,True,(0, 100, 0))
            screen.blit(text2,(60,600))
            text = font_navigate.render("Press ENTER to view result...",True,(220,133,63))
            screen.blit(text , (30 , 720))           
            #text4 = font_navigate.render(str(choice),True,(205,133,63))
            #screen.blit(text4,(0,0))
            

     if count >0.2:
      if angle >= 360:
        angle = 1
        count -= 0.3
     else:
      if angle > rangle:
        angle = rangle

     angle +=count
     img = pygame.transform.rotate(image_wheel , angle)
     rect = img.get_rect()
     screen.blit(img , (800-rect.center[0] , 370-rect.center[1]))      

     pygame.display.update()
     fpsclock.tick(FPS)
   
def result(naam,iamt,amt,lamt,wamt,bno,bamt,pamt,choice):
    if int(bno) == choice:
      wamt = str(int(wamt) + 10*int(bamt))
      screen.blit(image_win,(0,0)) 
      amt = str(int(pamt) + 10*int(bamt))
    else:    
      lamt = str(int(lamt) + int(bamt))
      screen.blit(image_loose,(0,0))
      amt = str(int(pamt) - int(bamt))
              
    if choice == int(bno):
      text2 = font_TYL.render("YOU" ,True,(121, 3, 1))
      text3 = font_TYL.render("WIN" ,True,(121, 3, 1))
      screen.blit(text2,(400,30))
      screen.blit(text3,(640,30))
      text = font_data.render("NAME:- " + naam ,True,(0, 100, 0))
      screen.blit(text,(500,390))
      text2 = font_data.render("TOTAL AMOUNT:- " + iamt ,True,(0, 100, 0))
      screen.blit(text2,(500,450))
      text2 = font_data.render("BETTING NUMBER:- " + bno ,True,(0, 100, 0))
      screen.blit(text2,(500,510))
      text2 = font_data.render("WINNING NUMBER:- " + str(choice) ,True,(0, 100, 0))
      screen.blit(text2,(500,570))
      text2 = font_data.render("WINNING AMOUNT:- " + wamt ,True,(0, 100, 0))
      screen.blit(text2,(500,630))  
      text2 = font_data.render("REMAINING AMOUNT:- " + amt ,True,(0, 100, 0))
      screen.blit(text2,(500,690))
    else:
      text2 = font_TYL.render("YOU" ,True,(121, 3, 1))
      text3 = font_TYL.render("LOOSE" ,True,(121, 3, 1))
      screen.blit(text2,(450,80))
      screen.blit(text3,(400,180))
      text = font_data.render("NAME:- " + naam ,True,(0, 100, 0))
      screen.blit(text,(500,390))
      text2 = font_data.render("TOTAL AMOUNT:- " + iamt ,True,(0, 100, 0))
      screen.blit(text2,(500,450))
      text2 = font_data.render("BETTING NUMBER:- " + bno ,True,(0, 100, 0))
      screen.blit(text2,(500,510))
      text2 = font_data.render("WINNING NUMBER:- " + str(choice) ,True,(0, 100, 0))
      screen.blit(text2,(500,570))
      text2 = font_data.render("LOSING AMOUNT:- " + lamt ,True,(0, 100, 0))
      screen.blit(text2,(500,630))
      text2 = font_data.render("REMAINING AMOUNT:- " + amt ,True,(0, 100, 0))
      screen.blit(text2,(500,690))
    
    text = font_navigate.render("Do you want to play again (Y/N)",True,(221,3,1))
    screen.blit(text , (30 , height-30))       
    loop = True
    pygame.display.update()
    fpsclock.tick(FPS)
    while loop:
       for event in pygame.event.get():
          if event.type == pygame.QUIT:
            loop = False
            return False

          elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                wheel(naam,iamt,amt,lamt,wamt,bno,bamt,pamt)
                return False

            if (event.key == pygame.K_n or event.key== pygame.K_ESCAPE):
                loop = False    
                return False               

    pygame.display.update()
    fpsclock.tick(FPS)

if __name__ == "__main__": 
    naam = "" 
    iamt = ""
    amt = "" 
    lamt = "0"
    wamt = "0"
    bno = ""
    bamt = ""
    pamt = ""
    intro(naam,iamt,amt,lamt,wamt,bno,bamt,pamt) 
    pygame.quit()
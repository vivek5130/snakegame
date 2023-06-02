#Add pause
#change coordintes so that score is in its own unique position
#add lifeline
#press r to reset high score
#handle lr and updown while length is one


import pygame
import random
import os
import time
pygame.init()
pygame.mixer.init()
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
clock = pygame.time.Clock()
swidth = 700
sheight = 400
fps = 50

bgimage = pygame.image.load("bgimg.png")

bgimage = pygame.transform.scale(bgimage, (240,240))
# grimg = pygame.image.load('greimg.jpg')
# grimg = pygame.transform.scale(grimg
# , (swidth, sheight))
font = pygame.font.SysFont('Creepster', 55)

def textscreen(text ,color, x,y):
  screentext = font.render(text,True,color)
  gameWindow.blit(screentext,[x,y])

def plotsnake(gameWindow, color,lst,s):
  for a,b in lst:
    pygame.draw.rect(gameWindow,color, [a,b,s,s])

pygame.display.set_caption("Snake Game by Vivek")
gameWindow = pygame.display.set_mode((swidth, sheight))

def welcome():
    exit_game = False
    wel = pygame.mixer.music.load("tunetank.com_3628_feel-good_by_99instrumentals.mp3")
    pygame.mixer.music.play()
    while not exit_game:
        gameWindow.fill((10,210,20))
        gameWindow.blit(bgimage,(220,180))
        textscreen("Snake Game", red, 200, 100)
        textscreen("Press Space bar to continue", red, 120, 150)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:   
                    time.sleep(0.2)
                    wel = pygame.mixer.music.load("tunetank.com_5685_comeback_by_audiotime.mp3")
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(fps) 

def gameloop():
  game_over  =False
  exit_game = False
  init_velocity = 5
  x = 50
  y = 50
  vx = init_velocity
  vy = 0
  s = 15
  score = 0
  lst = []
  length = 1
  fps = 50
  hiscore = 0
  food_x = random.randint(20, swidth/2)
  food_y = random.randint(20, sheight/2)
  if (not os.path.exists("highscore.txt")):
    with open("highscore.txt",'w') as f:
        f.write("0")
  with open("highscore.txt","r") as f:
    hiscore = int(f.read())
      
  while not exit_game:
    if game_over:
      gameWindow.fill(white)
      
      textscreen("Game Over! Press Enter to continue", red,10,100)
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_RETURN:
                welcome()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                  vx = init_velocity
                  vy = 0
                if event.key == pygame.K_LEFT:
                  vx =  -init_velocity
                  vy = 0
                if event.key == pygame.K_UP:
                  vy = -init_velocity
                  vx = 0
                if event.key == pygame.K_DOWN:
                  vy =  init_velocity
                  vx = 0

        x = x + vx
        y = y + vy    
        if abs(x - food_x)<9 and abs(y-food_y) <9:
            score+=1
            # print("Your score is : ",score)
            food_x = random.randint(40, swidth/2)
            food_y = random.randint(40, sheight/2)
            length+=4
            if score> hiscore:
                hiscore = score
                with open("highscore.txt",'w') as f:
                    f.write(str(score))
                print(hiscore)

        #Fill should be within loop or else while updating the snake or food, the past position stays there itself
        gameWindow.fill(white)
        # gameWindow.blit(grimg, (0,0))

        textscreen("                 Score: " + str(score) + " Highscore: "+str(hiscore), red, 5, 5)
        head = []
        head.append(x)
        head.append(y)
        lst.append(head)
        pygame.draw.rect(gameWindow, red, [food_x, food_y,s,s])
        # pygame.draw.rect(gameWindow, black, [x,y,s,s])
        plotsnake(gameWindow, black,lst,s)
        time.sleep(0.028)
        if len(lst) > length:
          del lst[0]
        if x<0 or x>swidth or y<0 or y> sheight:
            pygame.mixer.music.load("081790_quotgame-overquot-evil-88883 (1).mp3")
            time.sleep(1)
            pygame.mixer.music.play()
            game_over = True
                        
        #   print("Game over")
        if head in lst[:-1]:
          pygame.mixer.music.load("081790_quotgame-overquot-evil-88883 (1).mp3")
          time.sleep(1)
          pygame.mixer.music.play()   
          game_over = True
          

    pygame.display.update()
    clock.tick(fps)
  pygame.quit()
  quit()

# gameloop()
welcome()
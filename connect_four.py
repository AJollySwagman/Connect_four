#this bot is degsined to play against another computer, and it assumes the oposition will not make a mistake.
import random
import pygame

clock = pygame.time.Clock()
pygame.init()

screen_width = 350
screen_height = 350
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('connect 4')

class sbot:



  def __init__(self, name,opp):
    #blank = 0, self = 1, enemy = 2
    self.board = [
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0]

    ]
    self.name = name
    self.opp=opp


  def findfour(self,board, name):
    # vertical
    #confirmed working
    if board[0][self.b] == name  and  board[1][self.b] == name and  board[2][self.b] == name and  board[3][self.b] == name:
      return True
    if board[4][self.b] == name  and  board[1][self.b] == name and  board[2][self.b] == name and  board[3][self.b] == name:
      return True
    if board[4][self.b] == name  and  board[5][self.b] == name and  board[2][self.b] == name and  board[3][self.b] == name:
      return True

    # diag down
    # confirmed working
    for self.l in range(4):
      try:
        if self.b-self.l > -1 and self.blev-self.l > -1:
          if board[self.blev-self.l][self.b-self.l] == name  and  board[(self.blev+1)-self.l][(self.b + 1) - self.l] == name and  board[(self.blev-self.l)+2][self.b+2-self.l] == name and  board[(self.blev-self.l)+3][self.b+3+-self.l] == name:
            return True
      except:

        pass


    # diag up
    #confirmed working

    for self.l in range(4):

      if self.b-3+self.l > -1 and self.blev - self.l > -1:

        try:
          if board[self.blev-self.l][self.b+self.l] == name  and  board[(self.blev+1)-self.l][(self.b - 1) + self.l] == name and  board[(self.blev-self.l)+2][self.b-2+self.l] == name and  board[(self.blev-self.l)+3][self.b-3+self.l] == name:

            return True
        except:
          pass

    #horizontal
    for self.l in range(4):
      try:
        if self.b-self.l > -1:
          if board[self.blev][self.b-self.l] == name  and  board[self.blev][(self.b + 1) - self.l] == name and  board[self.blev][self.b+2-self.l] == name and  board[self.blev][self.b+3-self.l] == name:
            return True
      except:
        pass

    return False

  def findthree(self, board, name):
    for self.dx in range(7):
      for self.dy in range(6):
        if board[self.dy][self.dx] != 0:
          continue
        self.threetestboard = [row[:] for row in board]
        #self.add(self.threetestboard, self.d, name)
        self.threetestboard[self.dy][self.dx] = name
        if self.findfour(self.threetestboard, name):
          return True

    return False
  
  def add(self,board,col,name):
    self.i=0
    while board[self.i][col]== 0:

      if self.i == 5:
        board[self.i][col]= name
        self.blev = self.i
        break

      if board[self.i + 1][col]!= 0:
        board[self.i][col]= name
        self.blev = self.i
        break
      self.i+=1
    return board

  def prioritycheck(self, board, col):
    #check enemy 3s
    for self.b in range(7):
      self.pritestboard = [row[:] for row in board]
  
      self.add(self.pritestboard,self.b,self.opp)
  
      if self.findfour(self.pritestboard,self.opp):
        return 2.5
    #check fillable twos
    for self.b in range(7):
      self.testboard = [row[:] for row in board]

      self.add(self.testboard, self.b, self.opp)

      filltwosum = 0
      tempblev = self.blev
      temptestboard = [row[:] for row in self.testboard]
      for self.j in range(7):

        self.testboard = [row[:] for row in temptestboard]

        self.add(self.testboard, self.j, self.opp)

        self.blev = tempblev
        if self.findfour(self.testboard,self.opp):
          filltwosum += 1


      if filltwosum > 1:
        return 3.5
    #check exposed 3s
    

    self.testboard = [row[:] for row in self.board]
    self.add(self.testboard, col, self.opp)
    self.add(self.testboard, col, self.name)
    if self.findfour(self.testboard,self.name):
      return 3.6

    #check enemy 3 step fillable 2s
    for aa in range(7):
      self.testboard = [row[:] for row in board]
      self.add(self.testboard, aa, self.opp)
      tempblev = self.blev
      for ab in range(7):
        self.abtestboard = [row[:] for row in self.testboard]
        self.add(self.abtestboard, ab, self.opp)
        filltwosum = 0
        for ac in range(7):
          self.actestboard = [row[:] for row in self.abtestboard]
          self.add(self.actestboard, ac, self.opp)
          self.b = aa
          self.blev = tempblev
          if self.findfour(self.actestboard,self.opp):
            filltwosum += 1
        if filltwosum > 1:
          return 4.5


    #check enemy unfillable twos
    for self.b in range(7):
      self.testboard = [row[:] for row in board]
      self.add(self.testboard, self.b, self.opp)

      if self.findthree(self.testboard,self.opp):
        return 5.4

    return 101


  
  def find(self):

    #BEGIN FIND SELF 3S
    for self.b in range(7):
      if self.b in self.banlist:
        continue

      self.testboard = [row[:] for row in self.board]

      self.add(self.testboard,self.b,self.name)

      if self.findfour(self.testboard,self.name):
        return self.b,1

    
    #BEGIN FIND ENEMY 3S
    for self.b in range(7):
      if self.b in self.banlist:
        continue
      self.testboard = [row[:] for row in self.board]

      self.add(self.testboard,self.b,self.opp)

      if self.findfour(self.testboard,self.opp):
        return self.b,2


    #BEGIN FIND self FILLABLE 2S
    #method: place one counter then look for fillable 3s. if there are 2 fillable 3s then block.
    for self.b in range(7):
      if self.b in self.banlist:
        continue
      self.testboard = [row[:] for row in self.board]

      self.add(self.testboard, self.b, self.name)
      
      filltwosum = 0
      tempblev = self.blev
      temptestboard = [row[:] for row in self.testboard]
      for self.j in range(7):

        self.testboard = [row[:] for row in temptestboard]
  
        self.add(self.testboard, self.j, self.name)
        
        self.blev = tempblev
        
        if self.findfour(self.testboard,self.name):
          filltwosum+=1


      if filltwosum > 1:
        return self.b,3
    #begin find self predicted fillable twos
    for self.aa in range(7):
      if self.aa in self.banlist:
        continue
      self.testboard = [row[:] for row in self.board]
      self.add(self.testboard,self. aa, self.name)
      tempblev = self.blev
      for self.ab in range(7):
        self.abtestboard = [row[:] for row in self.testboard]
        self.add(self.abtestboard,self. ab, self.name)
        if self.findfour(self.abtestboard,self.name):
          self.abtestboard[self.blev][self.ab] = self.opp

          for self.ac in range(7):
            self.actestboard = [row[:] for row in self.abtestboard]
            self.add(self.actestboard, self.ac, self.name)
            if self.findfour(self.actestboard,self.name):
              return self.aa,3


    #BEGIN FIND ENEMY FILLABLE 2S. 
    for self.b in range(7):
      if self.b in self.banlist:
        continue
      self.testboard = [row[:] for row in self.board]

      self.add(self.testboard, self.b, self.opp)

      filltwosum = 0
      tempblev = self.blev
      temptestboard = [row[:] for row in self.testboard]
      for self.j in range(7):

        self.testboard = [row[:] for row in temptestboard]

        self.add(self.testboard, self.j, self.opp)

        self.blev = tempblev 
        if self.findfour(self.testboard,self.opp):
          filltwosum += 1


      if filltwosum > 1:
        return self.b,4
    #BEGIN FIND DOUBLE 3 STEP FILLABLE TWOS SELF
    for aa in range(7):
      if aa in self.banlist:
        continue
      self.testboard = [row[:] for row in self.board]
      self.add(self.testboard, aa, self.name)
      tempblev = self.blev
      abfilltwosum = 0
      for ab in range(7):
        self.abtestboard = [row[:] for row in self.testboard]
        self.add(self.abtestboard, ab, self.name)
        acfilltwosum = 0
        for ac in range(7):
          self.actestboard = [row[:] for row in self.abtestboard]
          self.add(self.actestboard, ac, self.name)
          self.b = ac
          if self.findfour(self.actestboard,self.name):
            acfilltwosum += 1
        if acfilltwosum > 1:
          abfilltwosum +=1
      if abfilltwosum > 1:
        return aa,4.1

    
    #BEGIN FIND DOUBLE 3 STEP FILLABLE TWOS enemy
    for aa in range(7):
      if aa in self.banlist:
        continue
      self.testboard = [row[:] for row in self.board]
      self.add(self.testboard, aa, self.opp)
      tempblev = self.blev
      abfilltwosum = 0
      for ab in range(7):
        self.abtestboard = [row[:] for row in self.testboard]
        self.add(self.abtestboard, ab, self.opp)
        acfilltwosum = 0
        for ac in range(7):
          self.actestboard = [row[:] for row in self.abtestboard]
          self.add(self.actestboard, ac, self.opp)
          self.b = ac
          if self.findfour(self.actestboard,self.opp):
            acfilltwosum += 1
        if acfilltwosum > 1:
          abfilltwosum +=1
      if abfilltwosum > 1:
        return aa,4.2

    #BEGIN FIND 3 STEP FILLABLE TWOS SELF
    for aa in range(7):
      if aa in self.banlist:
        continue
      self.testboard = [row[:] for row in self.board]
      self.add(self.testboard, aa, self.name)
      tempblev = self.blev
      for ab in range(7):
        self.abtestboard = [row[:] for row in self.testboard]
        self.add(self.abtestboard, ab, self.name)
        filltwosum = 0
        for ac in range(7):
          self.actestboard = [row[:] for row in self.abtestboard]
          self.add(self.actestboard, ac, self.name)
          self.b = ac
          
          if self.findfour(self.actestboard,self.name):
            filltwosum += 1
        if filltwosum > 1:
          return aa,4.3

    #begin find 2 step self predicted fillable twos
    for self.od in range(7):
      if self.od in self.banlist:
        continue
      self.odtestboard = [row[:] for row in self.board]
      self.add(self.odtestboard, self.od, self.name)
      for self.aa in range(7):
        
        self.aatestboard = [row[:] for row in self.odtestboard]
        self.add(self.aatestboard, self.aa, self.name)

        for self.ab in range(7):
          self.abtestboard = [row[:] for row in self.aatestboard]
          self.add(self.abtestboard, self.ab, self.name)
          if self.findfour(self.abtestboard,self.name):
            self.abtestboard[self.blev][self.ab] = self.opp
  
            for self.ac in range(7):
              self.actestboard = [row[:] for row in self.abtestboard]
              self.add(self.actestboard, self.ac, self.name)
              if self.findfour(self.actestboard,self.name):
                return self.od, 4.3
      
    #BEGIN FIND 3 STEP FILLABLE TWOS ENEMY
    for aa in range(7):
      if aa in self.banlist:
        continue
      self.testboard = [row[:] for row in self.board]
      self.add(self.testboard, aa, self.opp)
      tempblev = self.blev
      for ab in range(7):
        self.abtestboard = [row[:] for row in self.testboard]
        self.add(self.abtestboard, ab, self.opp)
        filltwosum = 0
        for ac in range(7):
          self.actestboard = [row[:] for row in self.abtestboard]
          self.add(self.actestboard, ac, self.opp)
          self.b = ac
          if self.findfour(self.actestboard,self.opp):
            filltwosum += 1
        if filltwosum > 1:
          return aa,4.4
    #BEGIN FIND ENEMY 2 STEP PREDICDED FILLABLE TWOS
    for self.od in range(7):
      if self.od in self.banlist:
        continue
      self.odtestboard = [row[:] for row in self.board]
      self.add(self.odtestboard, self.od, self.opp)
      for self.aa in range(7):

        self.aatestboard = [row[:] for row in self.odtestboard]
        self.add(self.aatestboard, self.aa, self.opp)

        for self.ab in range(7):
          self.abtestboard = [row[:] for row in self.aatestboard]
          self.add(self.abtestboard, self.ab, self.opp)
          if self.findfour(self.abtestboard,self.opp):
            self.abtestboard[self.blev][self.ab] = self.name

            for self.ac in range(7):
              self.actestboard = [row[:] for row in self.abtestboard]
              self.add(self.actestboard, self.ac, self.opp)
              if self.findfour(self.actestboard,self.opp):
                return self.od,4.4
      

    #BEGIN FIND ENEMY UNFILLABLE TWOS
    for self.b in range(7):
      if self.b in self.banlist:
        continue
      self.testboard = [row[:] for row in self.board]
      self.add(self.testboard, self.b, self.opp)

      if self.findthree(self.testboard,self.opp):
        return self.b,5
        
        
    #BEGIN FIND SELF UNFILLABLE TWOS
    for self.b in range(7):
      if self.b in self.banlist:
        continue
      self.testboard = [row[:] for row in self.board]
      self.add(self.testboard, self.b, self.name)

      if self.findthree(self.testboard,self.name):
        return self.b,6
        
    
    #NOTHING
    print('nothing')
    while True:
      if len(self.banlist) >= 7:
        return 0,0
      rand = random.randint(0,6)
      if rand not in self.banlist:
        return rand,100


  def turn(self, col,oppname,oppturn = True):
    display(self.board)
    self.banlist = []
    self.prilist = []
    #place enemy disk 
    self.i=0
  
    if oppturn:
      self.add(self.board,col,self.opp)
      self.b = col
      if self.findfour(self.board,self.opp):
        print('game over. ' + self.opp + ' wins.')
        display(self.board)
        while True:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
          display(self.board)


    #find and confirm turn 

    for k in range(14):

      self.info = self.find()
      self.testboard = [row[:] for row in self.board]
      self.add(self.testboard, self.info[0], self.name)
      self.priority = self.prioritycheck(self.testboard, self.info[0])
      self.move = self.info[0]
      self.movepri = self.info[1]
      if len(self.banlist) >= 7:
        maxpri = -2
        for u in range(len(self.banlist)):
          if self.prilist[u] > maxpri:
            maxpri = self.prilist[u]
            self.move = self.banlist[u]
            self.movepri = self.prilist[u]
        self.priority = 0
      #find priorioty of self.move and set it to self.priority
      if self.board[0][self.move] != 0:
        self.priority = -1
        print('roof' + str(self.move))
      if self.priority > self.movepri:
        break
      else:
        self.banlist.append(self.move)
        self.prilist.append(self.priority)
        print(str(self.move)+' '+str(self.priority)+'<'+str(self.movepri))

    #place self disk

    self.add(self.board,self.move,self.name)


    #print new board
    print(str(self.name) + ' in col ' + str(self.move))
    print('priorioty: ' + str(self.movepri))
    print(self.banlist)
    printboard(self.board)
    display(self.board)

    if self.movepri == 1:
      print('game over. ' + self.name + ' wins.')
      display(self.board)
      while True:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        display(self.board)
    else:

      clock.tick(20)
      oppname(self.move,self.turn)
      while True:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        display(self.board)




class human:
  def __init__(self,name,opp):
    self.board = [
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0]
    ]
    self.name = name
    self.opp = opp

  def turn(self,col,oppname,oppturn = True):
    self.i = 0
    if oppturn:
      while self.board[self.i][col] == 0:
  
        if self.i == 5:
          self.board[self.i][col] = self.opp
          break
          
        if self.board[self.i + 1][col] != 0:
          self.board[self.i][col] = self.opp
          break
          
        self.i+=1

    try:
      go = int(input('collumn? '))
      self.board[self.i][go]
    except:
      go = int(input('invalid, type carefully. collumn? '))
    self.i = 0
    while self.board[self.i][go] == 0:
    
      if self.i == 5:
        self.board[self.i][go] = self.name
        break
        
      if self.board[self.i + 1][go] != 0:
        self.board[self.i][go] = self.name
        break
        
      self.i+=1
    printboard(self.board)
    display(self.board)
    oppname(go ,self.turn)
    
    

def display(board):
  screen.fill((0, 0, 0))
  for x in range(7):
    displayText(str(x),(x*50)+17.5,325,25)
    for y in range(6):
      if board[y][x] == 'r':
        color = (255,0,0)
      elif board[y][x] == 'y':
        color = (255,255,0)
      elif board[y][x] == 'a':
        color = (0,0,255)
      else:
        color = (0,0,0)
      pygame.draw.circle(screen, (150,150,150), (x*50 +25 , y * 50 +25 ), 23)
      pygame.draw.circle(screen, color, (x*50 +25 , y * 50 +25 ), 22)
  pygame.display.update()

def printboard(board):
  try:
    for i in range(6):
      for j in range(7):
        print(str(board[i][j]) + ', ', end = '')
      print('')
  except:
    print('ERROR: printboard called with less than 6 element array')
  print('')

def displayText(text, x, y, size):
  pygame.font.init()
  font = pygame.font.SysFont(None, size)
  textsurface = font.render(text, True, (255, 255, 255))
  screen.blit(textsurface, (x, y))

hue = human('y','r')
bot1 = sbot('r','y')

hue.turn(3,bot1.turn,False)


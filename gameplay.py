# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:14:25 2020
Coding: Modified Dynamic Connect 4 (Part-2 of the assignment)
@author: Alok Patel
ECSE-526: Artificial Intelligence
Assignment 1 - Game competation
[Note: Read the Readme file and the comments in the program to understand the program and and how to run it,
if you want to.]
"""

#Imported time library to measure time of the game play and to count time taken to visit number of states.
#Input is taken as current_state given in question.
#d is used to cut-off the depth to be visit, states is used to count the number of states visited.

import sys
import socket

d=0
m1=0
m2=0
m3=0
m4=0

human = sys.argv[1]
c = socket.socket()
c.connect(sys.argv[3],sys.argv[2])



current_state = [[' ','X','X',' ','O',' ',' '],        
                 [' ',' ',' ',' ',' ',' ','X'],
                 ['O',' ',' ',' ',' ',' ',' '],
                 ['O',' ',' ',' ',' ',' ','O'],
                 [' ',' ',' ',' ',' ',' ','O'],
                 ['X',' ',' ',' ',' ',' ',' '],
                 [' ',' ','O',' ','X','X',' ']]




'''
Here the is_end function is used to check the state of the game,
whether any X or O is winning or not.
''' 

def is_end():
  for i in range(7):
    for j in range(7):
      if(i<6 and j<6):
        if(current_state[i][j]=='O' and current_state[i+1][j]=='O' and current_state[i][j+1]=='O' and current_state[i+1][j+1]=='O'):
          return 'O'
        if(current_state[i][j]=='X' and current_state[i+1][j]=='X' and current_state[i][j+1]=='X' and current_state[i+1][j+1]=='X'):
          return 'X'

  return ' '   

'''
Here display function is used to display the current states, in the play function it is commented,
but can be accessed (called) to check the current state of the game.
'''
'''
def display():
  for i in range(7):
    for j in range(7):
      if(j==6):
        print(current_state[i][j])
      else:
        print(current_state[i][j]+',',end=" ")
    print()
'''
'''
Here maxi is the function max in minimax, and as the O is playing first it is placed in Maxi function to change its state.

'''
def maxi():          #alpha, beta

    # Possible values for maxv are:
    # -1 - loss
    # 0  - neutral
    # 1  - win
    global d
    global m1
    global m2
    global m3
    global m4
    d=d+1           #This is used to check how much depth the tree is visited.
    maxv = -10000
    px = None            #If will not get any O then will retun none.
    py = None 
    p=None        
    result = is_end() 
    if result == 'X':
        return (-1000, 0, 0, 0)
    elif result == 'O':
        return (1000, 0, 0, 0) 
    elif d>4:
        return (0, 0, 0, 0)
    # If the game came to an end, the function needs to return
    # the evaluation function of the end. That can be:
    # -1 - loss
    # 0  - neutral
    # 1  - win             
    for i in range(7):
        for j in range(7):
            if current_state[i][j] == 'O':
                z=mov('O',i,j) 
                current_state[i][j] = ' '
                  
                #S
                if ((i+1)<7 and current_state[i+1][j]== ' ' and z!=0):
                  a=posMov(z,'S',i,j) #Checking after cleaning the changed one and adding new one, so no worry.
                  current_state[i+a][j]='O'
                  (m1, min_i, min_j, min_k) = mini()   #alpha, beta
                  evl = heuristics(i+a,j)       #Check for new position O and if placed 
                  current_state[i+a][j] = ' '
                  # Above at the end if game is not win or loss then m1 will give the best value it could given by
                  # checking which has the best possibility to win the game. And if win then m1 will be 1000 viz. max so will go up.
                  # This is nothing but the Heuristic evaluation function
                  m1 = m1 + evl + a         
                  if m1 > maxv:
                    p=0
                    maxv = m1
                  #if f==0:
                  d=d-1                 #d-1 thing is perfect, no need of f thing
                  #if maxv>= beta:        #Inside if of each direction, as it checks for all.
                   #   return (maxv, i+1, j, 0) #Return simple, bcoz after there a is used.
                  #if maxv>alpha:
                  #    alpha = maxv
                #N
                if ((i-1)>=0 and current_state[i-1][j]== ' ' and z!=0):
                  a=posMov(z,'N',i,j)
                  current_state[i-a][j]='O'
                  (m2, min_i, min_j, min_k) = mini()    #alpha, beta
                  evl = heuristics(i-a,j) 
                  current_state[i-a][j] = ' '
                  m2= m2 + evl + a
                  if m2 > maxv:
                    maxv = m2
                    p=1
                  #if f==0:
                  d=d-1
                  #if maxv>= beta:
                  #   return (maxv, i-1, j, 1)
                 # if maxv>alpha:
                   #   alpha = maxv
                #W
                if ((j-1)>=0 and current_state[i][j-1]== ' ' and z!=0):
                  a=posMov(z,'W',i,j)
            
                  current_state[i][j-a]='O'
                  (m3, min_i, min_j, min_k) = mini()  #alpha, beta
                  evl = heuristics(i,j-a)
                  current_state[i][j-a] = ' '
                 
                  m3= m3 + evl + a
                  if m3 > maxv:
                    maxv = m3
                    p=2
                  #if f==0:
                  d=d-1
                  #if maxv>= beta:
                   #   return (maxv,i,j-1,2)
                  #if maxv>alpha:
                   #   alpha = maxv
                #E
                if ((j+1)<7 and current_state[i][j+1]== ' ' and z!=0):
                  a=posMov(z,'E',i,j) 
            
                  current_state[i][j+a]='O'
                  (m4, min_i, min_j, min_k) = mini()     #alpha, beta
                  evl = heuristics(i,j+a)
                  current_state[i][j+a] = ' '
                 
                  m4= m4 + evl + a
                  if m4 > maxv:
                    maxv = m4
                    p=3
                  #if f==0:
                  d=d-1
                  #if maxv>= beta:
                   #   return (maxv,i,j+1,3)
                  #if maxv>alpha:
                   #   alpha = maxv
                current_state[i][j] = 'O'
                #This will tell the AI to move this direction because in this 
                #we have optimal path to win
                #p = 0-S, 1-N, 2-W, 3-E 
                if(p==0):
                    px = i+1        #It will return one step only, but in play we have setup a so it will making it is possible.
                    py = j   
                elif(p==1):
                    px = i-1
                    py = j     
                elif(p==2):
                    px = i
                    py = j-1    
                elif(p==3):
                    px = i
                    py = j+1  
                #if maxv>=beta:              #To remove alphabeta comment this.
                 #   return (maxv,px,py,p)   #To remove alphabeta comment this.
               #if maxv>alpha:              #To remove alphabeta comment this.
                  #  alpha = maxv            #To remove alphabeta comment this.

    return (maxv, px, py, p)

'''
It is our min function which is used to move the O piece.
'''

def mini():                 #alpha, beta alpha_beta included

    # Possible values for minv are:
    # -1 - win for X
    # 0  - neutral
    # 1  - loss
    global d
    global m1
    global m2
    global m3
    global m4
    d=d+1
    minv = 10000
    qx = None               #If will not get any X then will retun none.
    qy = None       
    q=None
    result = is_end()
    if result == 'X':
        return (-1000, 0, 0, 0)
    elif result == 'O':
        return (1000, 0, 0, 0)
    elif d>4:
        return (0, 0, 0, 0)
        
    
    for i in range(7):
        for j in range(7):
            if current_state[i][j] == 'X':
                z=mov('X',i,j)
                current_state[i][j] = ' '
                # On the empty field player 'X' makes a move and calls Maxi
                # S
                if ((i+1)<7 and current_state[i+1][j]== ' ' and z!=0):
                  a=posMov(z,'S',i,j)
                 
                  current_state[i+a][j]='X'  
                  (m1, min_i, min_j, min_k) = maxi()      #alpha, beta
                  evl = heuristics(i+a,j)
                  current_state[i+a][j] = ' '
                   
                  m1 = m1 - evl - a
                  if m1 < minv:
                    minv = m1
                    q=0
                  #if f==1:
                  d=d-1
                  #if minv<=alpha:
                   #  return (minv,i+1,j,0)
                  #if minv<beta:
                  #    beta = minv
                #N
                if ((i-1)>=0 and current_state[i-1][j]== ' ' and z!=0):
                  a=posMov(z,'N',i,j)
                  
                  current_state[i-a][j]='X'
                  (m2, min_i, min_j, min_k) = maxi()      #alpha, beta
                  evl = heuristics(i-a,j)
                  current_state[i-a][j] = ' '
                  
                  m2 = m2 - evl - a
                  if m2 < minv:
                    minv = m2
                    q=1
                  #if f==1:
                  d=d-1
                  #if minv<=alpha:
                   #   return (minv,i-1,j,1)
                  #if minv<beta:
                  #    beta = minv
                #W
                if ((j-1)>=0 and current_state[i][j-1]== ' ' and z!=0):
                  a=posMov(z,'W',i,j)
                 
                  current_state[i][j-a]='X'
                  (m3, min_i, min_j,min_k) = maxi()      #alpha, beta
                  evl = heuristics(i,j-a)
                  current_state[i][j-a] = ' '
                   
                  m3 = m3 - evl - a
                  if m3 < minv:
                    minv = m3
                    q=2
                 # if f==1:
                  d=d-1
                  #if minv<=alpha:
                  #    return (minv,i,j-1,2)
                  #if minv<beta:
                  #    beta = minv
                #E
                if ((j+1)<7 and current_state[i][j+1]== ' ' and z!=0):
                  a=posMov(z,'E',i,j)
                  
                  current_state[i][j+a]='X'
                  (m4, min_i, min_j,min_k) = maxi()      #alpha, beta
                  evl = heuristics(i,j+a)
                  current_state[i][j+a] = ' '
                  
                  m4 = m4 - evl - a
                  if m4 < minv:
                    minv = m4
                    q=3
                  #if f==1:
                  d=d-1
                  #if minv<=alpha:
                   #   return (minv,i,j+1,3)
                  #if minv<beta:
                   #   beta = minv
                current_state[i][j] = 'X'
                #q = 0 to 3 for SNWE
                if(q==0):
                    qx = i+1
                    qy = j
                elif(q==1):
                    qx = i-1
                    qy = j
                elif(q==2):
                    qx = i
                    qy = j-1
                elif(q==3):         #Not put else because none then also will send this values
                    qx = i
                    qy = j+1   
                #if minv<=alpha:             #To remove alphabeta comment this.
                    #return (minv,qx,qy,q)   #To remove alphabeta comment this.
                #if minv<beta:               #To remove alphabeta comment this.
                #    beta=minv               #To remove alphabeta comment this.                      
    return (minv, qx, qy, q)
 
'''
This function is not used here, but used to check whether the input from the 
human is valid or not.
'''

def is_valid(px, py):
    if px < 0 or px > 6 or py < 0 or py > 6:
        return False
    elif current_state[px][py] == ' ':
        return True

'''
Here mov function is used to calculate the maximum possible moves possible,
by checking the number of opponent pieces around.
'''

def mov(op,i,j):
    if(op=='O'):
        op='X'
    else:
        op='O'
    sum=0
    if(i-1>=0 and current_state[i-1][j]==op):               #N
        sum=sum+1
    if(j-1>=0 and current_state[i][j-1]==op):               #W
        sum=sum+1
    if(i-1>=0 and j-1>=0 and current_state[i-1][j-1]==op):  #NW
        sum=sum+1
    if(i+1<7 and current_state[i+1][j]==op):                #S
        sum=sum+1
    if(i+1<7 and j-1>=0 and current_state[i+1][j-1]==op):   #SW
        sum=sum+1
    if(j+1<7 and current_state[i][j+1]==op):                #E
        sum=sum+1
    if(i+1<7 and j+1<7 and current_state[i+1][j+1]==op):    #SE
        sum=sum+1
    if(i-1>=0 and j+1<7 and current_state[i-1][j+1]==op):   #NE
        sum=sum+1
    if(sum==0):
        return 3
    elif(sum==1):
        return 2
    elif(sum==2):
        return 1
    else:
        return 0

'''
The function posMov will calculate whether the path is clear or not.
For ex: If 3 moves are possible, then it will take 3 moves or not.
'''

def posMov(maxMov,direction,i,j):
  if(direction=='E'):
      e=0
      for k in range(1,maxMov+1):
          if(j+k<7 and current_state[i][j+k]!=' '): #This if is used so that piece don't jump. Same in all others.
              break
          if(j+k<7 and current_state[i][j+k]==' '):
              e=e+1
      return e
  if(direction=='W'):
      w=0
      for k in range(1,maxMov+1):
          if(j-k>=0 and current_state[i][j-k]!=' '):
              break
          if(j-k>=0 and current_state[i][j-k]==' '):
              w=w+1
      return w
  if(direction=='S'):
      s=0
      for k in range(1,maxMov+1):
          if(i+k<7 and current_state[i+k][j]!=' '):
              break
          if(i+k<7 and current_state[i+k][j]==' '):
              s=s+1
      return s
  if(direction=='N'):
      n=0
      for k in range(1,maxMov+1):
          if(i-k>=0 and current_state[i-k][j]!=' '):
              break
          if(i-k>=0 and current_state[i-k][j]==' '):
              n=n+1
      return n

'''
Heuristics evaluation function is used to give the values to the non-terminal nodes
and specifically useful when there is cut-off in depth.
''' 

def heuristics(x,y):
    #Below a,b,c,and d list is used to store the data of the pieces for calculations in heuristic function.
    ax=[] #for i of O and if placed inside the heuristics function then will not print outside.
    by=[] #for j of O
    cx=[] #for i of X
    dy=[] #for j in X
    if current_state[x][y]=='O':
        for e in range(7):
            for f in range(7):
                if (e==x and f==y):
                    pass
                elif current_state[e][f]=='O':
                    ax.append(e)
                    by.append(f)
                elif current_state[e][f]=='X':
                    cx.append(e)
                    dy.append(f)
                else:
                   pass
    else:
        for g in range(7):
            for h in range(7):
                if (g==x and h==y):
                    pass
                elif current_state[g][h]=='O':
                    ax.append(g)
                    by.append(h)
                elif current_state[g][h]=='X':
                    cx.append(g)
                    dy.append(h)
                else:
                   pass
        
    distance1=0
    distance2=0
    pair = 0
    if len(ax) == 5:
        for l in range(5):
            distance1 = distance1 + abs(ax[l]-x) + abs(by[l]-y) 
    if len(ax) == 6:
        for l in range(6):
            distance1 = distance1 + abs(ax[l]-x) + abs(by[l]-y)
    if len(cx) == 6:
         for l in range(6):
            distance2 = distance2 + abs(cx[l]-x) + abs(dy[l]-y)
    if len(cx) == 5:
         for l in range(5):
            distance2 = distance2 + abs(cx[l]-x) + abs(dy[l]-y)
    
    #Below two if for checking the pair of two, if so then +20 points,
    #and pair of three then +40 in total. So best result.
    if current_state[x][y]=='O':
        pie = 'O'
    else:
        pie = 'X'
    if (x-1>=0 and current_state[x-1][y]==pie):  #Check North
        pair = pair + 20
    if (x+1<7 and current_state[x+1][y]==pie): #Check South
        pair = pair + 20
    if (y+1<7 and current_state[x][y+1]==pie):  #Check East
        pair = pair + 20
    if (y-1>=0 and current_state[x][y-1]==pie): #Check West 
        pair = pair + 20
    if (x-1>=0 and y-1>=0 and current_state[x-1][y-1]==pie): #Check NW
        pair = pair + 20
    if (x+1<7 and y-1>=0 and current_state[x+1][y-1]==pie):  #Check SW
        pair = pair + 20
    if (x+1<7 and y+1<7 and current_state[x+1][y+1]==pie):   #Check SE  
        pair = pair + 20
    if (x-1>=0 and y+1<7 and current_state[x-1][y+1]==pie):  #Check NE
        pair = pair + 20
    
    # 'b' in report is evaluation here, it the heuristic evaluation function value for a state
    if current_state[x][y]=='O':
        evaluation = distance2 - distance1  + pair
        return evaluation 
    else:
        evaluation = distance1 - distance2 + pair
        return evaluation

'''
send function is used to send the data from program to the server
'''
def send(x1, y1, direc, moves):
    data = str(x1)+str(y1)+direc+str(moves)
    c.send(bytes(data,'utf-8')) 
 
  
'''
play function is the main function which will start the game and execute the steps.
'''

def play():
    global d
    global human               #Comment this to run in the compiler
    x = 0
    y = 0
    m = 0
    if human == 'X':
        player = 'O'
        while True: 
            #display() 
            result = is_end()
            # Printing the appropriate message if the game has ended
            if result != None:
                if result == 'X':
                    print('The winner is X!')
                    break
                elif result == 'O':
                    print('The winner is O!')
                    break
            
            if player == 'O':
               data = c.recv(1024).decode()
               x = int(data[0])
               y = int(data[1])
               di = data[2]
               m = int(data[3])
               if(di=='N'):
                   current_state[x][y] = ' ' #when !=z will be added, at a=0 it will save that step.
                   current_state[x-m][y] = 'O'
               elif(di == 'S'):
                   current_state[x][y] = ' '
                   current_state[x+m][y] = 'O'
               elif(di=='E'):
                   current_state[x][y] = ' '
                   current_state[x][y+m] = 'O'
               else:   #W
                   current_state[x][y] = ' '
                   current_state[x][y-m] = 'O'
            
               player = 'X'
            
            else:
                d=0         #d=0 when its turn, so min will call 1st at d=0.
                (m, qx, qy, q) = mini()        #-10000,10000
                
                if(q!=None):
                  if(q==1):             #Bcoz earlier for N it was defined as q=1
                    #N
                    z=mov('X',qx+1,qy)
                    a=posMov(z,'N',qx+1,qy)
                    current_state[qx+1][qy] = ' '
                    current_state[qx+1-a][qy] = 'X'
                    send(qx+1,qy,'N',a)
                  elif(q==0):
                    #S
                    z=mov('X',qx-1,qy)
                    a=posMov(z,'S',qx-1,qy)
                    current_state[qx-1][qy] = ' '
                    current_state[qx-1+a][qy] = 'X'  
                    send(qx-1,qy,'S',a)
                  elif(q==3):           #Bcoz earlier 3 is for E and 2 is for W
                    #E
                    z=mov('X',qx,qy-1)
                    a=posMov(z,'E',qx,qy-1)
                    current_state[qx][qy-1] = ' '
                    current_state[qx][qy-1+a] = 'X'
                    send(qx,qy-1,'E',a)
                  else:
                    #W
                    z=mov('X',qx,qy+1)
                    a=posMov(z,'W',qx,qy+1)
                    current_state[qx][qy+1] = ' '
                    current_state[qx][qy+1-a] = 'X'
                    send(qx,qy+1,'W',a)
                
                player = 'O'
    else:
        player = 'X'
        while True: 
            #display() 
            result = is_end()
            # Printing the appropriate message if the game has ended
            if result != None:
                if result == 'X':
                    print('The winner is X!')
                    break
                elif result == 'O':
                    print('The winner is O!')
                    break
                  
            if player == 'O':
                d=0                     #Intially d=0 at the first node.
                (m, px, py,p) = maxi()        #-10000,10000
               
                if(p!=None):
                      if(p==1):
                        #N
                        z=mov('O',px+1,py)           #px+1 to get the original postion of O, from it is to be moved.
                        a=posMov(z,'N',px+1,py)
                        current_state[px+1][py] = ' ' #when !=z will be added, at a=0 it will save that step.
                        current_state[px+1-a][py] = 'O'
                        send(px+1,py,'N',a)
                      elif(p==0):
                        #S
                        z=mov('O',px-1,py)
                        a=posMov(z,'S',px-1,py)
                        current_state[px-1][py] = ' '
                        current_state[px-1+a][py] = 'O'
                        send(px-1,py,'S',a)
                      elif(p==3):
                        #E
                        z=mov('O',px,py-1)
                        a=posMov(z,'E',px,py-1)
                        current_state[px][py-1] = ' '
                        current_state[px][py-1+a] = 'O'
                        send(px,py-1,'E',a)
                      else:   #As p!=none defined so else is ok
                        #W
                        z=mov('O',px,py+1)
                        a=posMov(z,'W',px,py+1)
                        current_state[px][py+1] = ' '
                        current_state[px][py+1-a] = 'O'
                        send(px,py+1,'W',a)
            
                player = 'X'
        
            else:
               data = c.recv(1024).decode()
               x = int(data[0])
               y = int(data[1])
               di = data[2]
               m = int(data[3])
               if(di=='N'):
                   current_state[x][y] = ' ' #when !=z will be added, at a=0 it will save that step.
                   current_state[x-m][y] = 'X'
               elif(di == 'S'):
                   current_state[x][y] = ' '
                   current_state[x+m][y] = 'X'
               elif(di=='E'):
                   current_state[x][y] = ' '
                   current_state[x][y+m] = 'X'
               else:   #W
                   current_state[x][y] = ' '
                   current_state[x][y-m] = 'X'
            
               player = 'O'
    

play()    


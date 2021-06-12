import math
from GAME import *

alpha_initial = -math.inf
beta_initial = math.inf

# return a7sn move (lnode nafsha ka object) 
def Minimax_alphabeta(node , depthlevel , alpha , beta , AI_maxplayer ):
    
    if depthlevel == 0:
        return node.score  
    
    
    if AI_maxplayer == True:        
        bestpath  = alpha_initial      
        for child in range(node.children):
            
            if Game.RepeatTurn():  #lazm a3rf lw fy forsaa 
               AI_maxplayer = True
            else:
               AI_maxplayer = False
           
            value = Minimax_alphabeta(child , depthlevel-1 , alpha , beta , AI_maxplayer)
            bestpath  = max(value , bestpath)
            alpha - max(bestpath,alpha)
            
            if alpha >= beta:
                break #cut branch
        return alpha

    if AI_maxplayer == False:           
        bestpath  = beta_initial
   
        for child in range(node.children):
        
            if Game.RepeatTurn():
                AI_maxplayer = False
            else:
                AI_maxplayer = True
           
            value = Minimax_alphabeta(child , depthlevel-1 , alpha , beta , AI_maxplayer)
            bestpath  = min(value , bestpath)
            beta = min(bestpath,alpha)
            
            if alpha >= beta:
                break #cut branch
        return beta
                

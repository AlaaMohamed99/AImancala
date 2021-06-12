import copy
import math
# from GAME import *
from helperfns import is_finalboard
from heuristic import score_evaluation
from heuristic_fagr import *
alpha_initial = -math.inf
beta_initial = math.inf


class AI():
    def __init__(self,board):
        self.board = board

    def possible_moves(self, turn, board):
        moves = {}
        
        if turn == 0:
            #player 1, human
            #from 0 to 5
            for index in range(6):
                newboard = copy.deepcopy(board) 
                num_of_balls = newboard[index]
                if num_of_balls == 0:
                    continue
                newboard[index]=0
                pocket = index + 1
                
                for i in range(num_of_balls):
                    if pocket !=13:
                        newboard[pocket] = newboard[pocket] +1
                    else:
                        pocket = 0
                        newboard[pocket] = newboard[pocket] +1
                    pocket += 1
                pocket -= 1
                
                if pocket == 6:
                    turn = 0
                    # #print('repeat human')
                else:
                    turn = 1
                
                moves[tuple(newboard)] = turn
                
        elif turn == 1:
            #for AI, player 2
            for index in range(7,13):
                newboard = copy.deepcopy(board) 
                num_of_balls = newboard[index]
                if num_of_balls == 0:
                    continue
                newboard[index]=0
                pocket = index + 1
                
                for i in range(num_of_balls):
                    if pocket > 13:
                        pocket = 0
                        newboard[pocket] = newboard[pocket] +1
                    elif pocket == 6:
                        pocket = 7
                        newboard[pocket] = newboard[pocket] +1
                    else:
                        newboard[pocket] = newboard[pocket] +1
                    pocket += 1
                pocket -= 1
                if pocket == 13:
                    turn = 1
                    # #print('repeattt')
                else:
                    turn = 0
                moves[tuple(newboard)] = turn   
        return moves   


    # def Heuristic(self,move):
    #     # ay habal mo2qtn
    #     sum_player=0
    #     sum_player = sum(move[7:9])
        
    #     return sum_player


    # # def is_finalboard(board):
    #     count1 =0
    #     count2 =0
    #     for i in board[:6]:
    #         if i != 0:
    #             count1 =-1
    #             break
    #     for j in board[7:13]:
    #         if j != 0:
    #             count2 = -1
    #             break
    #     if (count1 == 0 or count2 ==0):
    #         return True
    #     return False
   
    def Minimax_alphabeta(self, currentboard , depthlevel,alpha , beta ,stealing  ,AI_maxplayer ):
    
        heuristic_score = 0
        
        
        #wslt lel akher aw khalst asasn
        
        if depthlevel == 0 or is_finalboard(currentboard):
            board_now = copy.deepcopy(currentboard)
            #heuristic_score = self.Heuristic(board_now)  
            heuristic_score = score_evaluation(board_now,AI_maxplayer,stealing)
            # heuristic_score = evaluation_function(board_now,AI_maxplayer,stealing)
            #print('score='+str(heuristic_score))
            #print('leaf board')        
            # #print(board_now)                 
            return heuristic_score , board_now , AI_maxplayer
        
        
        if AI_maxplayer == 1:     
            #print('depth='+str(depthlevel))
            bestpath  = alpha_initial 
            board_now = copy.deepcopy(currentboard)
            move_and_score = dict()
            # board_now = mancala_board.Board(currentboard) 
            moves = self.possible_moves(AI_maxplayer, board_now)
            for move_board,turn in moves.items():
                # #print(',,,,,,,,,,')
                # #print(move_board)

                value,m,AI_maxplayer= self.Minimax_alphabeta(list(move_board), depthlevel-1 ,alpha , beta,stealing ,turn)
                bestpath  = max(value , bestpath)
                alpha = max(bestpath,alpha)
                # #print(move_board)
                move_and_score[value] = move_board
                if alpha >= beta:
                    break #cut branch
                #print(move_and_score)
            #print(moves)
            return bestpath , list(move_and_score[bestpath]) , moves[move_and_score[bestpath]]
    
        if AI_maxplayer == 0:    
            #print('depth='+str(depthlevel))

            bestpath  = beta_initial
            board_now = copy.deepcopy(currentboard)
            move_and_score = dict()
            moves = self.possible_moves(AI_maxplayer, board_now)
            for move_board,turn in moves.items():
                # #print('-------------------')
                # #print(move_board)
               
                value,m ,AI_maxplayer= self.Minimax_alphabeta(list(move_board ), depthlevel-1, alpha , beta,stealing , turn)
                bestpath  = min(value , bestpath)
                alpha = min(bestpath,alpha)
                # #print(move_board)
                move_and_score[value] = move_board
                if alpha >= beta:
                    break #cut branch
                #print(move_and_score)
            #print(moves)
            return bestpath , list(move_and_score[bestpath]) , moves[move_and_score[bestpath]]

    def Minimax_alphabeta_client(self, currentboard , depthlevel,alpha , beta ,stealing  ,AI_maxplayer ):
        
            heuristic_score = 0
            
            
            #wslt lel akher aw khalst asasn
            
            if depthlevel == 0 or is_finalboard(currentboard):
                board_now = copy.deepcopy(currentboard)
                #heuristic_score = self.Heuristic(board_now)  
                heuristic_score = score_evaluation(board_now,AI_maxplayer,stealing)
                # heuristic_score = evaluation_function(board_now,AI_maxplayer,stealing)
                #print('score='+str(heuristic_score))
                #print('leaf board')        
                # #print(board_now)                 
                return heuristic_score , board_now , AI_maxplayer
            
            
            if AI_maxplayer == 0:     
                #print('depth='+str(depthlevel))
                bestpath  = alpha_initial 
                board_now = copy.deepcopy(currentboard)
                move_and_score = dict()
                # board_now = mancala_board.Board(currentboard) 
                moves = self.possible_moves(AI_maxplayer, board_now)
                for move_board,turn in moves.items():
                    # #print(',,,,,,,,,,')
                    # #print(move_board)
    
                    value,m,AI_maxplayer= self.Minimax_alphabeta(list(move_board), depthlevel-1 ,alpha , beta,stealing ,turn)
                    bestpath  = max(value , bestpath)
                    alpha = max(bestpath,alpha)
                    # #print(move_board)
                    move_and_score[value] = move_board
                    if alpha >= beta:
                        break #cut branch
                    #print(move_and_score)
                #print(moves)
                return bestpath , list(move_and_score[bestpath]) , moves[move_and_score[bestpath]]
        
            if AI_maxplayer == 1:    
                #print('depth='+str(depthlevel))
    
                bestpath  = beta_initial
                board_now = copy.deepcopy(currentboard)
                move_and_score = dict()
                moves = self.possible_moves(AI_maxplayer, board_now)
                for move_board,turn in moves.items():
                    # #print('-------------------')
                    # #print(move_board)
                   
                    value,m ,AI_maxplayer= self.Minimax_alphabeta(list(move_board ), depthlevel-1, alpha , beta,stealing , turn)
                    bestpath  = min(value , bestpath)
                    alpha = min(bestpath,alpha)
                    # #print(move_board)
                    move_and_score[value] = move_board
                    if alpha >= beta:
                        break #cut branch
                    #print(move_and_score)
                #print(moves)
                return bestpath , list(move_and_score[bestpath]) , moves[move_and_score[bestpath]]    
 

# board =[4]*6  + [0] + [4]*6 + [0]
# print(board)
# trial = AI(board)
# trial.Minimax_alphabeta(board,2,alpha_initial,beta_initial,1)

# # board = trial.possible_moves(1,board)
# #print(board)

      
        
        
      

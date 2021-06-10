import copy
# from itertools import chain, imap

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
                    elif pocket == 7:
                        pocket = 8
                        newboard[pocket] = newboard[pocket] +1
                    else:
                        newboard[pocket] = newboard[pocket] +1
                    pocket += 1
                pocket -= 1
                if pocket == 13:
                    turn = 1
                else:
                    turn = 0
                moves[tuple(newboard)] = turn   
        return moves   

        
        
        



board =[4]*6  + [0] + [4]*6 + [0]

trial = AI(board)
board = trial.possible_moves(1,board)
print(board)

import copy
# from itertools import chain, imap

class AI():
    def __init__(self,board):
        self.board = board
        
    # def valid_move(self, index):
    #     if self.board[index] == 0:
    #         return 'not valid'
    #     else:
    #         return 'valid'
    #1st 6 are the human, 2nd 6 are the AI
    def possible_moves(self, turn, board):
        moves = []
        # tree = Node(board)
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
                
                # tree.add_child(Node(newboard), turn)
                moves.append(newboard)
                
        elif turn == 1:
            #for AI, player 2
            for index in range(7,13):
                newboard = copy.deepcopy(self.boardMoves) 
                num_of_balls = newboard[index]
                if num_of_balls == 0:
                    continue
                newboard[index]=0
                pocket = index + 1
                print(index)
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
                    # print(pocket)
                # tree.add_child(newboard)
                moves.append(newboard)   
        return moves   
       
        
    def create_table(self, currentboard, turn, depth):
        self.BoardMoves = copy.deepcopy(currentboard)
        tree = Nodetree(self.BoardMoves)
        moves = self.possible_moves(0, self.BoardMoves)
        if depth == 0:
            return
        for move in moves:
            node = Nodetree(move)
            tree.add_child(node)
        for i in range(depth):
            for child in tree.children:
                possible_moves = self.possible_moves(0, child.board)
                node = Nodetree
                self.create_table(child.board,0,depth-1)
        return tree
        
        
class Nodetree:
    def __init__(self, board):
        self.board = board
        self.children = []
        self.parent = None
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)


board =[0,4,4,4,4,9]  + [0] + [4]*6 + [0]
# print(board)
trial = AI(board)
board = trial.create_table(board, 0, 3)
# trial.create_table(board, 0, 1)

# print(board)
# for x in board:
#     print(x)


# mytree = Node('A', Node('B', Node('D'), Node('E')), Node('C', Node('F'), Node('G')))

# walk(mytree)
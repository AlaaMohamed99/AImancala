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
        tree = Node(board)
        if turn == 0:
            #player 1, human
            #from 0 to 5
            for index in range(6):
                newboard = copy.deepcopy(board) 
                num_of_balls = newboard[index]
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
                tree.add_child(Node(newboard))
                moves.append(newboard)
                
        elif turn == 1:
            #for AI, player 2
            for index in range(7,13):
                newboard = copy.deepcopy(self.boardMoves) 
                num_of_balls = newboard[index]
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
                tree.add_child(newboard)
                moves.append(newboard)   
        return tree   
            # for i in range(6):
            #     if self.index != 7:
            #         self.board[self.index] = self.board[self.index]+1
            #     elif self.index == 7: 
            #         ##this is for human
            #         continue
            #     self.index += 1
                
            #     moves.append(self.board) 
        # return moves        
        # if self.valid_move(self.index) == 'valid' and self.index != 13:
        #    value = self.board[index]
        #    self.board[index]=0
        #    index += 1
        #    for i in range(value):
        #        if self.index != 13 and self.index != 7:
        #             self.board[index] = self.board[index]+1
        #        index += 1
        #        moves.append(self.board)
        # return moves
        #valid = self.valid_move(index)
        
    def create_table(self, currentboard, turn, depth):
        self.BoardMoves = copy.deepcopy(currentboard)
        
        
        
            
    

class Node:
    def __init__(self, root, children = None):
        self.val = None
        self.repeat = None
        self.root = root
        self.children = []
        # if children is not None:
        #     for child in children:
        #         self.add_child(child)
        
    # def __repr__(self):
    #     return self.name
    def add_child(self, node):
        assert isinstance(node, Node)
        self.children.append(node)

    def __iter__(self):
        "implement the iterator protocol"
        for v in chain(*imap(iter, self.children)):
            yield v
        yield self.value
        
    def __str__(self):
        return 'Node(' + str(self.val) + ')'
 
    def get_data(self):
        return self.val

    def set_data(self,val):
        self.val = val

    def get_children(self):
        # for child in self.children:
        #     print(child)
        
        return self.children

    def set_next(self,next):
        self.next = next
        
def walk(tree):
        if tree is not None:
            walk(tree.left)
            print(tree) #here ha3ml alpha-beta pruning
            walk(tree.right)





board =[0,4,4,4,4,9]  + [0] + [4]*6 + [0]
print(board)
trial = AI(board)
board = trial.possible_moves(0, board)

print(board.get_children())
# for x in board:
#     print(x)


# mytree = Node('A', Node('B', Node('D'), Node('E')), Node('C', Node('F'), Node('G')))

# walk(mytree)
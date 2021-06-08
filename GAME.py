class Game:
    def __init__(self):
        self.num_cups=6
        self.player1_cups=[4]*self.num_cups
        self.player2_cups=[4]*self.num_cups
        self.mancala_cups=[0,0] #dih l bylem feha#
        self.board = [0,4,4,4,4,4,4,0,4,4,4,4,4,4]
        self.player1_freeturn = False
        self.player2_freeturn = False
        
    def RepeatTurn(self):
 #### da msh lcondition bs m7taga agrb lminimax         
 
        if self.player1_freeturn == True:
            return True
        elif self.player2_freeturn == True:
            return True
        else : return False
    
    
        
        
        
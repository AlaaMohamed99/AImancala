
class Game:
    def __init__(self):
        self.num_cups=6
        #self.player1_cups=[4]*self.num_cups
        self.player1_cups=[4,4,4,4,4,4]
        
        #self.player2_cups=[4]*self.num_cups
        self.player2_cups=[4,4,4,4,4,4]
        self.mancala_cup_1=0 #dih l bylem feha#
        self.mancala_cup_2=0
        #self.final_list=self.player1_cups+self.mancala_cup_1+self.player2_cups+self.mancala_cup_2
        
        #print(self.final_list)


    def draw(self,board):
        print("AI Player")
        # print('     ','  0','   ','   1',' ','   2','    ','  3','       ','  4','     ','  5')
        print('     ','   1',' ','   2','    ','  3','       ','  4','     ','  5','     ','  6')
        print('[ ]',' ','(  '+ str(board[12]) + '  )','(  '+ str(board[11]) + '   )','(  '+ str(board[10]) + '   )','(   '+ str(board[9]) + '  )','(  '+ str(board[8]) + '   )','(   '+ str(board[7]) + '  )',' ','[ ]')        
        print('['+str(board[13]) +']'+ '                                                                                '+'['+str(board[6]) +']' )
        print('[ ]',' ','(  '+ str(board[0]) + '  )','(  '+ str(board[1]) + '   )','(  '+ str(board[2]) + '   )','(   '+ str(board[3]) + '  )','(  '+ str(board[4]) + '   )','(   '+ str(board[5]) + '  )',' ','[ ]')
        # print('     ','  5','   ','   4',' ','   3','    ','  2','       ','  1','     ','  0')

        print('     ','   1',' ','   2','    ','  3','       ','  4','     ','  5','     ','  6')
        
        print('Human Player')








       

        
   

class Game:
    def __init__(self):
        self.num_cups=6
        self.player1_cups=[4]*self.num_cups
        self.player2_cups=[4]*self.num_cups
        self.mancala_cups=[[0],[0]] #dih l bylem feha#
        self.final_list=self.player1_cups+self.mancala_cups[0]+self.player2_cups+self.mancala_cups[1]
        
        print(self.final_list)


        

    def draw(self):
        print("Player 1")
        print('     ','  5','   ','   4',' ','   3','    ','  2','       ','  1','     ','  0')
        print('[ ]',' ','(  '+ str(self.player1_cups[0]) + '  )','(  '+ str(self.player1_cups[1]) + '   )','(  '+ str(self.player1_cups[2]) + '   )','(   '+ str(self.player1_cups[3]) + '  )','(  '+ str(self.player1_cups[4]) + '   )','(   '+ str(self.player1_cups[5]) + '  )',' ','[ ]')
        print('[ ]',' ','(  '+ str(self.player2_cups[0]) + '  )','(  '+ str(self.player2_cups[1]) + '   )','(  '+ str(self.player2_cups[2]) + '   )','(   '+ str(self.player2_cups[3]) + '  )','(  '+ str(self.player2_cups[4]) + '   )','(   '+ str(self.player2_cups[5]) + '  )',' ','[ ]')
        print('     ','  0','   ','   1',' ','   2','    ','  3','       ','  4','     ','  5')
        print('Player 2')


    def update(self):
        " mch 3arfaaaaa"

g=Game()
g.draw()

        
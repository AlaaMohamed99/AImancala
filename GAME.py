
class Game:
    def __init__(self):
        self.num_cups=6
        self.player1_cups=[4]*self.num_cups
        self.player2_cups=[4]*self.num_cups
        self.mancala_cups=[0,0] #dih l bylem feha#
        print(self.player1_cups)


        

    def draw(self):
        print("zfff")
        print('         ','   5',' ','   4',' ','   3',' ','  2',' ','  1',' ','  0')
        print('[ ]',' ','('+  + '  )','(    )','(    )','(    )','(    )','(    )',' ','[ ]')
        print('[ ]',' ','(    )','(    )','(    )','(    )','(    )','(    )',' ','[ ]')
        print('         ','   0',' ',' 1',' ',' 2',' ',' 3',' ',' 4',' ',' 5')
        

g=Game()
g.draw()

        
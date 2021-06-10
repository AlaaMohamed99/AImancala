
class Game:
    def __init__(self):
        self.num_cups=6
        #self.player1_cups=[4]*self.num_cups
        self.player1_cups=[3,4,2,0,4,0]
        
        #self.player2_cups=[4]*self.num_cups
        self.player2_cups=[3,2,4,5,1,4]
        self.mancala_cup_1=0 #dih l bylem feha#
        self.mancala_cup_2=0
        #self.final_list=self.player1_cups+self.mancala_cup_1+self.player2_cups+self.mancala_cup_2
        
        #print(self.final_list)


        

    def draw(self):
        print("Player 1")
        print('     ','  5','   ','   4',' ','   3','    ','  2','       ','  1','     ','  0')
        print('[ ]',' ','(  '+ str(self.player1_cups[0]) + '  )','(  '+ str(self.player1_cups[1]) + '   )','(  '+ str(self.player1_cups[2]) + '   )','(   '+ str(self.player1_cups[3]) + '  )','(  '+ str(self.player1_cups[4]) + '   )','(   '+ str(self.player1_cups[5]) + '  )',' ','[ ]')
        print('[ ]',' ','(  '+ str(self.player2_cups[0]) + '  )','(  '+ str(self.player2_cups[1]) + '   )','(  '+ str(self.player2_cups[2]) + '   )','(   '+ str(self.player2_cups[3]) + '  )','(  '+ str(self.player2_cups[4]) + '   )','(   '+ str(self.player2_cups[5]) + '  )',' ','[ ]')
        print('     ','  0','   ','   1',' ','   2','    ','  3','       ','  4','     ','  5')
        print('Player 2')


    



    #def score(self,board,turn,stealing=True):
    def score(self):
        indices=[]
        for (index,i) in enumerate(self.player1_cups):
            if i==0:
               
                #print (index)
                indices.append(index)
        #print(indices)
        flag=0
        for i in indices:
           #3lchan lw feh aktr mn cup of zero#
         for (ind,stones) in enumerate( self.player1_cups):
            
            if i-ind > 0 :
                    #print("zero_index - l ablo")
                    x=i-ind
                    #print(x)
                    #print("stones ")
                    #print(stones)
                   
                    if i-ind ==stones:
                        cup=i-ind
                        flag=1
                    if flag==1 and self.player2_cups[i]!=0:
                        print(self.player2_cups[i])
                        score=self.player2_cups[i]
                        gain=self.player2_cups[i]
                        break
        self.mancala_cup_1+=self.player2_cups[i]
        print(self.mancala_cup_1)
        



       

        

g=Game()
#g.draw()
g.score()

        
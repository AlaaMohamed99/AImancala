from GAME import *

 def score(self):
        indices=[]
        for (index,i) in enumerate(self.player1_cups):
            if i==0:
               
                #print (index)
                indices.append(index)
        #print(indices)
        flag=0
        for i in indices:
           
           
            print(i)

        

            for (ind,stones) in enumerate( self.player1_cups):
            
            
                if i-ind > 0 :
                    #print("zero_index - l ablo")
                    x=i-ind
                    #print(x)
                    #print("stones ")
                    #print(stones)
                   
                    if i-ind ==stones:
                        flag=1
                    if flag==1 and self.player2_cups[i]!=0:
                        self.mancala_cup_1+=self.player2_cups[i]
        print(self.mancala_cup_1)
                    


             #if self.player1_cups[j-1]==1:

                 #cup = j-1
                 #print(cup)
         



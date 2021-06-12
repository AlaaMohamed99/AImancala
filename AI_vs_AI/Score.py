from GAME import *

   def score(self):
        indices=[]
        flag=0
        compressed_list=[]
        cup=0
        score=0
        for (index,i) in enumerate(self.player1_cups):
            if i==0:
               
              
                indices.append(index)
        
        
        for i in indices:
           #print(i)
        
           #3lchan lw feh aktr mn cup of zero#
          
           compressed_list.append( self.player2_cups[i])
        zero_index=self.player2_cups.index(max(self.player2_cups))

           
           #if i+1<5 and self.player2_cups[i+1]>self.player2_cups[i]:
           #    zero_index=i+1
          
        print(zero_index)




        for (ind,stones) in enumerate( self.player1_cups):
            
            if zero_index-ind > 0 :
                    #print("zero_index - l ablo")
                    x=zero_index-ind
                    #print(x)
                    #print("stones ")
                    #print(stones)
                   
                    if zero_index-ind ==stones:
                        cup=zero_index-ind
                        flag=1
                    if flag==1 and self.player2_cups[zero_index]!=0:
                        #print(self.player2_cups[i])
                        score=self.player2_cups[zero_index]
                        gain=self.player2_cups[zero_index]
                        break
        
        self.mancala_cup_1+=self.player2_cups[zero_index]
        print(self.mancala_cup_1)
        return cup, score
        

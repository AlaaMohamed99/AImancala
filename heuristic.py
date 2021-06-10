
# scoring ratio

stealing_score = 1
farther_score = 1
repeating_score = 0.8
prevent_stealing = 0.5 # * number of balls prevented from stealing  


def score_evaluation(board, turn, stealing=True):

    heu_score = [0,0,0, 0,0,0, 0 ,0,0,0, 0,0,0, 0]
    

    # heuristic ma3 panse 

    # heuristic 2 prefere again as long as total of balls in my pockets greater than or equla l 3ndo
    sum_human_player = sum(board[0:6])
    sum_ai_player = sum(board[7:])

    start = 7 if turn  ==  1 else 0

    if turn == 1 and sum_ai_player >= sum_human_player:
        # check if there is amove allows another move
        indices_again = [idx for idx in range(start, start+6) if (board[idx] == (13-idx)) or ((board[idx]-(13-idx)) % 12 == 0)]
        print (indices_again)

    elif turn == 0 and sum_ai_player <= sum_human_player:
        indices_again = [idx for idx in range(start, start+6) if (board[idx] == (6-idx)) or ((board[idx]-(6-idx)) % 12 == 0)]
        print (indices_again)

    for i in indices_again:
            heu_score[i]=1

    # heuristic 3 prefer pockets farther from the mancala (for both mode)
    far_score = farther_score
    for i in  board[(start,start+6)]:
        heu_score [i] +=  far_score
        far_score -= 0.15
   

    if stealing:
        # heuristic 4 prevent stealilng 
        #check if the opposite user can steal from me 
        opp_start = 0 if start  ==  7 else 7
        zero_idx_opp = [idx for idx in range(opp_start,opp_start+6) if board[idx]==0]
        if len (zero_idx_opp)>0:
            for idx in zero_idx_opp:
                for i in range (idx+1,opp_start+6):
                    if i-idx == board[i]:
                        if board[12-i]!=0: #the opposite pocket has balls that can be stealed
                            heu_score[12-i] = board[12-i]*prevent_stealing

    return heu_score 


print (score_evaluation([4, 4, 4, 4, 4, 4, 0, 6, 3, 3, 3, 6, 3, 0], 1, False))
stealing_score = 1.2
farther_score = 0.2
repeating_score = 1.5
prevent_stealing = 0.5  # * number of balls prevented from stealing


def score_evaluation(board, turn, stealing=True):

    heu_score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # heuristic 2 prefere again as long as total of balls in my pockets greater than or equla l 3ndo
    sum_human_player = sum(board[0:6])
    sum_ai_player = sum(board[7:13])

    start = 7 if turn == 1 else 0

    indices_again = list()
    if turn == 1 and sum_ai_player >= sum_human_player:
        # check if there is amove allows another move
        indices_again = [idx for idx in range(
            start, start+6) if (board[idx] == (13-idx)) or ((board[idx]-(13-idx)) % 12 == 0)]
    #    print (indices_again)

    elif turn == 0 and sum_ai_player <= sum_human_player:
        indices_again = [idx for idx in range(
            start, start+6) if (board[idx] == (6-idx)) or ((board[idx]-(6-idx)) % 12 == 0)]
    #    print (indices_again)

    if len(indices_again) > 0:
        for i in indices_again:
            heu_score[i] += repeating_score

    #print(f'from 1 {heu_score}')

    # heuristic 3 prefer pockets farther from the mancala (for both mode)
    for idx in range(start,start+6):
        if board[idx] != 0:
            heu_score[idx] += farther_score*(start+6-idx)
            break
    #print(f'from 3 {heu_score}')

    if stealing:
        # heuristic 1  give high weight for move causes stealing
        # figure out if there is an empty pocket
        zero_idx = [idx for idx in range(start, start+6) if board[idx] == 0]
        if len(zero_idx) > 0:  # it may be empty
            for idx in zero_idx:
                for i in range(start, idx):
                    if idx-i == board[i]:
                        if board[12-idx] != 0:  # the opposite pocket has balls that can be stealed
                            heu_score[12-idx] += board[12-idx]*stealing_score
        #print(f'from 2 {heu_score}')

        # heuristic 4 prevent stealilng
        # check if the opposite user can steal from me
        opp_start = 0 if start == 7 else 7
        ##print (opp_start)
        zero_idx_opp = [idx for idx in range(
            opp_start, opp_start+6) if board[idx] == 0]
        ##print (zero_idx_opp)
        if len(zero_idx_opp) > 0:
            for idx in zero_idx_opp:
                for i in range(opp_start, idx):
                    if idx-i == board[i]:
                        if board[12-idx] != 0:  # the opposite pocket has balls that can be stealed
                            heu_score[12-idx] += board[12-idx]*prevent_stealing
    #print(f'from 4 {heu_score}')
    #print(f'this is the max score for leaves {sum(heu_score)}')
    return sum(heu_score)


#print(score_evaluation([4, 4, 4, 4, 4, 4, 0, 5, 5, 5, 5, 0, 0, 0], 1, True))

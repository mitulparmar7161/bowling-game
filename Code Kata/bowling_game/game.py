class BowlingGameClass:
    # def normal_game(score):
    #     total = sum(score)
    #     return total

    # def multi_strike_game(score):
    #     total = 0
    #     for i in range(0,len(score)):
    #         if score[i] == 10:
    #             try:    
    #                 score[i] = score[i] + score[i+1] + score[i+2]
    #             except:
    #                 break

    #     if score[-3] >= 12:
    #         score = score[:-2]

    #     total = sum(score)    
    #     return total


    # def spare(score):
    #     total = 0
    #     for i in range(0,len(score)):
    #         try:
    #             temp = score[i] + score[i + 1] 
    #             if temp == 10:
    #                 score[i] = temp + score[i+2]
    #                 score[i+1]=0
    #         except:
    #             break
    #     score.pop(-1)    
    #     total = sum(score) 
    #     return total     
           
    def strike_spare(score):
        total = 0

        for i in range(0,len(score)):
            if score[i] == 10:
                try:    
                    score[i] = score[i] + score[i+1] + score[i+2]
                except:
                    break
        if score[-3] >= 12:
            score = score[:-2]
        total = sum(score)   
        print(score)
        print(total) 
        for i in range(0,len(score)):
            try:
                temp = score[i] + score[i + 1] 
                if temp == 10:
                    score[i] = temp + score[i+2]
                    score[i+1]=0
            except:
                break 
        if score[-1] == 30:
            score   
        elif score[-1] + score[-2] + score[-3] >= 12:
            score.pop(-1)
        total = sum(score)
        print(score)
        print(total)
        return total
    strike_spare([10,5,5,5,5,5,5,5,5,5,5,5,5,10,10,10,10,10])
    # strike_spare([10,10,10,10,10,5,5,5,5,5,5,5,5,5,5,5])
    # strike_spare([10,10,10,10,10,10,10,10,10,10,10,10])
    # strike_spare([5,5,3,2,4,2,10,3,2,1,1,3,2,3,2,3,2,3,2])

import random
def gambler(stake,goal,trial):
    t_bet=0
    t_win=0
    for i in range(trial):
        money=stake
        while(money>0 and money<goal):
            t_bet+=1
            ran_val=random.random()
            if(ran_val<0.5):
                money-=1
            else:
                money+=1
        if(money==goal):
            t_win+=1
    win_percent=(t_win/trial)*100
    loss_percent=100-win_percent

    print("Total Wins:", t_win)
    print("Win Percentage:", win_percent)
    print("Loss Percentage:", loss_percent)
   



stake = int(input("Enter Stake: "))
goal = int(input("Enter Goal: "))
trial = int(input("Enter Number of Trials: "))

gambler(stake,goal,trial)

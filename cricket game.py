#Cricket Game
import random
opt=["batting","bowling"]
numbers=[]
print("-------------------------------------------------")
print("\tWELCOME TO PLAY CRICKET WITH PYTHON")
print("-------------------------------------------------")
num=int(input("\n\tEnter the last value of play:"))
# function block 1
#------------------------------------------------------------------------------
def firstbatting(x):
    score=0
    x==score
    fscore=0
    i=0
    while(i>=0):
        print("------------------------------------------------------")
        bat=int(input("Enter your number:"))
        if bat<num+1 and bat>-1:
            ball=random.choice(numbers)
            print("The computer random value is:",ball)
            if bat!=ball:
                score+=bat
                i+=1
            elif bat==ball:
                fscore+=score
                print("------------------------------------------------------")
                print("OUTTTTTTT !!!! :((.. ..YOU HAVE SCORED :",fscore)
                print("------------------------------------------------------")
                return(fscore)
                break
        else:
            print("invalid input:(((!!!")
            exit()
def secondbatting(x,y):
    score=0
    cscore=0
    x=score
    cscore=y 
    fscore=0
    i=0
    while(i>=0):
        print("------------------------------------------------------")
        bat=int(input("Enter your number:"))
        if bat<num+1 and bat>-1:
            ball=random.choice(numbers)
            print("The computer random value is:",ball)
            if bat!=ball:
                score+=bat
                i+=1
            elif bat==ball:
                fscore+=score
                print("------------------------------------------------------")
                print("OUTTTTTTT !!!! :((.. ..YOU HAVE SCORED :",fscore)
                print("------------------------------------------------------")
                return(fscore)
                break
            if(score>cscore):
                return(score)
        else:
            print("invalid input:(((!!!")
            exit()
#--------------------------------------------------------------------------------
#function block 2
def firstbowling(x):
    score=0
    x==score
    fscore=0
    i=0
    while(i>=0):
        print("------------------------------------------------------")
        ball=int(input("Enter your number:"))
        if ball<num+1 and ball>-1:
            bat=random.choice(numbers)
            print("The computer random value is:",bat)
            if bat!=ball:
                score+=bat
            elif bat==ball:
                fscore+=score
                print("------------------------------------------------------")
                print("OUTTTTTTT !!!! :)).....YOU GOT HIS WICKET AT :",fscore)
                print("------------------------------------------------------")
                return(fscore)
                break
        else:
            print("invalid input:(((!!!")
            exit()

        i+=1
def secondbowling(x,y):
    score=0
    yscore=0
    x=score
    yscore=y
    fscore=0
    i=0
    while(i>=0):
        print("------------------------------------------------------")
        ball=int(input("Enter your number:"))
        if ball<num+1 and ball>-1:
            bat=random.choice(numbers)
            print("The computer random value is:",bat)
            if bat!=ball:
                score+=bat
            elif bat==ball:
                fscore+=score
                print("------------------------------------------------------")
                print("OUTTTTTTT !!!! :)).....YOU GOT HIS WICKET AT :",fscore)
                print("------------------------------------------------------")
                return(fscore)
            if(score>yscore):
                return(score)
        else:
            print("invalid input:(((!!!")
            exit()

        i+=1
#--------------------------------------------------------------------------------            
for i in range(0,num+1):
    numbers.append(i)
#GAME STARTS--------------------------------------------------------------------
print("\n-----------------------------------------------------------")
print("HERE ARE THE NUMBERS WHICH CAN BE USED TO PLAY THIS GAME:")
print("\n",numbers)
print("-----------------------------------------------------------")
print("NOW IT IS TIME FOR THE TOSS")
toss=int(input("\n1.ODD  \n2.EVEN \n\tchoose 1 or 2: "))
#odd is picked
if toss==1:
    call=int(input("ENTER A NUMBER FOR THE TOSS:"))
    if call<num+1 and num>-1:
        rnum =random.choice(numbers)
        print("--------------------------------------------------")
        print("Your value for the toss is  ",call)
        print("The computer's Random value for the toss is ",rnum)    
        sum=rnum+ call 
    else:
        print("invalid input!!!:(")
        exit()
#-------------------------------------------------------------------------------
#odd is picked and the toss is won by the user.
    if sum %2!=0:
        print("The computer's value and yours is=",sum)
        print("YOU WON THE TOSS!! :):)")
        print("--------------------------------------------------")
#--------------------------------------------------------------------------------
#user decides whether to bat or bowl.
        print("WHAT ARE YOU GOING TO DECIDE :\n1.Batting\n2.bowling")
        des=int(input("\tchoose 1 or 2"))
#user decides to bat first ..
        if des==1:
            batscore=firstbatting(0)
            print("------------------------------------------------------")
            print("YOU HAVE SCORED ",batscore,"WHILE YOU ARE BATTING ./")
            print("YOU HAVE TO DEFEND ",batscore,"TO WIN THE MATCH.")
            print("YOU ARE GOING TO BOWL NOW...BE READY WITH YOU BALL:))")
            print("------------------------------------------------------")
            ballscore=secondbowling(0,batscore)
            print("YOU HAVE CONCEDED",ballscore,"WHILE YOU ARE BOWLING ./")
            print("------------------------------------------------------")
            if batscore>ballscore:
                dif=batscore-ballscore
                print("YOU HAVE WON THE MATCH BY ",dif,"RUNS :))\nYOU HAVE DEFENDED:",batscore)
            
            elif batscore < ballscore:
                dif=ballscore-batscore
                print("YOU LOST THE MATCH TO THE COMPUTER :(( FAILD TO DEFEND:",batscore)
                print("BETTER LUCK NEXT TIME :))")

            elif batscore == ballscore:
                print("THE MATCH HAVE BEEN DRAWN :))")
#-------------------------------------------------------------------------------------------                
#user decides to bowl first..        
        elif des==2:
            ballscore=firstbowling(0)
            print("------------------------------------------------------")
            print("YOU HAVE CONCEDED",ballscore,"WHILE YOU ARE BOWLING ./")
            print("YOU HAVE TO SCORE ",ballscore+1,"TO WIN THE MATCH.")
            print("YOU ARE GOING TO BAT NOW...BE READY WITH YOU BAT:))")
            print("------------------------------------------------------")

            batscore=secondbatting(0,ballscore)
            print("YOU HAVE SCORED ",batscore,"WHILE YOU ARE BATTING ./")
            print("------------------------------------------------------")
            if batscore>ballscore:
                dif=batscore-ballscore
                print("YOU HAVE WON THE MATCH :))\nYOU HAVE CHASED DOWN",ballscore)
            
            elif batscore < ballscore:
                dif=ballscore-batscore
                print("YOU LOST THE MATCH :((( YOU FAILD TO CHACE DOWN:",ballscore)
                print("BETTER LUCK NEXT TIME :))")

            elif batscore == ballscore:
                print("THE MATCH HAVE BEEN DRAWN :))")
 
#user gives a wrong input or value ..            
        else:
            print("INVALID INPUT !! :((")
            exit()

#the odd is picked in toss but lost,then computer wins the toss
            
    else:
        print("The computer's value and yours is=",sum)
        print("YOU LOST THE TOSS!! :((")
        rtoss = random.choice(opt)
#----------------------------------------------------------------------------------------------
#The computer decide whether to bat or bowl.. 
        print("THE COMPUTER HAVE WON THE TOSS AND ELECTED TO ",rtoss,"FIRST")
        if rtoss=="bowling":
            print("YOU ARE GOING TO BAT NOW...BE READY WITH YOUR BAT:))")
            batscore=firstbatting(0)
            print("------------------------------------------------------") 
            print("YOU HAVE SCORED ",batscore,"WHILE YOU ARE BATTING ./")
            print("YOU HAVE TO DEFEND ",batscore,"TO WIN THE MATCH.")
            print("YOU ARE GOING TO BOWL NOW...BE READY WITH YOU BALL:))")
            print("------------------------------------------------------")
            ballscore=secondbowling(0,batscore)
            print("YOU HAVE CONCEDED",ballscore,"WHILE YOU ARE BOWLING ./")
            print("------------------------------------------------------")
            if batscore>ballscore:
                dif=batscore-ballscore
                print("YOU HAVE WON THE MATCH :))\nYOU HAVE DEFENDED:",batscore)
            
            elif batscore < ballscore:
                dif=ballscore-batscore
                print("YOU LOST TO THE COMPUTER BY",dif,"RUNS :((")
                print("BETTER LUCK NEXT TIME :))")

            elif batscore == ballscore:
                print("THE MATCH HAVE BEEN DRAWN :))")
        elif rtoss=="batting":
            print("YOU ARE GOING TO FIELD NOW...BE READY WITH YOUR BALL:))")
            ballscore=firstbowling(0)
            print("------------------------------------------------------")
            print("YOU HAVE CONCEDED",ballscore,"WHILE YOU ARE BOWLING ./")
            print("YOU HAVE TO SCORE ",ballscore+1,"TO WIN THE MATCH.")
            print("YOU ARE GOING TO BAT NOW...BE READY WITH YOU BAT:))")
            print("------------------------------------------------------")

            batscore=secondbatting(0,ballscore)
            print("YOU HAVE SCORED ",batscore,"WHILE YOU ARE BATTING ./")
            print("------------------------------------------------------")
            if batscore>ballscore:
                dif=batscore-ballscore
                print("YOU HAVE WON THE MATCH BY ",dif,"RUNS :))\nYOU HAVE CHASED DOWN:",ballscore)
            
            elif batscore < ballscore:
                dif=ballscore-batscore
                print("YOU LOST TO THE COMPUTER :(( YOU FAILD TO CHASE DOWN:",ballscore)
                print("BETTER LUCK NEXT TIME :))")

            elif batscore == ballscore:
                print("THE MATCH HAVE BEEN DRAWN :))")
            
#---------------------------------------------------------------------------------------------
#user picks even number in the toss        
elif toss==2:
    call=int(input("ENTER A NUMBER FOR THE TOSS:"))
    if call <num+1 and num>-1:
        rnum =random.choice(numbers)
        print("Your value for the toss is  ",call)
        print("The computer's Random value for the toss is ",rnum)
        sum=rnum+ call 
    else:
        print("invalid input!!!:(")
#user wins the toss
    if sum%2==0:
        print("YOU WON THE TOSS!! :):)")
        print("--------------------------------------------------")
#--------------------------------------------------------------------------------
#user decides whether to bat or bowl.
        print("WHAT ARE YOU GOING TO DECIDE :\n1.Batting\n2.bowling")
        des=int(input("\tchoose 1 or 2"))
#user decides to bat first ..
        if des==1:
            batscore=firstbatting(0)
            print("------------------------------------------------------")
            print("YOU HAVE SCORED ",batscore,"WHILE YOU ARE BATTING ./")
            print("YOU HAVE TO DEFEND ",batscore,"TO WIN THE MATCH.")
            print("YOU ARE GOING TO BOWL NOW...BE READY WITH YOU BALL:))")
            print("------------------------------------------------------")
            ballscore=secondbowling(0,batscore)
            print("YOU HAVE CONCEDED",ballscore,"WHILE YOU ARE BOWLING ./")
            print("------------------------------------------------------")
            if batscore>ballscore:
                dif=batscore-ballscore
                print("YOU HAVE WON THE MATCH :))\nYOU HAVE DEFENDED:",batscore)
            
            elif batscore < ballscore:
                dif=ballscore-batscore
                print("YOU LOST TO THE COMPUTER BY",dif,"RUNS :((")
                print("BETTER LUCK NEXT TIME :))")

            elif batscore == ballscore:
                print("THE MATCH HAVE BEEN DRAWN :))")
#-------------------------------------------------------------------------------------------                
#user decides to bowl first..        
        elif des==2:
            ballscore=firstbowling(0)
            print("------------------------------------------------------")
            print("YOU HAVE CONCEDED",ballscore,"WHILE YOU ARE BOWLING ./")
            print("YOU HAVE TO SCORE ",ballscore+1,"TO WIN THE MATCH.")
            print("YOU ARE GOING TO BAT NOW...BE READY WITH YOU BAT:))")
            print("------------------------------------------------------")

            batscore=secondbatting(0,ballscore)
            print("YOU HAVE SCORED ",batscore,"WHILE YOU ARE BATTING ./")
            print("------------------------------------------------------")
            if batscore>ballscore:
                dif=batscore-ballscore
                print("YOU HAVE WON THE MATCH BY ",dif,"RUNS :))\nYOU HAVE CHASED DOWN:",ballscore)
            
            elif batscore < ballscore:
                dif=ballscore-batscore
                print("YOU LOST TO THE COMPUTER :(( YOU FAILD TO CHASE DOWN:",ballscore)
                print("BETTER LUCK NEXT TIME :))")

            elif batscore == ballscore:
                print("THE MATCH HAVE BEEN DRAWN :))")
 
#user gives a wrong input or value ..            
        else:
            print("INVALID INPUT !! :((")
            exit()
#--------------------------------------------------------------------------------------------
        
#user loss the toss
    else:
        print("YOU LOST THE TOSS!! :((")
        rtoss = random.choice(opt)
#----------------------------------------------------------------------------------------------
#The computer decide whether to bat or bowl.. 
        print("THE COMPUTER HAVE WON THE TOSS AND ELECTED TO ",rtoss,"FIRST")
        if rtoss=="bowling":
            print("YOU ARE GOING TO BAT NOW...BE READY WITH YOUR BAT:))")
            batscore=firstbatting(0)
            print("------------------------------------------------------") 
            print("YOU HAVE SCORED ",batscore,"WHILE YOU ARE BATTING ./")
            print("YOU HAVE TO DEFEND ",batscore,"TO WIN THE MATCH.")
            print("YOU ARE GOING TO BOWL NOW...BE READY WITH YOU BALL:))")
            print("------------------------------------------------------")
            ballscore=secondbowling(0,batscore)
            print("YOU HAVE CONCEDED",ballscore,"WHILE YOU ARE BOWLING ./")
            print("------------------------------------------------------")
            if batscore>ballscore:
                dif=batscore-ballscore
                print("YOU HAVE WON THE MATCH :))\nYOU HAVE DEFENDED:",batscore)
            
            elif batscore < ballscore:
                dif=ballscore-batscore
                print("YOU LOST TO THE COMPUTER BY",dif,"RUNS :((")
                print("BETTER LUCK NEXT TIME :))")

            elif batscore == ballscore:
                print("THE MATCH HAVE BEEN DRAWN :))")
        elif rtoss=="batting":
            print("YOU ARE GOING TO FIELD NOW...BE READY WITH YOUR BALL:))")
            ballscore=firstbowling(0)
            print("------------------------------------------------------")
            print("YOU HAVE CONCEDED",ballscore,"WHILE YOU ARE BOWLING ./")
            print("YOU HAVE TO SCORE ",ballscore+1,"TO WIN THE MATCH.")
            print("YOU ARE GOING TO BAT NOW...BE READY WITH YOU BAT:))")
            print("------------------------------------------------------")

            batscore=secondbatting(0,ballscore)
            print("YOU HAVE SCORED ",batscore,"WHILE YOU ARE BATTING ./")
            print("------------------------------------------------------")
            if batscore>ballscore:
                dif=batscore-ballscore
                print("YOU HAVE WON THE MATCH BY ",dif,"RUNS :))\nYOU HAVE CHASED DOWN:",ballscore)
            
            elif batscore < ballscore:
                dif=ballscore-batscore
                print("YOU LOST TO THE COMPUTER :(( YOU FAILD TO CHASE DOWN:",ballscore)
                print("BETTER LUCK NEXT TIME :))")

            elif batscore == ballscore:
                print("THE MATCH HAVE BEEN DRAWN :))")
#user gives an invalid input.       
else:
    print("INVALID INPUT !! :((")
    exit()

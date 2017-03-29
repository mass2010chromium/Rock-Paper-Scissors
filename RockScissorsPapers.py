#***********************************************************#
#********************Name: Rock04.py************************#
#********************Author: Derek Li******************#
#***********************************************************#

import random
c = ["rock","paper","scissors"]
rep = 1
lwr = 0
upr = 2
result1 = " wins the Round"
result2 = "The round is a tie"
m1 = "Student A"
m2 = "Student B"
aRoundWins = 0
bRoundWins = 0
aGameWins = 0
bGameWins = 0
gameTies = 0
aWin = 0
bWin = 0
tie = 0
print "*" * 43
print "*"
print "*      WELCOME TO ROCK, PAPER, SCISSORS       "
print "*"
print "*" * 43
print
while rep == 1:
    print "1)Play ROCK,PAPER,SCISSORS"
    print "2)Quit"
    rep = input("Please enter a choice --> ")
    if rep == 1:
        x = 1
        maxRounds = input("Please Enter Number of Rounds --> ")
        while x <= maxRounds:
            print 
            aChoice = random.randint(lwr,upr)
            print "Round "+ str(x) + ": " + m1 + " throws " + c[aChoice]
            bChoice = random.randint(lwr,upr)
            print "Round "+ str(x) + ": " + m2 + " throws " + c[bChoice]
            x = x + 1
            if aChoice == 1 and bChoice == 0:
                print m1 + str(result1)
                aWin = aWin + 1
                aRoundWins = aRoundWins + 1
            if aChoice == 0 and bChoice == 2:
                print m1 + str(result1)
                aWin = aWin + 1
                aRoundWins = aRoundWins + 1
            if aChoice == 2 and bChoice == 1:
                print m1 + str(result1)
                aWin = aWin + 1
                aRoundWins = aRoundWins + 1
            if bChoice == 1 and aChoice == 0:
                print m2 + str(result1)
                bWin = bWin + 1
                bRoundWins = bRoundWins + 1
            if bChoice == 0 and aChoice == 2:
                print m2 + str(result1)
                bWin = bWin + 1
                bRoundWins = bRoundWins + 1
            if bChoice == 2 and aChoice == 1:
                print m2 + str(result1)
                bWin = bWin + 1
                bRoundWins = bRoundWins + 1
            if aChoice == bChoice:
                print str(result2)
                tie = tie + 1
        if aWin > bWin:
            aGameWins = aGameWins + 1
        if bWin > aWin:
            bGameWins = bGameWins + 1
        if aWin == bWin:
            gameTies = gameTies + 1
        awin = 0
        bwin = 0
        
        print
    else:
        print
        print "             ROUND STATS        GAME STATS"
        print "Player       W    L    T   ||   W    L    T"
        print "-" * 45
        print m1 + "    " + str(aRoundWins) + "    " + str(bRoundWins) + "    " + str(tie) + "   ||   " + str(aGameWins) + "    " + str(bGameWins) + "    " + str(gameTies)
        print m2 + "    " + str(bRoundWins) + "    " + str(aRoundWins) + "    " + str(tie) + "   ||   " + str(bGameWins) + "    " + str(aGameWins) + "    " + str(gameTies)
        print
        print "Thanks for Playing ROCK,PAPER,SCISSORS. Goodbye."

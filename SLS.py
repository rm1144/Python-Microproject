from random import randint
t = ["Spock", "Lizard", "Scissors"]
computer = t[randint(0,2)]
player = False
a="Spock"
b="Lizard"
c="Scissors"
d="d"
m=0
n=0
print"\n\t# SPOCK , LIZARD , SCISSORS #"
print("\n**Type the option code**")
print("**TYPE d TO EXIT**")
print"\n*SCORE*\n+1 for winning\n-1 for losing\n 0 for tie"
while m<5 and n<5:
    player = input("\na:Spock, b:Lizard, c:Scissors : \n")
    if player == computer:
        print"\nYOU : ",player,"\tCOMPUTER : ",computer
        print"\n*Tie!*"
        print"\nYour score is ",m
        print"Computers score is",n
        print" "
        if m==5 :
            print "\n\tYOU WIN\n"
        elif n==5:
            print"\n\tYOU LOSE\n"
	player = False
    	computer = t[randint(0,2)]
    elif player == a:
        if computer == b:
            print"\nYOU : ",player,"\tCOMPUTER : ",computer
            print"\n*You lose!", computer, "poisons the", player,"*"
            n+=1
            print"\nComputers  score is ",n
            print"Your score is ",m
            print" "    
            if m==5 :
    	        print "\n\tYOU WIN\n"
            elif n==5:
    	        print"\n\tYOU LOSE\n"
            
	    player = False
  	    computer = t[randint(0,2)]
        else:
            print"\nYOU : ",player,"\tCOMPUTER : ",computer
            print"\n*You win!", player, "smashes the", computer,"*"
            m+=1
            print"\nComputers  score is ",n
            print"Your score is" ,m
            print" " 
            if m==5 :
    	         print "\n\tYOU WIN\n"
            elif n==5:
    	         print"\n\tYOU LOSE\n"
            
	    player = False
            computer = t[randint(0,2)]
    elif player == b:
        if computer == c:
            print"\nYOU : ",player,"\tCOMPUTER : ",computer
            print"\n*You lose!", computer, "decapitates the ", player,"*"
            n+=1
            print"\nComputer  score is ",n
            print"Your score is ",m
            print" "   
            if m==5 :
    	          print "\n\tYOU WIN\n"
            elif n==5:
    	          print"\n\tYOU LOSE\n"
           
	    player = False
            computer = t[randint(0,2)]
        else:
            print"\nYOU : ",player,"\tCOMPUTER : ",computer
            print"\n*You win!", player, "poisons the", computer,"*"
            m+=1
            print"\nComputer score is ",n
            print"Your score is ",m
            print" "  
            if m==5 :
    	        print "\n\tYOU WIN\t"
            elif n==5:
    	        print"\tYOU LOSE\n"
            
	    player = False
            computer = t[randint(0,2)]
    elif player == c:
        if computer == a:
            print"\nYOU : ",player,"\tCOMPUTER : ",computer
            print"\n*You lose...", computer, "smashes the ", player,"*"
            n+=1
            print"\nComuter score is ",n
            print"Your score is ",m
            print" "   
            if m==5 :
                print "\n\tYOU WIN\n"
            elif n==5:
    	        print"\n\tYOU LOSE\n"
            
	    player = False
            computer = t[randint(0,2)]
        else:
            print"\nYOU : ",player,"\tCOMPUTER : ",computer
            print"\n*You win!", player, "decapitates the", computer,"*"
            m+=1
            print"\nComputer score is ",n
            print "Your score is ",m
            print" "    
            if m==5 :
    	         print "\n\tYOU WIN\n"
            elif n==5:
    	         print"\n\tYOU LOSE\n"
           
	    player = False
            computer = t[randint(0,2)]
   
    elif player == d:
            print"\n\tYOUR TOTAL SCORE = ",m," \n"
            print"COMPUTERS SCORE= ",n
            print"\t**End of the game**\n\t**Thank You**\n\t**Play Again**"
            player!= False
 

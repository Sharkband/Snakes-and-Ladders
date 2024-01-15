#Lucas drennan
#comp1405_f22_101259409_assignment_06.py

import pygame
import random
#information about the game
#red square is finish line
#black squares are extra turns
#ladder will move you ahead

print("Each player will roll until one passes the red square there is a ladder that will transfer you")
print("and black squares that give you an extra turn")
print("there are two dice one rolls 1-6 and the second rolls 1-3")

#I made global varibles becuase it was more effiecent since I dont have a main() 
#also because this assignment does not require funtions
w_in_squares = 8
h_in_squares = 9

square_dim = 50

drawing_window = pygame.display.set_mode((h_in_squares*square_dim, w_in_squares*square_dim))

#my game board funtion that creates the game board with checker tiles 
#aswell as ladder and black squares and finish line
#I call this funtion when ever I want to re draw the players
def game_board():
    
    drawing_window.fill((127, 127, 127))

    the_colour_white = (255, 255, 255)
    the_colour_black = (255,   0,100)

    current_colour = the_colour_white
    
    #making grid for 9x8
    for i in range(0, h_in_squares):
        for j in range(0, w_in_squares):
            pygame.draw.rect(drawing_window, current_colour, (i * square_dim, j * square_dim, square_dim, square_dim))
            pygame.display.update()	
            if current_colour == the_colour_white:
                current_colour = the_colour_black
            else:
                current_colour = the_colour_white
        if current_colour == the_colour_white:
            current_colour = the_colour_black
        else:
            current_colour = the_colour_white
    #Drawing the ladder for my game using lines      
    pygame.draw.line(drawing_window, (10,10,10), (160,140), (210,310), 10)
    pygame.draw.line(drawing_window, (10,10,10), (190,140), (240,310), 10)
    pygame.draw.line(drawing_window, (10,10,10), (160,150), (190,150), 9)
    pygame.draw.line(drawing_window, (10,10,10), (175,190), (205,190), 9)
    pygame.draw.line(drawing_window, (10,10,10), (185,230), (215,230), 9)
    pygame.draw.line(drawing_window, (10,10,10), (200,270), (230,270), 9)
    pygame.draw.line(drawing_window, (10,10,10), (210,300), (240,300), 9)
    #drawing double turn sqaures 
    pygame.draw.rect(drawing_window, (1,1,1), (300,50, square_dim, square_dim))
    pygame.draw.rect(drawing_window, (1,1,1), (50,300, square_dim, square_dim))
    #drawing finish line
    pygame.draw.rect(drawing_window, (255,1,1), (400,350, square_dim, square_dim))
    pygame.display.update()

#dice one funtion 1-6
def dice_1():
    random1 = random.randint(1,6)
    return random1
    
#dice two funtion 1-3    
def dice_2():
    random2 = random.randint(1,3)
    return random2
    
#varible for while loop   
x=True
#varibles for player1 and player2 x,y values or Width and Hieght
player1_H=0
player1_W=0
player2_H=0
player2_W=0

#count is for the player turn
count=0
 
#setting up game board and drawing players on thier starting positions 
game_board()
pygame.draw.circle(drawing_window, (0,0,255), (12,12), 5)
pygame.draw.circle(drawing_window, (0,255,0), (32,32), 5)
pygame.display.update() 

#my main while loop for the game       
while(x):
    #added timer so the game does not finish so fast and you can watch it 
    pygame.time.delay(1000)
    
    #if count is even its player one turn if its odd its player2 turn thats how I did turns
    if(count%2==0):
        print("Player one's turn")
        roll=dice_1()
        roll2=dice_2()
        #reseting board
        game_board()
        #rolling both dice then adding them together to get total roll
        player1_W += (roll + roll2)
        #after player1 reaches a certain width they must go down 
        #so +1 to hieght and -9 to thier width becuase it starts at 0
        if(player1_W > 8):
            player1_H += 1
            player1_W -= 9
        #drawing player1 if they moved and player2 stays
        pygame.draw.circle(drawing_window, (0,0,255), (12+(player1_W*square_dim),12+(player1_H*square_dim)), 5)
        pygame.draw.circle(drawing_window, (0,255,0), (32+(player2_W*square_dim),32+(player2_H*square_dim)), 5)
        pygame.display.update()
        #printing roll for each dice
        print("Player one rolled a "+str(roll)+ " and a "+str(roll2))
    else:
        print("Player two's turn")
        roll=dice_1()
        roll2=dice_2()
        #reseting board
        game_board()
        #rolling both dice then adding them together to get total roll
        player2_W += (roll + roll2)
        #after player2 reaches a certain width they must go down 
        #so +1 to hieght and -9 to thier width becuase it starts at 0
        if(player2_W > 8):
            player2_H += 1
            player2_W -= 9
        #drawing player2 if they moved and player1 stays
        pygame.draw.circle(drawing_window, (0,255,0), (32+(player2_W*square_dim),32+(player2_H*square_dim)), 5)
        pygame.draw.circle(drawing_window, (0,0,255), (12+(player1_W*square_dim),12+(player1_H*square_dim)), 5)
        pygame.display.update()
        #printing roll for each dice
        print("Player two rolled a "+str(roll)+ " and a "+str(roll2))
        
        
        
        #checking to see if the players are on the ladder using the width and hieght
        #if they are then send them to a new width and height
    if(player1_W==3 and player1_H==2):
        print("Player one landed on a ladder")
        game_board()
        player1_W = 4
        player1_H = 6
        #redrawing player1
        pygame.draw.circle(drawing_window, (0,0,255), (12+(player1_W*square_dim),12+(player1_H*square_dim)), 5)
        pygame.draw.circle(drawing_window, (0,255,0), (32+(player2_W*square_dim),32+(player2_H*square_dim)), 5)
        pygame.display.update()
        #for player2
    if(player2_W==3 and player2_H==2):
        print("Player two landed on a ladder")
        game_board()
        player2_W = 4
        player2_H = 6
        #redrawing player2
        pygame.draw.circle(drawing_window, (0,0,255), (12+(player1_W*square_dim),12+(player1_H*square_dim)), 5)
        pygame.draw.circle(drawing_window, (0,255,0), (32+(player2_W*square_dim),32+(player2_H*square_dim)), 5)
        pygame.display.update()
        
        
        
        #checking to see if players are on black squares
        #if they are then add an extra turn using same logic as a normal turn
    if((player1_W==6 and player1_H==1) or (player1_W==1 and player1_H==6)):
        print("Player one landed on a extra turn")
        roll=dice_1()
        roll2=dice_2()
        #reset board
        game_board()
        player1_W += (roll + roll2)
        if(player1_W > 8):
            player1_H += 1
            player1_W -= 9
        #draw players
        pygame.draw.circle(drawing_window, (0,255,0), (32+(player2_W*square_dim),32+(player2_H*square_dim)), 5)
        pygame.draw.circle(drawing_window, (0,0,255), (12+(player1_W*square_dim),12+(player1_H*square_dim)), 5)
        pygame.display.update()
        print("Player one rolled a "+str(roll)+ " and a "+str(roll2))
        #for player2    
    if((player2_W==6 and player2_H==1) or (player2_W==1 and player2_H==6)):
        print("Player two landed on a extra turn")
        roll=dice_1()
        roll2=dice_2()
        #reset board
        game_board()
        player2_W += (roll + roll2)
        if(player2_W > 8):
            player2_H += 1
            player2_W -= 9
        #draw players
        pygame.draw.circle(drawing_window, (0,255,0), (32+(player2_W*square_dim),32+(player2_H*square_dim)), 5)
        pygame.draw.circle(drawing_window, (0,0,255), (12+(player1_W*square_dim),12+(player1_H*square_dim)), 5)
        pygame.display.update()
        print("Player two rolled a "+str(roll)+ " and a "+str(roll2))
        
    #checking to see if the player one if they pass the red square they win
    #so if they hieght it 8 or greater they won
    #also ends the while loop
    if(player1_H >=8):
        print("player one Wins")
        x=False
    if(player2_H >=8):
        print("player two Wins")
        x=False
    #couting +1 for the player turn
    count += 1
    

#this while loop is for when you want to exit the game using the x in the top right		
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
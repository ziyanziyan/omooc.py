# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import math
import random

msg = "Guessing number!"

# initialize global variables used in your code here
#num_range = 100


# helper function to start and restart the game
#def new_game():
 #   print "let's play the number guessing game!"
    
# define event handlers for control panel
#def range100():
    # button that changes the range to [0,100) and starts a new game 


#def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    

    
#def input_guess(guess):
    # main game logic goes here	
    
    

# create frame
f = simplegui.create_frame("Guess a number", 300, 200)

# Parts of the frame
window_name = "Guess a number"
canvas_width = 200
canvas_height = 300
f.set_canvas_background("White")
def draw(canvas):
    canvas.draw_text(msg, [40,100], 30, "pink")

f.set_draw_handler(draw)

# create control elements
#frame.add_button("Input a number between 0 and 100", range100, 200)
#frame.add_button("Input a number between 0 and 1000", range1000, 200)
#frame.add_input("Enter a guess", input_guess, 200)




#new_game()
    


# register event handlers for control elements and start frame


# call new_game 
#new_game()


# always remember to check your completed program against the grading rubric
f.start()
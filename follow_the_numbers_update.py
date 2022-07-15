import pgzrun, random, math
"""Project No. Follow the Numbers 
Ten dots appear at random positions, each with a number next to it. Click on the dots in the correct order to connect them.
The game will finish once all of the dots are connected. If you make a mistake, all the lines will disapear and you will
have to start over again 

would this project be an introduction to arrays? 

Hacks and Tweaks 

add more dots 

create a "next level"

set the number of attempts and print out "game over"

make a function so that the dots do not overlap the previous one 


"""

#set our vars
WIDTH = 400  #declaring global vairables to set the screen size in pixels
HEIGHT = 400


dots = [] #will be a list of actors
lines = []
next_dot = 0
current_dot=0
attempts = 3
end_game = False



def place_dots(actor,index):
    global dots
    actor.pos = random.randint(20, WIDTH - 20), random.randint(20, HEIGHT - 20)

    x1 = actor.pos[0]
    y1 = actor.pos[1]

    for i in range(len(dots)-1): #subtract one because you don't need current dot to compare its position to itself
        x2 = dots[i].pos[0]
        y2 = dots[i].pos[1]
        dist = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
        #print("========="+str(dist))
        while True:
            if dist<100:
                actor.pos = random.randint(20, WIDTH - 20), random.randint(20, HEIGHT - 20)
                new_x=actor.pos[0]
                new_y = actor.pos[1]
                dist = math.sqrt(math.pow(x2 - new_x, 2) + math.pow(y2 - new_y, 2))
                #print(dist)
            else:
                break


def draw():
    screen.fill("black")
    screen.draw.text("Attempts: {}".format(attempts), color="white",topleft=(10,10))
    number = 1

    #draw the dots
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0],dot.pos[1]+12))#dot.pos[0] => is the x coord and dot.pos[1] is the y coord. pos is a list of [x,y]
        dot.draw()
        number +=1

    #draw the lines
    for line in lines:
        screen.draw.line(line[0],line[1], (100,0,0)) #line function line(x,y,(rgb values))

    if end_game:
        screen.clear()
        screen.draw.text('Game Over', color='white', topleft=((WIDTH/2)-40,HEIGHT/2))

def on_mouse_down(pos):
    global next_dot, lines, current_dot, attempts

    if dots[current_dot].collidepoint(pos):
        if current_dot == 0: #if user clicks on the 1 dot, dont do anythhing
            pass
        else: # anything but the first dot, append new line
            lines.append((dots[current_dot-1].pos, dots[current_dot].pos))
        current_dot += 1
    else:
        #user connected incorrectly
        lines=[]
        current_dot=0
        attempts-=1
        if attempts == 0:
            game_over()
    print(current_dot)
    if current_dot == len(dots):  # you reached the last dot
        print("look here")
        next_level()

def game_over():
    global end_game
    end_game = True

def next_level():
    global current_dot,lines,dots
    lines = []
    current_dot=0
    dots = []

    for i in range(0, 15):
        actor = Actor("dot")
        actor.pos = random.randint(20, WIDTH - 20), random.randint(20, HEIGHT - 20)
        dots.append(actor)  # add this actor object to our list
        if i != 0:
            place_dots(actor, i)



#MAIN FUNCTION 1ST LEVEL
for i in range (10):
    actor = Actor("dot")
    #actor.pos = random.randint(20, WIDTH-20), random.randint(20,HEIGHT-20)
    dots.append(actor) #add this actor object to our list
    if i!=0:
        place_dots(actor,i)


pgzrun.go()
import pgzrun, random
"""Project No. Follow the Numbers 
Ten dots appear at random positions, each with a number next to it. Click on the dots in the correct order to connect them.
The game will finish once all of the dots are connected. If you make a mistake, all the lines will disapear and you will
have to start over again 

would this project be an introduction to arrays? 
"""

#set our vars
WIDTH = 400  #declaring global vairables to set the screen size in pixels
HEIGHT = 400


dots = [] #will be a list of actors
lines = []
next_dot = 0

#set up the actors with a list
for dot in range (0,10):
    actor = Actor("dot")
    actor.pos = random.randint(20, WIDTH-20), random.randint(20,HEIGHT-20)
    dots.append(actor) #add this actor object to our list

def draw():
    screen.fill("black")
    number = 1

    #draw the dots
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0],dot.pos[1]+12))#dot.pos[0] => is the x coord and dot.pos[1] is the y coord. pos is a list of [x,y]
        dot.draw()
        number +=1

    #or
    """for i in range(dots.len):
        screen.draw.text(i+1,(dot.pos[0],dot.pos[1]+12))
        dot.draw()"""

    #draw the lines
    for line in lines:
        screen.draw.line(line[0],line[1], (100,0,0)) #line function line(x,y,(rgb values))

def on_mouse_down(pos):
    global next_dot
    global lines
    print(lines)
    print(next_dot)
    #if mouse position is on the next dot in the sequencef
    if dots[next_dot].collidepoint(pos):

        if next_dot: # an integer as a conditional? Still confused but basically means once the mosue clicks on the dot, if statement checks if the player clicked on the first dot
            print("next dot {}".format(next_dot))
            lines.append( (dots[next_dot-1].pos,dots[next_dot].pos) )
            #print (lines[len(lines)-1])
        next_dot+=1
    else: #start over
        lines = []
        next_dot=0
    #print (lines) [((326.0, 169.0), (322.0, 172.0)), ((322.0, 172.0), (193.0, 216.0)), ((193.0, 216.0), (77.0, 309.0))]
    #the lines [] is a list of lists that contain two coordiante pairs [ [ [0],[0] ], [ [0],[[0] ]   ]
def update():
    pass



pgzrun.go()
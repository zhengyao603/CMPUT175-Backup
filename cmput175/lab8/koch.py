import turtle

def Koch(length, order):
    '''
    order 0 Koch is just a straight line
    '''
    if order == 0:
        turtle.forward(length)
    else:
        '''
        TODO:
        make recursive calls to do the drawing
        order d Koch is composed of 4 of order (d-1) Koch
        '''
        Koch(length / 3, order - 1)
        turtle.left(60)
        Koch(length / 3, order - 1)
        turtle.right(120)
        Koch(length / 3, order - 1)
        turtle.left(60)
        Koch(length / 3, order - 1)


#test
def main():
    turtle.setworldcoordinates(-1, -1, 150, 150)
    turtle.penup()
    turtle.goto(10,70)
    turtle.pendowns()
    Koch(120, 3)
    turtle.mainloop()  
    
main()
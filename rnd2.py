def solution(x,y):
    '''
    ________Part 1_________________
    Missed grabbing the exact question and copying my solution, 
    but it had to do with finding the correct value based on a 2d array
    
    |7|
    |4|8|
    |2|5|9|
    |1|3|6|10|
    '''
    #col 1:
        #y*(y-1)/2 + 1
        #row 1: 1*(1-1)/2 + 1
        #row 2: 2*(2-1)/2 + 1
    #col 2:
        #((y+1) * (y+0))/2 + 2
        #row 1: ((1+1) * (1+0))/2 + 2
        #row 2: ((2+1) * (2+0))/2 + 2
        #row 3: ((3+1) * (3+0))/2 + 2
    
    #x is horizontal position, y is vertical, so

    #normalize:(x + (y-1)) * ((x-1) + (y-1))/2 + x

    return str(x + ((x+y-1) * (x+y-2)) / 2)


def solution2(string):
    '''
    Write a program that counts how many salutes are exchanged during a typical walk along a hallway. 
    The hall is represented by a string. For example:
"--->-><-><-->-"

Each hallway string will contain three different types of characters: '>', an employee walking to the right; 
'<', an employee walking to the left; and '-', an empty space. Every employee walks at the same speed either 
to right or to the left, according to their direction. Whenever two employees cross, each of them salutes the other. 
They then continue walking until they reach the end, finally leaving the hallway. In the above example, they salute 10 times.

Write a function solution(s) which takes a string representing employees walking along a hallway and returns the number 
of times the employees will salute. s will contain at least 1 and at most 100 characters, each one of -, >, or <.
    '''


    #It's really a matter of calculating combinations of >< in order
    #A simple way could be to loop through the list and count left facing and right facing in order
    #We would want to restart this count each time we come to a < character
    
    
    salutes = 0
    
    r = 0
    for i in string:
        if i == ">":
            r += 1
        elif i == "-":
            continue
        elif r == 0:
            string.replace(i, '-', 1)
        else:
            salutes += r*2
    
    return salutes

    
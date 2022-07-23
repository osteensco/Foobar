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
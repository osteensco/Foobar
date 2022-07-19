# There's some unrest in the minion ranks: minions with ID numbers like "1", "42", and other "good" numbers have been lording it over the poor minions who are stuck with more boring IDs. To quell the unrest, Commander Lambda has tasked you with reassigning everyone new random IDs based on a Completely Foolproof Scheme. 

# Commander Lambda has concatenated the prime numbers in a single long string: "2357111317192329...". Now every minion must draw a number from a hat. That number is the starting index in that string of primes, and the minion's new ID number will be the next five digits in the string. So if a minion draws "3", their ID number will be "71113". 

# Help the Commander assign these IDs by writing a function solution(n) which takes in the starting index n of Lambda's string of all primes, and returns the next five digits in the string. Commander Lambda has a lot of minions, so the value of n will always be between 0 and 10000.





def solution(i):
    """
    For some reason the Commander isn't providing me with this string? Seems ineffecient but ok boss.
    Since I have to create the string myself, I need a function that determines if a given int is a prime number.
    I know that n will always be between 0 and 10000, so my max length of this string will be 10000. 
    I can then use my prime function to find prime numbers and concatenate each to my string until I reach the max length. 
    Then it's as easy as slicing the string based on input i to get the unique id.
    """
    def prime(n):
        for x in range(2,n):
            if n % x == 0:
                return False
        return True
        
    s = ""
    y = 2
    while True:
        if prime(y):
            s += str(y)
        if len(s) < 10000:
            y += 1
        else:
            break
    
    return s[i:i+5]

print(solution(3))
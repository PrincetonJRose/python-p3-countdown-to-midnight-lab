# your code goes here!
import time

def countdown(number):
    pass
    while number >= 0:
        if number > 0:
            print( f"{ number } SECOND(S)!" )
        else: print( "HAPPY NEW YEAR!" )
        number -= 1


def countdown_with_sleep( number ):
    pass
    while number >= 0:
        if number > 0:
            print( f"{ number } SECOND(S)!" )
        else: print( "HAPPY NEW YEAR!" )
        number -= 1
        time.sleep( 1 )
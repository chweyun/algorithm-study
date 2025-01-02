import math

def solution(r1, r2):
    result = 0

    for y in range(1, r2+1): 
        r1_y = math.sqrt(r1**2 - y**2) if r1**2 - y**2 >= 0 else 0 
        r2_y = math.sqrt(r2**2 - y**2) 

        if r1_y > 0:
            min_x = math.ceil(r1_y) 
        else:
            min_x = 0  

        max_x = math.floor(r2_y) 

        if min_x <= max_x:
            result += max_x - min_x + 1

    return result * 4 

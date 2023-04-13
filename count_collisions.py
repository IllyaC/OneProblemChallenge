def countCollisions(directions):
    """
    :type directions: str
    :rtype: int
    """
    startIndex, movingRightCounter, finalCollisions = 0, 0, 0
    
    while startIndex < len(directions) and directions[startIndex] == "L":
        startIndex +=1
    
    while startIndex < len(directions):    
        if directions[startIndex] == "R":
            movingRightCounter +=1 

        if directions[startIndex] == "S":
            finalCollisions += movingRightCounter
            movingRightCounter = 0
        
        if directions[startIndex] == "L":
            finalCollisions += movingRightCounter +1
            movingRightCounter = 0
        startIndex+=1
        
    return finalCollisions
        

directions = "RLRSLL"
print(countCollisions(directions))
from collections import defaultdict
def leastBricks(wall):
    column_path  = defaultdict(int)
    for row in range (len(wall)):
        rolling_sum = 0
        for column in range (len(wall[row])-1):
            rolling_sum += wall[row][column]
            column_path[rolling_sum] +=1
            
    print(column_path)
    if not column_path:
        return len(wall)
    return len(wall) - max(column_path.values())
            

wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
print(leastBricks(wall))
            
        
        
        
    
            
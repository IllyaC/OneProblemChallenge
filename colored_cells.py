def coloredCells(self, n):
    random = 0
    
    # if n == 1:
    #     return 1
    # else:
    #     return (4*(n-1))+self.coloredCells(n-1)
    if n == 1:
        return 1
    prev_cell = 1
    for i in range (2, n):
        prev = prev + i *4
    return prev +4
# in progress
1



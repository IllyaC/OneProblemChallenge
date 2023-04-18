def numRabbits(answers):
    numbers = {}
    min_total = 0
    for number in  answers:
        if number == 0:
            min_total +=1
        else:
            if number not in numbers or number == numbers[number]:
                numbers[number] = 0
                min_total += (number +1)
            else:
                numbers[number] +=1 
            
    
    return min_total
    
        
answers = [0,0,1,1,1]
print(numRabbits(answers))
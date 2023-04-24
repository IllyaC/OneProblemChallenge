"""
There are n cars going to the same destination along a one-lane road. 
The destination is target miles away.

You are given two integer array position and speed, both of length n, 
where position[i] is the position of the ith car and speed[i] is the 
speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to 
it and drive bumper to bumper at the same speed. The faster car will 
slow down to match the slower car's speed. The distance between these 
two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position 
and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it 
will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.
"""
def carFleet(target, position, speed):
    time_to_reach_target = [] 
    sorted_position_speed  = sorted(zip(position, speed))
    sorted_pos, sorted_spd = zip(*sorted_position_speed)
    sorted_pos = tuple(sorted_pos)
    sorted_spd = tuple(sorted_spd)

    if len(position) == 1:
        return 1
    
    
    for pos, spd in zip(sorted_pos, sorted_spd):
        time = (target - pos)/spd
        time_to_reach_target.append(time)
    
    print(time_to_reach_target)
    counter = 1
    curr_time = time_to_reach_target[len(time_to_reach_target)-1]
    for i in range (len(time_to_reach_target)-1, 0, -1):
        if time_to_reach_target[i-1] <= curr_time:
            continue
        else:
            curr_time = time_to_reach_target[i-1]
            i -= 1
            counter+=1
        
    return counter
        
        
        
    
    
target = 10
position = [0, 4, 2]
speed = [2, 1, 3]
print(carFleet(target, position, speed))
        
        
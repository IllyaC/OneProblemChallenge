def insert(intervals, newInterval):
         if not intervals:
            return [newInterval]

        index, final = 0, []
        current_start, current_end = newInterval
        while index < n:
            original_start, original_end = intervals[iterator_1]
            
            #bigger
            if original_end < current_start:
                final.append([original_start, original_end])
                index += 1
                continue
            #smaller
            if current_end < original_start:
                final.append([current_start, current_end])
                current_start, current_end = original_start, original_end
                index += 1
                continue
            
            #overlap
            current_start, current_end = min(original_start, current_start), max(original_end, current_end)
            index += 1

        final.append([current_start, current_end])
        return final

intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(insert(intervals, newInterval))

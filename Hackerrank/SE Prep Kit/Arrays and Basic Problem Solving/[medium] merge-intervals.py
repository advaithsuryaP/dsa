'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals 
that cover all the intervals in the input.

Ex: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, we merge them into [1,6].

'''

from operator import itemgetter
def mergeHighDefinitionIntervals(intervals):
    # Write your code here
        
    no_of_intervals = len(intervals)
    
    if(no_of_intervals == 0):
        return []
        
    if(no_of_intervals == 1): 
        return intervals
    
    intervals.sort(key=itemgetter(0))
        
    result: list[list[int]] = []
    
    for interval in intervals:
        if(len(result) == 0):
            result.append(interval)
            continue
        
        start_time: int = interval[0]
        end_time: int = interval[1]
        
        if(start_time <= result[-1][1]):
            # The current interval is colliding with the merge interval
            if(end_time >= result[-1][1]):
                # The end time of the current interval exceeds the result's end time colliding, so update
                result[-1] = [result[-1][0], end_time]
        else:
            result.append(interval)
                
    return result


print(mergeHighDefinitionIntervals([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]
print(mergeHighDefinitionIntervals([[1,4],[2,6], [3,7], [8,9]])) # [[1,7],[8,9]]

'''
Solution:
The trick is to sort the intervals by the start time first so we know all the intervals are in ascending order.
Then, we maintain a result list of intervals and iterate through the intervals.

If the result list is empty, we simply append the current interval to the result list. This is the base case and used for further iterations.
For subsequent interations, 
if the start time of the current interval is less than the end time of the last interval, we check if the current interval's end time is greater 
than the last interval's end time. If it is, we update the last interval's end time to the current interval's end time.
If it is not, we simply append the current interval to the result list.
Finally, we return the result list.
'''
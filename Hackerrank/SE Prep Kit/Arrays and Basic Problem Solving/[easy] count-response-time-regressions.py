#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    # If the number of elements is 0, then return 0
    if len(responseTimes) == 0:
        return 0
    
    # Initialize the result and the average to 0
    result: int = 0
    average: int = 0
    
    for index in range(0, len(responseTimes)):        
        responses: list[int] = responseTimes[0: index]
        total_responses: int = len(responses)
        
        if total_responses == 0: 
            continue
                
        average = sum(responses) / total_responses
        
        if(responseTimes[index] > average): 
            result += 1
        
    return result
        

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)

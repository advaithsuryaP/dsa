'''
Given an array of integers, round each element to the nearest multiple of 5.
Example:
Input: [73, 67, 38, 33]
Output: [75, 67, 40, 33]

'''

def gradingStudents(grades):
    # Write your code here
    rounded_grades: list[int] = []
    for grade in grades:
        if(grade < 38):
            rounded_grades.append(grade)
            continue
        
        base_multiple: int = grade // 5
        rounded_score: int = (base_multiple + 1) * 5
        
        difference: int = rounded_score - grade
        if(difference < 3): 
            rounded_grades.append(rounded_score)
        else: 
            rounded_grades.append(grade)
        
    return rounded_grades

print(gradingStudents([73, 67, 38, 33])) # [75, 67, 40, 33]

'''
Problem:
The trick is to find the next multiple of 5 and then check the difference between the grade and the calculated number
'''
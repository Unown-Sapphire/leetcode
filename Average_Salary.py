def average(salary):
    return float(sum(sorted(salary)[1:-1]))/float(len(salary)-2)
    
        
print(average([4000,3000,1000,2000]))
print(average([8000,9000,2000,3000,6000,1000]))
"""
:type salary: List[int]
:rtype: float
sorted_salary = [1000,2000,3000,4000,8000]
sorted_even_salary = [1000,2000,3000]
"""
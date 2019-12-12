"""
Purpose: adding further block in a python list
Author:Ketan Dekate
Date: 12 Dec 2019
"""
employee_ids=[1,2,3,4,5,6,7,8]
print("The existing string is: ")
print(employee_ids)
print("Enter the block you want to add at end of the string: ")
x=int(input())
employee_ids.append(x)
print(employee_ids)

"""
Purpose: Python List Entering
Author:Ketan Dekate
Date: 12 Dec 2019
"""
employee_ids=[1,2,3,4,5,6,7,8,9]
print("The exployee ids are: ")
print(employee_ids)

x=int(input("Enter start index: "))
y=int(input("Enter end index: "))
z=int(input("Enter the number by hoe much block you want to skip: "))
#if you don't want to slice then put z=1
print("The updated list is:")
print(employee_ids[x:y:z])


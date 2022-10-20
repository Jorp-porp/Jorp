# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 13:14:33 2022

@author: jorpp
"""

'''
Program that takes yearly salary, ideal % of income saved per month, and cost 
of home to calculate how many months it will take to save up for a down payment
'''

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25 #Required down payment as percent of total cost.
total_down = portion_down_payment * total_cost
current_savings = 0.0 #You begin with 0 savings.
interest = 0.04 #Interest rate on investments.
num_months = 0 #a counter that displays the number of total months.
monthly_interest = interest/12
monthly_salary = annual_salary/12


while(current_savings < total_down): #Saving will repeat monthly until your current savings surpass the needed down payment.
    current_savings = current_savings + current_savings * monthly_interest #First each month your return on investment is calculated .
    current_savings = current_savings + monthly_salary * portion_saved #Adds your monthly savings to your current savings.
    num_months += 1 #increments to the next month. 

print("number of months needed to save:", num_months)

    
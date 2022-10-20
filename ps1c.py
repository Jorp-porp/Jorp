# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 13:14:33 2022

@author: jorpp
"""

'''
Takes a starting salary from the user and determines, if possible, the optimal 
monthly portion of salary put away to save up for a down payment on a house in
exactly 36 months.
'''

def savings_36(portion, annual_salary, interest_rate, semi_annual_raise):
    """takes portion, annual_salary, interest_rate, and semi_annual_raise and 
    returns savings as a float."""
    salary = annual_salary/12 #resets monthly salary
    savings = 0 #Resets savings
    for i in range(1, 37): #starts at 0, ends at 35. 36 total loops.
        savings = savings + savings * interest_rate / 12 #interest on savings per month
        savings = savings + salary * (portion/10000) #adds a portion of your salary into savings, converts portion to a decimal.
        if(i%6==0 and i>0): #Increase your wage AFTER the 6th month, 12th, 18th, 24th, 30th, and 36th.
            salary += salary * semi_annual_raise
    return savings

def bisection_loop(annual_salary, interest_rate, total_down, epsilon, semi_annual_raise, low, high, portion):
       """Once called, takes an initial guess as defined in optimal_saving_rate.
       Bisects solving for 'savings' until savings is close to the down_payment. 
       Returns the optimal savings rate, portion, along with the number of steps"""
       savings = 0 #initialize savings
       steps = 0 #number of times through the loop
       #initializing loop.. 
       while(abs(savings - total_down) > epsilon):
           steps += 1
           portion = (low + high)//2 #find a portion
           savings = savings_36(portion, annual_salary, interest_rate, semi_annual_raise) #calculate savings with that portion.
           if savings < total_down:
               low = portion
           if savings > total_down:
               high = portion                      
       return portion, steps
   
def optimal_saving_rate(annual_salary, interest_rate, semi_annual_raise, total_down, epsilon):
    """Takes the global varials and user input as inputs. Determines what portion
    of your monthly salary you should invest if you'd like to purchase a home
    in exactly 36 months. If not possible in that time frame, informs the user."""
    if(savings_36(10000, annual_salary, interest_rate, semi_annual_raise) < total_down):
        print('it is not possible to pay the down payment in three years.')
    else:
        portion, steps = bisection_loop(annual_salary, interest_rate, total_down, epsilon, semi_annual_raise, 0, 10000, 5000) #Initializes bisection_loop with the first range and the first guess.
        print('Best savings rate: ', portion/10000)
        print('Number of steps in bisection: ', steps)
    
#Global variables
annual_salary = int(input("Enter your annual salary: "))#starting pay
semi_annual_raise = 0.07 #bi-yearly raise
interest_rate = 0.04 #interest on investments
total_down = 250000
epsilon = 100 #we want to save within 100 dollars of the downpayment.
optimal_saving_rate(annual_salary, interest_rate, semi_annual_raise, total_down, epsilon) #call optimal_savings_rate with the above constants, plus the user input salary.





    
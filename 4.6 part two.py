def computepay(h, r):
    strandard_rate = hrs - 40
    overtime_rate = rate * 1.5
    print(strandard_rate)
    print(overtime_rate)
    normal_wage = (hrs - strandard_rate) * rate
    print(normal_wage)
    overtime_wage = strandard_rate * overtime_rate
    payment_after_all = normal_wage + overtime_wage
    return payment_after_all

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
p = computepay(10, 20)
print("Pay", p)
#this took a week got burned out after I couldn't figure out in the first try with 3 hours of brute forcing

'''
4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.



'''
#the autograder wont accept it because there isn't an if statement even though it didn't told me that in the text above. The if statement requirement made it way harder for me because I would have to code in wages different from 40 hours a week.
#here is a better version help by phind ai (gpt4) uses input as standard because the unknown standard rates can be different across people.
'''
'''
# This function calculates the total payment for an employee based on the hours worked, the hourly rate, and the standard hours for overtime.
def computepay(h, r, s):
    # If the hours worked is less than or equal to the standard hours
    if h <= s:
        # The total payment is calculated as hours worked times the hourly rate
        payment_after_all = h * r
    # If the hours worked is more than the standard hours
    else:
        # The overtime hours is calculated as hours worked minus the standard hours
        overtime_hours = h - s
        # The overtime rate is calculated as 1.5 times the hourly rate
        overtime_rate = r * 1.5
        # The total payment is calculated as the sum of the payment for the standard hours and the payment for the overtime hours
        payment_after_all = (s * r) + (overtime_hours * overtime_rate)
    # The function returns the total payment
    return payment_after_all
# Ask the user to input the hours worked and convert it to a floating point number
hrs = float(input("Enter Hours:"))
# Ask the user to input the hourly rate and convert it to a floating point number
rate = float(input("Enter Rate:"))
# Ask the user to input the standard hours for overtime and convert it to a floating point number
standard = float(input("Enter Standard Hours:"))
# Call the computepay function with the hours worked, the hourly rate, and the standard hours for overtime, and assign the result to the variable p
p = computepay(hrs, rate, standard)
# Print the total payment
print("Pay", p)

#looks super clean compared to the above abomination






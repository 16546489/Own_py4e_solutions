hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
standard_rate = 40
if h > 40: # overtime calculation I couldn't find the "=" after 2 hours of thinking I asked gpt. I was trying h - 40 and I couldn't see why its wrong.
    h = h - 40
    print(h) # delete this line for the autograder
    increased_rate = r * 1.5
    overtime = (h * increased_rate)
    print(overtime) # delete this line for the autograder
print(standard_rate * r + overtime) # I plan to look at it once but I think this is a nice solution

''' Task was

py4e Conditional Execution
Autograder: Exercise 3.1

'''
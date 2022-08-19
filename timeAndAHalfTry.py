#Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input

#Enter Hours: forty
#Error, please enter numeric input

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

try:
    fHours = float(hours)
    fRate = float(rate)
except: 
    print("Error, please enter numeric input")
    quit()

# give the employee 1.5 times the hourly rate for hours worked above 40 hours.
if fHours > 40:
    pay = ( fHours - 40 ) * (1.5 * fRate) + (40 * fRate)
else:
    pay = fHours * fRate
print('Pay:',pay)
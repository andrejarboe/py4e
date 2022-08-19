
hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

# give the employee 1.5 times the hourly rate for hours worked above 40 hours.
if hours > 40:
    pay = ( hours - 40 ) * (1.5 * rate) + (40 * rate)
else:
    pay = hours * rate

print('Pay:',pay)
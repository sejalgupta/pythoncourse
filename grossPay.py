hrs = input("Enter Hours:")
ratePerHour = input("Enter Rate Per Hour:")
if hrs > 40:
    regular = float(40) * float(ratePerHour)
    overtime = (float(hrs)-40) * float(ratePerHour) * 1.5
    grossPay = regular + overtime
else:
    grossPay = float(hrs) * float(ratePerHour)
print(grossPay)

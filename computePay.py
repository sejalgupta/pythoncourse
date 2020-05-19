def computepay(hrs, ratePerHour):
  hrs = float(hrs)
  if hrs > 40:
      regular = 40 * float(ratePerHour)
      overtime = (hrs-40) * float(ratePerHour) * 1.5
      grossPay = regular + overtime
  else:
      grossPay = hrs * float(ratePerHour)
  return grossPay

h = input("Enter Hours:")
r = input("Enter Rate Per Hour:")
pay = computepay(h, r)
print("Pay", pay)

num = input('Enter a number between 0.0 and 1.0')
n = float(num)
if n > 1.0:
    print('Error the number is not in the range')
elif n < 0.0:
    print('Error the number is not in the range')
else:
  if n >= 0.9:
      score = 'A'
  elif n >= 0.8:
      score = 'B'
  elif n >= 0.7:
      score = 'C'
  elif n >= 0.6:
      score = 'D'
  else:
      score = 'F'
  print(score)

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        number = int(num)
    except:
        print("Invalid input")
        continue
    if smallest is None:
        smallest = number
    if largest is None:
        largest = number
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
print("Maximum is", largest)
print("Minimum is", smallest)
celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 1.8) + 32
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))

fahrenheit = float(input("Enter temperature in fahrenheit: "))
celsius = (fahrenheit - 32) / 1.8
print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))

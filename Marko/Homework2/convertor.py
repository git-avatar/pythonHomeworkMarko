question = input('Do you want to convert celsius to farenheit or the other way around(F-C)(C-F)?')
if question.lower() == 'f-c':
   fahrenheit = float(input("Enter temperature in Fahrenheit: "))
   celsius = (fahrenheit - 32) * 5/9
   print("Temperature in Celsius",celsius)
elif question.lower() == 'c-f':
    celsius = float(input("Enter temperature in celsius: "))
    farenheit = ((celsius*9)/5)+32
    print(farenheit)
else:
    print('INVALID-TRY AGAIN!!!')
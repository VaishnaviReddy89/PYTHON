#Formula:

#Celsius = (Fahrenheit - 32) × 5 / 9
print("WITHOUT FUNCTION")
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)
#same logic repeated three items
print("WITH FUNCTION")
def fahrenheit_to_celsius(fahrenheit):#👉 fahrenheit is input
      return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))
#write once
#reuse many times
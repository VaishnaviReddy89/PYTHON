"""
Python has three logical operators:
and - Returns True if both statements are true
or - Returns True if one of the statements is true
not - Reverses the result, returns False if the result is true
"""
#first do and operator
#BOTH conditions should be True

#Example1
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  #Example 2
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login Success")
else:
    print("Invalid")
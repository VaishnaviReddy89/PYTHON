# 23 FORMATE ARE THERE
txt="MY NAME IS VAISHNAVI REDDY and my {age}"
print(txt.format(age=21))
v="THE CAR {PRICE:.2f}"
print(v.format(PRICE=1700000))
#LEFT ALIGN
a="my name {:<8} vaishnavireddy."
print(a.format("is"))
#RIGHT ALIGN
a="my name {:>8} vaishnavireddy."
print(a.format("is"))
#CENTER ALIGN
a="my name {:^8} vaishnavireddy."
print(a.format("is"))
#SIGN IN LEFT MOST POSITION.
A="YOUR ACCOUNT IS {:=8} DEBITED."
print(A.format(-50000))
#PLUS SIGN
TEMP="THE TEMPERATURE IS BETWEEN {:+} and {:+} DEGREE CELSUIUS."
print(TEMP.format(-2,-2))
#NEGATIVE SIGN it is use to indicate the result is positive or negative.
TEMP="THE TEMPERATURE IS BETWEEN {:-} and {:-} DEGREE CELSUIUS."
print(TEMP.format(-2,-2))#it uses for negative value only.
#SPACE SIGN
S= "The temperature is between {: } and {: } degrees celsius."
print(S.format(-3, 7))
#COMMA SIGN
C = "The universe is {:,} years old."
print(C.format(13800000000))
#UNDER SCORE
D = "The universe is {:_} years old."
print(D.format(13800000000))
#BINARY
B = "The binary version of {0} is {0:b}"
print(B.format(5))
#SCIENTIFIC "e"
e = "We have {:e} chickens."
print(e.format(5))
#SCIENTIFIC "E"
E = "We have {:E} chickens."
print(E.format(5))
#"F" SIGN
i = float('inf')
j = "The price is {:F} dollars."
print(j.format(i))
#OCTAL
O = "The octal version of {0} is {0:o}"
print(O.format(9))
#x
z = "The Hexadecimal version of {0} is {0:x}"
print(z.format(255))
#X
Q= "The Hexadecimal version of {0} is {0:X}"
print(Q.format(255))
#%
W = "You scored {:%}"
print(W.format(0.25))

#Or, without any decimals:

I = "You scored {:.0%}"
print(I.format(0.25))


print("COUNT EVEN NUMBERS")
n= [10, 15, 22, 31, 40, 55]
count=0
i=0
while i<len(n):
   if i%2==0:
      count=count+1
   i=i+1
print(count)
print("FIND LARGEST NUMBER")
numbers = [12, 45, 7, 89, 23]
largest=numbers[0]
i=1
while i<len(numbers):
   if numbers[i] > largest:
      largest = numbers[i]
   i = i + 1
print(largest)
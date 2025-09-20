import math
num=int(input("Enter a number : "))
square_root=math.sqrt(num)
if num>0:
    natural_log=math.log(num)
else:
    print("value is not defined")
sine_value=math.sin(num)
print("Square root : ",square_root)
print("Natural log : ",natural_log)
print("Sine value : ",sine_value)

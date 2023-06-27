# Build application calculator
# requirements - work with 3 inputs, basic arith operations - +-/*
#
# input from user number1, number2, operation -(+-/*)


# string="hello dear students"
# number
#   - integer = 1,2,100
#   - float = 1.2, 0.3, etc
# bool = true/false
# list = ["1", "2", 3, dir]
# tuple = (1,2. dir)
# dictionary = { "key":"value" }

# "1" + "sad" = "1sad"
# "hello" + "   " + "world
# if <cond> else action for not cond

number1 = 1 #  placeholder for var1
number2 = "2" # placeholder for var2
operation = '+'

result = str(number1) + number2

print(result)


a=1
b=0
result = a / b if b > 0 else "division by zero is not allowed"
print(result)


print(1,2,3,4,5,6,7,8,9,10)

# 10 equal opeartion for string chars, 1-100, 1
string = "division by zero is not allowed"
for i in string:
    print(i)

for i in range(1,100,1):
    print(i)

a = 2
b = 1


while b < 5:
    print(b)
    b = b + 1

print(b)

a = 1
b = a * 50


for i in range(a,b,1):
     print(i)
     if i == 45:
         print("done")
         pass


# function to multiply two numbers and return result


def multiplier(num1, num2):
    result = num1 * num2
    return int(result)

demo1 = multiplier(2, 4)
demo2 = multiplier(2, 2*2*2)
demo3 = multiplier(4, 2.0)

print(demo1)
print(demo2)
print(demo3)
number1=1

number2=2

number1=number2

number3=1

result=number1 + number2

b=+1

print(result)
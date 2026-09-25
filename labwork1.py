'''
#Exercise 1:
radius = float(input("Enter the circle radius: "))
circle_area = 3.14 * radius ** 2
print("The area of the circle is: ", circle_area)
#Exercise 2:
temp = float(input("Enter the temperature in Celsius: "))
fahrenheit = (temp * 9/5) + 32
print("The temperature in Fahrenheit is: ", fahrenheit)
#Exercise 3: prime number check
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
#Exercise 4: 2^p−1(2p−1) perfect number check
n = int(input("Enter a number: "))
if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            print(n, "is not a perfect number")
            break
    else:
        print(n, "is a perfect number")

#Exercise 5:
list.color = ["red", "green", "blue", "yellow", "orange"]
color = input("Enter a color: ")
if color in list.color:
    print(f"{color} is in the list at number {list.color.index(color)+1}")
#Exercise 6:
print(range(0, 6))
print(range(1, 10, 3))
print(range(5, 0, -1))
print(range(6, -3, -2))
#Exercise 7: remove the $ sign
input_string = input("Enter a string with $ sign: ")
output_string = input_string.replace("$", "")
print("The string without $ sign is: ", output_string)
#Exercise 8:
list = [1, -1, 10, 4, 5]
for i in list:
    if i < 0 and i % 2 != 0:
        list.remove(i)
print("The list after removing negative odd numbers is: ", list)
#Exercise 9: calculate factorial of a number
n = int(input("Enter a number : "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print("The factorial of", n, "is", factorial(n))

#Exercise 10:
import math

def get_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)   
#Exercise 11: calculate distance between two points
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("The distance between the two points is: ", distance)
'''
#Exercise 12: 
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

def print_pattern(m, n):
    for i in range(m):
        row = []
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                row.append("*")
            else:
                row.append(" ")
        print(" ".join(row))

print_pattern(m, n)
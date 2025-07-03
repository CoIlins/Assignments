#1) Define a recursive function that takes two integers as input and returns their product using repeated addition, without employing the multiplication operator.
def addition(x, y):
    if y==0 or y==1:
        return x
    else:
        return x+addition(x, y-1)
print(addition(5,3))


 #2) Define a recursive function that computes the result of raising a given base to a specified exponent, without using the exponentiation operator(**)
def power(x, y):
    if y==0 or y==1:
        return x
    else:
        return x*power(x, y-1)
print(power(5,3))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))


# #3)Implement a recursive function that prints all integers from a given number n down to 0.
def descending(n):
    if n == 0:
        return 0
    else:
        print(n)
        return descending(n-1)

test=int(input("Enter a natural number:"))
print(descending(test))

# #4)Implement a recursive function that prints all integers from 0 up to a given number n by modifying the previous countdown function.

def ascending(n, count = 0):

    if  count > n:

        return "end of the list"

    else:

        print(count)

        return ascending(n, count +1)

test = int(input("Enter a natural number:"))
print(ascending(test))
#
# #5) Write a recursive function that takes a string as input and returns a reversed copy of the string, using only string concatenation.

def reverse_string(s):
    if s == "":
        return ""
    else:
        return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))



#6)Write a recursive function that determines whether a given integer n is a prime number by checking for divisibility by integers less than n.
def prime(n, divisor=None):
    if n < 2:
        return False
    if divisor is None:
        divisor = n-1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return prime(n, divisor - 1)

print(prime(31))
print(prime(10))



#7)Write a recursive function that takes in one argument n and computes Fn, the nth value of the Fibonacci sequence. Recall that the Fibonacci sequence is defined by the relation Fn = Fn−1 + Fn−2 where F0 = 0 and F1 =1
def fibonacci(n):
    if n ==0:
        return 0
    if n==1:
        return 1
    else:

        return fibonacci(n-1)+fibonacci(n-2)


test = int(input("Enter a natural number:"))
print("The ", test,"th term is :",fibonacci(test))












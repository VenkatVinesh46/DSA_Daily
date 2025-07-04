#Count the Number of Digits
import math


def count_no_digits(n):
    count=0
    while n>0:
        digit=n%10
        count+=1
        n=n//10
    return count

#Check if the number is prime
def check_prime(n):
    if n==0 or n==1:
        return False
    elif n==2:
        return True
    elif n>2:
        for i in range(1,int(math.sqrt(n))+1):
            if n%i==0:
                return False
            else:
                return True
#Sum of Digits (Recursive Function Only)

    def sum_digits(n):
        if n == 0:
            return 0  # Base case
        else:
            return (n % 10) + sum_digits(n // 10)  # Recursive step

#Check Palindrome (Only for Numbers)
def check_palindrome(n):
    original_number=n
    reversed_number=0
    while n>0:
        digit=n%10
        reversed_number=reversed_number*10+digit
        n=n//10
    if original_number==reversed_number:
        return True
    else:
        return False

#Fibonacci Sequence (First n terms using Recursion)
def fibonacci(n):
    if n==0 or n==1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)



##Count Vowels in a String (Without Built-ins)

def count_vowels(str):
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    count=0
    for char in str:
        if char in vowels:
            count+=1
    return count


##Reverse a Number

def reverse_no(n):
    if n>=0 and n<10:
        return n
    else:
        original_number=n
        reversed_number=0
        while n>0:
            digit=n%10
            reversed_number=reversed_number+digit
            n=n//10

        return reverse_no(original_number)


##Convert Decimal to Binary (Manual, No bin() or format)

def decimal_to_binary(n):
    binary = ""
    if n == 0:
        return "0"
    while n > 0:
        rem = n % 2
        binary = str(rem) + binary
        n = n // 2
    return binary

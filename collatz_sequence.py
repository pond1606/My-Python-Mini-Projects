"""Collatz Sequence by Phan Huynh Thien Phuc
The Collatz sequence is a sequence of numbers produced from a starting
number n, following three rules:
1) If n is even, the next number n is n / 2.
2) If n is odd, the next number n is n * 3 + 1.
3) If n is 1, stop. Otherwise, repeat."""

# Make sure a number has been entered
while True:
    number = input("Enter a number: ")
    try:
        number = int(number)
        break
    except ValueError:
        pass

# Calculating
print(number)
while number != 1:
    if number % 2 == 1:  # Odd number
        number = number * 3 + 1
        print(int(number))
    else:
        number /= 2
        print(int(number))
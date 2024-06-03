# Task 1: Triple Double
growing_number = 15

def growing_number():
    num1 = 15
    a = num1 * 2 / 2
    b = num1 * 2 / 2
    c = num1 * 2 / 2 
    return a,b,c

num2 = growing_number()
print(num2)

# Task 2: Value Swap
first_number = 5
second_number = 8

print(first_number, second_number)


num1 = first_number
num2 = second_number
first_number = num2
second_number = num1

print(first_number, second_number)



# Task 3: Five and Two & 3 & 7

five = 3
two = 7

print(five * two)



# Task 4: Assign New Value
current_year = str(2021)

print("current year is : "+ current_year)


# Task 5: Input Birth Year
birth_year = input("Type your birth year ")

print("Birth year is " + birth_year)


# Task 6: Calculate Current Age:

def age():
    a = input("what is your birth year? ")
    a = int(a)
    b = 2021 - a
    b = str(b)
    return(b)

age1 = age()

print("Your age is: " + age1)


# Task 7: Total Ticket Cost:

def show():
    a = input("Whta is the name of show? ")
    b = input("Next, how much is the ticket? ")
    c = input("At last, how many tickets you want? ")
    b = int(b)
    c = int(c)
    x = b * c
    x = int(x)
    return (a,b,c,x)

a ,b, c, x = show()

A1 = str(a)
B2 = str(b)
C3 = str(c)
X4 = str(x)

print("Total price for " + C3 +  " is "+  X4 + " Enjoy "+  A1 + " !")




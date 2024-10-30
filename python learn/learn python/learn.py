#print("My name is", "Python.", end=" ")
#print("Monty Python.")
#print("My name is", "Python.", sep=" ", end=" ")
#print("My name is", "Python.", end=" ")
#print("Monty Python.")
#print("    *")
#print("   * *")
#print("  *   *")
#print(" *     *")
#print("***   ***")
#print("  *   *")
#print("  *   *")
#print("  *****")
#print("My\nname\nis\nBond.", end=" ")
#print("James Bond.")
#print("sep" ,"copy", "fish\nchips")
#print('Greg\'s book.')
#print("'Greg's book.'")
#print('"Greg\'s book."')
#print("Greg\'s book.")
#print("Greg's book.")
#print('I\'m Monty Python.')
#var = 100
#var = var+200 + 300
#print(var)
#a = 3.0
#b = 4.0
#c = (a ** 2 + b ** 2) ** 0.5
#print("c =", c)
#kilometers = 12.25
#miles = 7.38

#miles_to_kilometers = miles*1.61
#kilometers_to_miles = kilometers/1.61

###x = 0
#x = float(x)
#y = 3 * x**3 - 2 * x**2 + 3 * x - 1
#print("y =", y)

#x = 1
#x = float(x)
#y = 3 * x**3 - 2 * x**2 + 3 * x - 1
#print("y =", y)

#x = -1
#x = float(x)
#y = 3 * x**3 - 2 * x**2 + 3 * x - 1
#print("y =", y)
#var = "007"
#print("Agent " + var)
#var = 2
#print(var)

#var = 3
#print(var)

#var += 1
#print(var)
#a = '1' # point to be noted
#b = '1'
#print(a + b)
# a = 6     for comment use shortcut use ctrl /
# b = 3
# a /= 2 * b
# print(a)
# x = float(input("Enter value for x: ")) function that have a value like this 1/x+1/x+1/x+1/x
# y = 1./(x + 1./(x + 1./(x + 1./x)))
# print("y =", y)
# here is a project that you show time when test is starting and end
# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))
# mins = mins + dura # find a total of all minutes
# hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
# mins = mins % 60 # correct minutes to fall in the (0..59) range
# hour = hour % 24 # correct hours to fall in the (0..23) range
# print(hour, ":", mins, sep='')
# this for intro
# name = input("Enter your name: ")
# print("Hello, " + name + ". Nice to meet you!")

# this is for end of program
# name = input("Enter your name: ")
# print("Hello, " + name + ". Nice to meet you!")

# print("\nPress Enter to end the program.")
# input()
# print("THE END.")

# x = int(input("Enter a number: ")) # The user enters 2
# print(x * "5")
# making a simple program
# n=1000
# print(n<50)
# print(n>=100)
# program should be like this
# n = int(input("Enter a number: "))
# print(n >= 100)
# if the_weather_is_good:
    # go_for_a_walk()
# have_lunch()

# print("The weather is good, so let's go for a walk!")
# if sheep_counter >= 120:
    # make_a_bed()
    # take_a_shower()
    # sleep_and_dream()
# feed_the_sheepdogs()

# if true_or_false_condition:
    # perform_if_condition_true
# else:
    # perform_if_condition_false

# if the_weather_is_good:
    # if nice_restaurant_is_found:
        # have_lunch()
    # else:
        # eat_a_sandwich()
# else:
    # if tickets_are_available:
        # go_to_the_theater()
    # else:
        # go_shopping()


# Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))

# Choose the larger number
# if number1 > number2:
    # larger_number = number1
# else:
    # larger_number = number2

# Print the result
# print("The larger number is:", larger_number)


# Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))

# Choose the larger number
# if number1 > number2: larger_number = number1
# else: larger_number = number2

# Print the result
# print("The larger number is:", larger_number)

# Read three numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
# largest_number = number1

# We check if the second number is larger than the current largest_number
# and update the largest_number if needed.
# if number2 > largest_number:
    # largest_number = number2/

# We check if the third number is larger than the current largest_number
# and update the largest_number if needed.
# if number3 > largest_number:/
    # largest_number = number3

# Print the result
# print("The largest number is:", largest_number)


# Read three numbers. for deep writing  a program
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

# largest_number = max(number1, number2, number3)

# Print the result.
# print("The largest number is:", largest_number)

# project for learn
# name = input("Enter flower name: ")

# if name == "Spathiphyllum":
    # print("Yes - Spathiphyllum is the best plant ever!")
# elif name == "spathiphyllum":
    # print("No, I want a big Spathiphyllum!")
# else:
    # print("Spathiphyllum! Not", name + "!")

# simple project
# Once upon a time there was a land – a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course – their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:

# if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was what they called tax relief)
# if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
# income = float(input("Enter the annual income: "))

# if income < 85528:
	# tax = income * 0.18 - 556.02
# else:
	# tax = (income - 85528) * 0.32 + 14839.02

# if tax < 0.0:
	# tax = 0.0

# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")

# making the calender/

# As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.

# Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

# if the year number isn't divisible by four, it's a common year;
# otherwise, if the year number isn't divisible by 100, it's a leap year;
# otherwise, if the year number isn't divisible by 400, it's a common year;
# otherwise, it's a leap year.
# year = int(input("Enter a year: "))

# if year < 1582:
	# print("Not within the Gregorian calendar period")
# else:
	# if year % 4 != 0:
		# print("Common year")
	# elif year % 100 != 0:
		# print("Leap year")
	# elif year % 400 != 0:
		# print("Common year")
	# else:
		# print("Leap year")


# lab15-if-essentials.py - a simple script to determine if a year is a leap year or a common year

# Hint: use modulo % and not equal !=

# if the year number isn't divisible by four, it's a common year;
# otherwise, if the year number isn't divisible by 100, it's a leap year;
# otherwise, if the year number isn't divisible by 400, it's a common year;
# otherwise, it's a leap year.

year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    # Write the if-elif-elif-else block here.
    if year % 4 != 0:
        print(f"The year {year} is a common year.")

    elif year % 100 != 0:
        print(f"The year {year} is a leap year.")

    elif year % 400 != 0:
        print(f"The year {year} is a common year.")

    else:
        print(f"The year {year} is a leap year.")
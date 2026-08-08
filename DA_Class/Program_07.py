def find_leap_years(given_year):
    leap_years = []
    year = given_year

    while len(leap_years) < 15:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            leap_years.append(year)
        year += 1

    return leap_years


given_year = int(input("Enter a year: "))
list_of_leap_years = find_leap_years(given_year)
print("Next 15 leap years:", list_of_leap_years)
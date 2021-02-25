# Python exercise: determining if the input is a leap year
# MOOC: https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/
# URL: ./231174-creez-des-structures-conditionnelles

def isleapyear(year):
    if year <= 0:
        raise ValueError()
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return 1
    else:
        return 0


# Test
if __name__ == "__main__":
    try:
        userInput = int(input("Enter a year: "))
        if isleapyear(userInput):
            print("It is a leap year.")
        else:
            print("It is not a leap year.")
    except ValueError:
        print("Invalid input.")

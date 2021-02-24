# Python exercise: determining if the input is a leap year
# MOOC: https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/
# URL: ./231174-creez-des-structures-conditionnelles

def isleapyear(year):
    if year % 4 != 0:
        return 0  # Not a leap year
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 1
            else:
                return 0
        else:
            return 1


# Test
if __name__ == "__main__":
    try:
        userInput = int(input("Enter a year: "))
        if isleapyear(userInput):
            print("It is a leap year.")
        else:
            print("It is not a leap year.")
    except:
        print("Something went wrong.")

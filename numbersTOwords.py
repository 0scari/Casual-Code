def num2words(number):
    """Function that will convert numeral input to equivalent text in English.

        1. According to the value of the input decision to apply the appropriate function is taken
        (0-9): Funnction "ones"
        (10-99): Function "Tens"
        (100-999): Function "Hundreds"
        (1000-9999): function "Thousands"

    """

    if number < 10:
        return ones(number)

    elif 10 <= number < 100:
        return tens(number)

    elif 100 <= number < 1000:
        return hundreds(number)

    else:
        return thousands(number)


# Lists to identify the equivalent name of the digit
onesArray = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teensArray = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
              "nineteen"]
tensArray = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def ones(number):
    """Function to convert single digit input(int) to equivalent text output"""
    if number == 0:
        return onesArray[0]
    elif number == 1:
        return onesArray[1]
    elif number == 2:
        return onesArray[2]
    elif number == 3:
        return onesArray[3]
    elif number == 4:
        return onesArray[4]
    elif number == 5:
        return onesArray[5]
    elif number == 6:
        return onesArray[6]
    elif number == 7:
        return onesArray[7]
    elif number == 8:
        return onesArray[8]
    elif number == 9:
        return onesArray[9]


def tens(number):
    """Function to convert 2 digit input(int) to equivalent text output"""

    def teen(number):
        """Function to convert input in range 10 - 19"""
        if number == 0:
            return teensArray[0]  # ten
        elif number == 1:
            return teensArray[1]
        elif number == 2:
            return teensArray[2]
        elif number == 3:
            return teensArray[3]
        elif number == 4:
            return teensArray[4]
        elif number == 5:
            return teensArray[5]
        elif number == 6:
            return teensArray[6]
        elif number == 7:
            return teensArray[7]
        elif number == 8:
            return teensArray[8]
        elif number == 9:
            return teensArray[9]

    # Decision about whether the input belongs to 10 - 19 or 20 - 99
    if number in range(10, 20):
        return teen(number % 10)
    else:
        if number % 10 == 0:
            return tensArray[number // 10]  # will fetch -ty suffix
        else:
            return tensArray[number // 10] + ' ' + ones(number % 10)  # -ty suffix and name of 1-9 number


def hundreds(number):
    if number % 100 == 0:
        return ones(number // 100) + " hundred"  # quantity of hundreds
    elif number % 100 in range(1, 10):
        return ones(number // 100) + " hundred " + ones(number % 100)  # hundreds and ones
    else:
        return ones(number // 100) + " hundred " + tens(number % 100)  # hundreds and tens


def thousands(number):
    if number % 1000 == 0:
        return ones(number // 1000) + " thousand"  # quantity of thousands
    elif number % 1000 in range(1, 10):
        return ones(number // 1000) + " thousand " + ones(number % 1000)  # quantity of thousands and ones
    elif number % 1000 in range(11, 10):
        return ones(number // 1000) + " thousand " + ones(number % 1000)  # quantity of thousands and ones
    elif number % 1000 in range(10, 100):
        return ones(number // 1000) + " thousand " + tens(number % 1000)  # quantity of thousands and tens
    else:
        return ones(number // 1000) + " thousand " + hundreds(number % 1000)  # quantity of thousands and hundreds


if __name__ == "__main__":
    input = input("Enter a positive integer <= 1,000,000: ")
    if int(input) >= 1000000:
        raise Exception()
    num2words(int(input))
    # try:
    #
    # except:
    #     print(":(")

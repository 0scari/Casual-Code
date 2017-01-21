def num2words(inNumber):
    """Function to convert numeral input to equivalent text expression in English.

        1. According to the value of the input decision to apply the appropriate function is taken
        (0-9): Funnction "ones"
        (10-99): Function "Tens"
        (100-999): Function "Hundreds"
        (1000-9999): function "Thousands"

        """

    # Lists to identify the equivalent name of the digit
    txt = ["zero","one","two","three","four", "five","six","seven","eight","nine"]
    txt1 = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    txt2 = ["","","twenty","thirty","forty", "fifty","sixty","seventy","eighty","ninety"]

    def ones(inNumber):
        """Function to convert single digit input(int) to equivalent text output"""
        if inNumber == 0:
            return txt[0]
        elif inNumber ==1:
            return txt[1]
        elif inNumber == 2:
            return txt[2]
        elif inNumber == 3:
            return txt[3]
        elif inNumber == 4:
            return txt[4]
        elif inNumber ==5 :
            return txt[5]
        elif inNumber == 6:
            return txt[6]
        elif inNumber == 7:
            return txt[7]
        elif inNumber == 8:
            return txt[8]
        elif inNumber == 9:
            return txt[9]

    def tens(inNumber):
        """Function to convert 2 digit input(int) to equivalent text output"""

        def teen(inNumber):
            """Function to convert input in range 10 - 19"""
            if inNumber == 0:
                return txt1[0]  #ten
            elif inNumber == 1:
                return txt1[1]
            elif inNumber == 2:
                return txt1[2]
            elif inNumber == 3:
                return txt1[3]
            elif inNumber == 4:
                return txt1[4]
            elif inNumber == 5:
                return txt1[5]
            elif inNumber == 6:
                return txt1[6]
            elif inNumber == 7:
                return txt1[7]
            elif inNumber == 8:
                return txt1[8]
            elif inNumber == 9:
                return txt1[9]

        # Decision about whether the input belongs to 10 - 19 or 20 - 99
        if inNumber in range(10, 20):
            return teen(inNumber % 10)

        else:
            if inNumber % 10 == 0:
                return txt2[inNumber//10] # will fetch -ty suffix
            else:
                return txt2[inNumber//10] + ' ' + ones(inNumber % 10) # -ty suffix and name of 1-9 number

    def hundreds(inNumber):
        if inNumber % 100 == 0:
            return ones(inNumber // 100) + " hundred" # quantity of hundreds

        elif inNumber % 100 in range(1, 10):
            return ones(inNumber // 100) + " hundred " + ones(inNumber % 100) # hundreds and ones

        else:
            return ones(inNumber // 100) + " hundred " + tens(inNumber % 100) # hundreds and tens

    def thousands(inNumber):
         if inNumber % 1000 == 0:
             return ones(inNumber // 1000) + " thousand" #quantitity of thousands
         elif inNumber % 1000 in range(1,10):
             return ones(inNumber // 1000) + " thousand " + ones(inNumber % 1000) #quantitity of thousands and ones
         elif inNumber % 1000 in range(10, 100):
             return ones(inNumber // 1000) + " thousand " + tens(inNumber % 1000) # quantitity of thousands and tens
         else:
             return ones(inNumber // 1000) + " thousand " + hundreds(inNumber % 1000) # quantitity of thousands and hundreds

    if inNumber < 10:
        return ones(inNumber)

    elif inNumber >= 10 and inNumber <100:
        return tens(inNumber)

    elif inNumber >= 100 and inNumber < 1000:
        return hundreds(inNumber)

    else:
        return thousands(inNumber)








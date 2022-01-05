# Name: Dana Huang
# School: FEU Alabang
# Machine Problem number - 3

import sys

class Roman:
    def RomToInt(self, romstr):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_num = 0
        for i in range(len(romstr)):
            if i > 0 and roman[romstr[i]] > roman[romstr[i - 1]]:
                int_num += roman[romstr[i]] - 2 * roman[romstr[i - 1]]
            else:
                int_num += roman[romstr[i]]
        return int_num

class IntNum:
    def IntToRom(self, int_num):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        letter = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ''
        i = 0
        while int_num > 0:
            for _ in range(int_num // val[i]):
                roman += letter[i]
                int_num -= val[i]
            i += 1
        return roman

# classes for error handling
class Error(Exception):
    """Base class for error handling"""
    pass
class ExceedValue(Error):
    """Raised when integer input exceeds 5000"""
    pass
class NegativeInt(Error):
    """Raised when integer input is negative"""
    pass
class DataTypeErr(Error):
    """Raised when input is not a string"""
    pass
class InvalidLetter(Error):
    """Raised when input is not a letter used int the roman numerals"""
    pass

chkletter = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
ans = True
while ans:
    print("\nMain Menu")
    print("1. Convert an Integer to Roman Numeral")
    print("2. Convert a Roman Numeral to Integer")
    print("3. Exit Program")
    ans = input("Enter Your Choice: ")
    if ans == "1":
        holder = True
        while holder:
            try:
                int_num = int(input("Enter Integer: "))
                if int_num > 5000:
                    raise ExceedValue
                if int_num < 1:
                    raise NegativeInt
            except ExceedValue:
                print("Entered value exceeds 5000. Please try again\n")
            except NegativeInt:
                print("Entered value is less than 1 or is negative. Please try again\n")
            except:
                print("Wrong data type entered. Please try again\n")
            else:
                test = IntNum()
                print("Output in Roman Numerals is: ", test.IntToRom(int_num))
                holder = False

    elif ans == "2":
        holder = True
        while holder:
            try:
                rom_str = input("Enter roman numerals: ")
                rom_str = rom_str.upper()
                if rom_str.isalpha() == False:
                    raise DataTypeErr
                for i in rom_str:
                    if i not in chkletter:
                        raise InvalidLetter
            except DataTypeErr:
                print("Wrong data type. Please enter a string / roman numerals\n")
            except InvalidLetter:
                print("Error in input. Please try again.\n")
            else:
                test = Roman()
                print("Output in Integer is:", test.RomToInt(rom_str))
                holder = False

    elif ans == "3":
        print("You have exited the program")
        print("Thank you for using\n")
        sys.exit()

    else:
        print("Invalid Choice. Please try again.")
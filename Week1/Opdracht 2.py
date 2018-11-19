# Naam: Deniz Lektemur
# Studentnummer: 1722313
# Klas: V2C
# Docent: Frits Dannenberg

def getNumbers(s):
    numbers = []
    previous_was_digit = False
    for i in s:
        if i.isdigit():
            if previous_was_digit:
                numbers[len(numbers) - 1] *= 10
                numbers[len(numbers) - 1] += int(i)
            else:
                numbers.append(int(i))
            previous_was_digit = True
        else:
            previous_was_digit = False
    print(numbers)

mystring = "asg7g90sadgus90djg09sd90809g8sd09g8sa09"
getNumbers(mystring)

# def getNumbers(s):
#     numbers = []
#     previous_was_digit = False
#     for i in s:
#         try:
#             if previous_was_digit:
#                 numbers[len(numbers) - 1] *= 10
#                 numbers[len(numbers) - 1] += int(i)
#             else:
#                 numbers.append(int(i))
#             previous_was_digit = True
#         except:
#             previous_was_digit = False
#     print(numbers)
#
# mystring = "asg7g90sadgus90djg09sd90809g8sd09g8sa09"
# getNumbers(mystring)
